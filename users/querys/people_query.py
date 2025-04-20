from models.people import People
from database.db_sqlalchemy import db

class PeopleQuerys:
    
    def get_all_peoples(self):
        return People.query.all()
    
    def get_people_by_id(self, people_id):
        return People.query.get(people_id)
    
    def create_people(self, data:dict):
        people_new = People(**data)
        db.session.add(people_new)
        db.session.commit()
        return people_new
    
    def update_people(self, people_id:int, data:dict):
        people = People.query.filter_by(id=people_id).update(data)
        db.session.commit()
        return people
    
    def delete_people(self, people: People):
        db.session.delete(people)
        db.session.commit()
    
    
    