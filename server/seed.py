#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Author, Post


fake = Faker()

with app.app_context():

    Author.query.delete()
    Post.query.delete()

    for n in range(25):
        author = Author(
            name=fake.name(), 
            phone_number='1324543333')
        db.session.add(author)
        db.session.commit()
        
    posts = []
    for n in range(25):
        post = Post(title='Secret banana', content='This is the content Secret' * 50, category= 'Fiction', summary="Summary Secret" )
        posts.append(post)

    db.session.add_all(posts)

    db.session.commit()