from tkinter import *
from tkinter import simpledialog, messagebox

window = Tk()

window.title('My library')
window.geometry('800x600+50+20')

# List to store books
library = []

def add_new_book_click():
    book_title = simpledialog.askstring("Input", "Enter book title:")
    if book_title:
        library.append(book_title)
        update_library_listbox()
        messagebox.showinfo("Success", f"Book '{book_title}' added to the library.\nLibrary: {library}")
    else:
        messagebox.showwarning("Warning", "Please enter a valid book title.")

def delete_book_click():
    book_title = simpledialog.askstring("Input", "Enter book title to delete:")
    if book_title in library:
        library.remove(book_title)
        update_library_listbox()
        messagebox.showinfo("Success", f"Book '{book_title}' deleted from the library.\nLibrary: {library}")
    else:
        messagebox.showwarning("Warning", f"Book '{book_title}' not found in the library.")

def update_library_listbox():
    library_listbox.delete(0, END)
    for book in library:
        library_listbox.insert(END, book)

# Create listbox to display library
library_listbox = Listbox(window, selectmode=SINGLE)
library_listbox.pack(pady=10)

# Buttons to add and delete books
add_button = Button(window, text="Add Book", command=add_new_book_click)
add_button.pack(pady=5)
delete_button = Button(window, text="Delete Book", command=delete_book_click)
delete_button.pack(pady=5)

main_menu = Menu()
add_book_menu = Menu(tearoff=0)
delete_book_menu = Menu(tearoff=0)
help_menu = Menu(tearoff=0)
settings_menu = Menu(tearoff=0)

main_menu.add_cascade(label="Add", menu=add_book_menu)
main_menu.add_cascade(label="Delete", menu=delete_book_menu)

settings_menu.add_command(label="Save")
settings_menu.add_command(label="Open")

add_book_menu.add_command(label="Add Book", command=add_new_book_click)
add_book_menu.add_cascade(label="Settings", menu=settings_menu)
add_book_menu.add_separator()
add_book_menu.add_command(label="Exit")

delete_book_menu.add_command(label="Delete Book", command=delete_book_click)
delete_book_menu.add_cascade(label="Settings", menu=settings_menu)
delete_book_menu.add_separator()
delete_book_menu.add_command(label="Exit")

window.config(menu=main_menu)

window.mainloop()
