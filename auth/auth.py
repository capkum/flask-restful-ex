from flask_restful import reqparse, abort, Api, Resource


class CreateUser(Resource):

    def __init__(self, _mysql):
       print ('abc')

    def post(self):

        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userName = args['user_name']
            _userPassword = args['password']

            # conn = self.mysql.connect()

            rt = {
                    'Email': args['email'], 
                    'UserName': args['user_name'],
                    'Password': args['password'],
                    'status': 'success',
                }
            return rt

        except Exception as e:
            rt = {
                'status': 'error',
                'msg': str(e),
            }
            return rt

