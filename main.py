import tkinter as tk
from widgets import Window
from widgets import Button
from widgets import Label
from search_api import search
import webbrowser

WIDTH = 700
HEIGHT = 500

root = Window("Search Engine++", f"{WIDTH}x{HEIGHT}", "white")

google_label = Label(root, "Google++", ("Courior", 30), "white", "black")
google_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

search_input = tk.Entry(root, width=40)
search_input.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def open_link(link):
    webbrowser.open_new_tab(link)


def create_result_window():
    results = search(search_input.get())

    result_window = Window("RESULTS", "900x600", "white")
    
    for result in results:
        r = result["link"]
        link = Label(result_window, r, ("Courior", 10), "white", "blue")
        link["cursor"] = "hand2"
        link.bind("<Button-1>", lambda e:open_link(link["text"]))
        link.pack()

    result_window.mainloop()

search_button = Button(root, "Search", 20, 2, "white", create_result_window)
search_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()