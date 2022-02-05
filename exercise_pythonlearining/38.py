# Write a program having classes as Product, Order, Customer
# Do appropriate inheritance of the above classes
# Write appropriate methods / constructors in each classes
# Following output is expected
# Order No : SO001
# Customer : Sanjay Patel
# Customer Email : sanjay@dummy.com
# Name of the product is 'Pencil'
# Product Qty is : 15
# Unit Price is 20
# Order total is : 300

class Customer:
    def __init__(self,customer , customer_email):
        self.customer = customer
        self.customer_email = customer_email

class Product:
    def __init__(self,prod_name,prod_qty,prod_price):
        self.prod_name = prod_name
        self.prod_qty = prod_qty
        self.prod_price = prod_price

class Order(customer,Product):
    def __init__(self, orderno,customer, customer_email,prod_name, prod_qty, prod_price):
        customer.__init__(self, customer, customer_email)
        Product.__init__(self, prod_name,prod_qty,prod_price)
        self.orderno=orderno
        print(" Order No :{}\n Customer :{}\n Customer Email :{}\n Name of the product is :{}\n Product Qty is :{}\n Unit Price is {}\n Order total is :{}"
              .format(self.orderno,self.customer,self.customer_email,self.prod_name,self.prod_qty,self.prod_price,(self.Qty*self.prod_price)))



o=Order('SO001','Sanjay Patel','sanjay@dummy.com','Pencil',15,20)


