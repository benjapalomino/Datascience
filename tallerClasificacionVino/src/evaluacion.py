from sklearn.metrics import accuracy_score, classification_report

def evaluar_arbol(modelo, X_test, y_test):
    # a. Realizar predicciones sobre el conjunto de prueba
    y_pred = modelo.predict(X_test)
    
    # b. Calcular el accuracy del modelo
    acc = accuracy_score(y_test, y_pred)
    
    # c. Analizar el desempeño obtenido
    print("\n--- Evaluación ---")
    print(f"Accuracy: {acc}")
    print("Reporte de clasificación:\n", classification_report(y_test, y_pred))