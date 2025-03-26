#!/usr/bin/env python
import webapp2
import json

# Global list to store the to-dos in memory
todos = []

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # HTML template to render the to-do list with added CSS for styling
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>To-Do List</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    width: 100%;
                    max-width: 400px;
                }
                h2 {
                    text-align: center;
                    color: #333;
                }
                #todo-input {
                    width: calc(100% - 110px);
                    padding: 10px;
                    margin-right: 10px;
                    border: 2px solid #ddd;
                    border-radius: 5px;
                    font-size: 16px;
                }
                button {
                    padding: 10px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                }
                button:hover {
                    background-color: #45a049;
                }
                .todo-list {
                    margin-top: 20px;
                    padding: 0;
                    list-style-type: none;
                }
                .todo-item {
                    padding: 10px;
                    margin: 8px 0;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    background-color: #f9f9f9;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .todo-item.complete {
                    background-color: #d3ffd3;
                    text-decoration: line-through;
                }
                .todo-item button {
                    background-color: #f44336;
                }
                .todo-item button:hover {
                    background-color: #e53935;
                }
                .todo-item.complete button {
                    background-color: #e0e0e0;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>To-Do List</h2>
                <form id="todo-form">
                    <input type="text" id="todo-input" placeholder="Enter a new task" required>
                    <button type="submit">Add Task</button>
                </form>
                <ul class="todo-list" id="todo-list">
                    <!-- To-Do list will be rendered here -->
                </ul>
            </div>
            <script>
                // Function to render the to-do list from the server response
                function renderTodos(todos) {
                    const todoList = document.getElementById('todo-list');
                    todoList.innerHTML = ''; // Clear current list
                    todos.forEach(function(todo, index) {
                        const li = document.createElement('li');
                        li.className = 'todo-item' + (todo.completed ? ' complete' : '');
                        li.innerHTML = `
                            <span>${todo.task}</span>
                            <div>
                                <button onclick="toggleComplete(${index})">Complete</button>
                                <button onclick="deleteTask(${index})">Delete</button>
                            </div>
                        `;
                        todoList.appendChild(li);
                    });
                }

                // Function to handle adding a new task
                document.getElementById('todo-form').addEventListener('submit', function(event) {
                    event.preventDefault();
                    const todoInput = document.getElementById('todo-input');
                    const newTask = todoInput.value;
                    if (newTask) {
                        fetch('/add_task', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ task: newTask })
                        }).then(response => response.json())
                          .then(data => {
                            renderTodos(data.todos);
                            todoInput.value = ''; // Clear input field
                        });
                    }
                });

                // Function to toggle the completion status of a task
                function toggleComplete(index) {
                    fetch('/toggle_complete', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ index: index })
                    }).then(response => response.json())
                      .then(data => {
                        renderTodos(data.todos);
                    });
                }

                // Function to delete a task
                function deleteTask(index) {
                    fetch('/delete_task', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ index: index })
                    }).then(response => response.json())
                      .then(data => {
                        renderTodos(data.todos);
                    });
                }

                // Initial render of the to-do list
                fetch('/get_tasks')
                    .then(response => response.json())
                    .then(data => {
                        renderTodos(data.todos);
                    });
            </script>
        </body>
        </html>
        """
        self.response.write(html)

class GetTasksHandler(webapp2.RequestHandler):
    def get(self):
        # Return the list of to-dos as JSON
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps({'todos': todos}))

class AddTaskHandler(webapp2.RequestHandler):
    def post(self):
        # Get the new task from the request
        data = json.loads(self.request.body)
        task = data.get('task')
        if task:
            todos.append({'task': task, 'completed': False})
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps({'todos': todos}))

class ToggleCompleteHandler(webapp2.RequestHandler):
    def post(self):
        # Toggle the completion status of a task
        data = json.loads(self.request.body)
        index = data.get('index')
        if 0 <= index < len(todos):
            todos[index]['completed'] = not todos[index]['completed']
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps({'todos': todos}))

class DeleteTaskHandler(webapp2.RequestHandler):
    def post(self):
        # Delete a task from the list
        data = json.loads(self.request.body)
        index = data.get('index')
        if 0 <= index < len(todos):
            todos.pop(index)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps({'todos': todos}))

# Setting up the routes for the app
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/get_tasks', GetTasksHandler),
    ('/add_task', AddTaskHandler),
    ('/toggle_complete', ToggleCompleteHandler),
    ('/delete_task', DeleteTaskHandler)
], debug=True)
