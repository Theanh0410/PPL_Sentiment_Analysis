import tkinter as tk
from tkinter import scrolledtext
from run import Sentiment

def launch_chat_window(root):
    # Destroy all widgets in root window (welcome screen)
    for widget in root.winfo_children():
        widget.destroy()

    # Launch chat in the same root window
    ChatApp(root)

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analyzer")
        self.root.geometry("450x400")
        self.root.configure(bg="#FFD1D1")

        # Emojis    
        emoji_frame = tk.Frame(root, bg="#FFD1D1")
        emoji_frame.pack(pady=50)

        self.happy_img = tk.PhotoImage(file="Images/happy.png").subsample(8, 8)
        self.neutral_img = tk.PhotoImage(file="Images/neutral.png").subsample(7, 7)
        self.sad_img = tk.PhotoImage(file="Images/sad.png").subsample(8, 8)

        tk.Label(emoji_frame, image=self.happy_img, bg="#FFD1D1").pack(side="left", padx=20)
        tk.Label(emoji_frame, image=self.neutral_img, bg="#FFD1D1").pack(side="left", padx=20)
        tk.Label(emoji_frame, image=self.sad_img, bg="#FFD1D1").pack(side="left", padx=20)


        # Title
        tk.Label(root, text="Sentiment  Analysis", font=("Arial", 24, "bold"), bg="#FFD1D1").pack(pady=10)

        # Analyze Button
        tk.Button(root, text="Analyze", font=("Arial", 14, "bold"), bg="#5D5FEF", fg="white", padx=20, pady=10, command=self.go_to_chat).pack(pady=30)

    def go_to_chat(self):
        launch_chat_window(self.root)


class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Messenger")

        # Main frame
        self.frame = tk.Frame(root, bg="#ECE5DD")
        self.frame.pack(expand=True, fill='both')

        # Canvas + scrollbar for messages
        self.canvas = tk.Canvas(self.frame, bg="#ECE5DD", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.frame, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        # Frame inside canvas to hold messages
        self.messages_frame = tk.Frame(self.canvas, bg="#ECE5DD")
        self.canvas.create_window((0, 0), window=self.messages_frame, anchor='nw')
        
        self.messages_frame.columnconfigure(0, weight=1)
        self.messages_frame.columnconfigure(1, weight=1)
        
        self.messages_frame.bind("<Configure>", self.on_frame_configure)

        # Input area
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(side='left', fill='x', expand=True, padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", bg="#075E54", fg="white", font=("Arial", 12, "bold"), command=self.send_message)
        self.send_button.pack(side='right', padx=5, pady=10)

        self.bot = Sentiment()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def send_message(self, event=None):
        user_text = self.entry.get().strip()
        if not user_text:
            return
        self.entry.delete(0, tk.END)

        self.add_message(user_text, sender="user")
        sentiment = self.bot.sentiment(user_text)
        self.add_message(f"that feel {sentiment}", sender="bot")

    def add_message(self, text, sender):
        bubble = tk.Label(self.messages_frame, text=text, font=("Arial", 16), wraplength=200, justify='left', padx=10, pady=5)

        # Get current row count in messages_frame
        row = self.messages_frame.grid_size()[1]

        if sender == "user":
            bubble.config(bg="#DCF8C6", fg="black", justify='right')
            bubble.grid(row=row, column=1, sticky='e', pady=2, padx=10)
        else:
            bubble.config(bg="white", fg="black", justify='left')
            bubble.grid(row=row, column=0, sticky='w', pady=2, padx=10)

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
