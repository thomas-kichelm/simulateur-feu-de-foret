from tkinter import *
from random import *
import time
root = Tk()
root.title("SIMULATEUR DE FEU DE FOrÊT (par Thomas KICHELM et Matéo BURKHARD)")
root.geometry("1600x900")
root.minsize(300, 300)
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.x1 ,self.y1 = 0,0
        self.z=self.b=self.x=1
        self.can_x=0
        self.r=self.n=0
        self.click=0
        self.seconde=0
        self.continu=1
        self.liste_3p=["...","..",".","..","..."]
        self.can2=Canvas(self,height=5000,width=5000)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        def change_color(event):

            self.feu=randint(1,self.chance)
            self.x=0
            self.x1 ,self.y1 = event.x ,event.y
            for item in self.can1.find_overlapping(self.x1,self.y1,self.x1,self.y1):
                self.can1.itemconfig(item, fill="orange")
                if self.click!=1:
                    self.click=1
                    maj()

        def pre_create():
            if d.get()==liste_decl[0]:self.chance=4
            if d.get()==liste_decl[1]:self.chance=3
            if d.get()==liste_decl[2]:self.chance=2
            if d.get()==liste_decl[0]:self.decl="l'allumette"
            if d.get()==liste_decl[1]:self.decl="le mégot"
            if d.get()==liste_decl[2]:self.decl="la foudre"
            try:
                print(self.chance)
                l3.grid_forget()
                create_forest()

            except:
                l3.config(text="veuillez saisir un declencheur")

        def create_forest():


            taille_forest=v.get()
            if taille_forest == "petite":
                self.can_x=300
                root.geometry("310x375")

            if taille_forest=="moyenne":
                self.can_x=500
                root.geometry("600x600")
            if taille_forest=="grande":
                self.can_x=700
                root.geometry("800x800")
            self.can1 = Canvas(self,bg='dark grey',height=self.can_x,width=self.can_x)
            for i in range(0,int(nb_arbre.get())):
                x1=randint(0,self.can_x-5)
                y1=randint(0,self.can_x-5)
                self.oval1 = self.can1.create_oval(x1,y1,x1+10,y1+10,width=0,fill='green',tags="arbre")
            for i in range(0,int(nb_sapin.get())):
                x1=randint(0,self.can_x-5)
                y1=randint(0,self.can_x-5)
                self.oval1 = self.can1.create_rectangle(x1,y1,x1+10,y1+10,width=0,fill='green',tags="sapin")
            self.oval2=self.can2.create_oval(self.can_x+5,self.can_x//8+5,self.can_x+15,self.can_x//8+15,width=0,fill='green',tags="arbre")
            self.can2.config(height=self.can_x+10,width=self.can_x+100)
            self.can2.grid()
            self.can1.place(x=0,y=0)


            l5=Label(text="sapin")
            l5.place(x=self.can_x+20,y=self.can_x//8)
            self.QUIT = Button(text="QUIT", fg="red",command=root.destroy)
            self.QUIT.place(x=self.can_x-25,y=self.can_x-2,height=25, width=30)
            self.can1.bind("<Button-1>",change_color)
            l1.config(text="toucher un arbre pour y envoyer {}".format(self.decl))
            l1.place(y=self.can_x+25,x=self.can_x/2)
            nb_arbre.grid_forget()
            taille.grid_forget()
            b1.grid_forget()
            decl.grid_forget()
            l4.grid_forget()
            nb_sapin.grid_forget()

        l1=Label(text=" nombre d arbre dans la foret ?")
        l1.grid()
        nb_arbre = Spinbox(root,from_=100 ,to=10000,increment=10,width=5)

        nb_arbre.grid()
        l4=Label(text ="nombre de sapin (moins inflamable)")
        l4.grid()
        nb_sapin = Spinbox(root,from_=100 ,to=10000,increment=10,width=5)

        nb_sapin.grid()
        listeOptions = ( "petite","moyenne","grande")
        v = StringVar()
        v.set("selectionnez la taille de la foret")
        def click(self):

            global arbre
            if v.get()=="petite":z="500"
            elif v.get()=="moyenne":z="4000"
            elif v.get()=="grande":z="10000"


            nb_arbre.delete(0,5)
            nb_arbre.insert(0,int(int(z)/2))
            nb_sapin.delete(0,5)
            nb_sapin.insert(0,int(int(z)/2))

            l1.config(text="nombre d arbre dans la foret ? ({} arbres sont conseillés pour une forêt {})".format(z,v.get()))
            b1.config(text="creer la foret ",command=pre_create)
            b1.grid()

        taille=  OptionMenu(root, v, *listeOptions,command=click)
        taille.grid()
        b1=Button()
        d=StringVar()
        d.set("selectionnez le déclancheur du feu ")
        liste_decl = ("allumettes (25 % de chance de propagation du feu)","mégots (33 % de chance de propagation)","foudre(50 % de chance de propagation)")
        decl =OptionMenu(root,d,*liste_decl)

        decl.grid()
        l2=Label()
        l3=Label()
        l3.grid()


        def maj():
            if self.continu!=5:
                if self.feu==1:
                    self.seconde+=0.2
                    l4.config(text="nombre de minutes depuis l incendie {}".format(int(self.seconde)))
                    l4.place(x=self.can_x/2-110,y=self.can_x+50)
                    arbre_brulés=(int(nb_arbre.get())+int(nb_sapin.get())-len(self.can1.find_all()))
                    arbre_brulés_pc=((arbre_brulés/(int(nb_arbre.get())+int(nb_sapin.get())))*100)
                    print(arbre_brulés)
                    if arbre_brulés!=0:
                        l2.config(text="le feu à déja brulé {} % des arbres !!".format(int(arbre_brulés_pc)))
                        l2.place(x=self.can_x/2-110,y=self.can_x+27.5)

                    if self.r>4.9:self.r=0
                    liste= self.liste_3p[int(self.r)]
                    l1.config(text="le feu se propage {}".format(liste))
                    l1.place(x=self.can_x/2-110,y=self.can_x+5)
                    self.r+=0.4

                    for item in self.can1.find_overlapping(self.x1,self.y1,self.x1+self.x,self.y1+self.x):
                        self.can1.itemconfig(item, fill="orange")
                    for item in self.can1.find_overlapping(self.x1,self.y1,self.x1+self.x,self.y1-self.x):
                        self.can1.itemconfig(item, fill="orange")
                    for item in self.can1.find_overlapping(self.x1,self.y1,self.x1-self.x,self.y1+self.x):
                        self.can1.itemconfig(item, fill="orange")
                    for item in self.can1.find_overlapping(self.x1,self.y1,self.x1-self.x,self.y1-self.x):
                        self.can1.itemconfig(item, fill="orange")
                    self.x+=0.3
                    if self.x>20:
                        for item in self.can1.find_overlapping(self.x1,self.y1,self.x1+self.z,self.y1+self.z):
                            self.can1.itemconfig(item, fill="black")
                        for item in self.can1.find_overlapping(self.x1,self.y1,self.x1+self.z,self.y1-self.z):
                            self.can1.itemconfig(item, fill="black")
                        for item in self.can1.find_overlapping(self.x1,self.y1,self.x1-self.z,self.y1+self.z):
                            self.can1.itemconfig(item, fill="black")
                        for item in self.can1.find_overlapping(self.x1,self.y1,self.x1-self.z,self.y1-self.z):
                            self.can1.itemconfig(item, fill="black")
                        self.z+=0.3
                    if self.x>40:
                        for item in self.can1.find_overlapping(self.x1,self.y1,self.x1+self.b,self.y1+self.b):
                            self.can1.delete(item)
                        for item in self.can1.find_overlapping(self.x1,self.y1,self.x1+self.b,self.y1-self.b):
                            self.can1.delete(item)
                        for item in self.can1.find_overlapping(self.x1,self.y1,self.x1-self.b,self.y1+self.b):
                            self.can1.delete(item)
                        for item in self.can1.find_overlapping(self.x1,self.y1,self.x1-self.b,self.y1-self.b):
                            self.can1.delete(item)
                        self.b+=0.3
                    if len(self.can1.find_all())==0:
                        l1.config(text="le feu a tout brulé")
                        l2.grid_forget()
                    self.continu=randint(1,1000)
                else:
                    l1.config(text="le feu n a pas pris relancer {}".format(self.decl) )

            else:l1.config(text="le feu s'est eteint")
            root.after(200,maj)









app = Application(master=root)
root.mainloop()
