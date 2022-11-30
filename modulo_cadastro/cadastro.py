def cadastrar():

    with open(r'../modulo_txt/usuario.txt', 'r') as usuario_txt:
        usuario = usuario_txt.readlines()

    print('')
    print('')
    print('class usuario -->', type(usuario))
    print('usuario -->', usuario)
    print('')

    return usuario


def funcao_tratamento():
    lista = cadastrar()
    usuario = lista[0][:-1]
    print(usuario, lista[1])
    print('')

    lista = [usuario, lista[1]]
    print('class retorno funcao_tratamento -->', type(lista))
    print('lista retorno funcao_tratamento -->', lista)
    print('')

    return lista


funcao_tratamento()
