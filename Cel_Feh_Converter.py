def cel_to_fah(res):
    return (res*(9/5))+32


def fah_to_cel(res):
    return (res-32)*(5/9)


degree = int(input("1. Celsius to Fahrenheit \n2.Fahrenheit to Celsius\n"))

if(degree == 1):
    res = int(input("Celsius: "))
    print(f'Fahrenheit: {cel_to_fah(res)}')
else:
    res = int(input("Fahrenheit: "))
    print(f'Celsius: {fah_to_cel(res)}')
