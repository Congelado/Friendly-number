from sys import exit
def sumdivisors(num):
    """
    Args:
        num(int): enter a list of whole numbers to have all their divisors

    Returns:
        int : returns the sum of all divisors
    """
    lista = [divisor for divisor in range(1, num)if num % divisor == 0]
    return sum(lista)


while True:
    try:
        user1, user2= int(input('write the first number: ')),int(input('write the second number: '))
    except:
        continue

    if  user1 == sumdivisors(user2) and user2 == sumdivisors(user1):
        resultado = 'the number {} {} are friends of the soul.'
    else:
        resultado = 'The number {} {} are not friends of the soul.'

    print(resultado.format(user1, user2))

    while True:     
        if (repetidor := input('do you want to use the program again? yes/No: ').upper()) == 'NO':
            exit(0)
        elif repetidor == 'YES':
            break
