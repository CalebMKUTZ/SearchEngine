import tkinter as tk


class Window(tk.Tk):
    def __init__(self, _title, size, bg):
        tk.Tk.__init__(self)
        self._title = _title
        self.size = size
        self.bg = bg
        self.title(self._title)
        self.geometry(self.size)
        self["bg"] = self.bg


class Button(tk.Button):
    def __init__(self, master, text, width, height, bg, command):
        tk.Button.__init__(self, master=master, command=command)
        self.master = master
        self.text = text
        self.width = width
        self.height = height
        self.bg = bg
        self.command = command
        self["text"] = self.text
        self["width"] = self.width
        self["height"] = self.height
        self["bg"] = self.bg


class Label(tk.Label):
    def __init__(self, master, text, font, bg, fg):
        tk.Label.__init__(self, master=master)
        self.text = text
        self.font = font
        self.bg = bg
        self.fg = fg
        self["text"] = self.text
        self["font"] = self.font
        self["bg"] = self.bg
        self["fg"] = self.fg

