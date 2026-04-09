import os
dir: str = "/tmp/exercicios"
arq: str = "exSO3.txt"

def main():
    pasta:str = ""
    pasta = "/tmp/exercicios"
    os.makedirs(pasta,exist_ok=True)
    os.chmod(pasta,0o744)
    numero = int(input("Digite um número:"))
    entrada(numero)

def entrada(n):
    soma = 1
    contador = 1
    while (contador<= n):
        fatorial = f_fatorial(contador)
        resultado = f_divisao(fatorial)
        print("1/", contador,"!")
        escrevefat:str = "1/" + str(contador) + "!" + "\n"
        arquivo (escrevefat)
        soma = soma + resultado
        contador = contador + 1
    print ("soma:",soma)
    global dir, arq
    enc = dir + "/" + arq
    with open(enc, "a") as file:
        file.write("Essa é o resultado da série:" + str(soma))


def arquivo (efat):
    global dir, arq
    file: str = ""
    tipo: str = ""
    enc: str = ""
    if (os.path.exists(dir) and os.path.isdir(dir)):
        enc = dir + "/" + arq
        if os.path.exists(enc):
            tipo = 'a'
        else:
            tipo = 'w'

        with open(enc, tipo) as file:
            file.write(efat)


def f_fatorial(num):
    conte = 1
    fat = 1
    while (conte<=num):
        fat = fat * conte
        conte = conte + 1
    return fat


def f_divisao(fat):
    result = 1/fat
    return result
    
   


if __name__ == "__main__":
    main()