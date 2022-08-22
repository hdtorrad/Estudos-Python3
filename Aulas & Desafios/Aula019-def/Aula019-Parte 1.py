def saudacao(n='Júlia', m='Meu nome é'):
    print(m, n)


a = input('Qual seu nome: ')
saudacao(a)
saudacao(m='Legal, você se chama', n=a)
saudacao()
