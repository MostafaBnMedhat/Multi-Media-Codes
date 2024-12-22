Encoding = input()
Decoding =''
numbers = ''
list_number= []
list_character = []
for element in Encoding:
    if element.isdigit():
        numbers += element
    else:
        if numbers:
            list_number.append(int(numbers))
            numbers = ''
    if not element.isdigit():
     list_character.append(element)
print(list_number)
print(list_character)

for i in range(len(list_number)-1):
    Decoding += list_number[i]*list_character[i]
Decoding += list_number[-1]*list_character[-1]
print(Decoding)