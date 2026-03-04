from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "change-this-in-production"  # needed for flash messages


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        if name and message:
            flash(f"Thanks {name}! Your message was received.", "success")
        else:
            flash("Please fill in all fields.", "error")
        return redirect(url_for("contact"))
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
