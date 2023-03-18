import numpy as np
import S4
from materials_lib import SiO2, Ge, TiO2
import Emissivity_average

materials = ["SiO2", "Ge", "TiO2"]
Lambda = 1


def fitness_func(solution, solution_idx):
    S = S4.New(Lattice=((Lambda, 0), (0, Lambda)), NumBasis=10)

    S.SetMaterial(Name='SiO2', Epsilon=(1 + 0.0j) ** 2)
    S.SetMaterial(Name='Vacuum', Epsilon=(1 + 0.0j) ** 2)
    S.SetMaterial(Name='TiO2', Epsilon=(1 + 0.0j) ** 2)
    S.SetMaterial(Name='Ge', Epsilon=(1 + 0.0j) ** 2)

    S.AddLayer(Name='AirAbove', Thickness=0, Material='Vacuum')
    for ii in range(12):
        S.AddLayer(Name='Film{}'.format(ii), Thickness=solution[ii + 12] / 1000, Material=materials[solution[ii]])
    S.AddLayer(Name='Film13', Thickness=400, Material='SiO2')
    S.AddLayer(Name='Airbelow', Thickness=0, Material='Vacuum')

    S.SetExcitationPlanewave(IncidenceAngles=(0, 0), sAmplitude=0, pAmplitude=1, Order=0)
    S.SetOptions(PolarizationDecomposition=True)

    wavelength_space = np.arange(3, 14.01, 0.1)
    A = []
    for lam in wavelength_space:
        # print(i)
        epsilon1 = SiO2(lam)
        n1, k1 = epsilon1[0], epsilon1[1]
        epsilon2 = TiO2(lam)
        n2, k2 = epsilon2[0], epsilon2[1]
        epsilon3 = Ge(lam)
        n3, k3 = epsilon3[0], epsilon3[1]
        S.SetMaterial(Name='SiO2', Epsilon=(n1 + 1.0j * k1) ** 2)
        S.SetMaterial(Name='TiO2', Epsilon=(n2 + 1.0j * k2) ** 2)
        S.SetMaterial(Name='Ge', Epsilon=(n3 + 1.0j * k3) ** 2)
        f = 1 / float(lam)
        S.SetFrequency(float('{:.6f}'.format(f)))
        (forward, backward) = S.GetPowerFlux(Layer='AirAbove')
        A.append(1 + backward.real / forward.real)
    epsilon_average = Emissivity_average.emissivity_aver(A)
    # print(epsilon_average)
    fitness = 1.0 / (0.333*epsilon_average[0]+0.333*(1-epsilon_average[1])+0.333*epsilon_average[2])
    # print(fitness)
    return fitness
