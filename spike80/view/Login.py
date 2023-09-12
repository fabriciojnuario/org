import tkinter as tk


class Login:
    def __init__(self, win):
        self.label_name = tk.Label(win, text='Insert your name:')
        self.label_id = tk.Label(win, text="Insert your ID:")
        self.txt_name = tk.Entry(win)
        self.txt_id = tk.Entry(win)
        self.label_name.place(x=160, y=180)
        self.txt_name.place(x=285, y=180)
        self.label_id.place(x=180, y=230)
        self.txt_id.place(x=285, y=230)
        self.button_entry = tk.Button(win, text="Login")
        self.button_cancel = tk.Button(win, text="Cancel")
        self.button_entry.place(x=225, y=270)
        self.button_cancel.place(x=325, y=270)


root = tk.Tk()
Login(root)
root.title('Tkinter Window - Center')

window_width = 600
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)
root.attributes('-alpha', 0.5)
root.mainloop()
