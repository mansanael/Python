# Implement an abstract class called product abstract and implement this product abstract in another abstract class called Product Manager
# 
# let the Product Manager inherit from the abstract class, create as many functions in the abstract class as possible

from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class ProductAbstract(ABC):

    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self, product_id):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self, product_id, image):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass


class ProductManager(ProductAbstract, ABC):

    def __init__(self, product: Product):
        self.product = product

    def create_product(self, product: Product):
        print("Product created ")

    def edit_product(self, product_id):
        print("Product edited")

    def get_product_by_id(self, product_id):
        print("Product number x ")

    def get_all_products(self):
        print("This is all products")

    def upload_product_image(self, product_id, image):
        print("Product image uploaded successfully")

    def delete_product(self, product_id):
        print("Product x deleted")


my_product = Product("Biscuits", "Food", "10GHC")

product_tomanage = ProductManager(my_product)

product_tomanage.get_all_products()
