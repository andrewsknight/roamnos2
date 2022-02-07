valores_romanos = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

valores_romanosT = [
    (1000, 'M'),
    (500, 'D'),
    (100, 'C'),
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
]

# 36 -> XXXVI
def arabigo_a_romano(n):
    romano = ''
    resto = None

    while resto != 0:
        for valor, simbolo in valores_romanosT:
            if n >= valor:
                break
        
        cociente = n // valor
        resto = n % valor
        if cociente > 3:
            romano +='*'

        else:
            romano += cociente * simbolo
            n = resto
    
    return romano