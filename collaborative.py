#importación de librerias a usar

import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


import ManejoBd as bd

def collaborative (matriz, puntos, matrizG):

    filas = matriz[:3]

    filasOP= filas*puntos

    Nmatriz = np.vstack(filasOP)

    ptotales = np.sum(Nmatriz, axis = 0)

    listaPtotales = []

    for i in ptotales:
        listaPtotales.append(i)

    

    
    

