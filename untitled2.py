from tkinter import*
root = Tk()
root.title("MultiDimensional Array")

root.geometry("500x500")
label = Label(root)

Array_1d = ["John","James","Thomson"]
print(Array_1d[0])

Array_2d = [["John","A+"],["James","A"],["Thomson","B"]]
print(Array_2d[0][1])

Array_3d = [["John","A+","Excellent"],["James","A","Good"],["Thomson","B","Good"]]
print(Array_3d[0][0][2])

def report():
    label["text"] = Array_3d[0][0][0] + "Got Grade" + Array_3d[0][0][1] + "And He Is Doing" + Array_3d[0][0][2]

btn = Button(root,text="Show report",command=report)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()