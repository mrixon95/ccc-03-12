from main import ma
from models.Book import Book
from marshmallow.validate import Length

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
    # Add validation rules to the schema
    title = ma.String(required=True, validate=Length(min=1))

book_schema = BookSchema()
books_schema = BookSchema(many=True)