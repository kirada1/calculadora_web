from flask import Flask, render_template, request, session  # type: ignore


app = Flask(__name__)
app.secret_key = "primeira key"


@app.route("/", methods=["GET", "POST"])
def index():

    if "tecla" not in session:
        session["tecla"] = ""

    if request.method == "POST":
        tecla = request.form.get("key")

        if tecla == "c":
            session["tecla"] = ""

        elif tecla == "backspace":
            try:
                session["tecla"] = session["tecla"][:-1]
            except Exception as e:
                return f"nada para apagar {e}"

        elif tecla == "=":
            try:
                session["tecla"] = str(eval(session["tecla"]))
            except Exception:
                session["tecla"] = "erro"

        else:
            session["tecla"] += tecla

    return render_template("index.html", expressao=session["tecla"])


if __name__ == "__main__":
    app.run(debug=True)
