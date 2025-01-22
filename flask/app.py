from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("vitej.html")


@app.route("/form")
def form():
    recenze = request.args.get("recenze")
    if recenze == "nic":
        recenze = "uživatel byl příliš líný na napsání recenze"
    return render_template("form.html", recenze=recenze)


if __name__ == "__main__": #kontrola jestli je app spuštěná přímo a ne jako import
    app.run(debug=True) #spuštění aplikace v režimu vývojáře

