import tkinter
from tkinter import filedialog

def Hello():
    print ('Yet another hello world')

def Quit ():
    global root
    root.destroy()

def LoadFile():
    fn = tkinter.filedialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    Textbox.delete('1.0','end')
    Textbox.insert('1.0',open(fn, 'rt').read())

def SaveFile():
    fn = tkinter.filedialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open (fn, 'wt').write (Textbox.get('1.0', 'end'))

root = tkinter.Tk()
root.geometry("800x700+0+0")

PanelFrame = tkinter.Frame(root,
                   height = 60, bg ='gray')
PanelFrame.pack(side = 'top', fill = 'x')

TextFrame = tkinter.Frame(root,
                   height = 150, width = 300)
TextFrame.pack(side = 'bottom', fill = 'both', expand = 1)

Textbox = tkinter.Text (TextFrame,
                        font = 'Arial 14', wrap = 'word')

Scrollbar = tkinter.Scrollbar(TextFrame)
Scrollbar['command'] = Textbox.yview()
Textbox['yscrollcommand'] = Scrollbar.set

Textbox.pack(side ='left', fill ='both', expand = 1)
Scrollbar.pack(side = 'right', fill = 'y')


WriteButton = tkinter.Button(root,
                        text='Write',
                        width = 40, height = 5,
                        bg='white', fg='black',
                        command=Hello)

ExitButton = tkinter.Button(root,
                        text='Exit',
                        width = 40, height = 5,
                        bg='white', fg='black',
                        command=Quit)

LoadButton = tkinter.Button(root,
                        text='Load',
                        width = 40, height = 5,
                        bg='white', fg='black',
                        command=LoadFile)

SaveButton = tkinter.Button(root,
                        text='Save',
                        width = 40, height = 5,
                        bg='white', fg='black',
                        command=SaveFile)

LoadButton.place(x=10,y=10, height = 40, width=40)
SaveButton.place (x= 50, y = 10, height = 40, width = 40)
ExitButton.place(x=90,y=10, height = 40, width=40)
WriteButton.place(x=130,y=10, height = 40, width=40)


root.mainloop()