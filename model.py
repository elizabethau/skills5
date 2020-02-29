"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 1 of Skills 5: SQLAlchemy & AJAX.
"""

from flask_sqlalchemy import SQLAlchemy


# Instantiate a SQLAlchemy object. We need this to create our db.Model classes.
db = SQLAlchemy()


##############################################################################
# PART 1: COMPOSE ORM


class Human(db.Model):
    """Data model for a human."""

    __tablename__ = "humans"

    # Define your columns and/or relationships here
    human_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(15))
    lname = db.Column(db.String(15))
    email = db.Column(db.String(30))

    def __repr__(self):
        """Return a human-readable representation of a Human."""

        # Finish this __repr__ method
        return f"<Human ID: {self.human_id} Email: {self.email}>"


class Animal(db.Model):
    """Data model for an animal."""

    __tablename__ = "animals"

    # Define your columns and/or relationships here
    animal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'))
    name = db.Column(db.String(15))
    animal_species = db.Column(db.String(15))
    birth_year = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """Return a human-readable representation of a Human."""

        # Finish this __repr__ method
        return f"<{self.name} was born on {self.birth_year}>"


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///animals"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
