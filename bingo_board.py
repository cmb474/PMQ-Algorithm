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
            "Yells at someone for talking", "Jonesy rizz", "Captain sleeps", "Mentions a Test",
            "Bends down to pick something up", "Makes joke no one laughs at"
        ]

        self.bingo_items = self.bingo_items * 2  # Multiply to ensure sufficient items
        random.shuffle(self.bingo_items)
        self.bingo_items = self.bingo_items[:25]

        self.click_counts = {}  # Track how many times each square is clicked
        self.checked_squares = {}  # Store checked squares with counts
        self.create_bingo_grid()

    def create_bingo_grid(self):
        self.buttons = {}
        for row in range(5):
            for col in range(5):
                text = self.bingo_items.pop(0) if (row, col) != (2, 2) else "Free Space"
                self.click_counts[(row, col)] = 0  # Initialize click count

                btn = tk.Button(self.root, text=text, font=("Helvetica", 12), bg="#303030", fg="#FFFFFF",
                                width=12, height=4, bd=2, relief="solid", wraplength=150,
                                command=lambda r=row, c=col: self.mark_cell(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                self.buttons[(row, col)] = btn

        self.center_free_space()

        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1, uniform="equal")
            self.root.grid_rowconfigure(i, weight=1, uniform="equal")

    def center_free_space(self):
        btn = self.buttons[(2, 2)]
        btn.config(bg="#FF6F61", fg="#FFFFFF", text="Free Space")
        self.checked_squares["Free Space"] = 1

    def mark_cell(self, row, col):
        btn = self.buttons[(row, col)]
        self.click_counts[(row, col)] += 1
        count = self.click_counts[(row, col)]

        btn.config(bg="#4CAF50", activebackground="#4CAF50", fg="#FFFFFF",
                   text=f"{btn.cget('text').split(' (')[0]} ({count})")
        self.checked_squares[btn.cget("text").split(" ("[0])] = count

        self.check_bingo()

    def check_bingo(self):
        bingo_squares = []
        for i in range(5):
            if all(self.buttons[(i, j)]["bg"] == "#4CAF50" for j in range(5)):
                bingo_squares.extend([self.buttons[(i, j)].cget("text") for j in range(5)])
            if all(self.buttons[(j, i)]["bg"] == "#4CAF50" for j in range(5)):
                bingo_squares.extend([self.buttons[(j, i)].cget("text") for j in range(5)])

        if all(self.buttons[(i, i)]["bg"] == "#4CAF50" for i in range(5)):
            bingo_squares.extend([self.buttons[(i, i)].cget("text") for i in range(5)])
        if all(self.buttons[(i, 4 - i)]["bg"] == "#4CAF50" for i in range(5)):
            bingo_squares.extend([self.buttons[(i, 4 - i)].cget("text") for i in range(5)])

        if bingo_squares:
            self.show_bingo(bingo_squares)

    def show_bingo(self, bingo_squares):
        bingo_popup = tk.Toplevel(self.root)
        bingo_popup.title("Bingo!")
        bingo_popup.config(bg="#2C3E50")

        tk.Label(bingo_popup, text="Bingo! You won!", font=("Helvetica", 16), bg="#2C3E50", fg="#FFFFFF").pack(padx=10,
                                                                                                               pady=10)

        checked_text = "Bingo Squares:\n" + "\n".join(bingo_squares)
        tk.Label(bingo_popup, text=checked_text, font=("Helvetica", 12), bg="#2C3E50", fg="#FFFFFF").pack(pady=10)

        tk.Button(bingo_popup, text="Close", font=("Helvetica", 12), command=bingo_popup.destroy,
                  bg="#FF6F61", fg="#FFFFFF").pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()
