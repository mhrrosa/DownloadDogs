import time
from threading import Thread
import os

inicio = time.time()

rodando = True

arquivo = open("dog.txt", "r")

listaApk = []

for linha in arquivo:
    linha = linha.replace("\r", "")
    linha = linha.replace("\n", "")
    listaApk.append(linha)

arquivo.close()


def download_url(url):
    print("downloading: " + url + "\n")
    os.system("curl http://localhost/dog/" + url + " --ssl-no-revoke -L -O")
    return url


quantidade = len(listaApk)
parte1 = int(quantidade * 1 / 10)
parte2 = int(quantidade * 2 / 10)
parte3 = int(quantidade * 3 / 10)
parte4 = int(quantidade * 4 / 10)
parte5 = int(quantidade * 5 / 10)
parte6 = int(quantidade * 6 / 10)
parte7 = int(quantidade * 7 / 10)
parte8 = int(quantidade * 8 / 10)
parte9 = int(quantidade * 9 / 10)
parte10 = int(quantidade * 10 / 10)


def thread(parte, quantidade):
    for posicao in range(parte, quantidade):
        download_url(listaApk[posicao])


t0 = Thread(target=thread, args=(0, parte1))
t0.start()
t1 = Thread(target=thread, args=(parte1, parte2))
t1.start()
t2 = Thread(target=thread, args=(parte2, parte3))
t2.start()
t3 = Thread(target=thread, args=(parte3, parte4))
t3.start()
t4 = Thread(target=thread, args=(parte4, parte5))
t4.start()
t5 = Thread(target=thread, args=(parte5, parte6))
t5.start()
t6 = Thread(target=thread, args=(parte6, parte7))
t6.start()
t7 = Thread(target=thread, args=(parte7, parte8))
t7.start()
t8 = Thread(target=thread, args=(parte8, parte9))
t8.start()
t9 = Thread(target=thread, args=(parte9, parte10))
t9.start()

while t1.is_alive() or t2.is_alive() or t3.is_alive() or t4.is_alive() or t5.is_alive():
    print('Estou rodando...')
    time.sleep(.5)
    rodando = False
print("Encerrando msg")

fim = time.time()

tempo_total = fim - inicio

print("====================================================")
print(f"O tempo de execução foi de {tempo_total:,.2f} segundos")
print("====================================================")
