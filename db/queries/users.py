# Заготовка для работы с пользователями (с Prisma или SQLAlchemy)
async def get_user_by_id(user_id: int):
    # Пример Prisma: await prisma.user.find_unique(where={"id": user_id})
    pass

async def create_user(user_id: int, name: str):
    pass
