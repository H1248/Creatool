from tkinter import *
from tkinter import Tk, ttk

from tkinter import filedialog as fd

from PIL import Image, ImageTk

from tkinter import IntVar

import cv2

# cores -----------------------------------

cor0 = "#f0f3f5"  # preto
cor1 = "#feffff"  # branco
cor2 = "#FFDB1F"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"  # letra
cor5 = "#e06636"  # - profit
cor6 = "#645400" # cor salvar

# criando janela ----------------------------

janela = Tk()
janela.title("")
janela.geometry("300x356")
janela.configure(background=cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# abrindo imagem logo
app_img = Image.open('imagens/logo1.png')
app_img = app_img.resize((50,50))
app_img = ImageTk.PhotoImage(app_img)

# configuracoes topo
app_logo = Label(janela, image=app_img, text="Imagem para > Desenho a lápis", width=300, compound=LEFT, relief=RAISED, anchor=NW, font=("System 10 bold"), bg=cor1, fg=cor4)
app_logo.place(x=0, y=0)
app_logo.image = app_img #codHosana
app_logo.config(image=app_img, padx=10) #codHosana

global imagem_original , l_imagem , imagem

imagem_original = ['']

# funcao para abrir imagem

def escolher_imagem():
    global imagem_original, l_imagem, imagem
    imagem = fd.askopenfilename()
    imagem_original.append(imagem)

    # abrindo a imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)


    l_imagem = Label(janela, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=60, y=60)


# funcao converter imagem

def converter_imagem():
    global imagem_original, l_imagem, imagem

    valor_escala = escala.get()

    # carregar a imagem escolhida
    imagem = cv2.imread(imagem_original[-1])

    # converter uma imagem de espaco de cores para outra
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    desfoco = cv2.GaussianBlur(imagem_cinza, (21,21) , 0,0)

    imagem_para_lapis = cv2.divide(imagem_cinza, desfoco, scale=valor_escala)

    cv2.imwrite('imagens/imagem_corvertida.png', imagem_para_lapis)

    # abrindo a imagem que foi convertida
    imagem = Image.open('imagens/imagem_corvertida.png')
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(janela, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=60, y=60)

# valor inicial da escala
valor_escala = IntVar()
valor_escala.set(255)  # valor inicial da escala como 255

# ------------------ opcoes -------------------

l_opcoes = Label(janela, text="configurações -------------------------------------------".upper(), width=300, anchor=NW, font=("Verdana 7 bold"), bg=cor0, fg=cor4)
l_opcoes.place(x=10, y=260)

escala = Scale(janela,variable=valor_escala, command=converter_imagem ,from_=0, to=255, length=120, bg=cor1, fg='red', orient=HORIZONTAL )
escala.place(x=10, y=300)



b_escolher = Button(janela,command=escolher_imagem, text="Escolher imagem", width=15, overrelief=RIDGE, font=("ivy 10"), bg=cor1, fg=cor4)
b_escolher.place(x=147, y=287)

b_salvar = Button(janela, command=converter_imagem, text="Salvar", width=15, overrelief=RIDGE, font=("ivy 10 bold"), bg=cor2, fg=cor6)
b_salvar.place(x=147, y=317)



janela.mainloop()
