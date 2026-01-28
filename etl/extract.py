import requests
import json
import os

def extract_and_save(base_url, filename, total_pages):
    all_data = []

    for page in range(1, total_pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            all_data.append(response.json())
            print(f"Page {page} extracted")
        else:
            print(f"No more pages. Stopping at page {page}.")
            break

    os.makedirs("raw_data", exist_ok=True)

    with open(f"raw_data/{filename}.json", "w") as f:
        json.dump(all_data, f, indent=4)

    return all_data
