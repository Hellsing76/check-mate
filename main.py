import sys
import tkinter as tk
import api


class Application(tk.Frame):  # for there's only one frame, so this will be the main one
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()  # after initial setup; we now setup the window and its parts

    # def init_window(self):
    #     def display_credit():  # use our get_student_credit function and output it to the text1 Tk variable
    #         output = api.get_credit_with_login(entry_username.get(), entry_password.get())
    #         message_box.config(text=output)
    #
    #     entry_username = tk.Entry(self)  # creating the Tk widgets
    #     entry_password = tk.Entry(self, show='*')
    #     message_box = tk.Label(self, width='200')
    #     button_get_credit = tk.Button(self, text="Fetch Credit", command=display_credit)
    #
    #     self.pack(fill='both', expand=1)  # displaying the Tk widgets with pack()
    #     entry_username.pack()
    #     entry_password.pack()
    #     button_get_credit.pack()
    #     message_box.pack()

    def init_window(self):
        def display_credit():
            output = api.get_credit_with_mock(entry_id.get())
            message_box.config(text=output)

        entry_id = tk.Entry(self)
        button_get = tk.Button(self, text="Get Credit", command=display_credit)
        message_box = tk.Label(self)

        self.pack(fill='both', expand=1)
        entry_id.pack()
        button_get.pack()
        message_box.pack()

if __name__ == '__main__':
    root = tk.Tk()
    root.overrideredirect(1)  # makes the window actually seem "full screen"
    root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    # gets the size of the display and sets the screen size to those values (covers the whole display)
    app = Application(root)
    root.mainloop()
