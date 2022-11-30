
'''def funcao_query():
    nome = 'usuario'
    session = Session(bind=engine)
    query = session.execute(
        f'select {nome} from tb_login8'
    )
    for item in query:
        item = str(item)
        print(item)
        print(type(item))

funcao_query()'''


def funcao_busca():
    with open(r'../modulo_txt/usuario.txt', 'r') as usuario_txt:
        usuario = usuario_txt.readlines()

    lista = usuario
    print('')
    print(lista)

    usuario = lista[0][:-1]
    lista = [usuario, lista[1]]
    print('type retorno funcao_busca -->', type(lista))
    print('retorno funcao_busca -->', lista)
    print('')

    return lista


def funcao_query():
    from modulo_cadastro.conexao import engine, Session

    session = Session(bind=engine)

    busca = funcao_busca()
    nome = busca[0]
    #nome2 = 'sofia'
    print('type nome -->', type(nome))
    print('nome -->', nome)

    query = session.execute(
        f"select usuario from tb_login9 where usuario='{nome}'"
    )

    try:
        for row in query:
            lista = [row]

        print('')
        print('lista funcao_query -->', lista)
        print('query funcao_query -->', query)
        print('')
        return lista

    except UnboundLocalError:
        return ''


def funcao_tratamento():
    query = funcao_query()

    try:
        nome = str(query[0])
        nome = nome[2:-3]
        print('type usuario funcao_tratamento -->', type(nome))
        print('usuario funcao_tratamento -->', nome)
        print('')

        return nome     #usuario ja existe

    except IndexError:
        return ''       #usuario ainda n existe


'''variavel = funcao_query()
for item in variavel:
    usuario = item
    print(usuario)

print('')
print(usuario)

#print('funcao_query -->', funcao_query(), '\n')'''
