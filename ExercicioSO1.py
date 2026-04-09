import os
Número: float = 0
Maior: float = 0
Menor: float = 0
Contador: int = 0
dir: str = "/tmp/exercicios"
arq: str = "exSO1.txt"

def main():
    pasta:str = ""
    pasta = "/tmp/exercicios"
    os.makedirs(pasta,exist_ok=True)
    os.chmod(pasta,0o744)
    entrada()

def entrada():
    global Número, Maior, Menor, Contador
    linha: str = ""
    Emenor: str = ""
    Emaior: str = ""
    Número = float(input("Digite um número:"))
    while (Número<=0):
        print ("Inválido")
        Número = float(input("Digite outro número:"))
    linha = str(Número) + "\n"
    escreverArq(dir, arq, linha)
    Maior = Número
    Menor = Número
    Contador = Contador + 1
    while (Contador<10):
        Número = float(input("Digite outro número:"))
        while (Número<=0):
            print ("Inválido")
            Número = float(input("Digite outro número:"))
        linha = str(Número) + "\n"
        escreverArq(dir, arq,linha)
        if (Número>=Maior):
            Maior = Número
        if (Número<=Menor):
            Menor = Número
        Contador = Contador + 1 
        Emenor = str(Menor)
        Emaior = str(Maior)
    print (Emenor)
    print (Emaior)
    escreverme_ma(dir,arq,Emenor,Emaior)

def escreverArq (caminho,arquivo,linha_arq):
    file: str = ""
    tipo: str = ""
    enc: str = ""
    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        enc = caminho + "/" + arquivo

        if os.path.exists(enc):
            tipo = 'a'
        else:
            tipo = 'w'

        with open(enc, tipo) as file:
            file.write(linha_arq)

def escreverme_ma(caminho,arquivo,menor,maior):
    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha_menor: str = "Esse é o menor:" + str(menor) + "\n"
    linha_maior: str = "Esse é o maior:" + str (maior) + "\n"
    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        enc = caminho + "/" + arquivo

    if os.path.exists(enc):
        tipo = 'a'
    else:
        tipo = 'w'

    with open(enc, tipo) as file:
        file.write(linha_menor)
        file.write(linha_maior)

if __name__ == '__main__':
    main()

