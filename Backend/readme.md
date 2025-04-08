# Deep Search with LLM

## Backend Desription

- **Python**

- Version: 3.11

- Enviroments
  
  ```bash
  pip install -r requirements.txt
  ```

- Setting
  
  1. make .env file
  
  2. Write Info [sample](.env-sample)

## SQL

- **postgresql**

- Install

  ```bash
  docker-compose up -d
  ```

- Setting

  1. setting [query](sql/query.sql)

## Run

**Server**

- test

  ```bash
  uvicorn app:app --host 0.0.0.0 --port 13000 --reload
  ```

- dev

  ```bash
  python app.py
  ```