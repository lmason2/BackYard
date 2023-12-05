def create():
    from alembic.config import Config
    from alembic import command

    message = input("Migration message: ")
    config = Config("alembic.ini")
    command.revision(config, autogenerate=True, message=message)
    print("Migration file generated")

def up():
    from alembic.config import Config
    from alembic import command

    config = Config("alembic.ini")
    command.upgrade(config, "head")
    print("Migration complete")
