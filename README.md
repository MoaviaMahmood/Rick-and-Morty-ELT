# ETL Pipeline (Docker + Python + PostgreSQL)

An end-to-end **containerized ETL (Extract, Transform, Load) pipeline** that ingests data from the **public API**, processes it using **Python & Pandas**, and loads it into a **PostgreSQL** database using **Docker Compose**.

This project demonstrates **real-world data engineering practices** including API ingestion, data cleaning, container orchestration, and relational data storage.

---

## 🚀 Project Overview

The pipeline performs the following steps:

1. **Extract** data from the API (paginated JSON responses)
2. **Transform** raw data into structured, cleaned Pandas DataFrames
3. **Load** processed data into PostgreSQL tables
4. Persist cleaned datasets as CSV files for downstream use

The entire workflow runs inside Docker containers, ensuring **reproducibility** and **environment consistency**.

---

## 🧱 Architecture Overview

### Data Flow

```
API
        │
        ▼
ETL Container (Python)
  - Extract (requests)
  - Transform (pandas)
  - Load (SQLAlchemy)
        │
        ▼
PostgreSQL Container
```

### Architecture Description

* **API** acts as the external data source
* **ETL container** runs a Python application that:

  * Fetches paginated API data
  * Cleans and normalizes fields
  * Writes results to PostgreSQL
* **PostgreSQL container** stores transformed data in relational tables
* **Docker Compose** orchestrates service startup and networking

The ETL container runs as a **batch job** and exits after successful execution, while PostgreSQL remains available for querying.

---

## 🐳 Tech Stack

* **Python 3.11**
* **Pandas** – data transformation
* **Requests** – API ingestion
* **SQLAlchemy + psycopg2** – database connectivity
* **PostgreSQL 15** – relational storage
* **Docker & Docker Compose** – container orchestration

---

## 📂 Project Structure

```md
API_data_pipeline/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── raw_data/
├── useful_data/
├── docker-compose.yml
├── Dockerfile
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variables

The project uses environment variables for secure configuration:

```env
POSTGRES_USER=rm_user
POSTGRES_PASSWORD=rm_password
POSTGRES_DB=rick_morty
POSTGRES_HOST=postgres
```

These are injected into the ETL container at runtime via Docker Compose.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rick-morty-etl.git
cd rick-morty-etl
```

### 2️⃣ Start the Pipeline

```bash
docker-compose up --build
```

This will:

* Start PostgreSQL
* Run the ETL container
* Load data into the database

---

## 🗄️ Database Verification

Access PostgreSQL:

```bash
docker exec -it rick_morty-postgres-1 psql -U rm_user -d rick_morty
```

Check loaded tables:

```sql
\dt;
SELECT COUNT(*) FROM characters;
```

---

## 📊 Output

* PostgreSQL tables:

  * `characters`
  * `episodes`
* CSV files:

  * `useful_data/characters.csv`
  * `useful_data/episodes.csv`

---

## 🧠 Key Data Engineering Concepts Demonstrated

* API-based data ingestion
* Pagination handling
* Data cleaning & normalization
* Batch ETL processing
* Dockerized data pipelines
* Service orchestration with Docker Compose
* Relational data modeling

---

## 🔮 Future Improvements

* Add **Airflow** for orchestration
* Add **logging & retries** for failed API pages
* Incremental loads instead of full refresh
* Push raw data to **S3 / GCS**
* Add data quality checks

---

## 👤 Author

**Moavia Mahmood**
Data Engineer

---

⭐ If you found this project useful, feel free to star the repository!
