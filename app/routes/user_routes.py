from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.user import User
from passlib.hash import sha256_crypt

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    email = data.get("email").lower()
    password = data.get("password")
    phone_number = data.get("phone_number")
    first_name = data.get("first_name")
    last_name = data.get("last_name")

    missing_any_user_data = not email or not password or not phone_number or not first_name or not last_name

    if missing_any_user_data:
        return make_response(jsonify({"message": "Email, password, phone number, first name, and last name are required."}), 400)

    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return make_response(jsonify({"message": "Email already registered."}), 409)
    
    existing_phone_number = User.query.filter_by(phone_number=phone_number).first()
    if existing_number:
        return make_response(jsonify({"message": "Phone number already registered."}), 409)

    # hashing password
    hashed_password = sha256_crypt.encrypt(password)

    new_user = User(
        email=email,
        hashed_password=hashed_password, 
        phone_number=phone_number,
        first_name=first_name,
        last_name=last_name)
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict(), 201