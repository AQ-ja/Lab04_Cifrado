
import math
import random
import numpy as np
from skimage.data import camera
from PIL import Image
import matplotlib.pyplot as plt
import re
import matplotlib.pyplot as plt
from pygal import Histogram
from pygal.style import Style


def test(string, th=0.05):
    n = len(string)
    ones = string.count("1")
    zero = string.count("0")
    s = abs(ones-zero)
    p = math.erf(float(s/(math.sqrt(float(n))*math.sqrt(2.0))))
    sucess = (p >= th)
    if sucess == True:
        return [p, "SUCCESS"]
    else:
        return [p, "FAIL"]


def Wichmann_Hill(seedlst, listlength):
    seed1 = seedlst[0]
    seed2 = seedlst[1]
    seed3 = seedlst[2]

    numlist = []
    for i in range(listlength):

        seed1 = (171 * seed1) % 30269
        seed2 = (172 * seed2) % 30307
        seed3 = (170 * seed3) % 30323

        numlist.append((((seed1)/30269) + ((seed2) /
                       30307) + ((seed3)/30323)) % 1)

    # print(numlist[0:50])
        for i in range(len(numlist)):
            if numlist[i] <= 0.5:
                numlist.remove(numlist[i])
                numlist.append(0)
            if numlist[i] > 0.5:
                numlist.remove(numlist[i])
                numlist.append(1)
    numlist = "".join([str(_) for _ in numlist])

    return numlist

# Funcion XOR de dos cadenas


def xor(a, b):
    m = len(a)
    n = len(b)
    maxx = max(m, n)
    if (m < n):
        a = a + (n-m)*'0'
    if (n < m):
        b = b + (m-n)*'0'

    c = ''
    for i in range(0, maxx):
        c = c + str(int(a[i]) ^ int(b[i]))
    return c

# Funcion de generador pseudo aleatorio LCG


def LCG(a, b, N):
    bc = ''
    t = 16
    k = 8

    try:
        parse = list(map(int, [a, b, N]))
        a = parse[0]
        b = parse[1]
        N = parse[2]
    except:
        return "Como que no funciona"

    x = round(random.random() * 200) % N

    for i in range(t):
        x = (a*x + b) % N  # Segun la formula del lab
        binary = bin(x).replace('b', '').zfill(k)
        bc += binary

    return bc

# Funcion XOR de LFSR


def xorLFSR(temp_list1, inp_leng, tap_positions, temp_list2):
    xorLFSR = temp_list1[inp_leng-1]
    for i in range(len(tap_positions)-1):
        xorLFSR = temp_list1[tap_positions[i]] ^ xorLFSR
    temp_list2.append(xorLFSR)
    return temp_list2

# Funcion de generador de LFSR


def LFSR(bits, tap_positions, inp_data, op_bits):

    tap_positions = [int(i) for i in tap_positions]

    inp_data.insert(0, inp_data[len(inp_data)-1])
    inp_data.pop()

    output = [0]
    inp_leng = len(inp_data)
    temp_list1 = inp_data
    temp_list2 = []
    for i in range(int(op_bits)):
        output.insert(0, temp_list1[inp_leng-1])
        xorLFSR(temp_list1, inp_leng, tap_positions, temp_list2)
        for i in range(inp_leng - 1):
            temp_list2.append(temp_list1[i])

        temp_list1 = temp_list2
        temp_list2 = []

    output.pop()
    output.reverse()
    output_data = ''.join(str(x) for x in output)
    return output_data


datosAgrupados = []

for i in range(1000):
    seed1 = np.random.randint(1, 30000)
    seed2 = np.random.randint(1, 30000)
    seed3 = np.random.randint(1, 30000)
    semillas = [seed1, seed2, seed3]
    bits = np.random.randint(1, 30000)
    # Numero aleatorio para la funcion LFSR
    tap_positions = [np.random.randint(1, 30000)]
    # Arreglo cambiante
    # Numero aleatorio del tamano de la semilla fuente para la funcioon LFSR
    # Cambiar para que cambie la imagen
    sizeinp_data = np.random.randint(1, 100)
    # Genera una lista de bits de longitud aleatoria para poder usarse en el generador de LFSR
    inp_data = np.random.randint(2, size=sizeinp_data)
    inp_data = [int(i) for i in inp_data]
    op_bits = 10
    # Llama a la funcion LFSR
    # s2 = LFSR(bits, tap_positions, inp_data, op_bits)
    # s2 = Wichmann_Hill(semillas, 8)
    s2 = LCG(7, 8, 5)
    print(s2)
    # intervalos = ['00', '01', '10', '11']
    datosAgrupados.append(test(s2))
    print(i, test(s2))


# print(LCG(7, 8, 5))
# print(Wichmann_Hill(semillas, 8))


# print(test("1010111101101011"))
