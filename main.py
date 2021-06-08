from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html")
  
@app.route('/par')
def par():
    return render_template("par.html")

@app.route('/about')
def about():
  return render_template("par.html")

@app.route('/klienti')
def klienti():
    return render_template("klienti.html")
@app.route('/clients')
def clients():
    return render_template("klienti.html")

@app.route('/soferis')
def soferis():
  return render_template("soferis.html")
@app.route('/chauffer')
def chauffer():
    return render_template("klienti.html")

@app.route('/rezervet')
def rezervet():
  return render_template("book.html")
@app.route('/book')
def book():
    return render_template("klienti.html")

@app.route('/atgriezt')
def atgriezt():
  return render_template("atgriezt.html")  

    
app.run(host='0.0.0.0', port=8080)
