from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/spam/<string:text>/<int:count>")
def index(text="spam", count=10):
    text = " " + text
    return text * count
@app.route("/")
def indexs():
    return render_template("index.html")
@app.route("/registration")
def reqistration():
    return render_template("form.html")

@app.route("/submit_form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        value = int(request.form.get("age"))
        if value < 18:
            return f"Your Age {value} you cant get the finance help"
        else:
            return render_template("scam.html")

@app.route("/submit_form2", methods=["POST"])
def submit_form2():
    if request.method == "POST":
        value = request.form.get("card")

        value2 = request.form.get("money")
        print(value2)
        if value2 == None:
            return f"с вашего номера карты:{value} списалось 2 милионна гривен"
            return render_template("ez_zascamlen.html")
        else:
            return f"с вашего номера карты:{value} списалось 2 милиарда гривен"
            return render_template("zascamlen.html")




if __name__ == "__main__":
    app.run(debug=True)