# y42Task
This is a Python project on python webframework Django.

This project include Task 1 and Task 2, Task 1 as stack application and Task 2 as library application.

## Dependencies:
- [Python 3.9](https://github.com/pyenv/pyenv)

## Setting up the project 

1. Setting setup the environment
    Create a virtual environment where you will install all the dependencies for this project.
    
    ```sh
    python3 -m venv env
    source ./env/bin/activate
    ```

2. Setup [pre-commit](https://pre-commit.com/#install)
    ```sh
    pip install pre-commit
    pre-commit install
    ```

3. Install all the requirements for this project using the given command.
    ```sh   
    pip install -r requirements.txt
    ```

4. Migrate and Run Django Server,
    Migrate all the model so you will get db schema inplace.
    ```sh
    python manage.py migrate
    ```
    Run the Django server so 
    ```sh
    python manage.py runserver
    ```
5. Django Admin Admin interface for for Model management.
    ```
    http://localhost:8000/admin 
    ```
6. Django Admin Login Credentails
    ```
    Username: y42TestingUser
    Password: y42TestUser@1044
    ```
7. API Documentation:
    ```
    API Doucmentation is provide  as postman collection for testing out Task 2, inside Documentation folder at project root.
    ```
7. Run your unit tests with coverage.
    ```sh
    pytest
    ```
8. Lints and fixes files
    ```
    black .
    flake8
    ```

## Instructions for task details
1. **Testing a Struct interface**\
    All the testcase for stack functionaliy is written inside the `stack` application `tests` folder. To run the tests, run the
    ```
    pytest stack
    ```
    This will run the all the testcases inside the stack application.

2. **Data Store Library**\
    For task 2, there is an applciation name 
    `library` in this project which contains all the detials including models, testcases, endpoint for `Record CRUD` it includes all the required functionaliy, mentioned in the task document for task 2. It also includes extensive testing e.g **(Unit and integration testing)**.

