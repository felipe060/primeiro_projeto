import tkinter


class Janela():
    def __init__(self):
        self.janela = tkinter.Tk()
        self.tela()
        self.label()
        self.entry()
        self.botao()
        self.funcao_coleta()
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

        return [entry_usuario, entry_senha]

    def botao(self):
        botao_cadastrar = tkinter.Button(self.janela, text='cadastrar', bg='aqua', command=self.funcao_coleta())
        botao_cadastrar.place(x=286, y=200)

        print('entry_usuario -->', self.entry()[0])
        print('entry_senha -->', self.entry()[1])

    def funcao_coleta(self):
        coleta_usuario = self.entry()[0].get().strip()
        coleta_senha = self.entry()[1].get().strip()
        coleta_total = f'{coleta_usuario}\n{coleta_senha}'

        with open(r'../modulo_txt/usuario.txt', 'w') as usuario_txt:
            cadastrar = usuario_txt.write(str(coleta_total))

        return str(coleta_total)


if __name__ == '__main__':
    Janela()
