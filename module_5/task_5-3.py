from faker import Faker
import random

fake = Faker()

e_mail_ending = ["gmail.com", "wp.pl", "op.pl", "edu.pl", "mail.com"]
company_list = ["ABC", "Samsung", "Allegro", "Simens", "Bosch", "Empik", "Ikea"]
position_list = ["Sales Engineer", "Software Developer", "General Director", "Accountant", "IT Consultant", "HR Specialist", "Technical Support"]

class BaseContact():
    def __init__(self, name, surname, e_mail, phone):
        self.name = name
        self.surname = surname
        self.e_mail = e_mail
        self.phone = phone
        #Variables
        self._label_length = len(self.name) + len(self.surname) + 1
    
    @property
    def label_length(self):
        return self._label_length
    
    def contact(self):
        return f"I dial the number {self.phone} and call to {self.name} {self.surname}"
    
    def __str__(self):
        return f"{self.name} {self.surname}, e-mail: {self.e_mail}, phone: {self.phone}"

class BusinessContact(BaseContact):
    def __init__(self, business_phone, position, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone = business_phone
        self.position = position
        self.company = company
    
    def contact(self):
        return f"I dial the number {self.business_phone} and call to {self.name} {self.surname}"
    
    def __str__(self):
        return f"{self.name} {self.surname}, {self.position} in {self.company}\ne-mail: {self.e_mail}, phone: {self.phone}, business phone: {self.business_phone}"

def create_contact(contact_type):
    person = fake.name().split(" ")
    phone = "+48" + str(random.randrange(100000000, 1000000000))
    business_phone = "+48" + str(random.randrange(100000000, 1000000000))
    company = random.choice(company_list)
    if (issubclass(contact_type, BusinessContact)):
        return BusinessContact(name = person[0], surname = person[1], company = company, position = random.choice(position_list), e_mail = f"{person[0].lower()}.{person[1].lower()}@{company.lower()}.com", phone = phone, business_phone = business_phone)
    else:
        return BaseContact(name = person[0], surname = person[1], e_mail = f"{person[0].lower()}.{person[1].lower()}@{random.choice(e_mail_ending)}", phone = phone)

def create_contact_list(contact_type, amount):
    card_list = []
    for i in range(amount):
        card_list.append(create_contact(contact_type))    
    return card_list

business_contact_list = create_contact_list(BusinessContact, 2)
base_contact_list = create_contact_list(BaseContact, 3)

for item in business_contact_list:
    print(item)
    print(item.contact())

for item in base_contact_list:
    print(item)
    print(item.contact())