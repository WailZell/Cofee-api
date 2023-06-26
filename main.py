import requests
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class CustomersResource(Resource):
    def get(self):
        url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers"
        response = requests.get(url)
        if response.status_code == 200:
            customers = response.json()
            return customers, 200
        else:
            return [], 404

class OrdersResource(Resource):
    def get(self, customer_id):
        url = f"https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/{customer_id}/orders"
        response = requests.get(url)
        if response.status_code == 200:
            orders = response.json()
            return orders, 200
        else:
            return [], 404

class ProductsResource(Resource):
    def get(self, customer_id, order_id):
        url = f"https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/{customer_id}/orders/{order_id}/products"
        response = requests.get(url)
        if response.status_code == 200:
            products = response.json()
            return products, 200
        else:
            return [], 404

class AllOrdersResource(Resource):
    def get(self):
        url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/orders"
        response = requests.get(url)
        if response.status_code == 200:
            orders = response.json()
            return orders, 200
        else:
            return [], 404

class AllProductsResource(Resource):
    def get(self):
        url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/products"
        response = requests.get(url)
        if response.status_code == 200:
            products = response.json()
            return products, 200
        else:
            return [], 404

api.add_resource(CustomersResource, '/customers')
api.add_resource(OrdersResource, '/customers/<int:customer_id>/orders')
api.add_resource(ProductsResource, '/customers/<int:customer_id>/orders/<int:order_id>/products')
api.add_resource(AllOrdersResource, '/orders')
api.add_resource(AllProductsResource, '/products')

if __name__ == '__main__':
    app.run()
    