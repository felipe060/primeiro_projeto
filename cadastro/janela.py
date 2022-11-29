import tkinter


class Funcoes():
    def funcao_coleta(self):
        pass


class Janela(Funcoes):
    def __init__(self):
        self.janela = tkinter.Tk()
        self.tela()
        self.label()
        self.entry()
        self.botao()
        self.janela.mainloop()

    def tela(self):
        self.janela.geometry('400x400+100+100')
        self.janela['background'] = 'black'
        self.janela.title('cadastro')
        self.janela.resizable(height=False, width=False)

    def label(self):
        label_usuario = tkinter.Label(self.janela, text='usuario', bg='black', fg='white')
        label_usuario.place(x=40, y=60)

        label_senha = tkinter.Label(self.janela, text='senha', bg='black', fg='white')
        label_senha.place(x=40, y=120)

        label_resposta = tkinter.Label(self.janela, text='', bg='black', fg='white')
        label_resposta.place(x=40, y=200)

    def entry(self):
        entry_usuario = tkinter.Entry(self.janela, width=50)
        entry_usuario.place(x=40, y=80)

        entry_senha = tkinter.Entry(self.janela, width=50, show='*')
        entry_senha.place(x=40, y=140)

    def botao(self):
        botao_cadastrar = tkinter.Button(self.janela, text='cadastrar', bg='aqua')
        botao_cadastrar.place(x=286, y=200)


if __name__ == '__main__':
    Janela()
