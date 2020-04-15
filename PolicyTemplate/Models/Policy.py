from db import db


class PolicyModel(db.Model):
    __tablename__ = 'policies'
    # we need to pick a name
    #id = db.Column(db.Integer, primary_key=True) # we dont need to manually increment the id
    #name = db.Column(db.String(80)) # we need to set a column for each attribute of policy
    # state, sensors etc..
    policies = db.relationship('Sensor', lazy='dynamic')
    # variable that will sav all the sensors related to this policy
    # allocated lazy ( the parameter will get value only when we first use it )
    # we need to decide whether
    # 1: the policy "knows" the sensors related to it
    # 2: every sensor will " know" the policy related to it
    # for now the second is implemented
    def __init__(self, name):
        self.name = name
        # every column in the data base table that represent policy should become class variable

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            # we need to add important data about the policy
         }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #assumed name is unique identifier, if not we need to change it

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
