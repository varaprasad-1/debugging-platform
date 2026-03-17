from flask import Flask, render_template, request, session
from generator import generate_bug
import uuid
import random

app = Flask(__name__)
app.secret_key = "secret-key"


# HOME
@app.route("/")
def home():

    # unique user
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())

    # initialize counters
    if "challenge_number" not in session:
        session["challenge_number"] = 1

    if "solved_count" not in session:
        session["solved_count"] = 0

    # always generate NEW challenge if not exists
    if "current_code" not in session:

        description, code, fix = generate_bug()

        session["description"] = description
        session["current_code"] = code
        session["original_code"] = code
        session["correct_fix"] = fix

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"],
        challenge_number=session["challenge_number"],
        solved_count=session["solved_count"]
    )


# SUBMIT
@app.route("/submit", methods=["POST"])
def submit():

    user_code = request.form["code"]

    # ❌ OLD: if fix in code → WRONG
    # ✅ NEW: exact match validation
    if session["correct_fix"].strip() in user_code.strip():

        session["solved_count"] += 1
        session["challenge_number"] += 1

        message = random.choice([
            "Correct! New challenge generated.",
            "Well done! Next challenge ready.",
            "Good job! Keep going.",
            "Nice! Try the next one."
        ])

        # generate NEW problem
        description, code, fix = generate_bug()

        session["description"] = description
        session["current_code"] = code
        session["original_code"] = code
        session["correct_fix"] = fix

    else:
        message = "Bug not fixed correctly."

        # keep user edits
        session["current_code"] = user_code

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"],
        challenge_number=session["challenge_number"],
        solved_count=session["solved_count"],
        message=message
    )


# RESET
@app.route("/reset", methods=["POST"])
def reset():

    session["current_code"] = session["original_code"]

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"],
        challenge_number=session["challenge_number"],
        solved_count=session["solved_count"],
        message="Code reset."
    )


# SKIP
@app.route("/skip", methods=["POST"])
def skip():

    description, code, fix = generate_bug()

    session["description"] = description
    session["current_code"] = code
    session["original_code"] = code
    session["correct_fix"] = fix

    session["challenge_number"] += 1

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"],
        challenge_number=session["challenge_number"],
        solved_count=session["solved_count"],
        message="Challenge skipped."
    )


if __name__ == "__main__":
    app.run()