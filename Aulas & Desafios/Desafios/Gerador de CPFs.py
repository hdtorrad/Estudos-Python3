"""
CPF = 16899535009
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""
from random import randint
print('\033[1:35m-=-\033[m'*7, '\033[1:37m   GERADOR DE CPF', '\033[1:35m-=-\033[m'*7, sep='\n')
cpf = str(randint(100000000, 999999999))
ssd, spd = 0, 0
cg = 11
if cpf.isnumeric():
    for i in cpf[:10]:
        i = int(i)
        if cg != 2:
            ssd += (i * cg) if not cg == 11 else (11 * i)
            spd += (i * (cg-1)) if not cg == 11 else (10 * i)
            cg -= 1
            continue
        ssd += (i * cg)
        cg -= 1

    ud = str((11 - (spd % 11)) if (11 - (spd % 11)) <= 9 else 0) + str((11 - (ssd % 11)) if (11 - (ssd % 11)) <= 9 else 0)

print('{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:], ud))
