from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

# custom flask cli command
@db_commands.cli.command("richardsWisdom")
def wisdom():
    print("Hello World")

@db_commands.cli.command("create")
def create_db():
    # SQLachemy will read our models and create tables based on those models
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def drop_db():
    # SQLachemy will read our models and create tables based on those models
    db.drop_all()
    print("Tables deleted")


# Put fake data into our table
@db_commands.cli.command("seed")
def seed_db():
    from models.Book import Book
    from faker import Faker
    faker = Faker()

    for i in range(10):
        book = Book()
        book.title = faker.catch_phrase()
        db.session.add(book)
        print(f"{i} book record(s) created")
    
    db.session.commit()
    print("Tables seeded")


