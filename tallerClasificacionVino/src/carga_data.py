import pandas as pd
from sklearn.datasets import load_wine

def preparar_datos():
    # a. Cargar el dataset load_wine
    wine = load_wine()
    
    # b. Transformarlo a dataframe
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['target'] = wine.target
    
    # c. Realizar un análisis exploratorio
    print("--- Análisis Exploratorio ---")
    print("i. Primeros registros:\n", df.head())
    print("\nii. Nombres de variables:", wine.feature_names)
    print("\niii. Clases:", wine.target_names)
    print("\niv. Cantidad de datos:", df.shape)
    print("\nv. Estadísticas:\n", df.describe())
    
    # d. Separar variables independientes (X) y variable objetivo (y)
    X = df.drop('target', axis=1)
    y = df['target']
    
    return X, y, wine.feature_names, wine.target_names