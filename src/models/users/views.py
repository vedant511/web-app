from flask import Blueprint, render_template, request, session, url_for
from src.models.users.user import User
import src.models.users.errors as UserErrors

__author__ = 'Vedant Sharma'

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        identifier = request.form['email']
        password = request.form['password']

        try:

            if User.login(identifier, password):
                if User.get_by_mail(identifier) is not None:
                    user = User.get_by_mail(identifier)

                else:
                    user = User.get_by_unm(identifier)

                if user.isAdmin:
                    return render_template('admin.html', name=user.name)
                else:
                    return render_template('profile.html', name=user.name)

        except UserErrors.UserError as e:
            error = e.message
            return render_template('users/login.html', error=error)

    return render_template('users/login.html')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():

    if request.form["submit"] == "login":
        return render_template("login.html")

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        try:
            if User.register(name, email, password, username):
                session['email'] = email
                return render_template("profile.html", name=name)

        except UserErrors.UserError as e:
            error = e.message
            return render_template('users/register.html', error=error)

    return render_template('users/register.html')


@user_blueprint.route('/logout')
def logout_user():
    pass


@user_blueprint.route('/tasks')
def get_user_tasks():
    pass