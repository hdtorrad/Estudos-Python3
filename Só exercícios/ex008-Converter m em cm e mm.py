# Crie um código que leia um valor em m e mostre esse mesmo valor em cm e mm

fc = 'CONVERSOR DE m PARA cm E mm'
print(f'{fc:=^50}')
nm = float(input('\nInsira o valor em metro: '))
nkm = nm / 1000
nhm = nm / 100
ndam = nm / 10
ndm = nm* 10
ncm = nm * 100
nmm = nm * 1000
print('O valor em metro dado foi {:.0f}, logo: \ncm={:.0f} \nmm={:.0f}'.format(nm, ncm, nmm))

pe = 'EXTRA'
print(f'{pe:=^20}')
print('km={:.5f} \nhm={:.4f} \ndam={:.3f} \nm={:.2f} \ncm={:.0f} \nmm={:.0f}'.format(nkm, nhm, ndam, nm, ncm, nmm))

