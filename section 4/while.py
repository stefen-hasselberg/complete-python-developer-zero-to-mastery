# While loops

i = 0

while i < 50:
    print(i)
    i += 1
else:
    print("done with all the work")


while True:
    print("do some work")
    break

while True:
    response = input("say something")
    if response == 'bye':
        break
