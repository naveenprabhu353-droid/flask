from flask import Flask, render_template,request

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/course')
def cours():
    return render_template("course.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/register")
def sign():
    return render_template("register.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=='POST':
        name=request.form["name"]#Error
        password=request.form.get("password") #None
        confirm_password=request.form.get("confirm_password")
        email=request.form.get("email")
    
    if not name or not password or not confirm_password or not email:
        return "❌ All Values are Required"
    if len(name)<=3:
        return "❌ Your Name must be 3 characters"
    if len(password)<=3:
        return "❌ The Password is must be 4 values"
    if password!=confirm_password:
        return "❌ The Password is mismatch"
    if "@" not in email or "." not in email:
        return "❌ Enter Valid Email"
    return render_template("login.html",name=name,password=password)


if __name__ == '__main__':
    app.run(debug=True)
