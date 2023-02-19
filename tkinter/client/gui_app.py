import tkinter as tk
from tkinter import filedialog
from client.plot_netcdf import plot
from client.to_csv import export_csv
from client.generate_timelapse import gen_timelapse
from client.ih_to_csv import ih_to_csv
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu= barra_menu, width= 300, height= 300)

    menu_inicio = tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label= 'Inicio', menu= menu_inicio)

    menu_inicio.add_command(label= 'Some action')
    menu_inicio.add_command(label= 'Some action')
    menu_inicio.add_command(label= 'Salir', command= root.destroy)

    barra_menu.add_cascade(label= 'Action #2')
    barra_menu.add_cascade(label= 'Action #3')
    barra_menu.add_cascade(label= 'Action #4')

class Frame(tk.Frame):
    
    def __init__(self, root = None):
        super().__init__(root, width= 500, height= 350)
        self.root = root
        self.pack()
        self.config(bg= 'gray')

        self.campos_netcdf()

    def campos_netcdf(self):
        # Button open File
        self.button_tmin = tk.Button(self, text= 'Seleccione NetCDF para Temperatura Minima', command= lambda:self.open_file(tipo= 'tmin'))
        self.button_tmin.grid(row= 0, column= 0, padx= 10, pady= 10)

        self.button_tmax = tk.Button(self, text= 'Seleccione NetCDF para Temperatura Maxima', command= lambda:self.open_file(tipo= 'tmax'))
        self.button_tmax.grid(row= 1, column= 0, padx= 10, pady= 10)

        self.button_pr = tk.Button(self, text= 'Seleccione NetCDF para Precipitaciones', command= lambda:self.open_file(tipo= 'pr'))
        self.button_pr.grid(row= 2, column= 0, padx= 10, pady= 10)

        # Entry's
        self.entry_tmin = tk.Entry(self)
        self.entry_tmin.config(width= 50, state='readonly', font= ('Arial', 12))
        self.entry_tmin.grid(row=0, column= 1, padx= 10, pady= 10)

        self.entry_tmax = tk.Entry(self)
        self.entry_tmax.config(width= 50, state='readonly', font= ('Arial', 12))
        self.entry_tmax.grid(row=1, column= 1, padx= 10, pady= 10)

        self.entry_pr = tk.Entry(self)
        self.entry_pr.config(width= 50, state='readonly', font= ('Arial', 12))
        self.entry_pr.grid(row=2, column= 1, padx= 10, pady= 10)

        # Button show Map
        self.button_show_tmin = tk.Button(self, text= 'Ver Mapa', command= lambda:self.show_map(tipo= 'tmin'))
        self.button_show_tmin.grid(row= 0, column= 2, padx= 10, pady= 10)
        
        self.button_show_tmax = tk.Button(self, text= 'Ver Mapa', command= lambda:self.show_map(tipo= 'tmax'))
        self.button_show_tmax.grid(row= 1, column= 2, padx= 10, pady= 10)
        
        self.button_show_pr = tk.Button(self, text= 'Ver Mapa', command= lambda:self.show_map(tipo= 'pr'))
        self.button_show_pr.grid(row= 2, column= 2, padx= 10, pady= 10)


        # Button export to CSV
        self.button_export_tmin = tk.Button(self, text= 'Exportar a CSV', command= lambda:self.export(tipo= 'tmin'))
        self.button_export_tmin.grid(row= 0, column= 3, padx= 10, pady= 10)
        
        self.button_export_tmax = tk.Button(self, text= 'Exportar a CSV', command= lambda:self.export(tipo= 'tmax'))
        self.button_export_tmax.grid(row= 1, column= 3, padx= 10, pady= 10)
        
        self.button_export_pr = tk.Button(self, text= 'Exportar a CSV', command= lambda:self.export(tipo= 'pr'))
        self.button_export_pr.grid(row= 2, column= 3, padx= 10, pady= 10)

        # Button to generate GIF
        self.button_gif_tmin = tk.Button(self, text= 'Generar GIF', command= lambda: self.generate_gif(tipo= 'tmin') )
        self.button_gif_tmin.grid(row= 0, column= 4, padx= 10, pady= 10)

        self.button_gif_tmax = tk.Button(self, text= 'Generar GIF', command= lambda: self.generate_gif(tipo= 'tmax'))
        self.button_gif_tmax.grid(row= 1, column= 4, padx= 10, pady= 10)

        self.button_gif_pr = tk.Button(self, text= 'Generar GIF', command= lambda: self.generate_gif(tipo= 'pr'))
        self.button_gif_pr.grid(row= 2, column= 4, padx= 10, pady= 10)

        # Button to calculate the index risk of water
        #if len(self.entry_tmin.get()) > 0 and len(self.entry_tmax.get()) > 0 and len(self.entry_pr.get()) > 0:
        # Button to merge all netcdf
        self.lbl_ih = tk.Label(self, text= 'Calcular indice de riesgo hidrico')
        self.lbl_ih.grid(row= 3, column= 0, padx= 10, pady= 10)

        # Button show Map
        self.button_show_ih = tk.Button(self, text= 'Ver Mapa', command= lambda:self.show_map(tipo= 'ih'))
        self.button_show_ih.grid(row= 3, column= 1, padx= 10, pady= 10)

        # Button export to CSV
        self.button_export_ih = tk.Button(self, text= 'Exportar a CSV', command= lambda:self.export(tipo= 'ih'))
        self.button_export_ih.grid(row= 3, column= 2, padx= 10, pady= 10)

        # Button to generate GIF
        self.button_gif_ih = tk.Button(self, text= 'Generar GIF', command= lambda: self.generate_gif(tipo= 'ih') )
        self.button_gif_ih.grid(row= 3, column= 3, padx= 10, pady= 10)

    # Functions open file
    def open_file(self, tipo= ['tmin', 'tmax', 'pr', 'ih']):
        if tipo == 'tmin':
            path_netcdf = self.entry_tmin
            title = 'Abrir NetCDF para temperatura minima'
        
        if tipo == 'tmax':
            path_netcdf = self.entry_tmax
            title = 'Abrir NetCDF para temperatura maxima'
        
        if tipo == 'pr':
            path_netcdf = self.entry_pr
            title = 'Abrir NetCDF para precipitaciones'
        
        if tipo == 'ih':
            path_netcdf = self.entry_ih
            title = 'Abrir NetCDF para indice hidrico'

        file = tk.filedialog.askopenfilename(title= title, initialdir= 'C:/', filetypes= (("Archivos NetCDF","*.nc"), ("Cualquier Archivo", "*.*")))
        
        # validate the correct file
        if tipo in file:
            path_netcdf.config(state= 'normal')
            path_netcdf.delete(0, tk.END)
            path_netcdf.insert(0, file)
        else:
            tk.messagebox.showerror('Up! Archivo incorrecto', 'Por favor. Seleccione el archivo correspondiente')


    # Functions show map
    def show_map(self, tipo= ['tmin', 'tmax', 'pr', 'ih']):
        if tipo == 'tmin':
            path_netcdf = self.entry_tmin.get()
            msg = 'Por favor, ingrese archivo NetCDF para temperatura minima'
        
        if tipo == 'tmax':
            path_netcdf = self.entry_tmax.get()
            msg = 'Por favor, ingrese archivo NetCDF para temperatura maxima'
        
        if tipo == 'pr':
            path_netcdf = self.entry_pr.get()
            msg = 'Por favor, ingrese archivo NetCDF para precipitaciones'

        if tipo == 'ih':
            ruta_tmin = self.entry_tmin.get()
            ruta_tmax = self.entry_tmax.get()
            ruta_pr = self.entry_pr.get()
            msg = 'Son necesarios los archivos NetCDF de temperatura minima, maxima y de precipitaciones, para calcular el indice de riesgo hidrico'

            if len(ruta_tmin) > 0 and len(ruta_tmax) > 0 and len(ruta_pr) > 0:            
                self.modal_calendar(tipo= tipo, action= 'plot')
            else:
                tk.messagebox.showerror('Ups! Faltan archivos NetCDF', msg)

        
        if len(path_netcdf) > 0:
            # Create a modal to show the message
            self.modal_calendar(tipo= tipo, action= 'plot')
        else:
            tk.messagebox.showerror('Ups! Se te ha olvidado el archivo', msg)

    #  Function export to CSV
    def export(self, tipo= ['tmin', 'tmax', 'pr', 'ih']):
        if tipo == 'tmin':
            path_netcdf = self.entry_tmin.get()
            msg = 'Por favor, ingrese archivo NetCDF para temperatura minima'
        
        if tipo == 'tmax':
            path_netcdf = self.entry_tmax.get()
            msg = 'Por favor, ingrese archivo NetCDF para temperatura maxima'
        
        if tipo == 'pr':
            path_netcdf = self.entry_pr.get()
            msg = 'Por favor, ingrese archivo NetCDF para precipitaciones'
            
        if tipo == 'ih':
            ruta_tmin = self.entry_tmin.get()
            ruta_tmax = self.entry_tmax.get()
            ruta_pr = self.entry_pr.get()
            msg = 'Son necesarios los archivos NetCDF de temperatura minima, maxima y de precipitaciones, para calcular el indice de riesgo hidrico'

            if len(ruta_tmin) > 0 and len(ruta_tmax) > 0 and len(ruta_pr) > 0:            
                self.modal_calendar(tipo= tipo, action= 'csv')
            else:
                tk.messagebox.showerror('Ups! Faltan archivos NetCDF', msg) 
        
        if len(path_netcdf) > 0:
            self.modal_calendar(tipo= tipo, action= 'csv')
        else:
            tk.messagebox.showerror('Ups! Se te ha olvidad el archivo', msg)


    def modal_calendar(self, tipo= ['tmin', 'tmax', 'pr', 'ih'], action= ['plot', 'csv']):
        top = tk.Toplevel()
        top.title('Seleccione una fecha')
        top.geometry("680x80")

        lbl = tk.Label(top, text= 'Seleccione una fecha entre 1978-12-15 y 2019-01-01 (Formato: YYYY-MM-DD)')
        lbl.grid(row= 0, column= 0, padx= 10, pady= 10)
        cal = DateEntry(top, selectmode= 'day', date_pattern= 'YYYY-mm-dd')
        cal.grid(row= 0, column= 1, padx= 10, pady= 10)

        if tipo == 'tmin':
            title = 'Mapa de temperatura minima de '

        if tipo == 'tmax':
            title = 'Mapa de temperatura maxima de '

        if tipo == 'pr':
            title= 'Mapa de precipitaciones de '

        if tipo == 'ih':
            title= 'Mapa de indice de riesgo hidrico de '

        if action == 'plot':
            texto = 'Ver Mapa'
        else:
            texto = 'Exportar a CSV'

        self.button_date = tk.Button(top, text= texto, command= lambda: self.validate_date(fecha= cal.get_date(), 
                                                                                    titulo= title, tipo= tipo, action= action))
        self.button_date.grid(row= 0, column= 2, padx= 10, pady= 10)

        top.mainloop()
    
    # validate date in a valid range
    def validate_date(self, fecha, titulo, tipo = ['tmin', 'tmax', 'pr', 'ih'], action= ['plot', 'csv']):
        start_date = datetime.date(1978, 12, 15)
        ending_date = datetime.date(2019, 10, 30)
        if fecha < start_date or fecha > ending_date:
            return tk.messagebox.showerror('Ups! Fecha fuera de rango', 
                                            'Por favor, ingrese una fecha entre 1978-12-15 y 2019-10-30')
        else:
            if action == 'plot':
                self.modal_map(titulo= titulo, fecha= fecha, tipo= tipo)
            else:
                self.export_to_csv(fecha= fecha, tipo= tipo)

    # show image
    def modal_map(self, titulo, fecha, tipo= ['tmin', 'tmax', 'pr', 'ih']):
        if tipo == 'tmin':
            path_netcdf= self.entry_tmin.get()
        
        if tipo == 'tmax':
            path_netcdf= self.entry_tmax.get()

        if tipo == 'pr':
            path_netcdf= self.entry_pr.get()

        if tipo == 'ih':
            ruta_tmin = self.entry_tmin.get()
            ruta_tmax = self.entry_tmax.get()
            ruta_pr = self.entry_pr.get()

            # plot map ih

        res = plot(ruta= path_netcdf, fecha= fecha, tipo= tipo)
        image = ImageTk.PhotoImage(Image.open(res))
        top = tk.Toplevel()
        top.title(titulo + str(fecha))
        top.geometry("800x750")
        lbl = tk.Label(top, image= image)
        lbl.grid(row= 0, column= 0)
        tk.messagebox.showinfo('Imagen Guardada', 'La imagen se guardó correctamente en '+ str(res))
        top.mainloop()

    # geenerate gif
    def generate_gif(self, tipo= ['tmin', 'tmax', 'pr']):
        if tipo == 'tmin':
            path_netcdf= self.entry_tmin.get()
        
        if tipo == 'tmax':
            path_netcdf= self.entry_tmax.get()

        if tipo == 'pr':
            path_netcdf= self.entry_pr.get()
        
        res = gen_timelapse(ruta= path_netcdf, tipo= tipo)
        
        print('respuesta del timelapse: '+ res)

        if len(res) > 0:
            tk.messagebox.showinfo('GIF Guardado', 'El GIF se guardó correctamente en '+ res)
        else:
            tk.messagebox.showerror('Ups! Error al generar GIF', 'Lo sentimos. Hubo un error al generar el GIF')


    # export to csv
    def export_to_csv(self, fecha, tipo= ['tmin', 'tmax', 'pr', 'ih']):
        if tipo == 'tmin':
            path_netcdf= self.entry_tmin.get()
        
        if tipo == 'tmax':
            path_netcdf= self.entry_tmax.get()

        if tipo == 'pr':
            path_netcdf= self.entry_pr.get()

        if tipo == 'ih':
            ruta_tmin = self.entry_tmin.get()
            ruta_tmax = self.entry_tmax.get()
            ruta_pr = self.entry_pr.get()
            res = ih_to_csv(ruta_tmin= ruta_tmin, ruta_tmax= ruta_tmax, ruta_pr= ruta_pr, fecha= fecha)
        else:
            res = export_csv(path_netcdf, fecha, tipo)

        if res == None:
            tk.messagebox.showinfo('Exportado a CSV', 'Archivo CSV guardado correctamente en la carpera CSV')
        else:
            tk.messagebox.showerror('Ups! Error al exportar', 'Lo sentimos. No se pudo exportar a CSV')

