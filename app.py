#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///latenightshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Episodes(Resource):
    def get(self):
        episodes_list = [e.to_dict() for e in Episode.query.all()]
        return make_response(jsonify(episodes_list), 200)

api.add_resource(Episodes, '/episodes')

class EpisodebyID(Resource):
    def get(self,id):
        episode_by_id = Episode.query.filter(Episode.id == id).first()
        if episode_by_id:
            return make_response(jsonify(episode_by_id.to_dict()), 200)
        else :
            return make_response(jsonify({'error': 'Episode not found'}), 404)    

api.add_resource(EpisodebyID, '/episodes/<int:id>')

class Guests(Resource):
    def get(self):
        guests_list = [g.to_dict() for g in Guest.query.all()]
        return make_response(jsonify(guests_list), 200)

api.add_resource(Guests, '/guests')

class Appearances(Resource):
    def post(self):
        data = request.get_json()

        new_appearance = Appearance(
            rating = data['rating'],
            episode_id = data["episode_id"],
            guest_id = data["guest_id"],
        )

        db.session.add(new_appearance)
        db.session.commit()

        return make_response(new_appearance.to_dict(), 201)

api.add_resource(Appearances, '/appearances')   

if __name__ == '__main__':
    app.run(port=5555, debug=True)