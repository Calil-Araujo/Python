def verificador_par_impar():
    get_num = float(input("Insira um número para verificar se é par ou impar: "))
    num = get_num
    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é impar.")
    return 

verificador_par_impar()