from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from app.models import User
from app.models import Course
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from app.forms import ResetPasswordRequestForm
from app.email import send_password_reset_email
from app.forms import ResetPasswordForm
from app.auto_course_generator import generate_topics, generate_body
import os



@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    courses = Course.query.all()
    return render_template('index.html', title='Dashboard', courses=courses)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/explore', methods=['GET','POST'])
@login_required
def explore():
    courses = Course.query.order_by(Course.title).all()
    for c in current_user.courses:
        courses.remove(c)
    
    return render_template('explore.html', title='Explore', courses=courses)

@app.route('/add_course/<course_title>', methods=['GET','POST'])
@login_required
def add_course(course_title):
    course = Course.query.filter_by(title=course_title).first()
    current_user.register(course)
    db.session.commit()
    return redirect('/explore')

@app.route('/remove_course/<course_title>', methods=['GET','POST'])
@login_required
def remove_course(course_title):
    course = Course.query.filter_by(title=course_title).first()
    current_user.deregister(course)
    db.session.commit()
    return redirect('/index')

@app.route('/generate_courses/<course_title>', methods=['GET','POST'])
@login_required
def generate_courses(course_title):
    base = Course.query.filter_by(title=course_title).first()
    base.hasGeneratedRelatedCourses = True
    topics = generate_topics(base)
    for t in topics:
        course = Course(title=t,body=generate_body(t))
        db.session.add(course)
    db.session.commit()
    return redirect('/index')
