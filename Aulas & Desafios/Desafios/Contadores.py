"""
Desafio dos contadores:
00 10
01 09
02 08
03 07
04 06
05 05
06 04
07 03
08 02
"""

# i = 10
#
# for j in range(0,9):
#     print(f'{j:0>2} {i:0>2}')
#     i -= 1

for i, j in enumerate(range(10, 1, -1)):
    print(i, j)
