import tkinter as tk
from tkinter import Menu

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Argo-ToDo")  # Custom window title
        self.geometry("400x500")

        # Instruction label
        self.label = tk.Label(self, text="Right-click a task to delete it", fg="darkblue")
        self.label.pack(pady=5)

        # Entry for new tasks
        self.task_entry = tk.Entry(self, width=40)
        self.task_entry.pack(pady=5)

        # Add Task Button
        self.add_btn = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_btn.pack(pady=5)

        # Frame for scrollable tasks
        self.canvas = tk.Canvas(self, borderwidth=0, background="#f0f0f0")
        self.frame = tk.Frame(self.canvas, background="#f0f0f0")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)

        # Menu bar with custom colors
        self.menu = Menu(self, bg="midnight blue", fg="white", activebackground="steel blue", activeforeground="white")
        self.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=0, bg="midnight blue", fg="white", activebackground="steel blue", activeforeground="white")
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.quit)


        # Store task labels
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            task_label = tk.Label(self.frame, text=task_text, anchor="w", width=40, bg="white", relief="ridge", padx=5)
            task_label.pack(pady=2, fill="x")
            task_label.bind("<Button-3>", lambda e, lbl=task_label: self.remove_task(lbl))  # Right-click to delete
            self.tasks.append(task_label)
            self.task_entry.delete(0, tk.END)

    def remove_task(self, task_label):
        task_label.destroy()
        self.tasks.remove(task_label)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
