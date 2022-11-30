import pymysql.err
from sqlalchemy.orm import Query
from modulo_cadastro.conexao import Usuario, Session, engine
from modulo_cadastro.cadastro import funcao_tratamento


def funcao_commit():
    usuario_tratado = funcao_tratamento()

    try:
        session = Session(bind=engine)

        user = Usuario(usuario=usuario_tratado[0], senha=usuario_tratado[1])

        session.add(user)
        session.commit()

        print('')
        print('usuario cadastrado c sucesso')

        return 'usuario cadastrado c sucesso'

    except Exception:
        print('')
        print('eita deu ruim mano')

        return 'esse usuario ja existe'
