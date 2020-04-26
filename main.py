from flask import Flask, render_template, request, redirect, send_file
from scrapper import scrapping
from save_csv import save_csv

app = Flask("RedditNews")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/read")
def read():
    term = request.args.get("term")
    term.lower()
    if term in db:
        pass
    else:
        if scrapping(term):
            db[term] = scrapping(term)
            save_csv(term, db[term])
        else:
            return redirect("/")

    return render_template("read.html", db=db[term], term=term, length=len(db[term]))


@app.route("/export")
def export():
    job = request.args.get("job")
    if job:
        return send_file(f"{job}.csv",
                         mimetype="text/csv",
                         attachment_filename=f"{job}.csv",
                         as_attachment=True)
    else:
        return redirect("/")


app.run(host="0.0.0.0")
