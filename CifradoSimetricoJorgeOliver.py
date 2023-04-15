#Jorge Oliver López Fierro 22/Septiembre/2020 EncriptadorSimetricoPorSustitución

class Cifrado:
    
    def escribir_palabra(self,mensaje):
        mensajeNuevo=mensaje
        return mensajeNuevo
    
    def encriptacion(self,mensaje):
        mensajeParseado=str(mensaje.lower())
        listaMensaje=list(mensajeParseado)
        alfabeto=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','¿','?']
        alfabetoSustitucion=list(reversed(alfabeto))
        #Volteo el listado de alfabeto para obtener un listado reverse
        indices = [[i for i in range(len(alfabeto)) if item1 == alfabeto[i]]for item1 in listaMensaje]
        #Comparo si la lista reverse tiene los caracteres de las palabras y obtengo sus indices

        #Dado que la lista de indices la convierte a una lista de listas [[0],[1]], convierto esa lista en una lista plana [0,1]
        listaPlanaIndices = []
        for i in indices:
            listaPlanaIndices+=i
        #La palabra ya cifrada quedaría como por ejemplo asi = k3j9dj93j,  y la retorno para que otra funcion la utilice
        palabraCifrada=[ alfabetoSustitucion[i] for i in listaPlanaIndices ]
        return(palabraCifrada)
       
    def desencriptar(self,mensaje):
        #Aqui realizo lo mismo solo invierto las listas de alfabeto
        alfabeto=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','¿','?']
        alfabetoSustitucion=list(reversed(alfabeto))
        indices = [[i for i in range(len(alfabetoSustitucion)) if item1 == alfabetoSustitucion[i]]for item1 in mensaje]
        listaPlanaIndices = []
        for i in indices:
            listaPlanaIndices+=i
        listaDescrifrada=[ alfabeto[i] for i in listaPlanaIndices ]
        mensajeEncriptado = ""
        for g in mensaje:  
            mensajeEncriptado += g
        mensajeDescifrado = ""
        for f in listaDescrifrada:  
            mensajeDescifrado += f 
        print("El mensaje encriptado es:",mensajeEncriptado)
        print("El mensaje desencriptado es:",mensajeDescifrado)
        print("*EL MENSAJE SE BORRÓ POR SEGURIDAD*")
        print("**************************************")

    def encriptarArchivo(self,nombreArchivo):
        #Creo un try en caso que el nombre de archivo no exista y no truene el sistema
        try:
            #convierto la información del archivo a minusculas para que yo pueda comparar correctamente los arreglos
            archivo=str(nombreArchivo.lower())
            
            extension='.txt'
            #Abro el archivo con el nombre enviado y la extensión
            file = open(archivo+extension, 'r')
            archivoChar = list(file.read())
            #cada letra del archivo la convierto a lista [[h],[o],[l],[a]]
            archivoChar = [item.lower() for item in archivoChar]
            #El arreglo de arreglos lo convierto a un arreglo plano [h,o,l,a]
            alfabeto=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','¿','?']
            alfabetoSustitucion=list(reversed(alfabeto))
            #Creo 2 arreglos de alfabeto uno normal y otro volteado
            indices = [[i for i in range(len(alfabeto)) if item1 == alfabeto[i]]for item1 in archivoChar]
            listaPlanaIndices = []
            #Comparo si el arreglo de alfabeto tiene las mismas letras que el archivo y saco indices para sacar todas las letras volteadas del alfabeto alreves
            for i in indices:
                listaPlanaIndices+=i
            textoCifradoLista=[ alfabetoSustitucion[i] for i in listaPlanaIndices ]
            file = open(archivo+extension, "w")
            textoCifradoString = ""
            for g in textoCifradoLista:  
                textoCifradoString += g
            file.write(str(textoCifradoString))
            file.close()
            #Abro de nuevo el archivo y escribo en el el texto ya cifrado y por medio de un for convierto el arreglo de caracteres en una cadena y lo escribo en el archivo
            print("Texto cifrado correctamente")
            print("** COMPRUEBE SU ARCHIVO ENCRIPTADO **")
            print("**************************************")
        except:
            print("Algo salío mal asegurese que el archivo existe en el directorio o que su archivo contenga texto")
            file.close()
            print("**************************************")

    def desencriptarArchivo(self,nombreArchivo):
        #Realicé lo mismo que la otra función solo cambie los arreglos de alfabeto =) 
        try:
            archivo=str(nombreArchivo.lower())
            extension='.txt'
            file = open(archivo+extension, 'r')
            archivoChar = list(file.read())
            archivoChar = [item.lower() for item in archivoChar]
            alfabeto=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','¿','?']
            alfabetoSustitucion=list(reversed(alfabeto))
            indices = [[i for i in range(len(alfabetoSustitucion)) if item1 == alfabetoSustitucion[i]]for item1 in archivoChar]
            listaPlanaIndices = []
            for i in indices:
                listaPlanaIndices+=i
            textoDescifradoLista=[ alfabeto[i] for i in listaPlanaIndices ]
            file = open(archivo+extension, "w")
            textoDescifradoString = ""
            for g in textoDescifradoLista:  
                textoDescifradoString += g
            file.write(str(textoDescifradoString))
            file.close()
            print("Texto descifrado correctamente")
            print("** COMPRUEBE SU ARCHIVO DESENCRIPTADO **")
            print("**************************************")
        except:
            print("Algo salío mal asegurese que el archivo existe en el directorio o que su archivo contenga texto")
            file.close()
            print("**************************************")
        
        
        
      

class Usuario:
    mensajeEscribir=''
    bandera=False
    banderaCarga=False
    banderaCargaDes=False
    objeto=Cifrado()
    opcion=0
    opcionContinuar=0
    print(" _________________________________________________")
    print("|                                                 |")
    print("|          SISTEMA DE ENCRIPTADO SIMÉTRICO        |")
    print("|_________________________________________________|")
    print("")
    while True:      
        print("1.-Emisor del mensaje")
        print("2.-Receptor del mensaje")
        
        print("3.-Encriptar archivo")
        print("4.-Desencriptar archivo")
        print("5.-Salir del sistema")
        opcion=input("   Elija una opción:")
        if opcion=='1':
            if banderaCarga==False:
                while True:     
                    escribirMensaje=input("Escriba su mensaje (Puede incluir espacios y signos de interrogación (NO ACENTOS)):")
                    objeto.encriptacion(escribirMensaje)
                    print("Su mensaje se ha cifrado correctamente")
                    print("**************************************")
                    bandera=True
                    banderaCarga=True
                    break;
            else:
                while True:
                    if bandera==True:
                        print("Ya tiene un mensaje cargado, ¿Desea sobrescribir el mensaje?")
                        print("1.-Si  2.-No")
                        opcionContinuar=input("Elija una opción:")
                        if opcionContinuar=='1':
                            escribirMensaje=input("Escriba el nuevo mensaje:")
                            objeto.encriptacion(escribirMensaje)
                            print("Su mensaje se ha cifrado correctamente")
                            print("**************************************")
                            bandera=True
                            banderaCarga=True
                            break;
                        elif opcionContinuar=='2':
                            break;
                        else:
                            print("Opción desconocida")
        elif opcion=='2':
            while True:
                if bandera==False:
                    print("Aún no se ha escrito ningún mensaje")
                    break;
                else:
                    objeto.desencriptar(objeto.encriptacion(escribirMensaje))
                    bandera=False
                    banderaCarga=False
                    break;
        elif opcion=='3':
            while True:
                print("**************************************")
                print("*El archivo a elegir debe estar en el mismo directorio que este script")
                print("*ASEGURESE QUE SU ARCHIVO CONTENGA TEXTO*")
                continuarSecuencia2=input("¿DESEA CONTINUAR? 1.-SI 2.-NO :")
                try:
                    if continuarSecuencia2=='1':
                        nombreArchivo=input("Escriba el nombre del archivo (SIN EXTENSIÓN) ejemplo(mensaje):")
                        objeto.encriptarArchivo(nombreArchivo)
                        break;
                    elif continuarSecuencia2=='2':
                        break;
                    else:
                        print("Opción desconocida")
                except:
                    print("")
                    
        elif opcion=='4':
            while True:
                print("**************************************")
                print("*El archivo a elegir debe estar en el mismo directorio que este script")
                print("*EL ARCHIVO A ELEGIR SOLO DEBE TENER UNA CAPA DE ENCRIPTADO CON ESTE SISTEMA*")
                print("*SI ELIGE UN ARCHIVO SIN ENCRIPTAR SE PERDERÁ SU INFORMACIÓN*")
                continuarSecuencia=input("¿DESEA CONTINUAR? 1.-SI 2.-NO :")
                try:
                    if continuarSecuencia=='1':
                        nombreArchivoDes=input("Escriba el nombre del archivo (SIN EXTENSIÓN) ejemplo(mensaje):")
                        objeto.desencriptarArchivo(nombreArchivoDes)
                        break;
                    elif continuarSecuencia=='2':
                        break;
                    else:
                        print("Opción desconocida")
                except:
                    print("")
        elif opcion=='5':
            print("Gracias por usar el sistema de encriptado simétrico")
            break;
        else:
            print("Opción desconocida")
            
                    
                
            
            
            
























    
        
    


