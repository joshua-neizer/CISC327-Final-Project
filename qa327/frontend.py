"""This file defines the front-end part of the service.

It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder.
"""

from flask import render_template, request, session, redirect, flash
from qa327 import app
from qa327.login_format import is_valid_password, is_valid_username, is_valid_email
import qa327.backend as bn
from qa327.authenticate import authenticate

@app.route('/register', methods=['GET'])
def register_get():
    """
    If a user is logged in redirect to the home page, otherwise redirect to register
    :return: home page if logged in, register page if not logged in
    """
    if 'logged_in' in session:
        return redirect('/', code=303)
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    """
    Intake register form information and validate that all entered information follows 
    requirements R1 (login) and R2 (register).
    :return: if requirement not met, error page with specific error message
    :return: if requirements met, redirect to login page
    """

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    def error_page(msg):
        """
        Render error message on register page.
        :param msg: text of the error message
        :return: register page with error message
        """
        flash(msg)
        return redirect('/login', code=303)

    if not is_valid_email(email):
        return error_page("Email format is incorrect")

    if not is_valid_password(password):
        return error_page("Password format is incorrect")

    if not is_valid_password(password2):
        return error_page("Password2 format is incorrect")

    if not is_valid_username(name):
        return error_page("Username format is incorrect")

    if password != password2:
        return error_page("The passwords do not match")

    user = bn.get_user(email)

    if user:
        return render_template('register.html', message="User exists")

    if not bn.register_user(email, name, password, password2):
        return error_page("Failed to store user info.")

    flash('User registered successfully')
    return redirect('/login', code=303)


@app.route('/login', methods=['GET'])
def login_get():
    """If user is logged in, redirect to home page, otherwise redirect to login"""
    if 'logged_in' in session:
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    return render_template('login.html', message='Please Login')


@app.route('/login', methods=['POST'])
def login_post():
    """Intake all login form information and validate using login_user then redirect to home"""
    email = request.form.get('email')
    password = request.form.get('password')
    user = bn.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information
        between browser and the end server. Typically it is encrypted
        and stored in the browser cookies. They will be past
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        flash('email/password combination incorrect')
        return redirect('/login', code=303)
        #return render_template('login.html', message='Please Login')

@app.route('/buy', methods=['POST'])
def buy_post():
    '''buy a ticket using the HTML form'''
    flash(bn.buy_ticket(request.form))
    return redirect('/', 303)

@app.route('/sell', methods=['POST'])
@authenticate
def sell_post(user):
    '''
    Intake all information from ticket selling form and validate it meets requirements
    :return: if requirements are not met, redirect to user page with error
    :return: if requirements are met, post ticket information to user page 
    '''
    name = request.form.get('sell-ticket-name')
    quantity = request.form.get('sell-ticket-quantity')
    price = request.form.get('sell-ticket-price')
    expiration = request.form.get('sell-ticket-expiration-date')

    def error_page(msg):
        """
        Render error message on register page.
        :param msg: text of the error message
        :return: register page with error message
        """
        flash(msg)
        return redirect('/', code=303)

    if not is_valid_ticket_name(name):
        return error_page('Invalid ticket name')

    if not is_valid_quantity(quantity):
        return error_page('Invalid ticket quantity')

    if not is_valid_price(price):
        return error_page('Invalid ticket price')

    if not is_valid_date(expiration):
        return error_page('Invalid ticket date')

    flash(bn.sell_ticket(user, request.form))
    return redirect('/', 303)

@app.route('/update', methods=['POST'])
def update_post():
    '''update a ticket using the HTML form'''
    flash(bn.update_ticket(request.form))
    return redirect('/', 303)


@app.route('/logout')
def logout():
    """When user logs out, remove logged in user and redirect to home page
    :return: redirect to home page
    """
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')

@app.route('/')
@authenticate
def profile(user):
    """authentication is done in the wrapper function see above.

    by using @authenticate, we don't need to re-write
    the login checking code all the time for other
    front-end portals
    """
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)

@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors
    :param error: error message
    :return: display a 404 error page
    """
    return render_template('404.html')
