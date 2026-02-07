import tkinter as tk
from screeninfo import get_monitors
import os
from dotenv import load_dotenv

load_dotenv()
ID = os.getenv("ID")
PASSWORD = os.getenv("PASSWORD")

def main():
    root = tk.Tk()
    sub_windows = []
    monitors = get_monitors()
    root.attributes("-fullscreen", True)
    main_monitor = None

    for m in monitors:
        if m.is_primary:
            main_monitor = m

    root.geometry(f"{main_monitor.width}x{main_monitor.height}+{main_monitor.x}+{main_monitor.y}")
    root.configure(bg = "black")
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    
    for m in monitors:
        if not m.is_primary:
            sub = tk.Toplevel(root)

            sub.geometry(f"{m.width}x{m.height}+{m.x}+{m.y}")
            sub.configure(bg = "black")
            sub.overrideredirect(True)
            sub.attributes("-topmost", True)

            sub.bind("<Button>", lambda e: root.focus_force())

            sub_windows.append(sub)

    
    

    def contents():
        label = tk.Label(root, text=ID, font=("Arial", 40, "bold"), bg = root["bg"], fg="white")
        label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        ent = tk.Entry(root, font=("Arial", 20), width=30, justify="center", show="*")
        ent.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        def login():
            if ent.get() == PASSWORD:
                root.quit()

        button = tk.Button(root, text = "commit", command=login, width=10, bg = "white", fg = "black")
        button.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

    contents()
    root.mainloop()


if __name__ == "__main__":
    main()