import tkinter as tk
from tkinter import filedialog
from client.plot_netcdf import plot
from client.to_csv import export_csv
from client.generate_timelapse import gen_timelapse
from client.ih_to_csv import ih_export_csv
from client.combinar_netcdf import combinar_netcdf
from client.probandotesislogicafinal import export_ih_to_netcdf
from client.Mapa_mallas_beta import mapa_ih
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime
import os


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Some action')
    menu_inicio.add_command(label='Some action')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Action #2')
    barra_menu.add_cascade(label='Action #3')
    barra_menu.add_cascade(label='Action #4')


class Frame(tk.Frame):

    def __init__(self, root=None):
        super().__init__(root, width=500, height=350)
        self.root = root
        self.pack()
        self.config(bg='gray')

        self.campos_netcdf()

    def campos_netcdf(self):
        # Button open File
        self.button_tmin = tk.Button(
            self, text='Seleccione NetCDF para Temperatura Minima', command=lambda: self.open_file(tipo='tmin'))
        self.button_tmin.grid(row=0, column=0, padx=10, pady=10)

        self.button_tmax = tk.Button(
            self, text='Seleccione NetCDF para Temperatura Maxima', command=lambda: self.open_file(tipo='tmax'))
        self.button_tmax.grid(row=1, column=0, padx=10, pady=10)

        self.button_pr = tk.Button(
            self, text='Seleccione NetCDF para Precipitaciones', command=lambda: self.open_file(tipo='pr'))
        self.button_pr.grid(row=2, column=0, padx=10, pady=10)

        self.button_pr = tk.Button(
            self, text='Seleccione NetCDF para Índice Hídrico', command=lambda: self.open_file(tipo='ih'))
        self.button_pr.grid(row=3, column=0, padx=10, pady=10)

        # Entry's
        self.entry_tmin = tk.Entry(self)
        self.entry_tmin.config(width=50, state='readonly', font=('Arial', 12))
        self.entry_tmin.grid(row=0, column=1, padx=10, pady=10)

        self.entry_tmax = tk.Entry(self)
        self.entry_tmax.config(width=50, state='readonly', font=('Arial', 12))
        self.entry_tmax.grid(row=1, column=1, padx=10, pady=10)

        self.entry_pr = tk.Entry(self)
        self.entry_pr.config(width=50, state='readonly', font=('Arial', 12))
        self.entry_pr.grid(row=2, column=1, padx=10, pady=10)

        self.entry_ih = tk.Entry(self)
        self.entry_ih.config(width=50, state='readonly', font=('Arial', 12))
        self.entry_ih.grid(row=3, column=1, padx=10, pady=10)

        # Button show Map
        self.button_show_tmin = tk.Button(
            self, text='Ver Mapa', command=lambda: self.show_map(tipo='tmin'))
        self.button_show_tmin.grid(row=0, column=2, padx=10, pady=10)

        self.button_show_tmax = tk.Button(
            self, text='Ver Mapa', command=lambda: self.show_map(tipo='tmax'))
        self.button_show_tmax.grid(row=1, column=2, padx=10, pady=10)

        self.button_show_pr = tk.Button(
            self, text='Ver Mapa', command=lambda: self.show_map(tipo='pr'))
        self.button_show_pr.grid(row=2, column=2, padx=10, pady=10)

        # Button export to CSV
        self.button_export_tmin = tk.Button(
            self, text='Exportar a CSV', command=lambda: self.export(tipo='tmin'))
        self.button_export_tmin.grid(row=0, column=3, padx=10, pady=10)

        self.button_export_tmax = tk.Button(
            self, text='Exportar a CSV', command=lambda: self.export(tipo='tmax'))
        self.button_export_tmax.grid(row=1, column=3, padx=10, pady=10)

        self.button_export_pr = tk.Button(
            self, text='Exportar a CSV', command=lambda: self.export(tipo='pr'))
        self.button_export_pr.grid(row=2, column=3, padx=10, pady=10)

        # Button to generate GIF
        self.button_gif_tmin = tk.Button(
            self, text='Generar GIF', command=lambda: self.generate_gif(tipo='tmin'))
        self.button_gif_tmin.grid(row=0, column=4, padx=10, pady=10)

        self.button_gif_tmax = tk.Button(
            self, text='Generar GIF', command=lambda: self.generate_gif(tipo='tmax'))
        self.button_gif_tmax.grid(row=1, column=4, padx=10, pady=10)

        self.button_gif_pr = tk.Button(
            self, text='Generar GIF', command=lambda: self.generate_gif(tipo='pr'))
        self.button_gif_pr.grid(row=2, column=4, padx=10, pady=10)

        # Button to calculate the index risk of water
        # if len(self.entry_tmin.get()) > 0 and len(self.entry_tmax.get()) > 0 and len(self.entry_pr.get()) > 0:
        # Button to merge all netcdf
        # self.lbl_ih = tk.Label(self, text= 'Indice de Riesgo Hídrico')
        # self.lbl_ih.grid(row= 3, column= 0, padx= 10, pady= 10)

        # Button show Map
        self.button_show_ih = tk.Button(
            self, text='Ver Mapa', command=lambda: self.show_map(tipo='ih'))
        self.button_show_ih.grid(row=3, column=2, padx=10, pady=10)

        # Button merge netcdf
        self.button_merge = tk.Button(
            self, text='Exportar a NetCDF', command=lambda: self.validarCampos())
        self.button_merge.grid(row=3, column=3, padx=10, pady=10)

        # Button export to CSV
        self.button_export_ih = tk.Button(
            self, text='Exportar a CSV', command=lambda: self.export_to_csv(tipo='ih', fecha=''))
        self.button_export_ih.grid(row=3, column=4, padx=10, pady=10)

    # Functions open file

    def open_file(self, tipo=['tmin', 'tmax', 'pr', 'ih']):
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
            tipo = 'water_risk_index'
            path_netcdf = self.entry_ih
            title = 'Abrir NetCDF para indice hidrico'

        file = tk.filedialog.askopenfilename(title=title, initialdir=os.getcwd(
        ), filetypes=(("Archivos NetCDF", "*.nc"), ("Cualquier Archivo", "*.*")))

        # validate the correct file
        if tipo in file:
            path_netcdf.config(state='normal')
            path_netcdf.delete(0, tk.END)
            path_netcdf.insert(0, file)
        else:
            tk.messagebox.showerror(
                'Up! Archivo incorrecto', 'Por favor. Seleccione el archivo correspondiente')

    # Functions show map
    def show_map(self, tipo=['tmin', 'tmax', 'pr', 'ih']):
        if tipo == 'ih':
            ruta_ih = self.entry_ih.get()
            msg = 'Por favor, ingrese archivo NetCDF para el índice hídrico'

            if len(ruta_ih) > 0:
                self.show_ih(ruta_netcdf_fecha_zona=ruta_ih)
            else:
                tk.messagebox.showerror('Ups! Faltan archivos NetCDF', msg)
        else:
            if tipo == 'tmin':
                path_netcdf = self.entry_tmin.get()
                msg = 'Por favor, ingrese archivo NetCDF para temperatura minima'
        
            if tipo == 'tmax':
                path_netcdf = self.entry_tmax.get()
                msg = 'Por favor, ingrese archivo NetCDF para temperatura maxima'
            
            if tipo == 'pr':
                path_netcdf = self.entry_pr.get()
                msg = 'Por favor, ingrese archivo NetCDF para precipitaciones'

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
            ruta_ih = self.entry_ih.get()
            msg = 'Por favor, ingrese archivo NetCDF para el índice hídrico'

            if len(ruta_ih) > 0:            
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
        top.geometry("780x80")

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
            ruta_ih = self.entry_ih.get()
            # plot map ih

        res = plot(ruta= path_netcdf, fecha= fecha, tipo= tipo)
        image = ImageTk.PhotoImage(Image.open(res))
        top = tk.Toplevel()
        top.title(titulo + str(fecha))
        top.geometry("800x850")
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
            ruta_ih = self.entry_ih.get()
            # ! EXPORTAR INDICE HIDRCO A CSV
            res = ih_export_csv(ruta= ruta_ih)
            # ! IMPORTANTE
        else:
            res = export_csv(path_netcdf, fecha, tipo)

        if res == None:
            tk.messagebox.showinfo('Exportado a CSV', 'Archivo CSV guardado correctamente en la carpera CSV')
        else:
            tk.messagebox.showerror('Ups! Error al exportar', 'Lo sentimos. No se pudo exportar a CSV')

    def merge_netcdf(self, tmin , tmax, pr):
        res, output_path = combinar_netcdf(netcdf_tmin= tmin, netcdf_tmax= tmax, netcdf_pr= pr)

        print(res, output_path)

        if res == None:
            tk.messagebox.showinfo('Merge exitoso', 'Se combinaron los tres archivos NetCDF de forma exitosa en la carpeta NetCDF')
            return self.modal_ih(ruta_netcdf_merged= output_path)
        else:
            tk.messagebox.showerror('Ups! Error al combinar', 'Lo sentimos. No se pudo combinar los archivos NetCDF')
            return False

    def validarCampos(self):
        ruta_tmin = self.entry_tmin.get()
        ruta_tmax = self.entry_tmax.get()
        ruta_pr = self.entry_pr.get()

        ruta_actual = os.getcwd()
        ruta_completa = os.path.join(ruta_actual, 'netcdf', 'archivo_combinado.nc')

        if len(ruta_tmin) > 0 and len(ruta_tmax) > 0 and len(ruta_pr) > 0:
            # validar que exista el archivo combinado. caso contrario, crearlo
            if os.path.isfile(ruta_completa):
                # modal ih
                return self.modal_ih(ruta_netcdf_merged= ruta_completa)
            else:
                self.merge_netcdf(tmin= ruta_tmin, tmax= ruta_tmax, pr= ruta_pr)
        else: 
            return tk.messagebox.showerror('Ups! Faltan archivos NetCDF', 'Se deben ingresar los archivos tmin, tmax y pr NetCDF para combinarlos ⚠')

    # ? DEFINIR FUNCION PARA CREAR NETCDF POR ZONA Y FECHA (MES) SELECCIONADA
    def ih_to_netcdf(self, ruta, fecha, zona):

        res = export_ih_to_netcdf(ruta_nc_combinado= ruta, fecha= fecha, zona= zona)

        if len(res) > 0:
            tk.messagebox.showinfo('NetCDF Creado', 'Se creó el archivo NetCDF de forma exitosa en la carpeta NetCDF')
        else:
            tk.messagebox.showerror('Ups! Error al crear NetCDF', 'Lo sentimos. No se pudo crear el archivo NetCDF')

    def validar_fecha(self, fecha, zona, ruta):
        start_date = datetime.date(1978, 12, 15)
        ending_date = datetime.date(2019, 10, 30)

        if fecha < start_date or fecha > ending_date:
            return tk.messagebox.showerror('Ups! Fecha invalida', 'Lo sentimos. Ingrese una fecha valida')
        else:
            return self.ih_to_netcdf(ruta, fecha, zona)

    def modal_ih(self, ruta_netcdf_merged):
        top = tk.Toplevel()
        top.title('Seleccione una fecha y zona')
        top.geometry("500x180")

        # Fecha
        lbl = tk.Label(top, text= 'Seleccione una fecha (1978-12-15 y 2019-01-01)')
        lbl.grid(row= 0, column= 0, padx= 10, pady= 10)
        cal = DateEntry(top, selectmode= 'day', date_pattern= 'YYYY-mm-dd')
        cal.grid(row= 0, column= 1, padx= 10, pady= 10)
        
        # Zona
        lbl = tk.Label(top, text= 'Seleccione una zona')
        lbl.grid(row= 1, column= 0, padx= 10, pady= 10)

        OPTIONS = [
            "12",
            "03",
            "04",
            "05",
            "06",
            "07"
        ]

        variable = tk.StringVar(top)
        variable.set(OPTIONS[0]) # default value

        dropdown = tk.OptionMenu(top, variable, *OPTIONS)
        dropdown.grid(row= 1, column= 1, padx= 10, pady= 10)

        self.button_date = tk.Button(top, text= 'Exportar a NetCDF', command= lambda: self.validar_fecha(fecha= cal.get_date(), zona= variable.get(),ruta= ruta_netcdf_merged))
        self.button_date.grid(row= 2, column= 1, padx= 10, pady= 10)

        top.mainloop()

    # ? DEFINIR FUNCION PARA MOSTRAR EL MAPA DE LA ZONA Y FECHA (MES) SELECCIONADA
    def show_ih(self, ruta_netcdf_fecha_zona):
        res = mapa_ih(ruta_netcdf= ruta_netcdf_fecha_zona)

        if res != False:
            # exitoso. ruta de la imagen
            tk.messagebox.showinfo('Mapa IH', 'Se creó el mapa IH de forma exitosa en la carpeta img')
        else:
            # error
            tk.messagebox.showerror('Ups! Error al crear mapa IH', 'Lo sentimos. No se pudo crear el mapa IH')
             
    # ? DEFINIR FUNCION PARA EXPORTAR A CSV LA ZONA Y FECHA (MES) SELECCIONADA

    # ? DEFINIR FUNCION PARA GENERAR GIF DE LA ZONA Y FECHA (MES) SELECCIONADA

    