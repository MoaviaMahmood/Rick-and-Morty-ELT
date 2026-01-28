from etl.extract import extract_and_save
from etl.transform import transform_characters
from etl.load import load_characters

BASE_URL = "https://rickandmortyapi.com/api/"
CHARACTERS_ENDPOINT = "character"

def run_pipeline():
    raw_characters = extract_and_save(
        BASE_URL + CHARACTERS_ENDPOINT,
        "raw_data_characters",
        total_pages=42
    )

    df_characters = transform_characters(raw_characters)

    load_characters(df_characters)

if __name__ == "__main__":
    run_pipeline()
