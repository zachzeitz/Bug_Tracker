from flask import Blueprint, render_template, flash, request, jsonify  
from flask_login import  login_required, current_user
from .models import Ticket
from . import db 
import json

views= Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        ticket= request.form.get('ticket')
        title= request.form.get('title')

        if len(ticket) < 1:
            flash('Ticket is too short', category='error')
        else:
            new_title= Ticket(data=title, user_id= current_user.id)
            new_ticket= Ticket(data=ticket, user_id=current_user.id)
            db.session.add(new_title)
            db.session.add(new_ticket)
            db.session.commit()
            flash('Ticket posted', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-ticket', methods=['POST'])
def delete_ticket():
    ticket= json.loads(request.data)
    ticketId= ticket['ticketId']
    ticket= Ticket.query.get(ticketId)
    
    if ticket:
        if ticket.user_id == current_user.id:
            db.session.delete(ticket)
            db.session.commit()
    return jsonify({})