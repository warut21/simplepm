// Task Storage
let tasks = [];

// Get references to the form and task list
const addTaskForm = document.getElementById('addTaskForm');
const taskList = document.getElementById('taskList');

// Add Task
addTaskForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get values from input fields
    const taskName = document.getElementById('taskName').value;
    const assignee = document.getElementById('assignee').value;
    const dueDate = document.getElementById('dueDate').value;

    // Create new task object
    const newTask = {
        id: Date.now(),
        name: taskName,
        assignee: assignee,
        dueDate: dueDate,
        completed: false
    };

    // Add new task to tasks array
    tasks.push(newTask);

    // Render tasks
    renderTasks();

    // Clear form input fields
    addTaskForm.reset();
});

// Render Tasks
function renderTasks() {
    // Clear current content of taskList
    taskList.innerHTML = '';

    // Iterate through tasks array
    tasks.forEach(task => {
        // Create task element
        const taskElement = document.createElement('div');
        taskElement.classList.add('task');
        if (task.completed) {
            taskElement.classList.add('completed');
        }

        // Display task information
        taskElement.innerHTML = `
            <h3>${task.name}</h3>
            <p>Assignee: ${task.assignee}</p>
            <p>Due Date: ${task.dueDate}</p>
            <button class="complete-btn" data-id="${task.id}">${task.completed ? 'Undo' : 'Complete'}</button>
            <button class="delete-btn" data-id="${task.id}">Delete</button>
        `;

        // Append task element to taskList
        taskList.appendChild(taskElement);

        // Attach event listeners to buttons
        const completeButton = taskElement.querySelector('.complete-btn');
        completeButton.addEventListener('click', () => markTaskComplete(task.id));

        const deleteButton = taskElement.querySelector('.delete-btn');
        deleteButton.addEventListener('click', () => deleteTask(task.id));
    });
}

// Mark Task as Complete
function markTaskComplete(taskId) {
    // Find task in tasks array
    const task = tasks.find(task => task.id === taskId);

    // Toggle completed status
    if (task) {
        task.completed = !task.completed;
    }

    // Re-render tasks
    renderTasks();
}

// Delete Task
function deleteTask(taskId) {
    // Remove task from tasks array
    tasks = tasks.filter(task => task.id !== taskId);

    // Re-render tasks
    renderTasks();
}

// Initial render
renderTasks();
