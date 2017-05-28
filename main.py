from tkinter import *
from tkinter.ttk import *
import pickle
import random

class App:
    def __init__(self, root=None):
        array_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "p",
                        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        array_buttons = []

        s = Style()

        s.configure('Title.TFrame', background='#00008D')
        s.configure('Container.TFrame')
        s.configure('T.TLabel', background="#00008D", foreground="white", font=("", 35))
        s.configure('D.TLabel', foreground="#00008D", font=("", 15))
        s.configure('D.TEntry', foreground="#00008D")
        s.configure('MenuButtons.TButton', highlightbackground="#C8C4FF", foreground="#00008D", font=("", 15))

        titulo_frame = Frame(root, style='Title.TFrame')
        titulo_frame.place(height=100, width=800)
        titulo_frame.config()

        titulo = Label(titulo_frame, text="JOGO DA FORCA", style='T.TLabel')
        titulo.pack(pady=20)

        main_frame = Frame(root, style='Container.TFrame')
        main_frame.place(height=400, width=800, y=160)
        main_frame.config()

        def novojogo():
            main_frame.destroy()
            frame_iniciar_jogo = Frame(root, style='Container.TFrame')
            frame_iniciar_jogo.place(height=400, width=800, y=160)
            frame_iniciar_jogo.config()

            lbl_nome_jogador = Label(frame_iniciar_jogo, text="Nome do Jogador: ", style='D.TLabel')
            lbl_nome_jogador.pack(pady=20)

            def iniciar():
                frame_iniciar_jogo.destroy()
                frame_jogo_left = Frame(root, style='Container.TFrame')
                frame_jogo_left.place(height=400, width=335, x=50, y=150)
                frame_jogo_left.config()

                frame_jogo_right = Frame(root, style='Container.TFrame')
                frame_jogo_right.place(height=400, width=315, x=435, y=150)
                frame_jogo_right.config()

                palavra = ""
                #escolha da palavra
                inputFile = open("palavras.pkl", 'rb')
                if (difi == "Fácil"):
                    palavras1 = pickle.load(inputFile)
                    palavra = palavras1[random.randint(0,4)]
                elif (difi == "Médio"):
                    palavras2 = pickle.load(inputFile)
                    palavra = palavras2[random.randint(0,4)]
                elif (difi == "Difícil"):
                    palavras3 = pickle.load(inputFile)
                    palavra = palavras3[random.randint(0, 4)]

                # gerador do label que vai representar a palavra
                x = "_"
                y = " _"
                for i in range(len(palavra) - 1):
                    x += y
                print(palavra)
                print(x)

                # Traços
                ##                for i in range(len(palavra)):
                ##                    quantostracos += 1
                ##                tracos = Label(text)
                # botões

                # Forc
                forca = PhotoImage(file="forca0.png")
                label20 = Label(frame_jogo_left, image=forca)
                label20.pack(side="left")

                # palavra = palavras3[random.randint(0,4)]

                def jogar_letra(letra):
                    index = array_letras.index(letra)
                    array_buttons[index].state(["disabled"])

                frame1 = Frame(frame_jogo_right)
                frame1.place(height=380, width=75, x=0)
                frame1.config()
                frame2 = Frame(frame_jogo_right)
                frame2.place(height=380, width=75, x=80)
                frame2.config()
                frame3 = Frame(frame_jogo_right)
                frame3.place(height=380, width=75, x=160)
                frame3.config()
                frame4 = Frame(frame_jogo_right)
                frame4.place(height=380, width=75, x=240)
                frame4.config()

                x = 1
                for i in range(26):
                    if x == 1:
                        array_buttons.append(Button(frame1, text=array_letras[i],
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 2:
                        array_buttons.append(Button(frame2, text=array_letras[i],
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 3:
                        array_buttons.append(Button(frame3, text=array_letras[i],
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 4:
                        array_buttons.append(Button(frame4, text=array_letras[i],
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                        x = 0
                    x += 1

            iniciar = Button(frame_iniciar_jogo, text="Iniciar", style='MenuButtons.TButton', command=iniciar)

            def callback(nome):
                if nome.get() != "":
                    iniciar.state(["!disabled"])
                else:
                    iniciar.state(["disabled"])

            nome = StringVar()
            nome.trace("w", lambda name, index, mode, nome=nome: callback(nome))
            nome_jogador = Entry(frame_iniciar_jogo, style='D.TEntry', font=("", 15), width=30,
                                 textvariable=nome)
            nome_jogador.pack()

            lbl_dificuldade = Label(frame_iniciar_jogo, text="Dificuldade: ", style='D.TLabel')
            lbl_dificuldade.pack(pady=20)

            lista = StringVar(frame_iniciar_jogo)
            lista.set("Fácil")
            dificuldade = OptionMenu(frame_iniciar_jogo, lista, "Fácil", "Fácil", "Médio", "Difícil", style='D.TLabel')
            dificuldade.pack()
            difi = lista.get()

            def voltar():
                root.destroy()
                newroot = Tk()
                newroot.geometry("800x600+50+50")
                App(newroot)
                newroot.mainloop()

            iniciar.pack(pady=50)
            iniciar.state(["disabled"])

            voltar = Button(frame_iniciar_jogo, text="Voltar", style='MenuButtons.TButton', command=voltar)
            voltar.pack()

        novo_jogo = Button(main_frame, text="        Novo Jogo       ", style='MenuButtons.TButton', command=novojogo)
        novo_jogo.pack(pady=20)
        continuar_jogo = Button(main_frame, text="     Continuar Jogo    ", style='MenuButtons.TButton')
        continuar_jogo.pack(pady=20)
        placares_jogo = Button(main_frame, text="         Placares         ", style='MenuButtons.TButton')
        placares_jogo.pack(pady=20)
        gerenciar_palavras = Button(main_frame, text="  Gerenciar Palavras ", style='MenuButtons.TButton')
        gerenciar_palavras.pack(pady=20)

root = Tk()
root.geometry("800x600+50+50")
App(root)
root.mainloop()
