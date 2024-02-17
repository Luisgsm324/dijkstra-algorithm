from tkinter import *
from PIL import Image, ImageTk
from visualization import show_graph

class Screen:
    def __init__(self, graph):
        self.title = "Tokyo Metro"
        self.filephoto = 'assets\logo.png'
        self.window = Tk()
        self.graph = graph
        self.initial_station_var, self.final_station_var = StringVar(), StringVar()

        # Frames
        self.menu_frame = Frame(self.window)
        self.start_frame = Frame(self.window)

    def change_to_start(self):  
        self.start_frame.pack(fill='both', expand=1)
        self.menu_frame.forget()

    def change_to_menu(self):
        self.menu_frame.pack(fill='both', expand=1)
        self.start_frame.forget()
    
    def run_menu_frame(self):
        start_button = Button(self.menu_frame, text='Algoritmo', bd=4, font=('Arial', 12), width=15, command=self.change_to_start)
        start_button.place(x=570, y=300)
        
        exit_button = Button(self.menu_frame, text='Sair', bd=4, font=('Arial', 12), width=15, command=self.window.destroy)
        exit_button.place(x=570, y=500)
        

        self.menu_frame.pack(fill='both', expand=1)
    
    def run_algorithm(self):
        initial_station, final_station = self.initial_station_var.get(), self.final_station_var.get()
        print(initial_station, final_station)
        print("Teste")
        self.initial_station_var.set("")
        self.final_station_var.set("")

    def run_start_frame(self):
        label_initial_station = Label(self.start_frame, text="Estação Inicial: ", font=('Arial', 12))
        label_initial_station.place(x = 500, y = 300)

        entry_initial_station = Entry(self.start_frame, textvariable=self.initial_station_var)
        entry_initial_station.place(x = 700, y = 300)

        label_final_station = Label(self.start_frame, text="Estação Final: ", font=('Arial', 12))
        label_final_station.place(x = 500, y = 400)

        entry_final_station = Entry(self.start_frame,  textvariable=self.final_station_var)
        entry_final_station.place(x = 700, y = 400)      
        
        back_button = Button(self.start_frame, text='Voltar', bd=4, font=('Arial', 12), width=15, command=self.change_to_menu)
        back_button.place(x=10,y=680)

        run_button = Button(self.start_frame, text='Rodar', bd=4, font=('Arial', 12), width=15, command=self.run_algorithm)
        run_button.place(x=500,y=680)
        

    def run(self):
        # Setar as config básica
        #self.window.geometry(self.screen_size)
        self.window.attributes('-fullscreen', True)
        self.window.title(self.title)
        self.window.iconphoto(True, PhotoImage(file=self.filephoto))
        

        image = ImageTk.PhotoImage(Image.open("assets\large_logo.png").resize((400, 200)))
        label = Label(self.menu_frame, image=image, padx=200)
        label.place(x=450, y=25)
        
        self.run_menu_frame()
        
        image2 = ImageTk.PhotoImage(Image.open("assets\large_logo.png").resize((400, 200)))
        label2 = Label(self.start_frame, image=image2)
        label2.place(x=450, y=25)

        self.run_start_frame()
        self.window.mainloop()

#screen = Screen()

#screen.run()