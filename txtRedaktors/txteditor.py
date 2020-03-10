'''Vienkārš python teksta redaktors. Līdzinās notpad aplikācijai.
Programmu izveidoja Mārtiš Nīmanis D2-3.
'''
from tkinter import Tk, scrolledtext, filedialog, Menu, messagebox, END

#root ir galvenajam logs
root = Tk(className = " Teksta editors")
textArea = scrolledtext.ScrolledText(root, width=70, height=80) # height nezkādēļ nestrādā

#Funkcijas
def openFile():
    file = filedialog.askopenfile( parent=root, mode = 'rb', title='Izvēlies teksta failu') #Nestrādā: filetipe=("Teksta fails", "*.txt"), ("Visi faili"","."))

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode = 'w')
    
    if file != None:
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def closeWindow():
    if messagebox.askyesno("Iziet", "Vai esat droši, ka vēlaties iziet?"):
        root.destroy()
        
def about():
    label = messagebox.showinfo("Par aplikāciju", "Mārtiņa Nīmaņa D2-3 teksta redaktors.\nAtdarina notepad.")
      
#Izvēlnes opcijas
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Jauns") #vēl nav gatava funkcija
fileMenu.add_command(label="Atvērt", command = openFile)
fileMenu.add_command(label="Saglabāt", command = saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Iziet", command = closeWindow)
textArea.pack()

menu.add_cascade(label="Pamācība") #trūkst pamācības
menu.add_cascade(label="Par programmu", command = about)

root.mainloop()#patur galveno logu atvērtu
