import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()


def get_api_data(url: str, params: dict) -> dict| None:
    try:
        headers = {"x-cg-demo-api-key": os.getenv("API_KEY")}

        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"{e}")

def save_json_file(json_data: dict, target_dir: str, file_name: str):
    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file = os.path.join(target_dir, f"{current_timestamp}-{file_name}.json")
    with open(file, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
