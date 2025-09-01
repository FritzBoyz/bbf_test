import sqlite3
import xml.etree.ElementTree as ET
import os

def xml_books_to_sqlite():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(script_dir, "xml_data.xml")
    db_file = os.path.join(script_dir, "books.db")

    tree = ET.parse(xml_file)
    root = tree.getroot()

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT,
            price REAL,
            publication_year INTEGER
        )
    """)

    for book in root.findall("book"):
        book_id = book.get("id")
        title = book.findtext("title")
        author = book.findtext("author")
        genre = book.findtext("genre")
        price = float(book.findtext("price"))
        pub_year = int(book.findtext("publication_year"))

        cursor.execute("""
            INSERT OR REPLACE INTO books (id, title, author, genre, price, publication_year)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (book_id, title, author, genre, price, pub_year))

    conn.commit()
    conn.close()

    print(f"Database Saved {db_file}")

if __name__ == "__main__":
    xml_books_to_sqlite()
