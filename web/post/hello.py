from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username=="e" and password=="123":
            print ("welcome, %s !" %username)
            return "<h1>welcome, %s !</h1>" %username
        else:
            print ("login Failure1 !")
            return "<h1>login Failure !</h1>"    
    else:
        print ("login Failure2 !")
        return "<h1>login Failure !</h1>"


if __name__ == '__main__':
    app.run(debug=True)
