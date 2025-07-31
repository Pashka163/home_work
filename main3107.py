# Задача 1

# https://youtu.be/NDOPFWOId28?si=EZfqFzNud55QdcaD - видео
#
# Запустить и написать комментарии к коду.
# mvc_todo/
# │
# ├── model.py
# ├── view.py
# ├── controller.py
# └── main.py
#
# model.py
# class Task:
#     def __init__(self, title):
#         self.title = title
#         self.completed = False
#
#     def complete(self):
#         self.completed = True
#
#     def __str__(self):
#         return f"[{'X' if self.completed else ' '}] {self.title}"
#
#
# class TaskModel:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, title):
#         task = Task(title)
#         self.tasks.append(task)
#
#     def complete_task(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index].complete()
#
#     def get_tasks(self):
#         return self.tasks
#
# view.py
# class TaskView:
#     def show_tasks(self, tasks):
#         print("\nYour Tasks:")
#         for index, task in enumerate(tasks):
#             print(f"{index + 1}. {task}")
#
#     def show_message(self, message):
#         print(message)
#
# controller.py
# class TaskController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#
#     def add_task(self, title):
#         self.model.add_task(title)
#         self.view.show_message(f'Task "{title}" added.')
#
#     def complete_task(self, index):
#         self.model.complete_task(index)
#         self.view.show_message(f'Task {index + 1} completed.')
#
#     def show_tasks(self):
#         tasks = self.model.get_tasks()
#         self.view.show_tasks(tasks)
#
# main.py
#
# from model import TaskModel
# from view import TaskView
# from controller import TaskController
#
# def main():
#     model = TaskModel()
#     view = TaskView()
#     controller = TaskController(model, view)
#
#     while True:
#         command = input("\nEnter a command (add/show/complete/exit): ").strip().lower()
#
#         if command == "add":
#             title = input("Enter task title: ")
#             controller.add_task(title)
#
#         elif command == "show":
#             controller.show_tasks()
#
#         elif command == "complete":
#             index = int(input("Enter task number to complete: ")) - 1
#             controller.complete_task(index)
#
#         elif command == "exit":
#             break
#
#         else:
#             print("Unknown command. Please try again.")
#
# if __name__ == "__main__":
#     main()


# Комментарии к коду приложения MVC Todo
# Это простое консольное приложение для управления задачами, реализованное по паттерну MVC (Model-View-Controller).
#
# model.py
# Содержит бизнес-логику и данные приложения:
# Task - класс, представляющий отдельную задачу с названием и статусом выполнения
# TaskModel - класс для хранения и управления списком задач:
# add_task() - добавляет новую задачу
# complete_task() - отмечает задачу как выполненную
# get_tasks() - возвращает список всех задач
#
# view.py
# Отвечает за отображение информации пользователю:
# show_tasks() - выводит список задач с их статусом
# show_message() - выводит сообщения для пользователя
#
# controller.py
# Связывает модель и представление, обрабатывает пользовательский ввод:
# add_task() - делегирует модели добавление задачи и показывает сообщение
# complete_task() - отмечает задачу выполненной и показывает сообщение
# show_tasks() - запрашивает задачи у модели и передает их представлению
#
# main.py
# Точка входа в приложение:
# Создает экземпляры модели, представления и контроллера
# В бесконечном цикле обрабатывает команды пользователя:
# add - добавить задачу
# show - показать список задач
# complete - отметить задачу выполненной
# exit - выйти из приложения