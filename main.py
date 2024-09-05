from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas
tasks = [
    {"id": 1, "title": "Comprar leite", "done": False},
    {"id": 2, "title": "Estudar Python", "done": False}
]

# Endpoint para retornar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Endpoint para retornar uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Tarefa não encontrada"}), 404

# Endpoint para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.json
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)