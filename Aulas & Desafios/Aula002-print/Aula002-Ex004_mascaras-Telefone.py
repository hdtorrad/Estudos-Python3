#  Crie uma máscara para telefones


DDD = str(input('Insira o DDD do telefone: ')).strip()
t = str(input('Digite o telefone(s/espaços): ')).strip()

print('', '{}'.format(DDD), sep='(', end=')')
print(' {}'.format(t[:5]), '{}\nSeu telefone está organizado'.format(t[5:]), sep='-', end='!')