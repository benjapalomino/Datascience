from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def entrenar_arbol(X, y):
    # a. Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # b. Crear un modelo de árbol de decisión (limitamos max_depth para evitar overfitting)
    modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
    
    # c. Entrenar el modelo con los datos de entrenamiento
    modelo.fit(X_train, y_train)
    
    return modelo, X_test, y_test       