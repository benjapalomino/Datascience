import matplotlib.pyplot as plt
from sklearn import tree

def graficar_arbol(modelo, feature_names, class_names):
    # a. Graficar el árbol de decisión
    # b. Estilizar el gráfico creado
    plt.figure(figsize=(14, 8))
    tree.plot_tree(
        modelo,
        feature_names=feature_names,
        class_names=class_names,
        filled=True,
        rounded=True, # bordes redondeados
        fontsize=10,  # tamaño texto
        proportion=True # tamaños proporcionales
    )
    plt.title("Árbol de decisión - Clasificación de Vinos")
    plt.show()