from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseDAO:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.query.all()

    def get_by_id(self, id):
        return self.model.query.get(id)

    def save(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity