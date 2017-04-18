#!/usr/bin/env python
#-*- coding: utf-8-*-
import pandas as pd
import numpy as np
from sys import exit
import csv
import re
import xml.etree.ElementTree as ET
import gzip,io
import json,gzip

tabla=pd.read_csv("Municipios-Poblados-Colombia-DANE.csv") #DATAFRAME

def Menu():

    """Funcion que Muestra el Menu"""

    print( """************

Bases de datos de Municipios y Departamentos de colombia

************

Menu

1) Dataframe "Departamentos". Columnas: nombre, código.

2) Dataframe "Municipios". Columnas: nombre, código, departamento.

3) Dataframe "Poblados". Columnas: nombre, código, municipio.

4) Dataframe "Todo"

5) Salir""")

def Datos():

    Menu()

    opc = int(input("Selecione Opcion\n"))

    while (opc >0 and opc <5):

       
        if (opc==1):

            print (tabla[['Nombre-Departamento','Codigo-Departamento']])

            opc = int(input("Selecione Opcion\n"))

        elif(opc==2):

            print (tabla[['Nombre-Municipio','Codigo-Municipio','Nombre-Departamento']])

            opc = int(input("Selecione Opcion\n"))

        elif(opc==3):

            print (tabla[['Nombre-Poblado','Codigo-Poblado','Nombre-Municipio']])

            opc = int(input("Selecione Opcion\n"))

        elif(opc==4):

              print (tabla)

              opc = int(input("Selecione Opcion\n"))

Datos()
exit(0)
