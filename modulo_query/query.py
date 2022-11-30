from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, create_engine


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
    print(lista)

    return lista


def funcao_query():
    engine = create_engine('mysql+pymysql://root:felipe008@localhost/login', echo=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    busca = funcao_busca()
    nome = busca[0]
    #nome2 = 'sofia'
    print('nome -->', nome, '\n')

    query = session.execute(
        f"select * from tb_login where usuario='{nome}'"
    )

    try:
        for row in query:
            lista = [row]

        print('')
        print('lista -->', lista)
        print('query -->', query)

        return lista

    except UnboundLocalError:
        return ''


def funcao_tratamento():
    query = funcao_query()

    try:
        nome = query[0][1]
        print('')
        print('nome -->', nome)

        return nome     #usuario ja existe

    except IndexError:
        return ''       #usuario ainda n existe

#se a funcao_tratamento retornar vazio é pq o usuario ainda n existe
#se a funcao_tratamento retornar um nome é pq o usuario ja existe

'''variavel = funcao_query()
for item in variavel:
    usuario = item
    print(usuario)'''

#print('')
#print(usuario)

#print('funcao_query -->', funcao_query(), '\n')
