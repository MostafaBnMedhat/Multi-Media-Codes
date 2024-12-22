Text = input()
Counter = 1
TextCompression = ''
for i in range(len(Text)-1):
    if Text[i] == Text[i+1]:
        Counter += 1
    else:

        TextCompression += str(Counter) +Text[i]
        Counter = 1
TextCompression += str(Counter) + Text[-1]
print(TextCompression)