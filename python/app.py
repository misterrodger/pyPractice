import time

from flask import Flask, render_template, request

app = Flask(__name__)

timestamp = int(time.time() * 1000)


@app.route("/")  # b
def hello():
    return "Hello, World!!!"


@app.route("/user/<username>")  # simple route params
def show_user_profile(username):
    print(username)
    return f"User {username}"


@app.route("/template/<username>")  # route param and render_template
def template_example(username):
    items = ["Item 1", "Item 2", "Item 3"]
    current_time = timestamp
    return render_template(
        "template.html", username=username, items=items, current_time=current_time
    )


@app.route("/form")  # renders a form
def index():
    return render_template("form.html")


@app.route("/process_form", methods=["POST"])  # processes the form
def process_form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f"Submitted data: Name = {name}, Email = {email}"
    return "Form submission failed"


if __name__ == "__main__":
    app.run(debug=True)
