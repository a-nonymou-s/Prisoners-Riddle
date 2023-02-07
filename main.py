import tkinter as tk
import random

class PrisonerPuzzle(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("100 Prisoners and a Light Bulb")
        self.geometry("300x300")
        self.number_of_prisoners = 100
        self.light_bulbs = []
        self.prisoner_id = random.randint(1, 100)
        self.counter = 50
        self.fill_bulb_arr()
        self.label = tk.Label(text="Your ID is: {}".format(self.prisoner_id))
        self.label.grid(row=0, column=0, columnspan=10)
        self.buttons = []
        for i in range(self.number_of_prisoners):
            button = tk.Button(self, text=str(i), command=lambda i=i: self.check_id(i), bg="gold")
            button.grid(row=i//10+1, column=i%10)
            self.buttons.append(button)
        self.result_label = tk.Label(text="")
        self.result_label.grid(row=11, column=0, columnspan=10)

        # Code to make the GUI responsive:
        for i in range(10):
            self.grid_columnconfigure(i, weight=1)
        for i in range(12):
            self.grid_rowconfigure(i, weight=1)
    
    def fill_bulb_arr(self):
        for i in range(self.number_of_prisoners):
            nbr = random.randint(1, 100)
            while nbr in self.light_bulbs:
                nbr = random.randint(1, 100)
            self.light_bulbs.append(nbr)
    
    def check_id(self, index):
        if self.counter <= 0:
            self.result_label.config(text="You lost.....Exiting.....")
            self.after(3000,self.quit())
        else:
            self.counter -= 1
            if self.light_bulbs[index] == self.prisoner_id:
                self.result_label.config(text="You Won.")
                self.after(3000,self.quit())
            else:
                self.buttons[index].config(bg="pink")
                self.buttons[index].config(text=str(self.light_bulbs[index]))
                self.result_label.config(text="Number not found. You have {} chances left.".format(self.counter))

if __name__ == "__main__":
    app = PrisonerPuzzle()
    app.mainloop()
