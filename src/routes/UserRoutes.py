from src.services.UserService import UserService
from src.models.UserModel import User
from flask import Blueprint, jsonify, request

main = Blueprint('user_blueprint', __name__)

@main.route('/', methods=['POST'])
def resgister_user():
    try:
        user_registered = UserService.register_user(User(request.json['dni'],request.json['nom'],request.json['cognoms'], \
                                                         request.json['edat'],request.json['contrasenya']))
        if(user_registered == 0):
            return jsonify({'success': True, 'message': "Usuari registrat"})
        else:
            return user_registered
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'ERROR', 'success': False})

@main.route('/<string:id>', methods=['PUT'])
def update_user(id):
    try:
        user_updated = UserService.update_user(User(str(id),request.json['nom'],request.json['cognoms'], \
                                                         request.json['edat'],request.json['contrasenya']))
        if(user_updated == 0):
            return jsonify({'success': True, 'message': "Usuari actualitzat"})
        else:
            return user_updated
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'ERROR', 'success': False})

@main.route('/<string:id>', methods=['GET'])
def find_user(id):
    try:
        selected_user = UserService.select_user(User(str(id)))

        if selected_user['status'] == 'success':
            return jsonify({'success': True, 'user': selected_user['data']})
        else:
            return jsonify({'success': False, 'message': selected_user['message']})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'ERROR', 'success': False})

@main.route('/<string:id>', methods=['DELETE'])
def delete_user(id):
    try:
        selected_user = UserService.delete_user(User(str(id)))

        return jsonify({'success': selected_user['status'], 'user': selected_user['message']})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'ERROR', 'success': False})
