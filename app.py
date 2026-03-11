from flask import Flask,render_template,request
from generator import generate_bug

app=Flask(__name__)

current_code=""
correct_fix=""

@app.route("/")
def home():

    global current_code,correct_fix

    if current_code=="":
        current_code,correct_fix=generate_bug()

    return render_template("index.html",
                           code=current_code)

@app.route("/submit",methods=["POST"])
def submit():

    global current_code,correct_fix

    user_code=request.form["code"]

    if correct_fix in user_code:

        message="Correct! New challenge generated."

        current_code,correct_fix=generate_bug()

    else:

        message="Bug not fixed yet."

    return render_template("index.html",
                           code=current_code,
                           message=message)

if __name__=="__main__":
    app.run(debug=True)