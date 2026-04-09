import os

dir: str = "/tmp/exercicios"
arq1: str = "exSO1.txt"
arq2: str = "exSO2.txt"


def lerarquvio ():
    global dir, arq1, arq2
    file: str = ""
    enc1: str = ""
    numero: int = 0
    enc1 = dir + "/" + arq1
    with open (enc1,'r') as file:
        for linha in file:
            if ( not (("maior" in linha) or ("menor" in linha))):
                numero = int(float(linha.strip()))
                if (numero%5==0):
                    escreverarquivo(numero)

def escreverarquivo(valor):
    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo: str = ""
        enc2: str = ""
        enc2 = dir + "/" + arq2
        if os.path.exists(enc2):
            tipo = 'a'
        else:
            tipo = 'w'
        with open(enc2, tipo) as file:
            file.write((str(valor)) +"\n")

def main():
    pasta:str = ""
    pasta = "/tmp/exercicios"
    os.makedirs(pasta,exist_ok=True)
    os.chmod(pasta,0o744)
    lerarquvio()

if __name__ == "__main__":
    main()

         