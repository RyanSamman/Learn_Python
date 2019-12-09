from tkinter import *


def main():

    target_file = "TODO.txt"

    def read():
        output_one.delete(1.0, END)
        outstring = ""
        linecount = 0
        with open(target_file) as file_read:
            for i in file_read.readlines():
                linecount += 1
                outstring += format(linecount, "2d") + ". " + i
            output_one.insert(END, outstring)
        
    def run_add():
        with open(target_file, "a") as file_append:
            input_string = input_one.get() + "\n"
            file_append.write(input_string)
        reset()

    def run_subtract():
        delete_file = "del_" + target_file
        delete_line = eval(input_two.get()) - 1
        outstring = ""

        with open(target_file, "r") as file_delete:
            list = file_delete.readlines()
            add_deleted_line = list.pop(delete_line)

        with open(delete_file, "a") as deleted:
            deleted.write(add_deleted_line + "\n")

        with open(target_file, "w") as file_append:
            for i in list:
                outstring += i
            file_append.write(outstring)

        reset()

    def reset():
        output_one.delete(1.0, END)
        input_one.delete(0, END)
        input_two.delete(0, END)
        read()

    root = Tk()
    root.title("~~ To Do List ~~")
    top_gui = Frame(root)
    top_gui.grid(row=1)
    bottom_gui = Frame(root)
    bottom_gui.grid(row=2)

    # Top GUI
    Label(top_gui, text="Enter text to be added:", width=34).grid(row=1, column=1)
    runner = Button(top_gui, text="Run", width=34, command=lambda: run_add())
    runner.grid(row=1, column=2)

    input_one = Entry(top_gui, width=80)
    input_one.grid(row=2, column=1, columnspan=2)

    Label(top_gui, text="Enter line to be removed:", width=34).grid(row=3, column=1)
    Button(top_gui, text="Remove", command=lambda: run_subtract(), width=34).grid(row=3, column=2)

    input_two = Entry(top_gui, width=38)
    input_two.grid(row=4, column=1)

    Button(top_gui, text="Reset", command=lambda: reset(), width=34).grid(row=4, column=2)

    # Bottom GUI
    output_one = Text(bottom_gui, width=60, background="light gray")
    output_one.grid(row=2, column=1)
    Button(bottom_gui, width=68, text="QUIT", command=root.destroy, fg="red").grid(row=3, column=1)

    read()

    root.mainloop()


if __name__ == '__main__':
    main()