"""This file defines all backend logic that interacts with database and other services"""

from werkzeug.security import generate_password_hash, check_password_hash
from dateutil.parser import parse as parse_date
from qa327.models import db, User, Ticket

def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=5000)

    db.session.add(new_user)
    db.session.commit()
    return True


def get_all_tickets():
    """Going to be implemented when /sell and /buy is implemented"""
    return Ticket.query.all()

def get_ticket(seller, ticket_name):
    ticket = Ticket.query.filter_by(seller_id=seller, name=ticket_name).first()
    return ticket

def buy_ticket(form):
    '''buy a ticket, returns a message'''
    raise "TODO"

def sell_ticket(user, form):
    '''sell a ticket, returns a message'''
    ticket = Ticket(
        name=form['ticket-name'],
        quantity=form['ticket-quantity'],
        price=form['ticket-price'],
        expires=parse_date(form['ticket-expiration-date']),
        seller=user
    )
    db.session.add(ticket)
    db.session.commit()
    return 'ticket sold successfully'

def update_ticket(seller, form, isBlank):
    '''update a ticket, returns a boolean'''
    ticket = get_ticket(seller,  form['previous-ticket-name'])

    if not isBlank['name'] == 0:
        ticket.name = form['updated-ticket-name']

    if not isBlank['quantity'] == 0:
        ticket.quantity = form['ticket-quantity']

    if not isBlank['price'] == 0:
        ticket.price = form['ticket-price']

    if not isBlank['exp-date'] == 0:
        ticket.expires = form['ticket-expiration-date']

    db.session.commit()

    return True
