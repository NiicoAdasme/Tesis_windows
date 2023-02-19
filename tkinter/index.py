import tkinter as tk
import os
from client.gui_app import Frame, barra_menu

def main():
    if os.path.isdir('img') or os.path.isdir('csv'):
        pass
    else:
        os.makedirs('img/timelapse')
        os.mkdir('csv')
    
    root = tk.Tk()
    root.title('Calculo de indice hidrico')
    #root.iconbitmap('img/logoubb.ico')
    root.resizable(0,0)
    
    barra_menu(root)

    app = Frame(root = root)

    app.mainloop()

if __name__ == '__main__':
    main()