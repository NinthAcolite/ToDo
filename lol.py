from datetime import datetime
from tkinter import Tk, Label, StringVar, PhotoImage, Entry, Button


class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, date):
        self.tasks.append((task, date))

    def display_tasks(self):
        window = Tk()
        window.title("Your majesty tasks")

        photo = PhotoImage(file="./monty-python-camelot-dance-monty-python.gif")
        gif_label = Label(window, image=photo)
        gif_label.image = photo
        gif_label.pack()

        Label(window, text="Введите задачу:").pack()
        task_entry = Entry(window)
        task_entry.pack()

        Label(window, text="Введите дату (YYYY-MM-DD):").pack()
        date_entry = Entry(window)
        date_entry.pack()

        def add_task_from_entry():
            task = task_entry.get()
            try:
                date = datetime.strptime(date_entry.get(), "%Y-%m-%d")
                self.add_task(task, date)
            except ValueError:
                print(
                    "Введена некорректная дата. Пожалуйста, введите дату в формате YYYY-MM-DD."
                )

        add_button = Button(
            window, text="Add Royalty Task", command=add_task_from_entry
        )
        add_button.pack()

        now = datetime.now()
        for task, date in self.tasks:
            text = StringVar()
            if date < now:
                text.set(f"{date}: {task}")
                label = Label(window, textvariable=text, fg="red")
            elif date == now:
                text.set(f"{date}: {task}")
                label = Label(window, textvariable=text, fg="green")
            else:
                text.set(f"{date}: {task}")
                label = Label(window, textvariable=text, fg="blue")
            label.pack()
        window.mainloop()


todo = ToDo()
todo.add_task("Find Solid Snake", datetime(2024, 6, 2))
todo.add_task("Walk to the Silent Hill", datetime(2024, 6, 3))
todo.add_task("Destroy MetalGear", datetime(2024, 6, 4))
todo.add_task("Find the Great Mystery", datetime(2024, 6, 15))
todo.add_task("Pet my dog", datetime(2024, 6, 23))
todo.add_task("Rub my cat", datetime(2024, 6, 30))
todo.add_task("Find Sheril", datetime(2024, 7, 3))
todo.display_tasks()
