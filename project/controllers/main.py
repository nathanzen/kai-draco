from flask import render_template, request
from project import app
from project.models import cipher_text

owners_name = "Kai Draco"


@app.route("/")
def main():
    return render_template("index.html", name=owners_name)


@app.route("/about")
def about():
    return render_template("about.html", name=owners_name)


@app.route("/magic", methods=["GET", "POST"])
def textnum_algorithm():
    args = dict(request.form if request.method == "POST" else request.args)
    args.setdefault("mode", "decode")

    text = args.get("text")
    mode = args.get("mode")

    if text and mode:
        try:
            ctext = cipher_text.TextNumbers()

            if mode == "encode":
                result = ctext.encode(text)
            else:
                result = ctext.decode(int(text))

            return render_template("result.html", result=result)
        except (TypeError, ValueError):
            return render_template("error.html", name=owners_name, solution="You just entered an invalid data.")

    return render_template("error.html", name=owners_name, solution="You just entered an invalid parameter.")
