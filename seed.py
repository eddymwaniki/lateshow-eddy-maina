#!/usr/bin/env python3

from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():

    Episode.query.delete()
    Guest.query.delete()
    Appearance.query.delete()

    guest1 = Guest(name = "Michael J Fox", occupation = "Actor")
    guest2 = Guest(name = "Sade", occupation = "Singer")
    guest3 = Guest(name = "Uma Thurman", occupation = "Televison actress")

    episode1 = Episode(date = "25/02/2004", number = 1)
    episode2 = Episode(date = "23/02/2022", number = 2)
    episode3 = Episode(date = "31/08/2023", number = 3)

    appearance1 =  Appearance(rating = 5, episode_id = 1, guest_id = 2)
    appearance2 = Appearance(rating = 4, episode_id = 2, guest_id = 1)
    appearance3 = Appearance(rating = 4, episode_id = 3, guest_id = 3)

    db.session.add_all([guest1,guest2,guest3,episode1,episode2,episode3,appearance1,appearance2,appearance3])
    db.session.commit()