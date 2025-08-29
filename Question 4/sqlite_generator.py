import sqlite3
import xml.etree.ElementTree as ET
import os

def xml_books_to_sqlite(xml_file):
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    os.makedirs(documents_folder, exist_ok=True)

    db_file = os.path.join(documents_folder, "books.db")

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
        book_id = book.attrib.get("id")
        title = book.find("title").text if book.find("title") is not None else None
        author = book.find("author").text if book.find("author") is not None else None
        genre = book.find("genre").text if book.find("genre") is not None else None
        price = float(book.find("price").text) if book.find("price") is not None else None
        year = int(book.find("publication_year").text) if book.find("publication_year") is not None else None

        cursor.execute("""
            INSERT OR REPLACE INTO books (id, title, author, genre, price, publication_year)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (book_id, title, author, genre, price, year))

    conn.commit()
    conn.close()

    print(f"✅ Data saved to {db_file}")

if __name__ == "__main__":
    xml_books_to_sqlite("xml_data.xml")
