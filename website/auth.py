from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import check_password_hash, generate_password_hash 
from . import db
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form 
    print(data)
    if request.method == "POST": 
        email = request.form.get("email")
        password1 = request.form.get("password1")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password1): 
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else: 
                flash("Incorrect password, try again!", category="error")
        else: 
            flash("Email does not exist, sign up first!", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST": 
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Account already exists, go to login page!", category="error")
        elif len(email) < 5: 
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2: 
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2: 
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7: 
            flash('Password must be of atleast 7 characters.', category='error')
        else: 
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!.', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
