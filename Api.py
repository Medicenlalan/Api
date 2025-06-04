pip install flask


from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados
usuarios = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Luis"}
]

# Ruta principal
@app.route("/")
def inicio():
    return "¡Bienvenido a mi API!"

# Obtener todos los usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(usuarios)

# Obtener un usuario por ID
@app.route("/usuarios/<int:id>", methods=["GET"])
def obtener_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"error": "Usuario no encontrado"}), 404

# Crear un nuevo usuario
@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    datos = request.get_json()
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": datos["nombre"]
    }
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

if __name__ == "__main__":
    app.run(debug=True)

