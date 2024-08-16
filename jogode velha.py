import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2,
                                               command=lambda i=i, j=j: self.click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, i, j):
        if self.buttons[i][j]["text"] == "" and not self.check_winner():
            self.buttons[i][j]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Fim de Jogo", f"O jogador {self.current_player} venceu!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
