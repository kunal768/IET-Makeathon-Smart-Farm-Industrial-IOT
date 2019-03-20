from flask import *
app = Flask(__name__)
from random import randint


import scripts.firedb as firedb
import scripts.radiationdb as radiationdb
import scripts.raindb as raindb
import scripts.soildb as soildb
import scripts.tempdb as tempdb
import os

# main routes
@app.route("/",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        global user_name
        user_name = request.form["username"]
        return render_template("welcome.html",name = user_name)




@app.route("/lobby",methods = ["GET"])
def welcome():
    if request.method == "GET":
        return render_template("welcome.html",name = user_name)



# services
@app.route("/cattle")
def cattle_monitoring():
    # heat humidity temp glow
    return render_template("livestock.html")

@app.route("/AGV")
def agv_monitoring():
    # just camera
    # cloud monitoring
    return redirect(url_for("welcome"))

@app.route("/drone_feed")
def drone_feed():
    # just camera
    return redirect(url_for("welcome"))

@app.route("/fieldcare")
def field():
    # temp hum heat moist rain fire
    return render_template("field.html")

# sensors
@app.route("/light", methods = ["GET"])
def glow():
    if request.method == "GET":
        f = open("light.txt","w+")
        (status,time) = radiationdb.returnval()
        f.write(status+" "+time+"\n")
        return render_template("feed.html" , sensor = "light" , status = status , time = time)


@app.route("/soil", methods = ["GET"])
def soil():
    if request.method == "GET":
        f = open("soil.txt","w+")
        (status,time) = soildb.returnval()
        f.write(status+" "+time+"\n")
        return render_template("feed.html" , sensor = "soil" , status = status , time = time)


@app.route("/fire", methods = ["GET"])
def fire():
    if request.method == "GET":
        f = open("fire.txt","w+")
        (status,time) = firedb.returnval()
        f.write(status+" "+time+"\n")
        return render_template("feed.html" , sensor = "fire" , status = status , time = time )


@app.route("/rain", methods = ["GET"])
def rain():
    if request.method == "GET":
        f = open("rain.txt", "w+")
        (status,time) = raindb.returnval()
        f.write(status+" "+time+"\n")
        return render_template("feed.html" , sensor = "rain" , status = status , time = time)

@app.route("/temp", methods = ["GET"])
def temp():
    if request.method == "GET":
        f = open("temp.txt","w+")
        # (temp,time,humidity) = tempdb.returnval()
        list = tempdb.returnval()
        temp = list[0]
        time = list[1]
        humidity = list[2]
        f.write(temp +" "+time+" "+humidity+"\n")
        return render_template("feed_temp.html", sensor = "temperature and humidity", temp = temp , time = time , humidity = humidity)

@app.route("/prediction")
def predict():
    if request.method == "GET":
        os.system("jupyter notebook predict.ipynb")
        return redirect(url_for("welcome"))



if  __name__ == "__main__":
    app.run(debug =True)
