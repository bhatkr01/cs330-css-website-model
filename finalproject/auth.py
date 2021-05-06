from flask import Blueprint, render_template, redirect, url_for, request, jsonify, make_response
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Post
from flask_login import login_user, logout_user, login_required
import jwt
from functools import wraps

auth = Blueprint('auth', __name__)

@auth.route('/login',  methods=['POST','GET'])
def login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password,password):
            
            return render_template('login.html', message="Invalid Credentials. Please try again.") 

        login_user(user, remember=True)
        return redirect(url_for('main.profile'))
    return render_template('login.html')

@auth.route('/signup', methods=['POST','GET'])
def signup():
    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            
            return render_template('login.html', message="Email address already exists.Please Login!")
        
        new_user=User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))







@auth.route('/user', methods=['GET'])
def get_all_users():
    users=User.query.all()
    result=[]
    for user in users:
        user_data={}
        user_data['id']=user.id
        user_data['name']=user.name
        user_data['email']=user.email
        result.append(user_data)
    data=jsonify({'users': result})
    data.headers["Access-Control-Allow-Origin"]="*"
    data.headers["content-Type"]="application/json"
    return data