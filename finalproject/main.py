from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from datetime import datetime
from .models import User, Post, Events
from finalproject import create_app
app = create_app()

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts=Post.query.all()
    return render_template("index.html", posts=posts)

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)

@main.route('/about')
def about():
    return render_template("about.html")

@main.route('/createpost', methods=['GET', 'POST'])
@login_required
def createpost():
    if request.method=="POST":
        title=request.form.get('title')
        content=request.form.get('content')
        date=request.form.get('date')
        date = datetime.strptime(date, '%Y-%m-%d').date()
        if current_user.email=="bhatkr01@luther.edu":
            post=Post(title=title, content=content, pub_date=date, author_id=current_user.id)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            return render_template("createpost.html", message="Only Admin can post! Sorry!")
    return render_template("createpost.html")

@main.route('/addevent', methods=['GET', 'POST'])
@login_required
def addevent():
    if request.method=="POST":
        title=request.form.get('title')
        organizer=request.form.get('organizer')
        date=request.form.get('event_date')
        date = datetime.strptime(date, '%Y-%m-%d').date()
        if current_user.email=="bhatkr01@luther.edu":
            event=Events(title=title, organizer=organizer, event_date=date)
            db.session.add(event)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            return render_template("events.html", message="Only Admin can post! Sorry!")
    return render_template("events.html")

@main.route('/viewevents')
def viewevents():
    events=Events.query.all()
    return render_template("view_events.html", events=events)