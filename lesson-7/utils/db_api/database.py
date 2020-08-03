from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import POSTGRES_URI

db = Gino()


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html

async def create_db():
    await db.set_bind(POSTGRES_URI)

    # Create tables
    db.gino: GinoSchemaVisitor
    # await db.gino.drop_all()
    # await db.gino.create_all()
