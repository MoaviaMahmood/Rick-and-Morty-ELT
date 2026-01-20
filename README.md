# Rick and Morty API Data Extraction

This project demonstrates how to extract, process, and store data from the **Rick and Morty public API** using Python. It is designed as a beginner-friendly data engineering / data analysis project, showcasing API pagination handling, JSON processing, and basic data transformation with Pandas.

---

## Project Overview

The notebook fetches data from multiple endpoints of the Rick and Morty API:

- **Characters**
- **Locations**
- **Episodes**

The extracted data is paginated, combined into a single dataset per endpoint, and saved locally in **JSON format** for further analysis or database loading.

This project is suitable for:
- Practicing API data extraction
- Understanding paginated REST APIs
- Building a simple data ingestion pipeline
- Portfolio demonstration for data engineering or analytics roles

---

## Technologies Used

- Python 3  
- Requests – for API calls  
- Pandas – for data handling and transformation  
- JSON – for data storage  
- SQLAlchemy – for database integration  
- Jupyter Notebook  

---

## Data Source

**Rick and Morty API**  
https://rickandmortyapi.com/

Endpoints used:
- `/character`
- `/location`
- `/episode`

---

## How It Works

1. The notebook sends requests to the API endpoints.
2. Pagination is handled by looping through all available pages.
3. Data from each page is appended into a single list.
4. The final dataset is converted into a Pandas DataFrame.
5. Extracted data is saved as `.json` files locally.

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rick-and-morty-api-extraction.git
   
