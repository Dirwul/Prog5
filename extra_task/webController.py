from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from extra_task.model import Status, Task
from extra_task.taskController import TaskController

router = APIRouter()
task_controller = TaskController()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def hello(request: Request):
    return templates.TemplateResponse("mainView.html", {"request": request})

@router.get("/createTaskForm", response_class=HTMLResponse)
def showCreateTaskForm(request: Request):
    return templates.TemplateResponse("createTask.html", {"request": request})

@router.post("/createTask", response_class=HTMLResponse)
def createTask(request: Request, title: str = Form(...), description: str = Form(None), status: str = Form(Status.to_do)):
    task = Task(id = task_controller._task_id_counter, title=title, description=description, status=status)
    created_task = task_controller.createTask(task)
    return templates.TemplateResponse("task.html", {"request": request, "task": created_task})

@router.get("/tasks", response_class=HTMLResponse)
def viewAllTasks(request: Request):
    tasks = task_controller.getTasks()
    return templates.TemplateResponse("tasksList.html", {"request": request, "tasks": tasks})

@router.get("/task/{taskId}", response_model=Task)
def viewTask(request: Request, taskId: int):
    task = task_controller.getTask(taskId)
    return templates.TemplateResponse("task.html", {"request": request, "task": task})

@router.get("/deleteTask/{taskId}", response_model=Task)
def deleteTask(request: Request, taskId: int):
    deleted_task = task_controller.deleteTask(taskId)
    return templates.TemplateResponse("deletedTask.html", {"request": request, "task": deleted_task})

@router.get("/updateTask/{taskId}", response_model=Task)
def getUpdateTaskStatus(request: Request, taskId: int):
    task = task_controller.getTask(taskId)
    return templates.TemplateResponse("updateTask.html", {"request": request, "task": task})

@router.post("/updateTask/{taskId}", response_model=Task)
def updateTaskStatus(request: Request, taskId: int, status: Status = Form(...)):
    updated_task = task_controller.updateTaskStatus(taskId, status)
    return viewTask(request, taskId)
