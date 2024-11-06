# Employee Review Generator

This project is a Python application designed to assist managers in generating employee reviews efficiently. The app uses `llama` for generating initial questions and drafting reviews based on manager responses. The application is built using Python, with `uvicorn` as the ASGI server, managed by `poetry` for dependency management, and a `Makefile` for common operations.

## Features
- Generates 5 tailored questions about an employee based on their position.
- Accepts manager responses and compiles a comprehensive review using `llama`.
- Fast and asynchronous web service powered by `uvicorn`.

## Technologies Used
- **Python**: The core programming language for this project.
- **Uvicorn**: A lightweight ASGI server to run the application.
- **Poetry**: Dependency management and virtual environment handling.
- **Makefile**: Simplifies project setup and common tasks.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/employee-review-generator.git
   cd employee-review-generator

2. **Install dependencies**
   ```bash
   poetry install

3. **Activate the virtual environment**
   ```bash
    poetry shell
   
4. **Run the application**
    ```bash
    uvicorn app.main:app --reload
   
**Running Tests**
```bash
poetry run pytest