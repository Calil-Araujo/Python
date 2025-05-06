def celsius_fahrenheit():
    get_temp_c = float(input("Insira uma temperatura em Celsius para converter em Fahrenheit: "))
    calculo = (get_temp_c*1.8+32)
    return calculo

temp_fah = celsius_fahrenheit()

print(f"Sua temperatura em Fahrenheit é: {temp_fah}")

def fahrenheit_celsius():
    get_temp_f = float(input("Insira uma temperatura em Fahrenheit para converter em Celsius: "))
    calculo = round(((get_temp_f-32)*5/9), 2)
    return calculo

temp_cel = fahrenheit_celsius()

print(f"Sua temperatura em Celcius é: {temp_cel}")