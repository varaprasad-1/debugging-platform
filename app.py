import os
from flask import Flask, render_template, request, session
from generator import generate_bug
import uuid
import random

app = Flask(__name__)
app.secret_key = "debug-platform-secret"


@app.route("/")
def home():

    if "challenge_number" not in session:
        session["challenge_number"] = 1

    if "current_code" not in session:

        description, code, fix, difficulty = generate_bug()

        session["description"] = description
        session["current_code"] = code
        session["original_code"] = code
        session["correct_fix"] = fix
        session["difficulty"] = difficulty

    return render_template(
        "index.html",
        code=session["current_code"],
        description=session["description"],
        difficulty=session["difficulty"],
        challenge_number=session["challenge_number"]
    )
@app.route("/submit", methods=["POST"])
def submit():

    user_code = request.form["code"]

    if session["correct_fix"] in user_code:

        mes = ["Correct! New challenge generated.", "Bug fixed Successfully, Solve The Next Challange" , "Well done! Let's Try a New One" , "Good job! Try the next challange" , " Bug fixed successfully. Next challange ready " ]
        message = random.choice(mes)

        description, code, fix, difficulty = generate_bug()

        session["challenge_number"] += 1
        session["description"] = description
        session["current_code"] = code
        session["original_code"] = code
        session["correct_fix"] = fix
        session["difficulty"] = difficulty
    else:

        message = "Bug not fixed correctly. Try again."

        # keep user edits
        session["current_code"] = user_code

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
