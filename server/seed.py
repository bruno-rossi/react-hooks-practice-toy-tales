from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Toy

fake = Faker()

def create_toys():
    toys = []
    for _ in range(10):
        t = Toy(
            name=fake.first_name(),
            image="http://www.pngmart.com/files/3/Toy-Story-Woody-PNG-Photos.png",
            likes=0,
        )
        toys.append(t)

    return toys

if __name__ == '__main__':

    with app.app_context():
        print("Clearing db...")
        Toy.query.delete()

        print("Seeding toys...")
        toys = create_toys()
        db.session.add_all(toys)
        db.session.commit()

        print("Done seeding!")
