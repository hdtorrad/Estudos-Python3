#  Crie uma mascara para CNPJs

CNPJ = str(input('Insira seu CNPJ(s/espaços): ')).strip()

print(f'{CNPJ[:2]}.{CNPJ[2:5]}.{CNPJ[5:8]}/{CNPJ[8:12]}-{CNPJ[12:]}', '\nCNPJ organizado!')
