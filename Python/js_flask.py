from flask import Flask, request, jsonify
import pandas as pd
import openai
import os
import json
import re
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Каталог для збереження завантажених файлів
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

openai.api_key = os.getenv('OPENAI_API')  # Замініть на ваш API ключ OpenAI

def load_csv(file_path):
    """Завантаження CSV файлу."""
    try:
        data = pd.read_csv(file_path)
        print(f"Успішно завантажено CSV файл: {len(data)} рядків, {len(data.columns)} стовпців.")
        return data
    except Exception as e:
        print(f"Помилка при завантаженні файлу: {e}")
        return None


def generate_js_chart_data(data, prompt, char_limit=1000000):
    """Генерація JS структури даних для графіка з обмеженням за розміром."""
    try:
        data = data.astype(str).replace("nan", None)  # Перетворюємо в string та заміняємо NaN на None
        preview_data = data.head(500).to_dict(orient="records")  # Використовуємо тільки перші 500 рядків

        column_summary = {
            col: {
                "type": str(dtype),
                "unique_values": data[col].unique()[:10].tolist()
            }
            for col, dtype in data.dtypes.items()
        }

        json_data = {
            "column_summary": column_summary,
            "preview_data": preview_data
        }

        json_data_str = json.dumps(json_data, ensure_ascii=False)

        if len(json_data_str) > char_limit:
            raise ValueError("Тривалість прев'ю занадто велика. Спробуйте зменшити розмір даних.")

        full_prompt = f"""
        Я маю таблицю даних з такими характеристиками:
        {json_data_str}

        Користувач запитав: {prompt}

        Використовуючи ці дані, створіть JSON файл, що містить:
        1. Тип графіку (наприклад, 'bar', 'line', 'pie').
        2. Масив даних для осі X (Усі необхідні дані).
        3. Масив даних для осі Y (Усі необхідні дані).
        4. Додаткові масиви даних для інших осей, якщо потрібно (Усі необхідні дані).
        """

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ви експерт з аналізу даних і візуалізації."},
                {"role": "user", "content": full_prompt}
            ]
        )

        js_chart_data = response.choices[0].message['content']

        js_chart_data = re.sub(r"^.*```json", "", js_chart_data, flags=re.DOTALL)
        js_chart_data = re.sub(r"```.*$", "", js_chart_data, flags=re.DOTALL)
        js_chart_data = js_chart_data.strip()

        # Збереження відповіді в файл без змін у форматуванні
        output_file = 'output_chart_data_raw.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(js_chart_data)

        print("\nGPT згенерував JSON структуру:\n")
        print(js_chart_data)

        return js_chart_data
    except Exception as e:
        print(f"Помилка при запиті до GPT: {e}")
        return None


@app.route('/generate-chart', methods=['POST'])
def generate_chart():
    """API endpoint для генерації даних графіка."""
    try:
        # Отримуємо prompt та файл з запиту
        prompt = request.form.get('prompt')
        file = request.files.get('file')

        if not prompt or not file:
            return jsonify({"error": "Prompt та файл необхідні"}), 400

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Завантажуємо CSV файл
        data = load_csv(file_path)
        if data is None:
            return jsonify({"error": "Не вдалося завантажити CSV файл"}), 500

        # Генеруємо дані графіка
        js_chart_data = generate_js_chart_data(data, prompt)
        if not js_chart_data:
            return jsonify({"error": "Не вдалося згенерувати дані графіка"}), 500

        return jsonify({"chart_data": js_chart_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
