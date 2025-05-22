from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database Configuration
# User, password, database name should match docker-compose.yml
# Host is 'db' which is the service name in docker-compose.yml if Flask app runs in another Docker container.
# If Flask app runs on the host, host should be '127.0.0.1' or 'localhost'.
# For now, assuming Flask runs on host and MySQL in Docker.
db_user = os.environ.get('MYSQL_USER', 'project_user')
db_password = os.environ.get('MYSQL_PASSWORD', 'project_password')
db_name = os.environ.get('MYSQL_DATABASE', 'project_db')
db_host = '127.0.0.1' # Since MySQL is in Docker, accessible via localhost from host machine

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Task Model Definition
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    assignee = db.Column(db.String(100), nullable=True)
    due_date = db.Column(db.String(20), nullable=True) # Using String for simplicity with HTML date input
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.name}>'

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form.get('taskName')
    assignee = request.form.get('assignee')
    due_date = request.form.get('dueDate')

    if name: # Basic validation
        new_task = Task(name=name, assignee=assignee, due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
