import numpy as np
import cv2
import matplotlib.pyplot as plt

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]


def gerar_mensagem(mensagem):
    lista = []
    for m in mensagem:
        val = ord(m)
        bits = bitfield(val)

        if len(bits) < 8:
            for a in range(8 - len(bits)):
                bits.insert(0, 0)
        lista.append(bits)
    arr = np.array(lista)
    arr = arr.flatten()
    return arr


def abrirImagem():
    img = cv2.imread(input("Digite o nome da imagem: "))
    img2 = img.copy()

    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            if img2[i, j, 2] % 2 != 0:
                img2[i, j, 2] = img2[i, j, 2] - 1
    return img2


def abrirArquivoTXT():
    arquivo = open((input("Digite o nome do arquivo txt: ")), "r")
    texto = arquivo.read()
    message_Binary = gerar_mensagem(texto)
    arquivo.close()
    return message_Binary


def encriptar():
    message_bi = abrirArquivoTXT()
    img = abrirImagem()
    limite = message_bi.shape[0]
    cont = 0

    for i in range(img.shape[0]):
        if cont >= limite:
            break
        for j in range(img.shape[1]):
            if cont >= limite:
                break
            elif message_bi[cont] == 1:
                img[i, j, 2] = img[i, j, 2] + 1
            cont = cont + 1
    cv2.imwrite(input("Digite o nome da imagem a ser gravada: "), img)
    return img


def converter_mensagem(saida):
    bits = np.array(saida)
    mensagem_out = ''
    bits = bits.reshape(int(len(saida) / 8), 8)
    for b in bits:
        sum = 0
        for i in range(8):
            sum += b[i] * (2 ** (7 - i))
        mensagem_out += chr(sum)
    return mensagem_out


def descriptografar():
    texto = []
    test = cv2.imread(input("Digite o nome da imagen acompanhado de sua extenção: "))
    img = test.copy()
    cont = 0
    cont_aux = 0

    for i in range(img.shape[0]):
        if cont > 7 and cont_aux > 7:
            break
        elif cont_aux > 7:
            cont_aux == 0
        for j in range(img.shape[1]):
            if cont > 7 and cont_aux == 7:
                break
            elif cont_aux > 7:
                cont_aux == 0
            if img[i, j, 2] % 2 != 0:
                texto.append(1)
                cont = 0
                cont_aux = cont_aux + 1
            else:
                cont = cont + 1
                cont_aux = cont_aux + 1
                texto.append(0)
        print(texto)
        mensagen = converter_mensagem(texto)
    return mensagen


comando = input("Escolha uma opção. e para encriptar e d para descriptar: ")
if comando == "e":
    encriptar()
elif comando == "d":
    print(descriptografar())
else:
    print("opção invalida")