'''
Laço for
Iteração de str
range(star = 0, fim , step = +1)
'''

a = 'All I want is nothing more, to get an cancer as bestfriend'
na = ''
u = input('Digite a letra que deseja ficar maiuscula: ')
l = input('Digite a letra que deseja ficar minuscula: ')
for i in range(0,len(a)):
    if a[i] == u:
        na += a[i].upper()
    elif a[i] == l:
        na += a[i].lower()
    else:
        na += a[i]
    print(na)

print('\n\n', na)
