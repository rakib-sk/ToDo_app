from flask import Blueprint, request, redirect, url_for, session, flash

auth_bp = Blueprint("/auth", __name__) 

USER_VALIDATION = {
    "username":"admin",
    "password":"1234"
}

@auth_bp.route("/login",methods=["GET","POST"]) 
def login():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == USER_VALIDATION["username"] and password == USER_VALIDATION["password"]:
            session["user"] = username
            flash("Login successfully")
        else:
            flash("Invalid username or password") 
            
    return render_template("login.html")
    
    
@auth_bp.route("/logout") 
def logout():
    session.pop("user", None) 
    flash("loggoued successfully!")
    
    return redirect(url_for("auth.login")) 
    
    