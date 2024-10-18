from flask import Blueprint, jsonify, render_template
from models import Offer, Order, DeliveryPerson  # Import your models here

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/offer_of_the_day')
def offer_of_the_day():
    # Fetch the offer of the day. For now, we're just getting the first offer as an example.
    offer = Offer.query.first()  # You might want to add logic to fetch the actual "offer of the day"
    
    if offer:
        return jsonify({
            'restaurant_name': offer.restaurant.name,
            'description': offer.description,
            'price': offer.price,
            'reviews': offer.reviews,
            'image_url': offer.image_url,
            'phone_number': offer.restaurant.phone_number
        })
    else:
        return jsonify({'error': 'No offers available'}), 404