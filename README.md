# IT Company Task Manager 

## Description

- Task Manager will handle all possible problems during product development in your team.
- Everyone from the team can create, update, delete Task.
- Everyone from the team can assign Task to team-members.
- Everyone from the team can set a deadlines and mark the Task as done.


## Test user:
- login: admin
- password: admi1234

## How to install the project

1) Open the terminal and navigate to the folder where you want to clone the repository.
    ```
    cd path/to/your/directory
    ```

2) Use the git clone command to clone the repository.
   ```
   git clone repository_url
   ```
   
3) Go to the project directory.
   ```
   cd task_manager_project
   ```
   
4) Create and activate a virtual environment:
   ```
   python -m venv venv
   ```
   - for Windows:
   ```
   .\venv\Scripts\activate
   ```
   - for Linux/Mac:
   ```
   source venv/bin/activate
   ```
   
5) Use pip to install the requirements.
   ```
   pip install -r requirements.txt
   ```
   
6) Apply the migrations.
   ```
   python manage.py migrate
   ```