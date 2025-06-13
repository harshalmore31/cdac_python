from flask import Flask, render_template, app

app=Flask(__name__)

@app.route("/",methods=['GET'])
def getHome():
     return "Welcome Home"

@app.route("/books",methods=['GET'])
def getBooks():
    booklist=["Complete Reference Python","Mastering Python","Deep dive into MySQL"]
    return booklist


if __name__=='__main__':
    app.run(debug=True)
