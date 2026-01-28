import pandas as pd

def transform_characters(raw_characters):
    characters_list = []

    for page in raw_characters:
        for char in page["results"]:
            characters_list.append({
                "id": char["id"],
                "name": char["name"],
                "status": char["status"].lower(),
                "species": char["species"].lower(),
                "type": char["type"].lower() if char["type"] else None,
                "gender": char["gender"].lower()
            })

    return pd.DataFrame(characters_list)

def transform_episodes(raw_episodes):
    episodes_list = [] # List to hold processed episode data

    for page in raw_episodes: # Iterate through each page of episode data
        for char in page["results"]: # Iterate through each episode in the results
            episodes_list.append({ # Append selected episode attributes to the list
                "id": char["id"],
                "name": char["name"],
                "type": char["type"],
                "dimension": char["dimension"]
            })
    return pd.DataFrame(episodes_list) # Convert the list to a DataFrame and return it
