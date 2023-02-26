ps = 'Medo'
ld = []
chances = 3

while True:
    u = input('Digite uma letra: ')
    ld.append(u)
    if u in ps:
        print('Essa letra existe na palavra secreta')
        na = ''
        for i in ps:
            if i in ld:
                na += i
            else:
                na += '*'
        print(na)
    else:
        print('Putss não existe não...')
        chances -= 1
        if chances == 2:
            print('Você ainda tem duas chances')
            print('Dica: Bichinho roxo em um filme')
        elif chances == 1:
            print('Você ainda tem uma chances')
            print('Dica: Um sentimento que quase sempre sentimos...')

    if chances == 0:
        print('\nVocê perdeu!!, pois acabaram suas chances!')
        break
    if na == ps:
        print('Você ganhou!!')
        break
