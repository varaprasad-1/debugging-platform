from flask import Flask, render_template, request
from generator import generate_bug

app = Flask(__name__)

current_code = ""
correct_fix = ""
description = ""


@app.route("/")
def home():

    global current_code, correct_fix, description

    if current_code == "":
        description, current_code, correct_fix = generate_bug()

    return render_template(
        "index.html",
        code=current_code,
        description=description
    )


@app.route("/submit", methods=["POST"])
def submit():

    global current_code, correct_fix, description

    user_code = request.form["code"]

    # validate fix
    if correct_fix in user_code and correct_fix not in current_code:

        message = "Correct! New debugging challenge generated."

        description, current_code, correct_fix = generate_bug()

    else:

        message = "Bug not fixed correctly. Try again."

    return render_template(
        "index.html",
        code=current_code,
        description=description,
        message=message
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
