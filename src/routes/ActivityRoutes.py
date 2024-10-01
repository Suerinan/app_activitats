from src.services.ActivityService import ActivityService
from src.models.ActivityModel import Activity
from flask import Blueprint, jsonify, request

main = Blueprint('activity_blueprint', __name__)

@main.route('/', methods=['POST'])
def create_activity():
    try:
        activity_created = ActivityService.create_activity(Activity(request.json['nom'],request.json['descripció'], \
                                                                    request.json['capacitat_màxima']))
        if(activity_created == 0):
            return jsonify({'success': True, 'message': "Activitat creada"})
        else:
            return activity_created
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'ERROR', 'success': False})

@main.route('/name', methods=['GET'])
def find_activity():
    try:
        selected_activity = ActivityService.select_activity(Activity(request.json['nom']))

        if selected_activity['status'] == 'success':
            return jsonify({'success': True, 'activity': selected_activity['data']})
        else:
            return jsonify({'success': False, 'message': selected_activity['message']})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'ERROR', 'success': False})
