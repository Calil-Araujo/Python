def fahrenheit():
    temperatura = float(input("Insira uma temperatura em Celsius para converter em Fahrenheit: "))
    calculo = (temperatura*1.8+32)
    print(f"Sua temperatura em Fahrenheit é: {calculo}")

def celsius():
    temperatura = float(input("Insira uma temperatura em Fahrenheit para converter em Celsius: "))
    calculo = ((temperatura-32)*5/9)
    print(f"Sua temperatura em Celcius é: {calculo}")

fahrenheit()
celsius()