# Estrutura básica
# Eu posso ter na aplicação web várias rotas, e essas rotas serve para ponto de acesso para estabelecer comunicação (programas/usuários)
from flask import Flask

app = Flask(__name__)

@app.route("/") # Criando uma rota
def hello_world(): # vai ser executada
    return "Hello World" # Retorna esse texto

@app.route("/about") # Criando outra rota 'sobre'
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)