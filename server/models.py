from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 

    @validates('name')
    def name_validate(self, key, name):
        if name == '':
            raise ValueError("Name must not be empty")
        if Author.query.filter(Author.name == name).first() != None:
            raise ValueError("Name must be unique")
        return name

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('phone_number')
    def phone_validate(self, key, phone_number):
        if len(phone_number) != 10 or phone_number.isdigit() is False:
            raise ValueError("Phone Number must be exactly 10 digits")

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('title')
    def title_validate(self, key, title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if title == '':
            raise ValueError("Books Require titles")
        baited = False
        for bait in clickbait:
            if bait in title:
                baited = True
        if baited == False:
            raise ValueError("Bait harder, son")
        
        return title
    
    @validates('content')
    def content_validate(self, key, content):
        if len(content) < 250:
            raise ValueError("Posts must be at least 250 characters")
        return content
    
    @validates('summary')
    def summary_validate(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Summaries must be less than 250 characters")
    
    @validates('category')
    def category_validate(self, key, category):
        if str(category) != 'Fiction' and str(category) != 'Non-Fiction':
            raise ValueError("Must be fiction or Non-Fiction")
        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'