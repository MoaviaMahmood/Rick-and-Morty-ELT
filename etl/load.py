# etl/load.py
import os
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.INFO)

def get_engine():
    return create_engine(
        f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:5432/"
        f"{os.getenv('POSTGRES_DB')}"
    )

def load_characters(df):
    logging.info("Loading characters data...")

    os.makedirs("useful_data", exist_ok=True)
    df.to_csv("useful_data/characters.csv", index=False)

    engine = get_engine()

    df.to_sql(
        "characters",
        engine,
        if_exists="replace",  # IMPORTANT for now
        index=False
    )

    logging.info("Characters loaded successfully")

def load_episodes(df):
    logging.info("Loading episodes data...")

    os.makedirs("useful_data", exist_ok=True)
    df.to_csv("useful_data/episodes.csv", index=False)

    engine = get_engine()

    df.to_sql(
        "episodes",
        engine,
        if_exists="replace",
        index=False
    )

    logging.info("Episodes loaded successfully")
