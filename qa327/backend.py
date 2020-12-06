"""This file defines all backend logic that interacts with database and other services"""

from werkzeug.security import generate_password_hash, check_password_hash
from qa327.models import db, User, Ticket
from qa327.ticket_format import parse_date

# factor of 1.4 accounts for service fee (35%) + tax (5%)
COST_TO_PRICE_RATIO = 1.4

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
    """
    Gets a ticket by a given seller and ticket name
    :param seller: the user who is selling the ticket
    :param ticket_name: the name of the ticket
    :return: a ticket that has the matched seller and name
    """
    ticket = Ticket.query.filter_by(seller_id=seller, name=ticket_name).first()
    return ticket

def get_ticket_byname(ticket_name):
    """
    Gets a ticket by ticket name
    :param ticket_name: the name of the ticket
    """
    ticket = Ticket.query.filter_by(name=ticket_name).first()
    return ticket

def buy_ticket(user, name, buy_quantity):
    '''buy a ticket, returns a message'''
    ticket = get_ticket_byname(name)    

    if ticket is None:
        return 'No such ticket exists'

    if int(ticket.quantity) < buy_quantity:
        return 'Not enough tickets available'

    ticket_cost = ticket.price*buy_quantity*COST_TO_PRICE_RATIO
    if user.balance < ticket_cost:
        return 'Account balance is too low'

    ticket.quantity -= buy_quantity
    user.balance -= ticket_cost
    db.session.commit()

    return 'Ticket bought successfully'

def sell_ticket(user, name, quantity, price, expiration):
    '''sell a ticket, returns a message'''
    ticket = Ticket(
        name=name,
        quantity=quantity,
        price=price,
        expires=expiration,
        seller=user
    )
    db.session.add(ticket)
    db.session.commit()
    return 'ticket sold successfully'

def safe_parse_date(date_string):
    '''
    parses a date,
    returning none for the empty string case
    '''
    return (
        None
        if date_string == '' else
        parse_date(date_string)
    )

def update_ticket(seller, form):
    """
    Updates a ticket within the the database
    :param seller: the user who is selling the ticket
    :param form: a form containing all of the new information for the ticket
    :param form: a dictionary that indicates if a field was left blank
    :return: a boolean indicating if the ticket successfull updated
    """
    ticket = get_ticket(seller, form['previous-ticket-name'])

    ticket.name = form['updated-ticket-name'] or ticket.name
    ticket.quantity = form['ticket-quantity'] or ticket.quantity
    ticket.price = form['ticket-price'] or ticket.price
    ticket.expires = (
        safe_parse_date(form['ticket-expiration-date']) or
        ticket.expires
    )

    db.session.commit()

    return True
