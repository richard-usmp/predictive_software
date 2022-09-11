#MINIMIZAR EL ERROR CUADRATICO MEDIO
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

#cargamos la libreria
boston = load_boston()

#numero medio de habitaciones
X = np.array(boston.data[:, 5])
#valor medio de habitaciones
Y = np.array(boston.target)

plt.scatter(X, Y, alpha=0.5)

#añadimos columna de 1s para termino independiente
X = np.array([np.ones(506), X]).T

B = np.linalg.inv(X.T @ X) @ X.T @ Y

plt.plot([4, 9], [B[0]+B[1]*4, B[0]+B[1]*9], c="red")
plt.show()