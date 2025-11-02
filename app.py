from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    rutina = ""
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        peso = int(request.form.get("peso"))
        altura = int(request.form.get("altura"))
        salud = request.form.get("salud").lower()
        rutina += f"<h2>Hola {nombre}, tu rutina de hoy 💪</h2>"
        if "lesión" in salud or "dolor" in salud:
            rutina += "<ul>"
            rutina += "<li>Evita ejercicios de alto impacto y cargas pesadas</li>"
            rutina += "<li>10 minutos de movilidad y estiramientos</li>"
            rutina += "<li>15 minutos de remo o bicicleta estática</li>"
            rutina += "</ul>"
        else:
            intensidad = "moderada"
            if edad > 50 or peso > 100:
                intensidad = "ligera"
            rutina += "<ul>"
            rutina += f"<li>5 minutos de calentamiento ({intensidad})</li>"
            rutina += f"<li>3 series de 10 burpees ({intensidad})</li>"
            rutina += f"<li>3 series de 12 sentadillas con peso corporal ({intensidad})</li>"
            rutina += f"<li>3 series de 10 push-ups ({intensidad})</li>"
            rutina += "<li>10 minutos de cardio</li>"
            rutina += "</ul>"
    return render_template("index.html", rutina=rutina)
if __name__ == "__main__":
    app.run(debug=True)
