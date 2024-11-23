import pandas as pd
import openai
import os
import re
import json
from dotenv import load_dotenv

load_dotenv()

# 1. Налаштування OpenAI API
openai.api_key = os.getenv('OPENAI_API')  # Замініть на свій ключ


def load_csv(file_path):
    """Завантаження CSV-файлу."""
    try:
        data = pd.read_csv(file_path)
        print(f"Успішно завантажено CSV-файл: {len(data)} рядків, {len(data.columns)} колонок.")
        return data
    except Exception as e:
        print(f"Помилка завантаження файлу: {e}")
        return None


def generate_js_chart_data(data, prompt, file_name, char_limit=1000000):
    """Генерація структури даних для JS-фронтенду з обмеженням розміру тексту."""
    try:
        # Конвертуємо всі дані в JSON-сумісні типи
        data = data.astype(str).replace("nan", None)  # Приводимо до строк і замінюємо NaN на None

        # Вибираємо перші 100 рядків для передачі
        preview_data = data.head(500).to_dict(orient="records")  # Передаємо лише перші 100 рядків

        # Додаємо опис колонок
        column_summary = {
            col: {
                "type": str(dtype),
                "unique_values": data[col].unique()[:10].tolist()  # До 10 унікальних значень для кожної колонки
            }
            for col, dtype in data.dtypes.items()
        }

        # Генеруємо JSON з даними
        json_data = {
            "column_summary": column_summary,
            "preview_data": preview_data
        }

        # Конвертуємо в JSON-рядок
        json_data_str = json.dumps(json_data, ensure_ascii=False)

        # Перевіряємо розмір JSON
        if len(json_data_str) > char_limit:
            raise ValueError("Скорочення попереднього перегляду недостатньо. Спробуйте зменшити розмір датасету.")

        # Формуємо промпт
        full_prompt = f"""
        У мене є таблиця даних із наступними характеристиками:
        {json_data_str}

        Користувач запитав: {prompt}
        
        Використовуючи ці дані, створіть JSON файл, який містить:
        1. Тип графіка (наприклад, 'bar', 'line', 'pie').
        2. Масив даних для осі X (ВСІ ЩО ПОТРІБНО)
        3. Масив даних для осі Y (ВСІ ЩО ПОТРІБНО)
        4. Додаткові масиви даних для додаткових осей якщо потрібно (ВСІ ЩО ПОТРРІБНО)
        """

        # GPT-запит
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ти - експерт з аналізу даних і візуалізації."},
                {"role": "user", "content": full_prompt}
            ]
        )

        js_chart_data = response.choices[0].message['content']

        # Видаляємо все зайве, залишаючи лише JSON
        js_chart_data = re.sub(r"^.*```json", "", js_chart_data, flags=re.DOTALL)
        js_chart_data = re.sub(r"```.*$", "", js_chart_data, flags=re.DOTALL)
        js_chart_data = js_chart_data.strip()

        print("\nGPT Генерована JSON-структура:\n")
        print(js_chart_data)

        return js_chart_data
    except Exception as e:
        print(f"Помилка GPT-запиту: {e}")
        return None


def save_chart_data_as_json(js_chart_data, file_name="chart_data.json"):
    """Зберігає JSON-структуру у файл."""
    try:
        with open(file_name, 'w') as f:
            f.write(js_chart_data)
        print(f"JSON-структура успішно збережена у файл {file_name}")
    except Exception as e:
        print(f"Помилка збереження JSON: {e}")


# 2. Основний функціонал
def main():
    print("Вітаємо у Smart Data Ally для створення графіків! 🚀")
    file_path = input("Введіть шлях до вашого CSV-файлу (наприклад, 'data.csv'): ")
    data = load_csv(file_path)

    if data is not None:
        prompt = input(
            "Опишіть, який графік ви хочете побудувати (наприклад, 'порівняння підтверджених випадків і смертей по країнах'): ")
        print("Аналіз даних і створення JSON...")
        js_chart_data = generate_js_chart_data(data, prompt, file_path)
        if js_chart_data:
            save_chart_data_as_json(js_chart_data)
        else:
            print("Не вдалося створити JSON-структуру для графіка.")


if __name__ == "__main__":
    main()