"""
Visi standartiniai veiksmai su db, prijungsim sablone css
"""


from models import db, Automobilis
from flask import Flask, render_template, request, redirect, url_for, jsonify
from serializers import AutomobilisSchema
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

# fizines db prijungimas, konfiguracija

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# paleidžiam db
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/api/automobiliai")
def api_automobiliai():
    all_cars = Automobilis.query.all()
    cars_data = [AutomobilisSchema.model_validate(car).model_dump() for car in all_cars]
    return jsonify(cars_data)

@app.route("/api2/automobiliai")
def api2_automobiliai():
    all_cars = Automobilis.query.all()
    cars_data = [{
        "id": car.id,
        "gamintojas": car.gamintojas,
        "modelis": car.modelis,
        "spalva": car.spalva,
        "kaina": car.kaina,
        "kainaPVM": car.kaina_su_pvm,
        "sukurimo_data": car.sukurimo_data
    }for car in all_cars]
    return jsonify(cars_data)


@app.route("/")
def home():
    search_text = request.args.get("searchlaukelis")
    if search_text:
        filtered_rows = Automobilis.query.filter(Automobilis.gamintojas.ilike(f"{search_text}%"))
        bendra_suma_be_pvm = sum([automobilis.kaina for automobilis in filtered_rows])
        bendra_suma_su_pvm = sum([automobilis.kaina_su_pvm for automobilis in filtered_rows])
        return render_template("index.html", automobiliai=filtered_rows, bendra_suma_be_pvm=bendra_suma_be_pvm,
                               bendra_suma_su_pvm=bendra_suma_su_pvm)
    else:
        automobiliai = Automobilis.query.all()
        bendra_suma_be_pvm = sum([automobilis.kaina for automobilis in automobiliai])
        bendra_suma_su_pvm = sum([automobilis.kaina_su_pvm for automobilis in automobiliai])
        return render_template("index.html", automobiliai=automobiliai, bendra_suma_be_pvm=bendra_suma_be_pvm,
                               bendra_suma_su_pvm=bendra_suma_su_pvm)

@app.route("/automobilis/<int:row_id>")
def one_car(row_id):
    automobilis = Automobilis.query.get(row_id)
    if automobilis:
        return render_template("one_car.html", automobilis=automobilis)
    else:
        return f"Projekto su id: {row_id} nėra"

@app.route("/automobilis/redaguoti/<int:row_id>", methods=["get", "post"])
def update_car(row_id):
    automobilis = Automobilis.query.get(row_id)
    if not automobilis:
        return f"Projekto su id: {row_id} nėra"
    if request.method == "GET":
        return render_template("update_car.html", automobilis=automobilis)
    elif request.method == "POST":
        gamintojas = request.form.get("gamintojaslaukelis")
        modelis = request.form.get("modelislaukelis")
        spalva = request.form.get("spalvalaukelis")
        kaina = float(request.form.get("kainalaukelis"))
        automobilis.gamintojas = gamintojas
        automobilis.modelis = modelis
        automobilis.spalva = spalva
        automobilis.kaina = kaina
        db.session.commit()
        return redirect(url_for("home")) # nukreipimas į home funkcijos endpointa "/"
        # return redirect(f"/projektas/{row_id}")  # variantas nukreipia i vieno projekto rodyma

@app.route("/automobilis/trynimas/<int:row_id>", methods=["POST"])
def delete_car(row_id):
    automobilis = Automobilis.query.get(row_id)
    if not automobilis:
        return f"Projekto su id: {row_id} nėra"
    else:
        db.session.delete(automobilis)
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/automobilis/naujas", methods=["GET", "POST"])
def create_car():
    if request.method == "GET":
        return render_template("create_car.html")
    if request.method == "POST":
        gamintojas = request.form.get("gamintojaslaukelis")
        modelis = request.form.get("modelislaukelis")
        spalva = request.form.get("spalvalaukelis")
        kaina = float(request.form.get("kainalaukelis"))
        if gamintojas and modelis and spalva and kaina:
            new_car = Automobilis(gamintojas=gamintojas, modelis=modelis, spalva=spalva, kaina=kaina)
            db.session.add(new_car)
            db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(port=5001, debug=True)