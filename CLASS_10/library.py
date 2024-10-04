#ORDER LIBRAY BY GENRE
# {
#     ROMANCE : [{}, {}, {}],
#     SCI-FI : {},
#     COMEDY : {},
#     THRILLER : {}
# }

LIBRARY = {}
GENRES = ("ROMANCE", "SCI-FI", "COMEDY", "THRILLER")

#ADD BOOK
#books genre, books details - name, author

def validate(genre, name, author):
    is_valid = False
    if genre not in GENRES:
        print("INVALID BOOK GENRE!")
    elif not name:
        print("INVALID BOOK NAME!")
    elif not author:
        print("INVALID BOOK AUTHOR!")
    else:
        is_valid = True
    return is_valid


def add_book(genre, name, author):
    valid_book = validate(genre, name, author)
    if not valid_book:
        print("CANNOT SAVE BOOK")
        return

    if genre not in LIBRARY:
        #Created a new Genre List
        LIBRARY[genre] = []

        print(f"""We don't have your genre, but for you we can make an exception ;)
        ADDED NEW GENRE : {genre}""")

    new_book = {
        'name':name,
        'author': author
    }

    lib_genre = LIBRARY.get(genre)

    lib_genre.append(new_book)

    return f"""
    BOOK ADDED SUCCESSFULLY.
    {new_book}
"""

def list_by_genre():
    for genre in LIBRARY:
        print(f"CATEGORY:{genre}")

        for book in LIBRARY[genre]:
            print(book)

def search_book(name):
    for genre in LIBRARY:
        for book in LIBRARY[genre]:
            if book['name'] == name:
                return book

add_book("ROMANCE", "Half of a Yellow Sun", "Chimamanda Adichie")
add_book("THRILLER", "IN DEATH", "JD. ROB")
add_book("COMEDY", "ACT LIKE A LADY, THINK LIKE A MAN", "STEVE HARVEY")
add_book("SCI-FI", "OTHELLO", "WILLIAMS SHAKESPEARE")
# list_by_genre()
print(search_book("IN DEATH"))