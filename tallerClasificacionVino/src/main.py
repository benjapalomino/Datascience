from carga_data import preparar_datos
from modelo import entrenar_arbol
from evaluacion import evaluar_arbol
from visualizacion import graficar_arbol

def main():
    # 1. Preparar datos
    X, y, features, classes = preparar_datos()
    
    # 2. Entrenar modelo
    modelo, X_test, y_test = entrenar_arbol(X, y)
    
    # 3. Evaluar modelo
    evaluar_arbol(modelo, X_test, y_test)
    
    # 4. Visualizar y analizar
    # c. Interpretar variable raíz y d. Decisiones principales se analizan en base al gráfico generado aquí
    graficar_arbol(modelo, features, classes)

if __name__ == "__main__":
    main()