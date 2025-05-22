# Simple Project Management Website

This is a basic project management website created using HTML, CSS, and JavaScript. It allows users to add, view, complete, and delete tasks. The tasks are stored in the browser's memory and will be cleared when the page is refreshed.

## How to Run

This project uses Python and Flask.

1.  **Clone the repository:**
    Open your terminal and run the following command, replacing `your-repository-url` with the actual URL of this repository:
    ```bash
    git clone your-repository-url
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd name-of-the-repository-directory
    ```
    (Replace `name-of-the-repository-directory` with the actual folder name created by the clone command).

3.  **Create and activate a Python virtual environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    (On Windows, the activation command is `venv\Scripts\activate`)

4.  **Install dependencies:**
    Install Flask and any other required packages from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```

6.  **Open the website:**
    Once the Flask development server is running, it will typically tell you the address. Open your web browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

The task management functionality is client-side (JavaScript) and data will be lost on page refresh.
