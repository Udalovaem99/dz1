import pytest
from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://postgres:postgres@localhost:5432/QA123"
db = create_engine(db_connection_string)


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'users'
    assert names[6] == 'products'


def test_insert_product():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO products(art, product, category) VALUES (:art, :product, :category)") # noqa
    result =connection.execute(sql, {"art":"A14", "product":"телефон", "category":"техника"}) # noqa
    result = connection.execute(text("SELECT * FROM products WHERE art = :art"), {"art":"A14"}) # noqa
    assert result is not None
    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("update products set art  = :art where product  = :product")
    result = connection.execute(sql, {"art": "A15", "product": "телефон"})

    assert result.rowcount == 1

    updated_result = connection.execute(text("SELECT art FROM products WHERE product = :product"), {"product": "телефон"}) # noqa
    updated_art = updated_result.scalar()

    assert updated_art == "A15"
    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("delete from products where art = :art")
    connection.execute(sql, {"art": "A15"})
    transaction.commit()
    sql = text("SELECT * FROM products WHERE art = :art")
    result = connection.execute(sql, {"art": "A15"})
    assert result.fetchone() is None

    connection.close()
