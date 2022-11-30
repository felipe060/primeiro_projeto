def funcao_query():
    from query import funcao_tratamento

    query = funcao_tratamento()
    print('query session -->', query)

    if query == '':
        return ''       #usuario ainda n existe
    else:
        return query    #usuario ja existe


def funcao_subir():
    query = funcao_query()

    if query == '':     #usuario ainda n existe
        from query import funcao_tratamento
        from modulo_cadastro.session import Session
        from modulo_cadastro.conexao import engine, Usuario

        usuario_tratado = funcao_tratamento()

        session = Session(bind=engine)

        user = Usuario(usuario=usuario_tratado[0], senha=usuario_tratado[1])

        session.add(user)
        session.commit()

        print('')
        print('usuario cadastrado c sucesso')
        return 'usuario cadastrado c sucesso'

    else:
        print('')
        print('esse usuario ja existe')
        return 'esse usuario ja existe'


print('modulo vefrifica funcao_subir -->', funcao_subir())
