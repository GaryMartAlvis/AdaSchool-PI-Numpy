import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

class Column:
    """
    Clase para representar una columna de un conjunto de datos.
    
    Parameters:
    - data (Dataset): Conjunto de datos.
    - feature (str): El nombre de la columna del Dataset.
    
    Métodos:
    - convert_np: Convierte la columna a un array de numpy.
    """
    def __init__(self, data, feature):
        self.data = data
        self.feature = feature

    def convert_np(self):
        return np.array(self.data[self.feature])

# Diccionario para almacenar todas las columnas con sus respectivos nombres de variables
# Lista de nombre de variables en anexos al final de codigo
columns = {}
for feature in data.features:
    columns[feature] = Column(data, feature).convert_np()

# Promedio de edades
mean_age = np.mean(columns['age'])
zise_age = np.size(columns['age'])

print(f"El promedio de edad del los {zise_age} participantes en el estudio es de : {round(mean_age,2)} años.")






"""
ANEXOS
Lista de variable para cada nombre de la característica y su array de numpy:
	age
	has_anaemia
	creatinine_phosphokinase_concentration_in_blood
	has_diabetes
	heart_ejection_fraction
	has_high_blood_pressure
	platelets_concentration_in_blood
	serum_creatinine_concentration_in_blood
	serum_sodium_concentration_in_blood
	is_male
	is_smoker
	days_in_study
	is_dead
"""