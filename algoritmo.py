import random as rd
import os
import datetime
 
def palabras_a_codigo_ascii(cadena):
    ascii_vector = []
    contador = 0
    for letra in cadena:
        contador = contador + 1
        ascii_valor = ord(letra)  
        ascii_vector.append(ascii_valor)  
    
    return ascii_vector

def ascii_a_letras(ascii_vector):
    letras_vector = [] 
    for valor in ascii_vector:
        letra = chr(valor)  
        letras_vector.append(letra)  
    
    return letras_vector

def Num_Primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def MCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Generar_D(H):
    while True:
        numero = rd.randint(1, H - 1)
        if numero < H:
            if Num_Primo(numero):
                if MCD(numero, H) == 1:
                    return numero
def generar_numero_con_mcd_y_primo():
    while True:
        numero = rd.randint(1, 10000)  # Generar un n�mero aleatorio entre 2 y 1000
        if Num_Primo(numero):
            if MCD(numero, 1) == 1:
                return numero

def verificar_j_entero(z, k):
    for x in range(1, 30000):  # Itera sobre un rango de valores enteros para x
        j = (1 + x * z) / k
        if j.is_integer():  # Verifica si j es un n�mero entero
            l=int(j)
            return l

def Cancatenar_Lista(aLista):
    cCadena = ''
    for elemento in aLista:
        cCadena = cCadena + elemento
    return cCadena

def Codificar_Descodificar(palabras, mod, expo):
    Vector = palabras_a_codigo_ascii(palabras)
    #print(Vector)
    Palabra = []
    for elemento in Vector:
        base = (elemento ** expo)
        letra = base % mod
        Palabra.append(letra)
        #print(f"letra ", letra)
    MEZCLADO=ascii_a_letras(Palabra)
    #print(MEZCLADO)    
    return MEZCLADO


def ENCRIPTAR_ARCHIVO(name_file_orig, p, q):
    Clave = p*q
    h =(p-1)*(q-1)
    Clave_Privada = Generar_D(h)
    Clave_Publica = verificar_j_entero(h,Clave_Privada)  

    name_file_output = name_file_orig[0:len(name_file_orig)-3] + "enc"

    archivo_out = open( name_file_output,"w", encoding="utf8" )
    archivo_ori = open( name_file_orig,"r", encoding="utf8"  )
    for linea in archivo_ori:
        aListaCara = Codificar_Descodificar(linea,Clave,Clave_Publica)
        linea_encr = Cancatenar_Lista( aListaCara )
        archivo_out.write(linea_encr + "\n")
        
    archivo_ori.close()
    archivo_out.close()
    return Clave, Clave_Privada, name_file_output 

    
def DESENCRIPTAR_ARCHIVO(name_file_encri, Clave, Clave_Privada):
    name_file_output = name_file_encri[0:len(name_file_encri)-3] + "txt"

    archivo_out = open( name_file_output,"w", encoding="utf8" )
    archivo_ori = open( name_file_encri,"r", encoding="utf8" )
    for linea in archivo_ori:
        cCadena = linea[0:len(linea)-1]
        aListaCara = Codificar_Descodificar(cCadena, Clave, Clave_Privada)
        linea_desencr = Cancatenar_Lista( aListaCara )
        archivo_out.write(linea_desencr )
    archivo_ori.close()
    archivo_out.close()

def Encriptar(filename):
    # Nombre de la carpeta que contiene el archivo
    nombre_carpeta = "D:\\UPC\\CICLO 3\\COMPUTACIONAL\\Proyecto\\Pagina Web\\static\\uploads\\"

    # Obtener una lista de todos los archivos dentro de la carpeta
    archivos = os.listdir(nombre_carpeta)

    # Buscar el archivo que deseas leer
    nombre_archivo = filename
    ruta_archivo = None

    for archivo in archivos:
        if archivo == nombre_archivo:
            ruta_archivo = os.path.join(nombre_carpeta, archivo)
            break
    #INICIO
    p=131
    q=151
    print(ruta_archivo)
    cName_File = ruta_archivo
    # =======================================================================
    Clave, Clave_Privada, FileEncr = ENCRIPTAR_ARCHIVO(cName_File , p, q)
    print("CLAVE PRIVADA : ", Clave, Clave_Privada)

    return FileEncr, Clave, Clave_Privada

def Desencriptar(FileEncr, Clave, Clave_Privada):
    desencriptado = DESENCRIPTAR_ARCHIVO(FileEncr, Clave, Clave_Privada)
    return desencriptado
