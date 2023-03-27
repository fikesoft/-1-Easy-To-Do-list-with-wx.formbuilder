import wx
from vista import to_do
import json
import os 
import platform #Modulo para hallar sistema op.

#In this program i used wx.formbuilder to make the  the visual framework
#This is my 1 commit in git hub hi !
app = wx.App()

class to_doframe(to_do):    
    
    def __borar(self,num):
        #Metodo de borar texto 
        #Hacemos una lista con todo lo textos  
        cajitas=[self.m_textCtrl1, self.m_textCtrl2, \
            self.m_textCtrl3, self.m_textCtrl4, self.m_textCtrl5,\
            self.m_textCtrl6,  self.m_textCtrl7, self.m_textCtrl8, \
            self.m_textCtrl9, self.m_textCtrl10,self.m_textCtrl11,\
            self.m_textCtrl12,  self.m_textCtrl13, self.m_textCtrl14, \
            self.m_textCtrl15]
        #Un bucle que ittera sobre la lista y coje  el elemento necesitado  
        for i in cajitas:
            cajitas[num].SetValue("")
            break
    
    def __asignar_in_curso(self, texto):
        #Asignar la columna 2 
        # Buscar la caja que no esta llena 
        for i in [self.m_textCtrl6, self.m_textCtrl7, self.m_textCtrl8, \
            self.m_textCtrl9, self.m_textCtrl10]:
            
            if len(i.GetValue().strip()) == 0:
                # Hay una celda vacía. Intento anadir el texto  
                i.SetValue(texto)
                return True
                #Devuelvo true para despues en usarlo
                
        else:
            # No se ha encontrado una caja vacia 
            return False
            #Devuelvo false para despues en usarlo
    
        
    def __asignar_in_finished (self, texto):
        #Asignar in finished 
        # Buscar la caja que no esta llena 
        for i in [self.m_textCtrl11,\
            self.m_textCtrl12,  self.m_textCtrl13, self.m_textCtrl14, \
            self.m_textCtrl15]:
            
            if len(i.GetValue().strip()) == 0:
                # Hay una celda vacía. Intento anadir el texto  
                i.SetValue(texto)
                return True
                #Devuelvo true para despues en usarlo
                
        else:
            # No se ha encontrado una caja vacia 
            return False
            #Devuelvo false para despues en usarlo

    def __asignar_in_curso_desde_finished(self, texto):
        # Buscar la caja que no esta llena 
        for i in [self.m_textCtrl6, self.m_textCtrl7, self.m_textCtrl8, \
            self.m_textCtrl9, self.m_textCtrl10]:
            
            if len(i.GetValue().strip()) == 0:
                # Hay una celda vacía. Intento anadir el texto  
                i.SetValue(texto)
                return True
                #Devuelvo true para despues en usarlo
                
        else:
            # No se ha encontrado una caja vacia 
            return False
            #Devuelvo false para despues en usarlo
    
    def no_rep(self,objeto):
        # Comprobar si hay texto.
        texto = objeto.GetValue().strip() 
        if len(texto) != 0:
            # Intento añadir el texto en la segunda columna.
            cajita2columna  = self.__asignar_in_curso(texto)
            if  cajita2columna==False :
                # No se ha podido anadir  el texto push up notificaion  
                wx.MessageBox('La segunda columna está llena. Por favor, elimine algunas filas antes  de agregar más.', 'Columna llena', wx.OK | wx.ICON_INFORMATION) 

            else:
                # Dejar la caja vacía
                objeto.SetValue("")
    def no_rep2(self,objeto):
        # Comprobar si hay texto.
        texto = objeto.GetValue().strip() 
        if len(texto) != 0:
            # Intento añadir el texto en la segunda columna.
            cajita2columna  = self.__asignar_in_finished(texto)
            if  cajita2columna==False :
                # No se ha podido anadir  el texto push up notificaion  
                wx.MessageBox('La tercera columna está llena. Por favor, elimine algunas filas antes  de agregar más.', 'Columna llena', wx.OK | wx.ICON_INFORMATION) 

            else:
                # Dejar la caja vacía
                objeto.SetValue("")


    def no_rep3(self,objeto):
        # Comprobar si hay texto.
        texto = objeto.GetValue().strip() 
        if len(texto) != 0:
            # Intento añadir el texto en la segunda columna.
            cajita2columna  = self.__asignar_in_curso_desde_finished(texto)
            if  cajita2columna==False :
                # No se ha podido anadir  el texto push up notificaion  
                wx.MessageBox('La segunda columna está llena. Por favor, elimine algunas filas antes  de agregar más.', 'Columna llena', wx.OK | wx.ICON_INFORMATION) 

            else:
                # Dejar la caja vacía
                objeto.SetValue("")


    #-----------------------Movimiento columnas ----------
    
        
    def TD_St1(self, event):
        self.no_rep(self.m_textCtrl1)

    def TD_X1(self, event):
        self.__borar(int(0))
    
    def TD_St2(self, event):
        self.no_rep(self.m_textCtrl2)
    def TD_X2(self, event):
        self.__borar(int(1))

    def TD_St3(self, event):
        self.no_rep(self.m_textCtrl3)
    def TD_X3(self, event):
        self.__borar(int(2))

    def TD_St4(self, event):
      self.no_rep(self.m_textCtrl4)
    def TD_X4(self, event):
        self.__borar(int(3))

    def TD_St5(self, event):
        self.no_rep(self.m_textCtrl5)

    def TD_X5(self, event):
        self.__borar(int(4))

#-----------Segunda columna-----------
    def IC_Do1(self, event):
        self.no_rep2(self.m_textCtrl6)

    def IC_X1(self, event):
        self.__borar(int(5))


    def IC_Do2(self, event):
        
        self.no_rep2(self.m_textCtrl7)

    def IC_X2(self, event):
        self.__borar(int(6))

    def IC_Do3(self, event):
       
        self.no_rep2(self.m_textCtrl8)

    def IC_X3(self, event):
        self.__borar(int(7))

    def IC_Do4(self, event):
        self.no_rep2(self.m_textCtrl9)
    def IC_X4(self, event):
        self.__borar(int(8))

    def IC_Do5(self, event):
        self.no_rep2(self.m_textCtrl10)

    def IC_X5(self, event):
        self.__borar(int(9))
    #-------------3columna butones ---------
    def Fi_NF1(self, event):
        
       self.no_rep3(self.m_textCtrl11)

    def Fi_X1(self, event):
        self.__borar(int(10))

    def Fi_NF2(self, event):
        
        self.no_rep3(self.m_textCtrl12)

    def Fi_X2(self, event):
        self.__borar(int(11))


    def Fi_NF3(self, event):
        self.no_rep3(self.m_textCtrl13)
    def Fi_X3(self, event):
        self.__borar(int(12))
        

    def Fi_NF4(self, event):
        self.no_rep3(self.m_textCtrl14)

    def Fi_X4(self, event):
        self.__borar(int(13))

    def Fi_NF5(self, event):
        self.no_rep3(self.m_textCtrl15)
    def Fi_X5(self, event):
        self.__borar(int(14))
    #----------------------------Movimento entre columna todo acabado------------------------------
    def save_1(self, event):
        # Obtenemos directorio 
        dir_path = self.m_dirPicker1.GetPath()

        # Lista de todo texto
        cajitas = [
            self.m_textCtrl1, self.m_textCtrl2, self.m_textCtrl3, self.m_textCtrl4,
            self.m_textCtrl5, self.m_textCtrl6, self.m_textCtrl7, self.m_textCtrl8,
            self.m_textCtrl9, self.m_textCtrl10, self.m_textCtrl11, self.m_textCtrl12,
            self.m_textCtrl13, self.m_textCtrl14, self.m_textCtrl15
        ]

        # Crear una lista de listas con los valores de cada textCtrl
        lista = []
        for cajita in cajitas:
            objet = cajita.GetValue()
            lista.append([objet])

        # Crear un diccionario
        valores_textCtrl = {
            "m_textCtrl1": lista[0],
            "m_textCtrl2": lista[1],
            "m_textCtrl3": lista[2],
            "m_textCtrl4": lista[3],
            "m_textCtrl5": lista[4],
            "m_textCtrl6": lista[5],
            "m_textCtrl7": lista[6],
            "m_textCtrl8": lista[7],
            "m_textCtrl9": lista[8],
            "m_textCtrl10": lista[9],
            "m_textCtrl11": lista[10],
            "m_textCtrl12": lista[11],
            "m_textCtrl13": lista[12],
            "m_textCtrl14": lista[13],
            "m_textCtrl15": lista[14]
        }
        # Guardar los valores de cada cajita en un fichero datos.json 
        nom_de_archivo=self.m_textCtrlSave.GetValue()
        if nom_de_archivo[-5:] == ".json":
            archivo= open(os.path.join(dir_path,nom_de_archivo), "w") 
            json.dump(valores_textCtrl, archivo)
            wx.MessageBox("Datos guardados con exito ", "Done", wx.OK | wx.ICON_INFORMATION)
            self.m_textCtrlSave.SetValue("")
        else:
            wx.MessageBox("La extension del fichero no es valido debe ser .json ", 'No se puede guardar', wx.OK | wx.ICON_INFORMATION)

    
    def open_1( self, event):
        
        cajitas = [
                self.m_textCtrl1, self.m_textCtrl2, self.m_textCtrl3, self.m_textCtrl4,
                self.m_textCtrl5, self.m_textCtrl6, self.m_textCtrl7, self.m_textCtrl8,
                self.m_textCtrl9, self.m_textCtrl10, self.m_textCtrl11, self.m_textCtrl12,
                self.m_textCtrl13, self.m_textCtrl14, self.m_textCtrl15
            ]
        #Obtengo el directorio  que ha sido selecionada 
        directorio = self.m_filePicker1.GetPath()
        try:
            if directorio[-5:] == ".json":
                #Abro a fichero  que ha sido selecionado 
                archivo2 = open(directorio,"r")
                #Cargo los datos del dicionario
                valores=json.load(archivo2)
                #Cierro el fichero 
                archivo2.close()
                
                #Compruebo si es windows o linux 
                if platform.system() == 'Windows':
                    directorio = directorio.replace('\\', '/')
                else:
                    pass 
                #Hago un  bucle para iterar tantas veces cuanto cajas haya 
                for i in range(len(cajitas)):
                    #Dato va ser el obejto de  la lista al que vamos a acceder
                    dato = "m_textCtrl{}".format(str(i+1))#I+1 ya que se empieza desde 0 
                    setvalu = valores[dato][0] #Accedemos al objeto de la lista  
                    cajitas[i].SetValue("".join(setvalu)) # Plazamos el valor en una lista para hacer operaciones con el 
        except:
            wx.MessageBox("La extension del fichero no es valido debe ser .json o el fichero no ha sido creado por el programa ", 'No se puede guardar', wx.OK | wx.ICON_INFORMATION)


frame = to_doframe(None)
frame.Show()
app.MainLoop()

