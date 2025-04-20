from flask import Flask, render_template, request
import random
import urllib.parse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    options = request.args.getlist('option')
    
    if request.method == "POST":
        options = request.form.getlist("options[]")
        options = [opt.strip() for opt in options if opt.strip()]
        if options:
            result = random.choice(options)
    
    return render_template("index.html", result=result, options=options)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)

