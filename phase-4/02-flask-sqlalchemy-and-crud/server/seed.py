#!/usr/bin/env python3
# 📚 Review With Students:
# Seeding
# 5. ✅ Imports
from app import app
from models import Production, db

# db and Production from models

# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`


# 7. ✅ Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

with app.app_context():
    Production.query.delete()

    p1 = Production(
        title="Hamlet",
        genre="Drama",
        director="Bill Shakespeare",
        description="The Tragedy of Hamlet, Prince of Denmark",
        budget=100000.00,
        image="https://upload.wikimedia.org/wikipedia/commons/6/6a/Edwin_Booth_Hamlet_1870.jpg",
        ongoing=True,
    )

    db.session.add(p1)

    p2 = Production(
        title="Cats",
        genre="Musical",
        director="Andrew Lloyd Webber",
        description=" Jellicles cats sing and dance",
        budget=200000.00,
        image="https://upload.wikimedia.org/wikipedia/en/3/3e/CatsMusicalLogo.jpg",
        ongoing=True,
    )

    db.session.add(p2)

    p3 = Production(
        title="Carmen",
        genre="Opera",
        director="Georges Bizet",
        description="Set in southern Spain this is the story of the downfall of Don"
        "José, a naïve soldier who is seduced by the wiles of the fiery and beautiful"
        "Carmen.",
        budget=200000.00,
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Prudent-Louis_Leray_-_Poster_for_the_premi%C3%A8re_of_Georges_Bizet%27s_Carmen.jpg/300px-Prudent-Louis_Leray_-_Poster_for_the_premi%C3%A8re_of_Georges_Bizet%27s_Carmen.jpg",
        ongoing=False,
    )

    db.session.add(p3)
    p4 = Production(
        title="Hamilton",
        genre="Musical",
        director="Lin-Manuel Miranda",
        description="An American Musical is a sung-and-rapped-through musical by Lin-Manuel Miranda. It tells the story of American Founding Father Alexander Hamilton.",
        budget=400000.00,
        image="https://upload.wikimedia.org/wikipedia/en/thumb/8/83/Hamilton-poster.jpg/220px-Hamilton-poster.jpg",
        ongoing=False,
    )

    db.session.add(p4)
    
    db.session.commit()
    
    c1 = CastMember(name= "Example Name", production_id = p1.id)
    c2 = CastMember(name= "Example Name 2", production_id = p1.id)
    c3 = CastMember(name= "Example Name 3", production_id = p2.id)
    c4 = CastMember(name= "Example Name 4", production_id = p2.id)

    db.session.add_all(c1, c2, c3, c4)
    
    
# 8.✅ Create a query to delete all existing records from Production

# 9.✅ Create some seeds for production and commit them to the database.
# p1 = Production(title='Hamlet', genre= 'Drama', director='Bill Shakespeare', description='The Tragedy of Hamlet, Prince of Denmark', budget= 100000.00, image='https://upload.wikimedia.org/wikipedia/commons/6/6a/Edwin_Booth_Hamlet_1870.jpg', ongoing=True)
# p2 = Production(title='Cats', genre='Musical', director='Andrew Lloyd Webber', description=' Jellicles cats sing and dance', budget=200000.00, image='https://upload.wikimedia.org/wikipedia/en/3/3e/CatsMusicalLogo.jpg', ongoing=True)
# p3 = Production(title='Carmen', genre='Opera', director='Georges Bizet', description='Set in southern Spain this is the story of the downfall of Don José, a naïve soldier who is seduced by the wiles of the fiery and beautiful Carmen.', budget=200000.00, image='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Prudent-Louis_Leray_-_Poster_for_the_premi%C3%A8re_of_Georges_Bizet%27s_Carmen.jpg/300px-Prudent-Louis_Leray_-_Poster_for_the_premi%C3%A8re_of_Georges_Bizet%27s_Carmen.jpg', ongoing=False)
# p4 = Production(title= 'Hamilton', genre= 'Musical', director='Lin-Manuel Miranda', description='An American Musical is a sung-and-rapped-through musical by Lin-Manuel Miranda. It tells the story of American Founding Father Alexander Hamilton.', budget= 400000.00, image='https://upload.wikimedia.org/wikipedia/en/thumb/8/83/Hamilton-poster.jpg/220px-Hamilton-poster.jpg',ongoing=False)

# 10.✅ Run in terminal:
# `python seed.py`
# 11.✅ navigate to debug.py
