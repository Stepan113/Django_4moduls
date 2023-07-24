# Transient(временный) - до добавления в сессию
# Pending(ожидающий) - до добавления в сессию, однако прошел предварительную интерграцию данных
# Persistent(персистентный) - находится в сессии
# Deleted(удаленный) - еще в бд, но сам объект помечен длля удаления
# Detached(отсоединенный) - не существует в бд
from sqlalchemy import create_engine, inspect, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

engine = create_engine(url='sqlite+pysqlite:///:memory:', echo=True)

session = Session(engine, expire_on_commit=True, autoflush=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    surname: Mapped[str]


Base.metadata.create_all(engine)


def set_user(name: str, surname: str, age: int):
    session.add(User(age=age, name=name.capitalize(), surname=surname.capitalize()))


def get_user(name: str, surname: str, age: int):
    result = session.execute(
        select(User).where(User.name == name.capitalize(), User.surname == surname.capitalize(), User.age == age))
    return result.mappings().all()


set_user(name='Привет', surname='goodbye', age=123)
session.commit()
print(get_user(name='Привет', surname='goodbye', age=123))
