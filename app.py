from flask import Flask
app = Flask(__name__)
from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBSReg")
        pred = model.predict([[float(rates)]])
        print(pred)
        s = "The predicted DBS share price is " + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result="2"))

if __name__ == "__main__":
    app.run()




