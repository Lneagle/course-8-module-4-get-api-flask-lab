from flask import Flask, jsonify, request, make_response
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return make_response({"message": "welcome!"}, 200)

@app.route("/products")
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [item for item in products if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(products), 200

@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((item for item in products if item["id"] == id), None)
    if not product:
        return ("Product not found", 404)
    return jsonify(product) 

if __name__ == "__main__":
    app.run(debug=True)
