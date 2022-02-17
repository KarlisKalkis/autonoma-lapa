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
  return render_template("about.html")

@app.route('/about')
def about():
  return render_template("about.html")


@app.route('/atsauksmes')
def atsauksmes():
  return render_template("reviews.html")

@app.route('/reviews')
def reviews():
  return render_template("reviews.html")

@app.route('/brauksana')
def brauksana():
  return render_template("ride.html")

@app.route('/services')
def services():
  return render_template("services.html")

@app.route('/piedavajumi')
def piedavajumi():
  return render_template("services.html")

@app.route('/signin')
def signin():
  return render_template("sign.html")





    
app.run(host='0.0.0.0', port=8080)
