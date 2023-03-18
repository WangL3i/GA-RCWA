import numpy as np
from scipy import integrate

c1 = 3.7419e-16  # W·m^2
c2 = 1.4388e-2  # m·K


def I_BB(Lambda):
    Lambda = Lambda / 10**6  # m
    e_bb = (c1 / Lambda ** 5) / (np.exp(c2/(Lambda*523))-1)
    return e_bb


wavelength0 = np.arange(3, 5.01, 0.1)
E_0_0 = I_BB(wavelength0)
wavelength0_0 = wavelength0/10**6
I_0_0 = integrate.simps(E_0_0, wavelength0_0)

wavelength1 = np.arange(5, 8.01, 0.1)
E_1_0 = I_BB(wavelength1)
wavelength1_0 = wavelength1/10**6
I_1_0 = integrate.simps(E_1_0, wavelength1_0)

wavelength2 = np.arange(8, 14.01, 0.1)
E_2_0 = I_BB(wavelength2)
wavelength2_0 = wavelength2/10**6
I_2_0 = integrate.simps(E_2_0, wavelength2_0)


def emissivity_aver(emissivity):
    data0 = []
    for i in range(len(wavelength0)):
        data0.append(emissivity[i]*I_BB(wavelength0[i]))
    data0 = np.array(data0)
    epsilon_3_5 = integrate.simps(data0, wavelength0_0)/I_0_0
    data1 = []
    for j in range(len(wavelength1)):
        data1.append(emissivity[len(wavelength0)+j-1]*I_BB(wavelength1[j]))
    data1 = np.array(data1)
    epsilon_5_8 = integrate.simps(data1, wavelength1_0)/I_1_0
    data2 = []
    for k in range(len(wavelength2)):
        data2.append(emissivity[len(wavelength0) + len(wavelength1) + k-2] * I_BB(wavelength2[k]))
    data2 = np.array(data2)
    epsilon_8_14 = integrate.simps(data2, wavelength2_0) / I_2_0
    return epsilon_3_5, epsilon_5_8, epsilon_8_14


