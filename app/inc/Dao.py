from app import db
from exception import ResponseException


class Dao:


    @classmethod
    def read_all(cls):
        exist = cls.query.all()
        db.session.close()
        return exist


    @classmethod
    def read(cls, class_id):
        instance = cls.query.get(class_id)
        db.session.close()
        return instance


    def create(self):
        data = self.as_dict()
        data.pop('id')
        
        query = self.__class__(**data)
        db.session.add(query)
        try:
            db.session.commit()
            self.id = query.id
        except:
            raise ResponseException('Could not create the instance', 500)
        finally:
            db.session.close()


    def update(self):
        instance = self.as_dict()
        class_id = instance.pop('id')

        old_class = self.__class__.query.get(class_id)
        if not old_class:
            db.session.close()
            raise ResponseException(f'{self.__class__.__name__}.id: {class_id}', 404)

        for k, v in instance.items():
            setattr(old_class, k, v)

        try:
            db.session.commit()
        except:
            raise ResponseException('Could not update the instance', 500)
        finally:
            db.session.close()


    @classmethod
    def delete(cls, class_id):
        instance = cls.query.get(class_id)
        if not instance:
            raise ResponseException(f'{cls.__name__}.id: {class_id}', 404)

        db.session.delete(instance)
        db.session.commit()
        db.session.close()
        return instance
