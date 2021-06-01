from flask import Flask, render_template

app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def par():
    return render_template("par.html")
    

@app.route('/chauffeur')
def chauffeur():
    return render_template("chauffeur.html")



app.run(host='0.0.0.0', port=8080)
