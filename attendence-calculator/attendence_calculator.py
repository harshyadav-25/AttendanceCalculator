from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("PSIT Attendance Calculator")
root.geometry("380x350")
root.resizable(0, 0)
root.config(bg="lightyellow")

# ---------- Heading ----------
Label(root, text="Attendance Calculator",
      bg="lightyellow", fg="brown",
      font=("Arial", 22, "bold")).pack(pady=15)

# ---------- Frame for Inputs ----------
frame = Frame(root, bg="lightyellow")
frame.pack(pady=10)

Label(frame, text="Total Lectures Held:", bg="lightyellow").grid(row=0, column=0, sticky="w", pady=5)
s1 = Entry(frame, width=20)
s1.grid(row=0, column=1, pady=5)

Label(frame, text="Total Absent Lectures:", bg="lightyellow").grid(row=1, column=0, sticky="w", pady=5)
s2 = Entry(frame, width=20)
s2.grid(row=1, column=1, pady=5)

Label(frame, text="Total OAA Lectures:", bg="lightyellow").grid(row=2, column=0, sticky="w", pady=5)
s3 = Entry(frame, width=20)
s3.grid(row=2, column=1, pady=5)

# ---------- Calculate Function ----------
def calculate():
    try:
        total_lectures = int(s1.get())
        total_absent = int(s2.get())
        total_oaa = int(s3.get())

        percentage = 100 - (((total_absent - total_oaa) / total_lectures) * 100)
        l2.config(text=f"Attendance: {round(percentage, 2)}%")

    except:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

# ---------- Button ----------
Button(root, text="Calculate Attendance", bg="brown", fg="white",
       width=18, height=2, command=calculate).pack(pady=10)

# ---------- Output Label ----------
l2 = Label(root, text="Attendance: --%", bg="lightyellow",
           fg="brown", font=("Arial", 18))
l2.pack(pady=10)

root.mainloop()
