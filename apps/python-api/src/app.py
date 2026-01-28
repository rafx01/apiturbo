from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)


products = [
    {
        "id": 1,
        "name": "Notebook Dell Inspiron",
        "price": 3500.00,
        "category": "electronics",
        "stock": 15,
        "active": True,
    },
    {
        "id": 2,
        "name": "Mouse Logitech MX Master",
        "price": 450.00,
        "category": "electronics",
        "stock": 42,
        "active": True,
    },
    {
        "id": 3,
        "name": "Cadeira Gamer ThunderX3",
        "price": 1200.00,
        "category": "furniture",
        "stock": 8,
        "active": True,
    },
    {
        "id": 4,
        "name": "Teclado Mecânico Keychron K2",
        "price": 650.00,
        "category": "electronics",
        "stock": 0,
        "active": False,
    },
    {
        "id": 5,
        "name": "Monitor LG UltraWide 34'",
        "price": 2800.00,
        "category": "electronics",
        "stock": 5,
        "active": True,
    },
    {
        "id": 6,
        "name": "Webcam Logitech C920",
        "price": 380.00,
        "category": "electronics",
        "stock": 23,
        "active": True,
    },
    {
        "id": 7,
        "name": "Headset HyperX Cloud II",
        "price": 520.00,
        "category": "electronics",
        "stock": 18,
        "active": True,
    },
    {
        "id": 8,
        "name": "Mesa Escritório 120x60cm",
        "price": 450.00,
        "category": "furniture",
        "stock": 12,
        "active": True,
    },
]


@app.route("/get-all-products")
def getProducts():
    return jsonify(products), 200


@app.route("/get-product-by-id/<int:id>")
def getProductById(id):
    for product in products:
        if product.get("id") == id:
            return jsonify(product), 200


@app.route("/add-product", methods=["POST"])
def addProduct():
    data = request.json

    new_product = {
        "id": uuid.uuid4(),
        "name": data.get("name"),
        "price": data.get("price"),
        "category": data.get("category"),
        "stock": data.get("stock"),
        "active": data.get("active", True),
    }
    products.append(new_product)

    return jsonify(), 201


@app.route("/edit-product-by-id/<int:id>", methods=["PUT"])
def editProductById(id):
    edittedProduct = request.json
    for i, product in enumerate(products):
        if product.get("id") == id:
            products[i].update(edittedProduct)
            return jsonify(products[i]), 200


@app.route("/delete-product-by-id/<int:id>", methods=["DELETE"])
def deleteProductById(id):
    for i, product in enumerate(products):
        if product.get("id") == id:
            del products[i]
    return jsonify(products), 200


app.run(port=5000, host="localhost", debug=True)
