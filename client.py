import requests

task = {"title": "Nova tarefa", "done": False}
response = requests.post("http://localhost:5000/tasks", json=task)

response = requests.get("http://localhost:5000/tasks")
print(vars(response))


