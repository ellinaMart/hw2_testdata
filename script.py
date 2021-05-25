from json import loads, dumps
import csv


def get_users():
    with open('data/users.json', 'r') as json:
        j = json.read()
        users = loads(j)
        user_data = []
        for user in users:
            new_data = {
                'name': user['name'],
                'gender' : user['gender'],
                'address' : user['address']
            }
            user_data.append(new_data)
        json.close()
    return user_data

def get_books():
    with open('data/books.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        books = []
        for row in reader:
            new_book = {
                'title': row['Title'],
                'author': row['Author'],
                'height': row['Height']
            }
            books.append(new_book)
        csvfile.close()
    return books

def add_book_to_user(user_data, books):
    for i, user in enumerate(user_data):
        if i >= len(books):
            user_data[i]['books'] = []
        else:
            user_data[i]['books'] = books[i]

    with open('data/example.json', 'w') as outfile:
        s = dumps(user_data, indent=4)
        outfile.write(s)

if __name__ == "__main__":
    user_data = get_users()
    books = get_books()
    add_book_to_user(user_data, books)

