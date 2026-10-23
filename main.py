import json
import random
import string
from pathlib import Path 
from datetime import datetime

class Library:

    def gen_id(Prefix = "B"):
        random_id = ""
        for i in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)
            return Prefix + "-" + random_id

    def add_book(self):
        title = input("Enter  Book Title : ")
        author = input("Entet the book author : ")
        copies = int(input("How many copies :- "))

        book = {
            "id" : Library.gen_id(),
            "title" : title,
            "author" : author,
            "total_copies" : copies,
            "availabale_copies" : copies,
            "added_on" : datetimenow.()strftime("%Y-%m-%d %H:%M:%S"),
        }

        print(book)


hello = Library()

print("="*50)
print("Library Management System")
print("="*50)
print("1. Add Book")
print("2. List Books")
print("3. Add Members")
print("4. List Members")
print("5. Borrow Book")
print("6. Return Book")
print("0. Exit the Portal")
print("-"*50)
choice = input("What task you want to do")

if choice == "1":
    hello.add_book()