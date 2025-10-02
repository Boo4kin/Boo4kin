import pandas as pd

def load_books():
    books = pd.read_csv('books.csv', sep=";", on_bad_lines='skip', encoding="latin-1")
    mask = ~books['Year-Of-Publication'].isin(['0', 0, 'DK Publishing Inc', 'Gallimard'])
    books = books[mask]
    books['Year-Of-Publication'] = books['Year-Of-Publication'].astype(int)
    books = books[books['Year-Of-Publication'] <= 2024]
    books.dropna(inplace=True)
    mask = (books['Year-Of-Publication'] < 1900) & (books['ISBN'] != '0781228956')
    books = books[~mask]
    return books

def load_users():
    users = pd.read_csv('users.csv', sep=";", on_bad_lines='skip', encoding="latin-1")
    users.dropna(inplace=True)
    users['Age'] = users['Age'].astype(int)
    users = users[(users['Age'] <= 100) & (users['Age'] >= 13) & (users['Age'] != 0)]
    return users

def load_ratings():
    users = load_users()
    books = load_books()
    ratings = pd.read_csv('ratings.csv', sep=";", on_bad_lines='skip', encoding="latin-1")
    ratings = ratings[ratings['Book-Rating'] != 0].sample(n=50000, random_state=37)
    users_mask = ratings['User-ID'].isin(users['User-ID'])
    books_mask = ratings['ISBN'].isin(books['ISBN'])
    ratings = ratings[users_mask & books_mask].reset_index(drop=True)
    return ratings