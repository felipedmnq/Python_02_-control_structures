#leia o peso de 5 messoas e mostre qual o maior e qual o menor

bigger = 0
lower = 0

for c in range(1, 6):
    weight = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        bigger = weight
        lower = weight
    else:
        if weight > bigger:
            bigger = weight
        elif weight < lower:
            lower = weight
print('O maior peso cadastrado foi {}kg.'.format(bigger))
print('O menor peso cadastrado foi {}kg.'.format(lower))