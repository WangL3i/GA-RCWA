import numpy as np
from scipy import interpolate

data1 = np.loadtxt('materials/SiO2-Kischkat-Marcos.txt', delimiter='\t', dtype=np.float32, unpack=True)
data2 = np.loadtxt('materials/Ge_Amotchkina.txt', delimiter='\t', dtype=np.float32, unpack=True)
data3 = np.loadtxt('materials/TiO2-Siefke-0.12-125.txt', delimiter='\t', dtype=np.float32, unpack=True)
data4 = np.loadtxt('materials/ZnS_Querry.txt', delimiter='\t', dtype=np.float32, unpack=True)


def SiO2(lam):
    x = data1[0]
    y1 = data1[1]
    y2 = data1[2]
    f1 = interpolate.interp1d(x, y1, kind='cubic')
    f2 = interpolate.interp1d(x, y2, kind='cubic')
    i = f1(lam)
    j = f2(lam)
    return i, j


def Ge(lam):
    x = data2[0]
    y1 = data2[1]
    y2 = data2[2]
    f1 = interpolate.interp1d(x, y1, kind='cubic')
    f2 = interpolate.interp1d(x, y2, kind='cubic')
    i = f1(lam)
    j = f2(lam)
    return i, j


def TiO2(lam):
    x = data3[0]
    y1 = data3[1]
    y2 = data3[2]
    f1 = interpolate.interp1d(x, y1, kind='cubic')
    f2 = interpolate.interp1d(x, y2, kind='cubic')
    i = f1(lam)
    j = f2(lam)
    return i, j


def ZnS(lam):
    x = data4[0]
    y1 = data4[1]
    y2 = data4[2]
    f1 = interpolate.interp1d(x, y1, kind='cubic')
    f2 = interpolate.interp1d(x, y2, kind='cubic')
    i = f1(lam)
    j = f2(lam)
    return i, j

