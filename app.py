from flask import Flask, request, jsonify
from models.tasks import Tasks # importando em outro arquivo que eu fiz

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
    new_tasks = Tasks(id=tasks_id_control, title=data.get["title"], description=data.get("description", ""))
    tasks_id_control += 1
    tasks.append(new_tasks)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)