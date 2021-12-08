# import tools
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
from scraping import hemisphere

# set up Flask
## this starts a flask application running which is running all the time 
### just like a database waiting for html requests to arrive 
### like GET or POST or PUT or DELETE 
### https://www.tutorialspoint.com/http/http_requests.htm

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
### connect the flask application to the mongo db server 
### you would need to start the mongodb server before starting flask app 
### this is like a website running over port 27017 
### the default database/collection is called mars_app 
## the user is "mongodb"
## localhost means "this computers IP address "

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"

### use pymongo to create a mongo db connection passing the flask app class in as an argument 
mongo = PyMongo(app)


## "/" is the default route . 
# Set Up App Routes

@app.route("/")
def index():
   ### when a request arrives at "/" search mongo DB for a result 
   mars = mongo.db.mars.find_one()
   print("mars: ")
   print(mars)
   ### send the result back. Use the index.html file stored in "templates"
   ### pass the results of the query to the DB back over the internet to the browser
   return render_template("index.html", mars = mars)
   

### if a web requests arrives at this address "/scrape" do this 
### the webpage index.html has a button which using javascript 
### will send a "GET" request .. 
### ie "please send me some html back"

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   print("mars data")
   print(mars_data)
   print("updating mongo table")
   mars.update({}, mars_data, upsert=True) 
   ### redirect the URL in the browser from "/scrape" to "/" and use "code" to send a repsonse 
   ### to the browser 
   # return "Scraping Successful"
   return index()

@app.route("/hi")
def hi():
   return("hi")



### this is python crap for "run this after running any other crap in the file  "

if __name__ == "__main__":
    #### start a flask server up 
   app.run(debug=True)

