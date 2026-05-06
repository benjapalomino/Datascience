# Análisis del Modelo de Vinos

**a. ¿Qué accuracy obtuvo el modelo?**
Revisando la consola al correr el main, el modelo me tiró un accuracy de 0.9444. Básicamente, le achuntó al 94.4% de los datos de prueba, lo que está súper bueno.

**b. ¿Qué variable aparece en la raíz del árbol?**
En el gráfico que se generó, la primera variable que aparece arriba de todo (en el nodo raíz) es color_intensity. El modelo la puso ahí porque es la que le sirvió más para empezar a separar los tipos de vinos desde el principio.

**c. El modelo, ¿parece confiable?, justifique.**
Sí, yo diría que es bien confiable. Aparte de tener casi un 95% de accuracy, si miramos el reporte de clasificación, los f1-scores de las tres clases están parejitos y súper altos (0.96, 0.93 y 0.93). Esto significa que no está adivinando, sino que aprendió a clasificar bien datos que ni siquiera conocía.

**d. ¿Se observa overfitting o underfitting?**
Para nada. Como le pusimos el límite de profundidad al árbol (max_depth=3), evitamos que se pusiera a memorizar los datos de entrenamiento (así que no hay overfitting). Y como le fue tan bien en las pruebas, tampoco hay underfitting, el modelo entendió bien el problema.

**e. ¿Qué otras variables parecen más relevantes?**
Si uno sigue mirando para abajo en el gráfico del árbol, después de la intensidad del color, el modelo usa harto las variables proline, flavanoids y ash para tomar las decisiones finales.