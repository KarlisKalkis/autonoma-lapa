from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/home')
def home():
  return render_template("index.html")

@app.route('/ride')
def ride():
  return render_template("ride.html")


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
  return render_template("rezervet.html")
@app.route('/klienti')
def book():
    return render_template("klienti.html")

@app.route('/atgriezt')
def atgriezt():
  return render_template("atgriezt.html")  

@app.route('/atsauksmes')
def atsauksmes():
  return render_template("atsauksmes.html")

@app.route('/services')
def services():
  return render_template("services.html")

@app.route('/reviews')
def reviews():
  return render_template("reviews.html")
    
app.run(host='0.0.0.0', port=8080)
