from faker import Faker
import random

fake = Faker()

company_list = ["ABC", "Samsung", "Allegro", "Simens", "Bosch", "Empik", "Ikea"]
position_list = ["Sales Engineer", "Software Developer", "General Director", "Accountant", "IT Consultant", "HR Specialist", "Technical Support"]

class BusinessCard():
    def __init__(self, name, surname, company, position, e_mail_address):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.e_mail_address = e_mail_address

        #Variables
        self._length_of_name_and_surname = len(self.name) + len(self.surname) + 1
    
    def __str__(self):
        return f"{self.name} {self.surname}, e-mail: {self.e_mail_address}"

    @property
    def length_of_name_and_surname(self):
        return self._length_of_name_and_surname

    def contact(self):
        return f"Contact to: {self}"

def createBusinessCard():
    person = fake.name().split(" ")
    company = random.choice(company_list)
    return BusinessCard(person[0], person[1], random.choice(company_list), random.choice(position_list), f"{person[0].lower()}.{person[1].lower()}@{company.lower()}.com")
business_card_list = []
for i in range (1, 6):
    business_card_list.append(createBusinessCard())

for card in business_card_list:
    print(card)
    print(card.contact())
    print(card.length_of_name_and_surname)

sorted_by_name = sorted(business_card_list, key = lambda card: card.name)
sorted_by_surname = sorted(business_card_list, key = lambda card: card.surname)
sorted_by_e_mail = sorted(business_card_list, key = lambda card: card.e_mail_address)

print("Sorted by name:")
for card in sorted_by_name:
    print(card)

print("Sorted by surname:")
for card in sorted_by_surname:
    print(card)

print("Sorted by e_mail:")
for card in sorted_by_e_mail:
    print(card)