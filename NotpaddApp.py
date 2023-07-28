##Tkinter getiriyor
from tkinter import *

#bütün yapılacak şeyler main adlı fonksiyon içinde
def main():
    #main'e tkinter'i çekiyor
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None


class Window:

    def __init__(self, root):
        self.root = root
        self.root.geometry('654x560')
        self.root.title("NotDefterim")

        # textspace yapıyorum
        self.titlelabel = Label(root, text='Konuyu Giriniz').grid(padx=0, pady=0)
        self.topictext = Text(self.root, width=60, font=50, height=1)
        self.textspace = Text(self.root)

        self.topictext.grid(padx=2, pady=5)
        self.textspace.grid(padx=4, pady=10)

        # kaydetme ve açma butonları
        Button(self.root, text="Save", command=self.savefile).grid(padx=4, pady=10)
        Button(self.root, text="Open", command=self.openfile).grid(padx=6, pady=20)

    pass

    def savefile(self):
        savegui = Tk()
        savegui.geometry('560x50')
        filecontents = self.textspace.get(0.0, END)

        def writefile():
            titlee = self.topictext.get(0.0,END)
            with open(file_name.get() + '.txt', 'w+') as file:
                file.write("KONU:"+titlee)
                file.write(filecontents)
                file.close()
                savegui.destroy()
            return None

        Label(savegui, text="File Name").grid(row=0, column=0)
        file_name = Entry(savegui, width=40)
        file_name.grid(row=0, column=1)

        Button(savegui, text="Save", command=writefile).grid(row=0, column=2)

        return None

    def openfile(self):
        opengui = Tk()
        opengui.geometry('560x50')

        def opennew():
            try:
                with open(file_name.get(), "r") as file:
                    self.textspace.delete(0.0, END)
                    self.textspace.insert(0.0, file.read())
                    file.close()
                    opengui.destroy()
            except FileNotFoundError:
                file_name.delete(0.0, END)
                file_name.insert(0.0, "Dosya bulunamadı.")

            return None

        Label(opengui, text="File Name").grid(row=0, column=0)
        file_name = Entry(opengui, width=40 )
        file_name.grid(row=0, column=1)

        Button(opengui, text="Open", command=opennew).grid(row=0, column=2)

        return None

    pass
#fonksiyonu çalıştır
main()