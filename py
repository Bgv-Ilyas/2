import random
koloda = [6,7,8,9,10,2,3,4,11] * 4
random.shuffle(koloda)
count = 0
print('Сыграем в 21?')

while True:
    choice = input('Возьмете карту? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Выпало %d' %current)
        count += current
        if count > 21:
            print('Вы проиграли')
            break
        elif count == 21:
            print('Вы набрали 21, вы победили!')
            break
        else:
            print('У вас %d очков.' %count)
    elif choice == 'n':
        print('У вас %d очков и вы проиграли.' %count)
        break

print('Еще увидимся!')
