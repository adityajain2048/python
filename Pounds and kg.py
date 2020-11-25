weight = input('weight')
convert = input('Kg(k), L(l)')
if convert.upper() == 'K':
    print(float(weight) / 0.45)
    print('Weight in pounds')
elif convert.upper() == 'L':
    print(f'weight is {float(weight)*0.45}')