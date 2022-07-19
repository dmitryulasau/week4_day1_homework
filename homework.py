from datetime import datetime as dt


class User():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_on = dt.utcnow()

    def change_first_name(self, new_first_name):
        self.first_name = new_first_name
    
    def change_last_name(self, new_last_name):
        self.last_name = new_last_name
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return f"<User | {self.full_name} created on {self.created_on.strftime('%c')}>"
    
    def __repr__(self):
        return f"<User | {self.full_name} created on {self.created_on.strftime('%c')}>"

    def __eq__(self, __o):
        return self.email == __o.email

    def __eq__(self, __o):
        return self.created_on == __o.created_on
    
    def __lt__(self, __o):
        return self.created_on < __o.created_on

    def __gt__(self, __o):
        return self.created_on > __o.created_on
    
    def __le__(self, __o):
        return self.created_onr <= __o.created_on

    def __ge__(self, __o):
        return self.created_onr >= __o.created_on
    
    def __hash__(self):
        return hash(self.full_name + self.created_on.strftime('%c'))

class Employee(User):
    def __init__(
            self, first_name, last_name, email, home_address,
            security_level, department):
        super().__init__(first_name, last_name, email)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department
        self.id = self.full_name + "_" + self.department

    def change_department(self, new_department):
        self.department = new_department

class Customer(User):
    def __init__(
            self, first_name, last_name, email, shipping_address,
            billing_address, purchase_history):
        super().__init__(first_name, last_name, email)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history
        self.id = self.email + "_" + self.shipping_address

    def change_billing_address(self, new_billing_address):
        self.billing_address = new_billing_address

    def change_shipping_address(self, new_shipping_address):
        self.shipping_address = new_shipping_address

# Employees
amazon = Employee(first_name='Jeff', last_name='Bezos', email='jb@amazon.com', home_address='Albuquerque, NM', security_level='prime', department='flea market')

kojima = Employee(first_name='Hideo', last_name='Kojima', email='hiko@kokimap.com', home_address='Tokyo, Japan', security_level='green', department='games')

apple = Employee(first_name='Tim', last_name='Cook', email='timcook@apple.com', home_address='Cupertino, CA', security_level='apple', department='phones')

# Customers
spongebob = Customer('SpongeBob', 'SquarePants', 'sbobsp@bikinibottom.com', 'Pineapple, BB', 'Pineapple ATTN Gary, BB', 'Krabby Patty')

chandler = Customer('Chandler', 'Bing', 'mrbigbing@friends.com', '90 Bedford St, NY', '90 Bedford St, NY', 'Duck, Chicken')

forrest = Customer('Forrest', 'Gump', 'fgumpg@yahoo.com', '3547 Combahee Road, CA', "DON'T NEED", 'Shrimps')

print(spongebob)
users = [spongebob, chandler, forrest, amazon, kojima, apple]
users.sort()

count = 1
for user in users:
    print(f"\n{count}. {user}")
    count += 1

