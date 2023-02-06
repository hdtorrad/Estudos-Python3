#  Crie uma máscara para telefones

DDD = str(input('Insira o DDD do telefone: ')).strip()
numero_telefone = str(input('Digite o telefone(s/espaços): ')).strip()

print('({}) '.format(DDD), '{}'.format(numero_telefone[:5]), '-{}'.format(numero_telefone[5:]), '\nSeu telefone está organizado!', sep ="")
