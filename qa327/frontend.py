"""This file defines the front-end part of the service.

It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder.
"""

from flask import render_template, request, session, redirect, flash
from qa327 import app
from qa327.login_format import (
    is_valid_password, is_valid_username, is_valid_email
)
from qa327.ticket_format import (
    is_valid_ticket_name, is_valid_quantity, is_valid_price, is_valid_date,
    parse_date
)
import qa327.backend as bn
from qa327.authenticate import authenticate

def make_page_with_flash(route):
    '''
    second order function for returning a flash+redirect.
    call like make_page_with_flash('/register')('your message here')
    '''
    def page_with_flash(msg):
        flash(msg)
        return redirect(route, code=303)
    return page_with_flash

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

    login_page = make_page_with_flash('/login')

    if not is_valid_email(email):
        return login_page("Email format is incorrect")

    if not is_valid_password(password):
        return login_page("Password format is incorrect")

    if not is_valid_password(password2):
        return login_page("Password2 format is incorrect")

    if not is_valid_username(name):
        return login_page("Username format is incorrect")

    if password != password2:
        return login_page("The passwords do not match")

    user = bn.get_user(email)

    if user:
        return render_template('register.html', message="User exists")

    if not bn.register_user(email, name, password, password2):
        return login_page("Failed to store user info.")

    return login_page('User registered successfully')

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
    '''Intake all login form information and validate using login_user then redirect to home'''
    email = request.form.get('email')
    password = request.form.get('password')
    user = bn.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        '''
        Session is an object that contains sharing information
        between browser and the end server. Typically it is encrypted
        and stored in the browser cookies. They will be past
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.
        '''
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    flash('email/password combination incorrect')
    return redirect('/login', code=303)

@app.route('/buy', methods=['POST'])
@authenticate
def buy_post(user):
    '''
    Intake all information from the buying ticket form and ensure it meets all requirements
    outlined in R6.
    :return: if invalid information, redirect to user page with error
    :return: if valid information, decrease quantity of tickets and user's balance
    '''
    home_page = make_page_with_flash('/')

    name = request.form.get('ticket-name')
    quantity = request.form.get('ticket-quantity')

    if not is_valid_ticket_name(name):
        return home_page('Invalid ticket name')

    if not is_valid_quantity(quantity):
        return home_page('Invalid ticket quantity')

    buy_status = bn.buy_ticket(user, name, quantity)
    return home_page(buy_status)

@app.route('/sell', methods=['POST'])
@authenticate
def sell_post(user):
    '''
    Intake all information from ticket selling form and validate it meets requirements
    :return: if requirements are not met, redirect to user page with error
    :return: if requirements are met, post ticket information to user page
    '''
    name = request.form.get('ticket-name')
    quantity = request.form.get('ticket-quantity')
    price = request.form.get('ticket-price')
    expiration = parse_date(request.form.get('ticket-expiration-date'))

    home_page = make_page_with_flash('/')

    if not is_valid_ticket_name(name):
        return home_page('Invalid ticket name')

    if not is_valid_quantity(quantity):
        return home_page('Invalid ticket quantity')

    if not is_valid_price(price):
        return home_page('Invalid ticket price')

    if not is_valid_date(expiration):
        return home_page('Invalid ticket date')

    ticket_status = bn.sell_ticket(
        user,
        name, quantity, price, expiration
    )
    return home_page(ticket_status)

@app.route('/update', methods=['POST'])
@authenticate
def update_post(user):
    '''update a ticket using the HTML form'''
    home_page = make_page_with_flash('/')

    prev_ticket_name = request.form.get('previous-ticket-name')
    upt_ticket_name = request.form.get('updated-ticket-name')
    ticket_quantity = request.form.get('ticket-quantity')
    ticket_price = request.form.get('ticket-price')
    ticket_expiration_date = parse_date(request.form['ticket-expiration-date'])

    if not bn.get_ticket(user.id, prev_ticket_name):
        return home_page("Ticket doesn't exist")

    if not is_valid_ticket_name(upt_ticket_name):
        return home_page("Ticket name format is inccorrect")

    if not is_valid_quantity(ticket_quantity):
        return home_page("Ticket quantity format is inccorrect")

    if not is_valid_price(ticket_price):
        return home_page("Ticket price format is inccorrect")

    if not is_valid_date(ticket_expiration_date):
        return home_page("Ticket expiration date format is inccorrect")

    if not bn.update_ticket(user.id, request.form):
        return home_page("Error updating your ticket, please try again")

    return home_page('User updated ticket successfully')

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
def page_not_found(_error):
    """
    Handle 404 errors
    :param error: error message
    :return: display a 404 error page
    """
    return render_template('404.html')
