import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from schemas import User, Role, Document, Photo, Job, Product, Event, Invoice, Base
from ..conf import settings

host, port, db, user_name, password = settings.host, settings.port, settings.db, settings.user_name, settings.password

SCHEMA_MAP = {
    "user": User,
    "role": Role,
    "document": Document,
    "photo": Photo,
    "job": Job,
    "product": Product,
    "event": Event,
    "invoice": Invoice,
}


class PostgresORM:
    engine = None
    session = None

    def __init__(self) -> None:
        url = f"postgresql://{user_name}:{password}@{host}:{port}/{db}"
        if not database_exists(url):
            logging.info("Creating database")
            create_database(url)
        logging.info("attaching engine to url")
        self.engine = create_engine(url)
        # Base.metadata.create_all(bind=self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add(self, entry):
        self.session.add(entry)
        self.session.commit()

    def query(self, object_key):
        results = self.session.query(SCHEMA_MAP.get(object_key)).all()
        return results


if __name__ == "__main__":
    orm = PostgresORM()
    # role_admin = Role('admin')
    # orm.add(role_admin)
    # my_user = User('luke mason', 'lukesamuelmason@gmail.com', 'admin')
    # orm.add(my_user)
    results = orm.query("user")
    print(results)
    role_results = orm.query("role")
    print(role_results)
