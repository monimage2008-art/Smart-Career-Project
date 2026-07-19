from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("data/career_data.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        skill = request.form["skill"].strip().lower()

        result = data[
            data["Skills"].fillna("").str.lower().str.contains(skill) |
            data["Career"].fillna("").str.lower().str.contains(skill)
        ]
        if result.empty:
            result = pd.DataFrame({
        "Message": ["No matching career found"]
    })
    return render_template(
        "index.html",
        tables=[result.to_html(classes="table")] if result is not None else None
    )

if __name__ == "__main__":
    app.run(debug=True)