from random import randint as rn
def game():
    n=rn(int(input('\tот\n')),int(input('\tдо\n')))
    p=int(input('\tпопытки\n'))
    for i in range(p):
        if int(input())==n:
            print('\tвы выиграли\n')
            return
    print('\tвы проиграли\n')
game()
f=input('\tещё раз?\n')
if f=='да':
    game()
else:
    print('\tпока\n')
