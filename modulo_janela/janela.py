
if __name__ == '__main__':
    import tkinter


    def funcao_coleta():
        coleta_usuario = entry_usuario.get().strip()
        coleta_senha = entry_senha.get().strip()
        coleta_total = f'{coleta_usuario}\n{coleta_senha}'

        with open(r'../modulo_txt/usuario.txt', 'w') as usuario_txt:
            cadastrar = usuario_txt.write(str(coleta_total))

        from modulo_query.verifica import funcao_subir
        label_resposta['text'] = funcao_subir()

        return str(coleta_total)


    def funcao_dados():
        coleta_usuario = entry_usuario.get().strip()
        coleta_senha = entry_senha.get().strip()
        coleta_total = f'{coleta_usuario}\n{coleta_senha}'

        return str(coleta_total)


    janela = tkinter.Tk()
    janela.geometry('400x400+100+100')
    janela['background'] = 'black'
    janela.resizable(height=False, width=False)

    label_usuario = tkinter.Label(janela, text='usuario', bg='black', fg='white')
    label_usuario.place(x=40, y=60)

    label_senha = tkinter.Label(janela, text='senha', bg='black', fg='white')
    label_senha.place(x=40, y=120)

    label_resposta = tkinter.Label(janela, text='', bg='black', fg='white')
    label_resposta.place(x=40, y=200)

    entry_usuario = tkinter.Entry(janela, width=50)
    entry_usuario.place(x=40, y=80)

    entry_senha = tkinter.Entry(janela, width=50, show='*')
    entry_senha.place(x=40, y=140)

    botao_cadastrar = tkinter.Button(janela, text='cadastrar', bg='aqua', command=funcao_coleta)
    botao_cadastrar.place(x=286, y=200)

    janela.mainloop()
