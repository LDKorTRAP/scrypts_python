from tkinter import *
from random import randint
from time import sleep
nums = list()


def sorteia():
    texto_prev['text'] = f'Sorteando números!'
    for c in range(0, 9):
        nums.append(int(randint(0, 100)))
        sleep(.2)

    nums.sort()
    texto = f'{nums}'

    texto_sorteios["text"] = texto

    nums.clear()



janela = Tk()
janela.title('Sorteio')
janela.geometry("400x400")

texto_orientacao = Label(janela, text='Sorteio de números e somatório dos pares')
texto_orientacao.grid(column=0, row=0, padx= 100, pady=10)

botao = Button(janela, text='SORTEAR', command=sorteia)
botao.grid(column=0, row=1, padx= 100, pady=10)

texto_prev = Label(janela, text='')
texto_prev.grid(column=0, row=2, padx= 100, pady=10)

texto_sorteios = Label(janela, text='')
texto_sorteios.grid(column=0, row=3, padx= 100, pady=10)

janela.mainloop()