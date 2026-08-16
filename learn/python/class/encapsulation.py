
class Order:
    def __init__(self, customer_name,items,total_amount,discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount

    def __calculate_final_amt(self):
        return self.__total_amount-self.__discount
    
    def get_admin_view(self):
       return {
            "customer": self.customer_name,
            "items": self.items,
            "Total Amount": f"{self.__total_amount}" ,
            "Discount":f"{self.__discount}",
            "Final Bill": f"{self.__calculate_final_amt()}",

        }
    def get_customer_value(self):
        return {
            "customer": self.customer_name,
            "items": self.items,
            "Final Bill": f"{self.__calculate_final_amt()}",

        }

class AdminPortal:
    def show_admin_order(sel,order):
        return order.get_admin_view()
class CustomerPortal:
    def show_customer_order(self,order):
        return order.get_customer_value()

order=Order(customer_name="balamurugan",items=["coke","pepsi"],total_amount=150,discount=10)

# order.__calculate_final_amt()
# order.get_customer_value()


admin=AdminPortal()
print("admin show details")
print(admin.show_admin_order(order))

customer=CustomerPortal()
print("customer details")
print(customer.show_customer_order(order))


