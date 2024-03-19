from flask import Flask, request, jsonify
from models.tasks import Task
app = Flask(__name__)

# CRUD
# create, read, update e delete
# Tabela: Trefa

tasks = []
tasks_id_control = 1

@app.route("/tasks", methods=["POST"]) 
def create_tasks():
    global tasks_id_control
    data = request.get_json()
    new_tasks = Task(id=tasks_id_control, title=data["title"], description=data.get("description", ""))
    tasks_id_control += 1
    tasks.append(new_tasks)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    
    output = {
            "tasks": task_list,
            "total_taks": len(task_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"]) # obtendo tarefa específica
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    

if __name__ == "__main__":
    app.run(debug=True)