from sqlalchemy.future import select
from .models import User
from .auth import hash_password

async def create_user(db, user):
    new_user = User(
        username=user.username,
        password=hash_password(user.password)
    )
    db.add(new_user)
    await db.commit()
    return new_user

async def get_user(db, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar()
