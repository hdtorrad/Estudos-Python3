"""
*Args **Kwargs
"""


def f(*args, **kwargs):
    for a in args:
        print(a)
    print(f'\033[1:31m {kwargs["n"]} \033[m')


lista = [1,2,3,4,5,6,7,8,9,10]
a = "oias"
f(*lista, 20, 50, a, n='Oi')
