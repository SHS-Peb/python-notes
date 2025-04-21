# Make a list of 3 dictionaries, each one representing a book:

library = [
   {"title": "Sherlock", 
   "author": "Arthur Conan Doyle"},
   {"title": "Dune", 
   "author": "Frank Herbert"},
   {"title": "Midnight Sun", 
   "author": "Stephanie Myer"},
]

def addBook ():
    newTitle = input("What is the name?")
    newAuthor = input("What is the authors name?")
    newBook = {"title": newTitle, "author": newAuthor}
    library.append(newBook)

addBook()
print(library)

#Let the user enter 3 purchases and their prices. Use a dictionary to store them. Then total everything and show it.


shoppingList = []

def addItem ():
   newName = input("What item are you adding?")
   newPrice = float(input("How much does it cost?(with cents)"))
   newItem = {"itemName" : newName, "price" : newPrice}
   shoppingList.append(newItem)

for i in range(3):
   addItem()

print("Your shopping list:")
for item in shoppingList:
    print(f"{item['itemName']}")

total = 0
for item in shoppingList:
    total += item["price"]

print(f"Total cost: ${total:.2f}")