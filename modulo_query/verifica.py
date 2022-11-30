def funcao_query():
    from modulo_query.query import funcao_tratamento

    query = funcao_tratamento()
    print('query verifica -->', query)
    print('type query verifica -->', type(query))
    print('')

    if query == '':     #usuario ainda n existe
        from modulo_cadastro.cadastro import funcao_tratamento

        usuario = funcao_tratamento()
        print(usuario, 'ainda n existe')
        print('')
        return ''

    else:
        print(query, 'ja eixite')
        print('')
        return query    #usuario ja existe


def funcao_subir():
    query = funcao_query()

    if query == '':     #usuario ainda n existe
        print('usuario ainda n existe')

        from modulo_cadastro.cadastro import funcao_tratamento
        from modulo_cadastro.conexao import Usuario, Session, engine

        usuario_tratado = funcao_tratamento()
        session = Session(bind=engine)

        user = Usuario(usuario=usuario_tratado[0], senha=usuario_tratado[1])

        session.add(user)
        session.commit()

        print('')
        print('usuario cadastrado c suecesso')
        return 'usuario cadastrado c sucesso'

    else:               #usuario ja existe
        print('')
        print('esse usuario ja existe')
        return 'esse usuario ja existe'


print('-->', funcao_subir())
