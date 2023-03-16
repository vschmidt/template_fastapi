# FastAPI Template

## :coffee: Introduction

This Test API was created to solve a fake business rule.

## :octopus: Run with Docker Compose

### 1. Run Docker compose

- If necessary, set environment variables like `docker compose up -d`
- Access the docs from `127.0.0.1:8000/docs`

## :office: Run on HOST machine

### 1. Infrastructure Requirements

- You need a postgres server running

### 2. Install requirements

- Run `pip install -r requirements/dev.txt` command
- If necessary, set environment variables like `app/settings/environment.py`

### 2. Run app

- Start `run.py` file.
- It runs an uvicorn server at `127.0.0.1:8000`
- Access the docs from `127.0.0.1:8000/docs`

### 3. Build and Test

To run the tests just follow the steps:

- Run `pip install -r requirements/test.txt` command
- Run `pytest` command

# Latest releases

- v0.0.1 - First Release
