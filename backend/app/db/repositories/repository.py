from app.db.session import session_scope


class Repository(object):
    def __init__(self, entity_class):
        self.entityClass = entity_class

    def save(self, entity):
        with session_scope() as session:
            session.add(entity)
        return entity

    def get_all(self):
        res = None
        with session_scope() as session:
            res = session.query(self.entityClass).all()
        return res
