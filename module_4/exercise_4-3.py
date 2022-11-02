def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + f"Idę na zakupy do {shop}.\n" 
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + f" - {item}\n" 
    result = result + f"By zapłacić, używam {payment}" 
    return result

items = ["cola", "whiskey", "lód"]
text = shopping(items, 'card', 'small local shop')
print(text)

"""
print("Pokażę wszystko, co wpiszesz!")
text = input("Wpisz swoj tekst: ")
print(f"Oto Twój tekst: ***{text}***")
"""

items_text = "cola,whiskey,lód"
items = items_text.split(',')
print(type(items))
print(len(items))

if __name__ == "__main__":
    items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
    items = items_text.split(',')
    shopping_result = shopping(items)
    print(shopping_result)

name_surname = input("Write your name and surname: ")
print(f"Hallo {name_surname}!")

print("Witaj, ten program pomoże Ci sprawdzić czy jesteś pełnoletni/a")
adult = None
sex = input("Podaj proszę swoją płeć [M/K]: ")
if sex == 'M':
    age = int(input("Twój wiek? "))
    adult = age >= 18
elif sex == 'K':
    print("Kobiet o wiek się nie pyta, więc zrobię to delikatnie.")
    over18_yesno = input("Czy miałaś już osiemnastkę? [T/N]?")
    adult = (over18_yesno == 'T')
else:
    print("Nie ma takiej płci!")
    exit(1)
print("Już wiem. Twoja pełnoletniość w boolean to %s" % str(adult))