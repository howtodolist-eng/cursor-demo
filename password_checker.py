import re
from flask import Flask, render_template, request


def evaluate_password(password: str) -> dict:
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Contains uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Contains lowercase letter": bool(re.search(r"[a-z]", password)),
        "Contains a number": bool(re.search(r"\d", password)),
        "Contains a special character": bool(re.search(r"[^A-Za-z0-9]", password)),
    }
    return checks


def strength_rating(checks: dict) -> str:
    passed = sum(checks.values())
    if passed <= 2:
        return "Weak"
    if passed == 3 or passed == 4:
        return "Medium"
    return "Strong"


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    checks = None
    rating = None

    if request.method == "POST":
        password = request.form.get("password", "")
        checks = evaluate_password(password)
        rating = strength_rating(checks)

    return render_template(
        "password_checker.html",
        password=password,
        checks=checks,
        rating=rating,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
