from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.booking import Booking
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d %H:%M:%S')

        new_booking = Booking(name=name, email=email, phone=phone, date=date)
        db.session.add(new_booking)
        db.session.commit()

        return redirect(url_for('index'))

    bookings = Booking.query.all()
    return render_template('booking.html', bookings=bookings)
