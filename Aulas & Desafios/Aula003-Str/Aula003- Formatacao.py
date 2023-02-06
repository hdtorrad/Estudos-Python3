# F-strings, .format(), {variavel=}

a = 'aa'
b = 'b'
c= 'c'

string = "A= {}, B={}, C={}".format(a, b, c)

print("Formatação c/ .format() ", string)
print(f'Formatação com {a}')
print(f"{string=}")
