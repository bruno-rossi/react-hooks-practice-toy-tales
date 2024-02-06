from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

class Toy(db.Model, SerializerMixin):
    __tablename__ = 'toys'

    # Add columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    likes = db.Column(db.Integer)

    @validates('name')
    def validate_name(self, key, new_name):
        if not new_name:
            raise ValueError(f"Attribute cannot be null: {key}")
        return new_name

    # Add relationships
    # Add serialization rules

    def __repr__(self) -> str:
        return f'<Toy {self.name}>'
