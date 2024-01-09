
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class TaskController(metaclass=Singleton):
    def __init__(self):
        self.tasks = []
        self._task_id_counter = 1

    def _findArrayIndexById(self, task_id):
        index = 0
        for task in self.tasks:
            if task.id == task_id:
                return index
            index += 1
        return -1

    def getTasks(self):
        return self.tasks

    def getTask(self, taskId):
        index = self._findArrayIndexById(taskId)
        if (index == -1):
            print("Task not found")
            pass
        return self.tasks[index]

    def createTask(self, task):
        print("Айди задачи: ", self._task_id_counter)
        self.tasks.append(task)
        self._task_id_counter += 1
        return task

    def deleteTask(self, taskId):
        index = self._findArrayIndexById(taskId)
        if (index == -1):
            print("Task not found")
        else:
            #db
            return self.tasks[index]

    def updateTaskStatus(self, taskId, status):
        index = self._findArrayIndexById(taskId)
        if (index == -1):
            print("Task not found")
        else:
            self.tasks[index].status = status
            # db
