from flask import Blueprint, request, jsonify
from app.auth.models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Kullanıcı adı zaten kullanılıyor'})

    new_user = User(username, password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Kullanıcı kaydedildi'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        return jsonify({'message': 'Giriş başarılı'})
    else:
        return jsonify({'message': 'Kullanıcı adı veya şifre hatalı'})

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'Çıkış yapıldı'})