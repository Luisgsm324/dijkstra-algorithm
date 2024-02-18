from tkinter import *
from PIL import Image, ImageTk
from visualization import show_graph
from dijkstra import dijkstra_algorithm

class Screen:
    def __init__(self, graph):
        self.title = "Tokyo Metro"
        self.filephoto = 'assets\logo.png'
        self.window = Tk()
        self.height = self.window.winfo_screenheight()
        self.width = self.window.winfo_screenwidth()
        self.graph = graph
        self.initial_station_var, self.final_station_var = StringVar(), StringVar()
        self.result = None

        # Frames
        self.menu_frame = Frame(self.window)
        self.start_frame = Frame(self.window)
        self.final_frame = Frame(self.window)

    def change_frame(self, prev_frame, next_frame):
        next_frame.pack(fill='both', expand=1)
        prev_frame.forget()
    
    def change_to_menuf(self): # Final -> Menu
        self.label_result.destroy()
        self.menu_frame.pack(fill='both', expand=1)
        self.final_frame.forget()
    
    def change_to_start(self):  # Menu -> Start
        self.start_frame.pack(fill='both', expand=1)
        self.menu_frame.forget()

    def change_to_menu(self): # Start -> Menu
        self.menu_frame.pack(fill='both', expand=1)
        self.start_frame.forget()
    
    def change_to_final(self): # Start -> Final
        self.final_frame.pack(fill='both', expand=1)
        self.start_frame.forget()
    
    def run_menu_frame(self):
        start_button = Button(self.menu_frame, text='Algoritmo', bd=4, font=('Arial', 12), width=15, command=self.change_to_start)
        start_button.place(x = self.width // 2 - 150 // 2, y=300)

        visualize_button = Button(self.menu_frame, text='Visualizar', bd=4, font=('Arial', 12), width=15, command=self.run_graph_visualizer)
        visualize_button.place(x = self.width // 2 - 150 // 2, y=400)
        
        exit_button = Button(self.menu_frame, text='Sair', bd=4, font=('Arial', 12), width=15, command=self.window.destroy)
        exit_button.place(x = self.width // 2 - 150 // 2, y=500)

        self.menu_frame.pack(fill='both', expand=1)

    def run_final_frame(self):
        final_list = ["Início"]
        if self.result != None:
            keys = list(self.result.keys())
            count = 0
            for index in range(len(keys)):
                count += 1
                if index == 0:
                    final_list.append(keys[index-1])
                else:
                    final_list.append(keys[-index-1])
                if count == 5:
                    final_list.append("\n")
                    count = 0
            final_text = " -> ".join(final_list)
            print(final_text)
            self.label_result = Label(self.final_frame, text=final_text, font=('Arial', 20))
            self.label_result.pack()
            back_button = Button(self.final_frame, text='Voltar', bd=4, font=('Arial', 12), width=15, command=self.change_to_menuf)
            back_button.place(x = self.width // 2 - 150 // 2,y = 680)
        show_graph(self.result)

    
    def run_graph_visualizer(self):
        # Estava ocorrendo um problema que ao colocar a função show_graph direto no button ele já rodava, para evitar
        # fiz essa função de run_graph_visualizer (pensando em tirar o fullscreen enquanto o visualizer for clicado e colocar novamente ao fechar, pensar como fazer isso (talvez retornando algo?))
        show_graph(self.graph.nodes)

    def run_dijkstra_algorithm(self):
        # Processo está acontecendo no start
        initial_station, final_station = self.initial_station_var.get(), self.final_station_var.get()
        self.result = dijkstra_algorithm(initial_station, final_station, self.graph)
        self.initial_station_var.set("")
        self.final_station_var.set("")
        self.change_frame(self.start_frame, self.final_frame)
        self.run_final_frame()

    def run_start_frame(self):
        label_initial_station = Label(self.start_frame, text="Estação Inicial: ", font=('Arial', 12))
        label_initial_station.place(x = self.width // 2 - 150 // 2 - 60, y = 300)

        entry_initial_station = Entry(self.start_frame, textvariable=self.initial_station_var)
        entry_initial_station.place(x = self.width // 2 - 120 // 2 + 60, y = 300)

        label_final_station = Label(self.start_frame, text="Estação Final: ", font=('Arial', 12))
        label_final_station.place(x = self.width // 2 - 150 // 2 - 60, y = 400)

        entry_final_station = Entry(self.start_frame,  textvariable=self.final_station_var)
        entry_final_station.place(x = self.width // 2 - 120 // 2 + 60, y = 400)      
        
        back_button = Button(self.start_frame, text='Voltar', bd=4, font=('Arial', 12), width=15, command=self.change_to_menu)
        back_button.place(x=self.width // 2 - 150 // 2 - 100,y=680)

        run_button = Button(self.start_frame, text='Rodar', bd=4, font=('Arial', 12), width=15, command=self.run_dijkstra_algorithm)
        run_button.place(x=self.width // 2 - 150 // 2 + 100,y=680)
        

    def run(self):
        # Setar as config básica
        #self.window.geometry(self.screen_size)
        self.window.attributes('-fullscreen', True)
        self.window.title(self.title)
        self.window.iconphoto(True, PhotoImage(file=self.filephoto), PhotoImage(file=self.filephoto))
        
        # Imagem do Menu
        image = ImageTk.PhotoImage(Image.open("assets\large_logo.png").resize((400, 200)))
        label = Label(self.menu_frame, image=image, padx=200)
        label.place(x=self.width // 2 - 400 // 2, y=25)
        
        self.run_menu_frame()
        
        # Imagem da tela do algoritmo
        image2 = ImageTk.PhotoImage(Image.open("assets\large_logo.png").resize((400, 200)))
        label2 = Label(self.start_frame, image=image2)
        label2.place(x=self.width // 2 - 400 // 2, y=25)

        self.run_start_frame()

        self.window.mainloop()
