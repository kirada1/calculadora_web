from flask import Flask, render_template, request,jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/calcular", methods="POST")
def caculo():
    try:
        numero1 = float(request.get("formulario", 0)) # type: ignore
        numero2 = float(request.get("formulario", 0)) # type: ignore

    except Exception as e:
        return render_template("index.html", resultado=f"erro {e}")


if __name__ == "__main__":
    app.run(debug=True)
