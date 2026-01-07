from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/students"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add-student", methods=["POST"])
def add_student():
    # 1️⃣ Read form data from HTML
    student_data = {
        "name": request.form["name"],
        "gender": request.form["gender"],
        "phone": request.form["phone"],
        "email": request.form["email"]
    }

    try:
        # 2️⃣ Send data to FastAPI
        response = requests.post(FASTAPI_URL, json=student_data)

        # 3️⃣ Handle response
        if response.status_code == 200:
            return render_template(
                "success.html",
                student=student_data
            )
        else:
            return f"Error from API: {response.text}", 400

    except Exception as e:
        return f"FastAPI not reachable: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
