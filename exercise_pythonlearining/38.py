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

class customer:
    def __init__(self,Customer , CustomerEmail):
        self.Customer = Customer
        self.CustomerEmail = CustomerEmail

class Product:
    def __init__(self,Name,Qty,price):
        self.Name = Name
        self.Qty = Qty
        self.price = price

class Order(customer,Product):
    def __init__(self, orderno,Customer, CustomerEmail,Name, Qty, price):
        customer.__init__(self, Customer, CustomerEmail)
        Product.__init__(self, Name,Qty,price)
        self.orderno=orderno
        print(" Order No :{}\n Customer :{}\n Customer Email :{}\n Name of the product is :{}\n Product Qty is :{}\n Unit Price is {}\n Order total is :{}"
              .format(self.orderno,self.Customer,self.CustomerEmail,self.Name,self.Qty,self.price,(self.Qty*self.price)))



o=Order('SO001','Sanjay Patel','sanjay@dummy.com','Pencil',15,20)


