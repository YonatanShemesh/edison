from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.Policy import PolicyModel

class Policy(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',  # need to add all policy properties
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )


    #@jwt_required()  if we want the user to be loged in while doing this operation
    def get(self, name):
        policy = PolicyModel.find_by_name(name)
        if policy:
            return policy.json()
        return {'message': f"The policy {name} doesn't exist"}, 404

    def post(self, name):
        if PolicyModel.find_by_name(name):
            return {'message': "Policy with name '{}' already exists.".format(name)}, 400

        data = Policy.parser.parse_args()

        policy = PolicyModel(name, **data)  # creates the policy with all the data the client sent

        try:
            policy.save_to_db()
        except:
            return {"message": "An error occurred inserting the Policy."}, 500

        return policy.json(), 201

    def delete(self, name):
        policy = PolicyModel.find_by_name(name)
        if Policy:
            Policy.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': f"policy named {name} not found."}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        policy = PolicyModel.find_by_name(name)

        if policy:
            pass
            # the policy found which means the user would like to change it (and not add it)
            # so we need to take from var data the data that we want to change in the policy
            # Example: policy.state = data['state']

        else:
            policy = PolicyModel(name, **data)  # the policy doesnt exist so we add it to db

        policy.save_to_db()

        return policy.json()


class PolicyList(Resource):
    def get(self):
        return {'items': [policy.json() for policy in PolicyModel.find_all()]}
