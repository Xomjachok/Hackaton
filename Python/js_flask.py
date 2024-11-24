from flask import Flask, request, jsonify
import pandas as pd
import openai
import os
import re
import json
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Directory to save uploaded files
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

openai.api_key = os.getenv('OPENAI_API')  # Replace with your OpenAI key


def load_csv(file_path):
    """Load CSV file."""
    try:
        print(f"Attempting to load CSV file: {file_path}")
        data = pd.read_csv(file_path)
        print(f"Successfully loaded CSV file: {len(data)} rows, {len(data.columns)} columns.")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def generate_js_chart_data(data, prompt, char_limit=1000000):
    """Generate JS chart data structure with text size limit."""
    try:
        print("Converting data to JSON-compatible format...")
        data = data.astype(str).replace("nan", None)  # Convert to string and replace NaN with None
        preview_data = data.head(500).to_dict(orient="records")  # Use only the first 500 rows

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
            raise ValueError("Preview truncation is insufficient. Try reducing the dataset size.")

        print("Sending data to OpenAI for JSON chart generation...")
        full_prompt = f"""
        I have a data table with the following characteristics:
        {json_data_str}

        The user asked: {prompt}
        
        Using this data, create a JSON file that contains:
        1. Chart type (e.g., 'bar', 'line', 'pie').
        2. Array of data for the X axis (ALL NEEDED)
        3. Array of data for the Y axis (ALL NEEDED)
        4. Additional data arrays for additional axes if needed (ALL NEEDED)
        """

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in data analysis and visualization."},
                {"role": "user", "content": full_prompt}
            ]
        )

        js_chart_data = response.choices[0].message['content']

        js_chart_data = re.sub(r"^.*```json", "", js_chart_data, flags=re.DOTALL)
        js_chart_data = re.sub(r"```.*$", "", js_chart_data, flags=re.DOTALL)
        js_chart_data = js_chart_data.strip()

        print("Successfully generated JSON structure for chart!")
        return js_chart_data
    except Exception as e:
        print(f"Error with GPT request: {e}")
        return None


@app.route('/upload-file', methods=['POST'])
def upload_file():
    """API endpoint to upload CSV file."""
    print("Received file upload request...")
    if 'file' not in request.files:
        print("Error: No file part in the request.")
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        print("Error: No file selected for upload.")
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print(f"File saved to {file_path}")
        return jsonify({"file_path": file_path}), 200


@app.route('/generate-chart', methods=['POST'])
def generate_chart():
    """API endpoint to generate chart data."""
    print("Received chart generation request...")
    try:
        request_data = request.get_json()

        # Get file path and prompt from the request
        file_path = request_data.get('file_path')
        prompt = request_data.get('prompt')

        if not file_path or not prompt:
            print("Error: File path or prompt missing in request.")
            return jsonify({"error": "File path and prompt are required"}), 400

        print(f"File path: {file_path}, Prompt: {prompt}")
        # Load the CSV file
        data = load_csv(file_path)
        if data is None:
            print("Error: Failed to load CSV file.")
            return jsonify({"error": "Failed to load CSV file"}), 500

        # Generate chart data
        print("Generating chart data...")
        js_chart_data = generate_js_chart_data(data, prompt)
        if not js_chart_data:
            print("Error: Failed to generate chart data.")
            return jsonify({"error": "Failed to generate chart data"}), 500

        print("Chart data successfully generated!")
        return jsonify({"chart_data": js_chart_data}), 200
    except Exception as e:
        print(f"Error during chart generation: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(port=5000, debug=True)
