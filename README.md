# API Data ETL

This project demonstrates how to extract, process, and store data from the **Rick and Morty public API** using Python. It is designed as a beginner-friendly data engineering / data analysis project, showcasing API pagination handling, JSON processing, and basic data transformation with Pandas.

---

## Project Overview

<img width="1107" height="865" alt="Image" src="https://github.com/user-attachments/assets/dc630008-5aba-4113-b9ed-755097327f04" />

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

## Charts & Visualizations

The project includes basic data visualizations to better understand the extracted data.

### Character Status Distribution
A bar chart showing the number of characters by status (Alive, Dead, Unknown).
<img width="571" height="504" alt="Image" src="https://github.com/user-attachments/assets/4eac092d-2b1e-4011-b769-a6ca4210186b" />

### Gender Distribution
A bar chart representing the gender distribution of characters.
<img width="571" height="517" alt="Image" src="https://github.com/user-attachments/assets/250c7ee9-b313-4efc-812e-539bb6bc53a8" />

### Character Species Distribution
A bar chart representing the species distribution of characters.
<img width="571" height="593" alt="Image" src="https://github.com/user-attachments/assets/48ac269b-c6fc-4bd6-ad46-10b0241ebdc9" />

### Gender by Species
A bar chart showing what genders a specie have.
<img width="850" height="763" alt="Image" src="https://github.com/user-attachments/assets/79913732-64a5-4081-ab4a-92a304cd3e0b" />

### Status by Species
A bar chart showing the number of species by status (Alive, Dead, Unknown).
<img width="850" height="686" alt="Image" src="https://github.com/user-attachments/assets/0d35a180-41f9-4f70-944b-4341c97049dd" />

These visualizations help in:
- Understanding data distribution
- Identifying patterns in the dataset
- Improving data storytelling for analysis and reporting

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
   
