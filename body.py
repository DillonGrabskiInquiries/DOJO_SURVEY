from flask import Flask, render_template
app = Flask(__name__)

@app.route("/result")
def renderLists(name, location, language, comment):
    users = [
    {'name' : 'name'},
    {'dojo_location' : 'location'},
    {'favorite_language' : 'language'},
    {'comment' : 'comment'}
]
    return render_template("index2.html", userDoc = users)

if __name__=="__main__":
    app.run(debug=True)