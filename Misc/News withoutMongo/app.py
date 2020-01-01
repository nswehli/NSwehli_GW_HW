
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Newsscraper

# Create an instance of Flask
app = Flask(__name__)

@app.route("/scrape")
def scrape():

    # Run the scrape function
    Data = Newsscraper.scrape()
    

    # Redirect back to home page
    return redirect("/")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html", Data=Data)


# Route that will trigger the scrape function

if __name__ == "__main__":
    app.run(debug=True)

print(Data)
