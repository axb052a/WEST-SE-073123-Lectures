from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import Production, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/productions", methods=["GET"])
def productions():
    prods = Production.query.all()
    return make_response([p.to_dict() for p in prods], 200)


@app.route("/productions/<int:id>")
def production_by_id(id):
    prod = Production.query.get(id)
    if prod:
        return make_response(prod.to_dict(), 200)
    else:
        return make_response({"error": "Production not found."}, 404)

app.route("/productions", methods=["POST"])
def create_production():
    production_json = request.get_json()
    production = Production(title=production_json["title"])
    db.session.add(production)
    db.session.commit()
    
    return request.get_json(production.to_dict(), 201)

@app.route("/productions/<int:id>", methods=["GET", "PATCH", "DELETE"])
def production_by_id(id):
    prod = Production.query.get(id)
    if prod:
        return make_response(prod.to_dict(), 200)
    else:
        return make_response({"error": "Production not found."}, 404)
# elif request.method = "PATCH":
#     pass
# elif request.method = "DELETE":
#     pass


if __name__ == "__main__":
    app.run(port=5555, debug=True)
