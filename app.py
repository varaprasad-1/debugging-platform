from flask import Flask, render_template, request, session
from generator import generate_bug
import uuid

app = Flask(__name__)
app.secret_key = "debug-platform-secret"


@app.route("/")
def home():

    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())

    if "current_code" not in session:
        description, code, fix = generate_bug()

        session["description"] = description
        session["current_code"] = code
        session["original_code"] = code
        session["correct_fix"] = fix

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"]
    )


@app.route("/submit", methods=["POST"])
def submit():

    user_code = request.form["code"]

    if session["correct_fix"] in user_code:

        message = "Correct! New challenge generated."

        description, code, fix = generate_bug()

        session["description"] = description
        session["current_code"] = code
        session["original_code"] = code
        session["correct_fix"] = fix

    else:

        message = "Bug not fixed correctly. Try again."

        # keep user edits instead of resetting
        session["current_code"] = user_code

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"],
        message=message
    )


@app.route("/skip", methods=["POST"])
def skip():

    description, code, fix = generate_bug()

    session["description"] = description
    session["current_code"] = code
    session["original_code"] = code
    session["correct_fix"] = fix

    message = "Challenge skipped."

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"],
        message=message
    )


@app.route("/reset", methods=["POST"])
def reset():

    session["current_code"] = session["original_code"]

    message = "Code reset."

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"],
        message=message
    )


if __name__ == "__main__":
    app.run()
