from src.services.UserActivityService import UserActivityService
from src.models.UserActivityModel import UserActivity
from flask import Blueprint, jsonify, request

main = Blueprint('user_activity_blueprint', __name__)

@main.route('/', methods=['POST'])
def sign_user_activity():
    try:
        user_activity_signed = UserActivityService.register_user(UserActivity(request.json['dni'],request.json['nom_activitat']))
        if(user_activity_signed == 0):
            return jsonify({'success': True, 'message': "Usuari apuntat a activitat"})
        else:
            return user_activity_signed
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'ERROR', 'success': False})

