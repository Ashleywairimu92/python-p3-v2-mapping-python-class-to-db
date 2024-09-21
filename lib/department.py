import sqlite3
from __init__ import CURSOR, CONN
class Department:
    def __init__(self, name, location):
        self.id = None  # To be set when saved to the database
        self.name = name
        self.location = location

    @classmethod
    def create_table(cls):
        """Create the 'departments' table if it doesn't exist."""
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the 'departments' table if it exists."""
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        CONN.commit()

    def save(self):
        """Save a Department instance to the database and assign it an ID."""
        sql = """
            INSERT INTO departments (name, location)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        self.id = CURSOR.lastrowid  # Get the last inserted id
        CONN.commit()

    @classmethod
    def create(cls, name, location):
        """Create a new row in the database using parameter data and return a Department instance."""
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Update the corresponding database row to match the instance's current attribute values."""
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the instance's corresponding database row."""
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
