# znajdowanie wzorców
import re
pattern = r"\d{3}-\d{3}-\d{4}"  # np. dopasowuje numer telefonu w formacie 123-456-7890
pattern = r"\w{3}\w?"
text = "Mój numer to 100-456-7890 aaa 143-456-7890 aaaaaa 123-406-7890."
result = re.search(pattern, text)
print(f'findall {re.findall(pattern, text)}')
print(f'result {result}, typ {type(result)}')
if result:
    print("Numer:", result.group())
    print("Kody:", result.groups())

#TODO
# search() wypisuje pierwszy pasujący
# match() podobnie ale musi się string od tego zaczynac inaczej None
# find all znajdzie liste stringów albo liste tupli stringów jak ma byx cięcej elementów