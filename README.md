# Simple Project Management Website

This is a basic project management website created using HTML, CSS, and JavaScript. It allows users to add, view, complete, and delete tasks. The tasks are stored in the browser's memory and will be cleared when the page is refreshed.

## How to Run

This project uses Python, Flask, and MySQL (via Docker).

1.  **Clone the repository:**
    ```bash
    git clone your-repository-url
    cd name-of-the-repository-directory
    ```

2.  **Start the MySQL Database with Docker Compose:**
    Ensure you have Docker and Docker Compose installed. From the project's root directory (where `docker-compose.yml` is located), run:
    ```bash
    docker-compose up -d
    ```
    This will start the MySQL container in detached mode. The database service name is `db`, and it uses the credentials and database name specified in `docker-compose.yml` (`project_user`, `project_password`, `project_db`).

3.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    (On Windows: `venv\Scripts\activate`)

4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    When the Flask application starts, it will automatically attempt to create the necessary database tables (e.g., `task`) in the MySQL database if they don't already exist.

6.  **Open the website:**
    Open your web browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

**To stop the MySQL Docker container:**
```bash
docker-compose down
```

The task management functionality now uses the MySQL database for persistence.
