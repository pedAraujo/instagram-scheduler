from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# creates the SqlAlchemy connection

engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    # import models vai importar todos os modelos que estiverem no arquivo __init__.py dentro da pasta models (crie  se não tiver), senao nao importa nada
    Base.metadata.create_all(bind=engine)
