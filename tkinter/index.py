import tkinter as tk
import os
from client.gui_app import Frame, barra_menu

def main():
    # if os.path.isdir('img') or os.path.isdir('csv') or os.path.isdir('netcdf'):
    #     pass
    # else:
    #     os.makedirs('img/timelapse')
    #     os.mkdir('csv')
    #     os.mkdir('netcdf')
    
    if os.path.isdir('img'):
        pass
    else:
        os.makedirs('img/timelapse')

    if os.path.isdir('csv'):
        pass
    else:
        os.mkdir('csv')

    if os.path.isdir('netcdf'):
        pass
    else:
        os.mkdir('netcdf')

    root = tk.Tk()
    root.title('Calculo de indice hidrico')
    #root.iconbitmap('img/logoubb.ico')
    root.resizable(0,0)
    
    # theme
    root.tk.call("source", "Azure/azure.tcl")
    root.tk.call("set_theme", "dark")
    
    barra_menu(root)

    app = Frame(root = root)

    app.mainloop()

if __name__ == '__main__':
    main()