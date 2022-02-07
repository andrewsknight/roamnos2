valores_romanos = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


# 36 -> XXXVI
def arabigo_a_romano(n):
    romano = ''
    resto = None

    while resto != 0:
        for valor in sorted(valores_romanos.keys(), reverse=True):
            if n >= valor:
                break
        
        cociente = n // valor
        resto = n % valor
        romano += cociente * valores_romanos[valor]
        n = resto
    
    return romano