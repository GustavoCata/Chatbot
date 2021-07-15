# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, Vale muito apena sim pois os produtos são separadamente colhidos, diretamente de suas hortas, garantindo '
              f'sua qualidade e sabor.{os.linesep}')
    if resposta == '2':
        print(f'{os.linesep}{nome}, Temos vários produtos disponíveis, legumes, verduras, especiarias, venha conferir em nosso cardápio {os.linesep}')
    if resposta == '3':
        print(f'{os.linesep}{nome}, Os produtos são entregues toda terça feira da semana {os.linesep}')
    if resposta == '4':
        print(f'{os.linesep}{nome}, Se tiver outras dúvidas, visite nosso site')


def start():
    print("Olá seja bem vindo a Feira de Terça")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    while True:
        resposta = input(f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena comprar na Feira de Terça?{os.linesep}'
              f'[2] - Quais produtos tem disponíveis{os.linesep}[3] Que dia é entregue os produtos? {os.linesep}[4] Outras dúvidas{os.linesep}')
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()