# IT Company Task Manager 

## Description

- Task Manager will handle all possible problems during product development in your team.
- Everyone from the team can create, update, delete Task.
- Everyone from the team can assign Task to team-members.
- Everyone from the team can set a deadlines and mark the Task as done.


[Task manager project deployed to Render](https://task-manager-b0me.onrender.com/)


## Test user:
- login: Admin
- password: Admin1234

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
   
## Demo

![Website interface](website_images/main_page.png)

![Tasks interface](website_images/tasks_page.png)

![Task detail](website_images/tasks_detail.png)

![Task create](website_images/tasks_create.png)

![Positions interface](website_images/positions_page.png)

![Position update](website_images/positions_update.png)

![Position delete](website_images/positions_delete.png)

![Workers interface](website_images/workers_page.png)

![Workers create](website_images/workers_create.png)

![Worker detail](website_images/worker_detail.png)

![Task Types interface](website_images/tasktypes_page.png)

![Task Types update](website_images/tasktypes_update.png)

![Task Types delete](website_images/tasktypes_delete.png)

![Task Types create](website_images/tasktypes_create.png)

![Login interface](website_images/login_page.png)

![Logout interface](website_images/logout_page.png)
