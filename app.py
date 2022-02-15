from flask import Flask
app = Flask(__name__)
from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model1 = joblib.load("DBSReg")
        pred1 = model1.predict([[float(rates)]])
        model2 = joblib.load("DBSDT")
        pred2 = model2.predict([[float(rates)]])
        mode3 = joblib.load("DBSNN")
        pred3 = model3.predict([[float(rates)]])
        print(pred1)
        s = "The predicted DBS share price is " + str(pred1)
        return(render_template("index.html", result1 = s, result2=str(pred2), result3=str(pred3))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2"))

if __name__ == "__main__":
    app.run()




