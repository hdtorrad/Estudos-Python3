from random import randint
import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021m.mp3')
pygame.mixer.music.play()


print('\033[1:34m»' * 48, ' PENSEI EM UM NÚMERO. ADINHIVE SE FOR CAPAZ 😈👿', '»' * 48, sep='\n')

d = input('Escolha seu número de 1 a 5: ')
try:
    d = int(d)
    p = randint(1, 5)

    if d == p:
        print('Filho da puta, me pegou! 😥')
    else:
        print('Acertotu miseravi (¬‿¬)')

except:
    print('ばか')

