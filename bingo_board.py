import tkinter as tk
import random


class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mansor Bingo Sheet")
        self.root.geometry("700x700")  # Increased window size
        self.root.config(bg="#1D1D1D")

        self.bingo_items = [
            "Mentions Food", "Makes it to end of slide show", "Mentions tesla or apple",
            "Picks on Jonesy", "Picks on Peduzzi", "Asks why are you laughing",
            "Says you don't need to know this on the test", "Explains some random ass equation you don't need to know",
            "Sits on desk", "Uses the whiteboard", "Forgets someone's name", "Someone's phone goes off",
            "Yells at someone for talking", "Jonesy rizz", "Captain sleeps" , "Mentions a Test" , "Bends down to pick somthing up" , "Makes joke no one laughs at"
        ]

        # Duplicate the items if necessary to ensure we have 25 unique entries
        # Fill up the list until we have 25 unique items
        self.bingo_items = self.bingo_items * 2  # Multiply the list to ensure sufficient items
        random.shuffle(self.bingo_items)  # Shuffle the list to randomize the order

        # Truncate to exactly 25 items
        self.bingo_items = self.bingo_items[:25]

        self.create_bingo_grid()

    def create_bingo_grid(self):
        self.buttons = {}
        for row in range(5):
            for col in range(5):
                text = self.bingo_items.pop(0) if row != 2 or col != 2 else "Free Space"
                btn = tk.Button(self.root, text=text, font=("Helvetica", 12), bg="#303030", fg="#FFFFFF",
                                width=10, height=4, bd=2, relief="solid", wraplength=150,
                                command=lambda r=row, c=col: self.mark_cell(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                self.buttons[(row, col)] = btn

        self.center_free_space()

        # Make the grid responsive
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1, uniform="equal")
            self.root.grid_rowconfigure(i, weight=1, uniform="equal")

    def center_free_space(self):
        btn = self.buttons[(2, 2)]
        btn.config(bg="#FF6F61", fg="#FFFFFF", text="Free Space")

    def mark_cell(self, row, col):
        btn = self.buttons[(row, col)]
        if btn['bg'] == "#303030":
            btn.config(bg="#4CAF50", fg="#FFFFFF", text="X")
        elif btn['bg'] == "#4CAF50":
            btn.config(bg="#303030", fg="#FFFFFF", text=self.bingo_items[row * 5 + col])
        self.check_bingo()

    def check_bingo(self):
        # Check rows and columns
        for i in range(5):
            if all(self.buttons[(i, j)]['bg'] == "#4CAF50" for j in range(5)) or \
                    all(self.buttons[(j, i)]['bg'] == "#4CAF50" for j in range(5)):
                self.show_bingo()
                return

        # Check diagonals
        if all(self.buttons[(i, i)]['bg'] == "#4CAF50" for i in range(5)) or \
                all(self.buttons[(i, 4 - i)]['bg'] == "#4CAF50" for i in range(5)):
            self.show_bingo()

    def show_bingo(self):
        bingo_popup = tk.Toplevel(self.root)
        bingo_popup.title("Bingo!")
        bingo_popup.config(bg="#2C3E50")
        tk.Label(bingo_popup, text="Bingo! You won!", font=("Helvetica", 16), bg="#2C3E50", fg="#FFFFFF").pack(padx=10,
                                                                                                               pady=10)
        tk.Button(bingo_popup, text="Close", font=("Helvetica", 12), command=bingo_popup.destroy,
                  bg="#FF6F61", fg="#FFFFFF").pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()
