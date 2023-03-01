import datetime
import tkinter as tk

import customtkinter as ctk
from tkcalendar import Calendar

from calc import structureAnalysis

polovi = ["Muški","Ženski"]

class Menu:
    
    
    
    def __init__(self):
        
        
        
        
        self.polovi =   ["Male","Female"]
        self.godine =   [str(i) for i in range(1935,2023)]
        self.cigs =     ["Yes","No"]
        self.zuts =     ["Yes","No"]
        self.pritisak = ["Yes","No"]
        self.hronicna = ["Yes","No"]
        self.umor =     ["Yes","No"]
        self.alergija = ["Yes","No"]
        self.sistanje = ["Yes","No"]
        self.alkohol =  ["Yes","No"]
        self.kasalj =   ["Yes","No"]
        self.dah =      ["Yes","No"]
        self.gutljaj =  ["Yes","No"]
        self.grudi =    ["Yes","No"]
        self.anxs =     ["Yes","No"]
        
        ctk.set_appearance_mode("System")  
        ctk.set_default_color_theme("blue")  
        
        self.app = ctk.CTk()  
        self.app.geometry("1280x720")
        self.app.title("Lung Cancer Prediction")
        
        
        self.frame = ctk.CTkFrame(self.app)
        self.frame.pack(anchor='nw')
        
        self.frameContent = ctk.CTkFrame(self.app)
        self.frameContent.pack(anchor = "center")
        
        self.signature =ctk.CTkFrame(self.app)
        self.signature.pack(anchor = "se",side="bottom")
        
        self.button = ctk.CTkButton(master=self.frame, text="Lung Cancer Analysis", command=self.setup_page1)
        self.button.grid(column=1,row=1,pady=10,padx=10)
        self.infoButton = ctk.CTkButton(master=self.frame, text="About This Project", command = self.setup_page2)
        self.infoButton.grid(column=1,row=2,pady=10,padx=10)
        
        ctk.CTkLabel(self.signature,text="Karišić Đorđe 2023.").pack(anchor="s")
        
        
        self.polVar = ctk.StringVar(master=self.frameContent,value=self.polovi[0])
        self.godVar = ctk.StringVar(master=self.frameContent,value=self.godine[len(self.godine)-1])
        self.cigVar = ctk.StringVar(master=self.frameContent,value=self.cigs[0])
        self.zutVar = ctk.StringVar(master=self.frameContent,value=self.zuts[0])
        
        self.anxVar = ctk.StringVar(master=self.frameContent,value=self.anxs[0])
        
        
        self.pritisakVar = ctk.StringVar(master=self.frameContent,value=self.pritisak[0])
        self.hronicnaVar = ctk.StringVar(master=self.frameContent,value=self.hronicna[0])
        
        self.umorVar = ctk.StringVar(master=self.frameContent,value=self.umor[0])
        self.alergijaVar = ctk.StringVar(master=self.frameContent,value=self.alergija[0])
        self.sistanjeVar = ctk.StringVar(master=self.frameContent,value=self.sistanje[0])
        
        self.alkoholVar = ctk.StringVar(master=self.frameContent,value=self.alkohol[0])
        self.kasaljVar = ctk.StringVar(master=self.frameContent,value=self.kasalj[0])
        self.dahVar = ctk.StringVar(master=self.frameContent,value=self.dah[0])
        
        self.gutljajVar = ctk.StringVar(master=self.frameContent,value=self.gutljaj[0])
        self.grudiVar = ctk.StringVar(master=self.frameContent,value=self.grudi[0])
        
        self.setup_page1()
        self.app.mainloop()
        
    def setup_page2(self):
        for widgets in self.frameContent.winfo_children():
            widgets.destroy() 
            
        greeter=ctk.CTkLabel(self.frameContent,text="About this project")
        
        greeter.cget("font").configure(size=24)
        greeter.grid(column=0,row=0,pady=40)        #columnspan=3
        
        data = ctk.CTkLabel(self.frameContent,text="This application uses Kaggle Dataset Lung-Cancer,\n which provides one csv file with 16 columns and ~300 rows each containing information about people tested for lung cancer.")
        data.grid(column=0,row=1)
        ctk.CTkLabel(self.frameContent,text="It's worth mentioning that there's data inbalance in this dataset.\nThere are much more people who tested positive than negative, which may influence results.").grid(column=0,row=2)
        ctk.CTkLabel(self.frameContent,text="Results are being predicted using a neural network with 4 layers\n A preprocessing normalization layer, two layers with 10 neurons and a ReLU activation function, and a final layer with 1 neuron and linear activation function.").grid(column=0,row=3,pady=20)
        
        
    def setup_page1(self):
        for widgets in self.frameContent.winfo_children():
            widgets.destroy() 
        
        def analyze():
            today = datetime.date.today().year
            
            v1 =0 if self.polVar.get()=="Male" else 1
            v2 = int(today) - int(self.godVar.get())
            v3 = 2 if self.cigVar.get()=="Yes" else 1
            v4 = 2 if self.zutVar.get()=="Yes" else 1
            v45 = 2 if self.anxVar.get()=="Yes" else 1
            v5 = 2 if self.pritisakVar.get()=="Yes" else 1
            v6 = 2 if self.hronicnaVar.get()=="Yes" else 1
            v7 = 2 if self.umorVar.get()=="Yes" else 1
            v8 = 2 if self.alergijaVar.get()=="Yes" else 1
            v9 = 2 if self.sistanjeVar.get()=="Yes" else 1
            v10 = 2 if self.alkoholVar.get()=="Yes" else 1
            v11 = 2 if self.kasaljVar.get()=="Yes" else 1
            v12 = 2 if self.dahVar.get()=="Yes" else 1
            v13 = 2 if self.gutljajVar.get()=="Yes" else 1
            v14 = 2 if self.grudiVar.get()=="Yes" else 1
            print([v1,v2,v3,v4,v45,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14])
            
            txt = structureAnalysis([v1,v2,v3,v4,v45,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14])
                                    
            self.res = ctk.CTkLabel(master=self.frameContent,text = txt).grid(row=11,column=0,pady=50,columnspan=3)
        

        self.pol = ctk.CTkOptionMenu(master=self.frameContent,variable=self.polVar,values=self.polovi)
        self.polL=ctk.CTkLabel(self.frameContent,text="Gender").grid(column=0,row=0)
        self.pol.grid(column=0,row=1)
        
        

        self.god = ctk.CTkEntry(master=self.frameContent,textvariable=self.godVar)
        self.godL=ctk.CTkLabel(self.frameContent,text="Birth year").grid(column=1,row=0)
        self.god.grid(column=1,row=1,padx = [30,30])
        
        
        self.cig = ctk.CTkOptionMenu(master=self.frameContent,variable=self.cigVar,values=self.cigs)
        self.cigL=ctk.CTkLabel(self.frameContent,text="Cigarette consumption?").grid(column=2,row=0)
        self.cig.grid(column=2,row=1)
        
        
        self.zut = ctk.CTkOptionMenu(master=self.frameContent,variable=self.zutVar,values=self.zuts)
        self.zutL=ctk.CTkLabel(self.frameContent,text="Yellow marks on fingers?").grid(column=0,row=2)
        self.zut.grid(column=0,row=3)
        
        
        self.anx = ctk.CTkOptionMenu(master=self.frameContent,variable=self.anxVar,values=self.anxs)
        self.anxL=ctk.CTkLabel(self.frameContent,text="Are you anxious?").grid(column=1,row=2)
        self.anx.grid(column=1,row=3)
        
        
        self.prit = ctk.CTkOptionMenu(master=self.frameContent,variable=self.pritisakVar,values=self.pritisak)
        self.pritL=ctk.CTkLabel(self.frameContent,text="Peer pressure?").grid(column=2,row=2)
        self.prit.grid(column=2,row=3, padx = [30,30])
        
        
        
        self.hron = ctk.CTkOptionMenu(master=self.frameContent,variable=self.hronicnaVar,values=self.hronicna)
        self.hronL=ctk.CTkLabel(self.frameContent,text="Chronic disease?").grid(column=0,row=4)
        self.hron.grid(column=0,row=5)
        
        
        self.um = ctk.CTkOptionMenu(master=self.frameContent,variable=self.umorVar,values=self.umor)
        self.umL=ctk.CTkLabel(self.frameContent,text="Fatigue?").grid(column=1,row=4)
        self.um.grid(column=1,row=5)
        
        self.al = ctk.CTkOptionMenu(master=self.frameContent,variable=self.alergijaVar,values=self.alergija)
        self.alL=ctk.CTkLabel(self.frameContent,text="Any allergies?").grid(column=2,row=4)
        self.al.grid(column=2,row=5,padx = [30,30])
        
        self.sis = ctk.CTkOptionMenu(master=self.frameContent,variable=self.sistanjeVar,values=self.sistanje)
        self.sisL=ctk.CTkLabel(self.frameContent,text="Wheezing?").grid(column=0,row=6)
        self.sis.grid(column=0,row=7)
        
        
        self.alc = ctk.CTkOptionMenu(master=self.frameContent,variable=self.alkoholVar,values=self.alkohol)
        self.alcL=ctk.CTkLabel(self.frameContent,text="Alchohol consumption?").grid(column=1,row=6)
        self.alc.grid(column=1,row=7)
        
        self.kas = ctk.CTkOptionMenu(master=self.frameContent,variable=self.kasaljVar,values=self.kasalj)
        self.kasL=ctk.CTkLabel(self.frameContent,text="Coughing?").grid(column=2,row=6)
        self.kas.grid(column=2,row=7,padx = [30,30])
        
        self.dahp = ctk.CTkOptionMenu(master=self.frameContent,variable=self.dahVar,values=self.dah)
        self.dahpL=ctk.CTkLabel(self.frameContent,text="Shortness of breath?").grid(column=0,row=8)
        self.dahp.grid(column=0,row=9)
        
        
        
        
        self.gut = ctk.CTkOptionMenu(master=self.frameContent,variable=self.gutljajVar,values=self.gutljaj)
        self.gutL=ctk.CTkLabel(self.frameContent,text="Difficulty swallowing?").grid(column=1,row=8)
        self.gut.grid(column=1,row=9)
        
        
        self.gr = ctk.CTkOptionMenu(master=self.frameContent,variable=self.grudiVar,values=self.grudi)
        self.grL=ctk.CTkLabel(self.frameContent,text="Chest pain?").grid(column=2,row=8)
        self.gr.grid(column=2,row=9)
        
        
        
        
        self.submit = ctk.CTkButton(master=self.frameContent, text="Submit", command = analyze)
        self.submit.grid(column=1,row = 10,padx=30,pady=60)
        

        
def main():
    menu = Menu()
    
    
if __name__ == "__main__":
    main()