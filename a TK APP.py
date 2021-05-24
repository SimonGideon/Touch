import tkinter as tk


class HelloWorld(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        hello = tk.Label(self, text="Hello World! This is my kingdom!")
        hello.grid(row=0, column=0)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello World!")
    hello_frame = HelloWorldFrame(root)
    if __name__ == '__main__':
        hello_frame.mainloop()
