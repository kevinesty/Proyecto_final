from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

data = [
    {
        "id": "PLA-001",
        "plato": {
            "nombre": "Arroz con pollo",
            "dislikes": 0,
            "likes": 0,
            "image": "img/arroz_con_pollo.jpg",
        },
        "comentarios": [
            { 
                "reseña": "La comida fue espectacular y el ambiente muy acogedor. Sin duda, un lugar al que volveré.",
            }
        ],
    },
    {
        "id": "PLA-002",
        "plato": {
            "nombre": "Lomo saltado",
            "dislikes": 0,
            "likes": 0,
            "image": "img/lomo_saltado.jpg",
        },
        "comentarios": [
            { 
                "reseña": "Excelente servicio y platos deliciosos. ¡Muy recomendado!",
            }
        ],
    },
    {
        "id": "PLA-003",
        "plato": {
            "nombre": "Ensalada",
            "dislikes": 0,
            "likes": 0,
            "image": "img/ensalada_rusa.jpg",
        },
        "comentarios": [
            { 
                "reseña": "Excelente servicio y platos deliciosos. ¡Muy recomendado!",
            }
        ],
    },
    {
        "id": "PLA-004",
        "plato": {
            "nombre": "Ceviche",
            "dislikes": 0,
            "likes": 0,
            "image": "img/ceviche.jpg",
        },
        "comentarios": [
            { 
                "reseña": "Excelente servicio y platos deliciosos. ¡Muy recomendado!",
            }
        ],
    },
    {
        "id": "PLA-005",
        "plato": {
            "nombre": "Causa",
            "dislikes": 0,
            "likes": 0,
            "image": "img/causa.jpg",
        },
        "comentarios": [
            { 
                "reseña": "La comida estaba fría y el servicio fue lento. No volveré.",
            }
        ],
    },
]

@app.route("/platos", methods=["GET"])
def get_users():
    return jsonify(data)

@app.route("/platos/<string:plato_id>", methods=["GET"])
def get_plato(plato_id):
    plato = next((item for item in data if item["id"] == plato_id), None)
    if plato:
        return jsonify(plato) 
    return jsonify({"error": "Plato no encontrado"}), 404
 
@app.route("/plato/<string:plato_id>/comentario", methods=["POST"])
def create_platos(plato_id):
    body = request.json
    plato = next((item for item in data if item["id"] == plato_id), None)
    if plato:
        likes = body.get("likes", 0)
        dislikes = body.get("dislikes", 0) 
        plato["comentarios"].append(body)
        plato["plato"]["likes"] = likes
        plato["plato"]["dislikes"] = dislikes
        return jsonify(plato), 201
    return jsonify({"error": "Plato no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
# tod esto es un backend y para construirlo necesito una ruta y la funcion  