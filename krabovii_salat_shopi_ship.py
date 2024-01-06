from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index1.html")
@app.route("/about")
def about():
    return render_template("about krabovii_salat_shop_ship.html")
@app.route("/buy")
def buy():
    return render_template("buy_krabovii_salat.html")
@app.route("/zaskamlen")
def scammer_plan():
    return render_template("scam.html")

if __name__ == "__main__":
    app.run(debug=True)