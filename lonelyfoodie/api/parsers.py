from flask_restx import reqparse


pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                                  default=10, help='Results per page {error_msg}')

restaurant_search_arguments = reqparse.RequestParser()
restaurant_search_arguments.add_argument('name', type=str, required=False)
