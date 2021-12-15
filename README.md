# Api-Task

## Descripton
This project consists of an API that changes the task status based on a predefined state machine that this task must respect. It allows the user to do the normal CRUD operations.
The API have 4 main operations:
Create Task, Get Task, Delete Task, Update Task


## Run the app
``` python app.py ```

##### by Docker run :
```$ docker build --rm -t flaskapi:latest .```


##### and : ``` docker run --rm -d -p 5000:5000 flaskapi:latest ```

##### and on your browser : ```http://localhost:5000```


## REST API
#### Create Request ```POST```
``` http://127.0.0.1:5000/tasks ```
##### request body raw
``` {"status":"draft","title":"task_name"} ```
##### response
``` {"id": 3,"status": "draft","title": "task_name"} ```

#### Get Request ```GET```
``` http://127.0.0.1:5000/tasks/3 ```
##### response
``` {"id": 3,"status": "draft","title": "task_name"} ```

#### Delete Request ```DELETE```
``` http://127.0.0.1:5000/tasks/3 ```
##### response
``` 204 NO CONTENT ```

#### Update Request ```PUT```
``` http://127.0.0.1:5000/tasks/1/archived ```
##### response
``` {"id": 1, "status": "archived", "title": "task2"} ```

#### Get All Tasks ```GET```
``` http://127.0.0.1:5000/tasks ```
##### response
``` [{"id": 1, "status": "archived", "title": "task2"}, {"id": 2,"status": "draft", "title": "task1"}] ```