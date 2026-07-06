# Unidad 4: Aprendizaje Automático Supervisado

## 📚 Descripción

En esta unidad aprenderás a construir, entrenar y evaluar modelos de aprendizaje automático supervisado. Estos modelos aprenden patrones de datos etiquetados para realizar predicciones y clasificaciones.

## 🎯 Objetivos

- Implementar y entrenar distintos algoritmos de clasificación
- Entender la diferencia entre modelos lineales y no lineales
- Evaluar modelos usando métricas apropiadas
- Realizar ajuste de hiperparámetros
- Interpretar resultados y seleccionar el mejor modelo

## 📖 Contenido de la Unidad

### **Bloque 1: Árboles de Decisión**
- `U4_nb01_arboles.ipynb`
- Concepto de particionamiento recursivo
- Criterios de split (Gini, Entropía)
- Interpretabilidad del modelo
- Control de complejidad (profundidad, número de hojas)

### **Bloque 2: Random Forest**
- `U4_nb02_random_forest.ipynb`
- Ensambles de árboles
- Bootstrap Aggregating (Bagging)
- Importancia de variables
- Ventajas sobre árboles simples

### **Bloque 3: SVM y KNN**
- `U4_nb03_svm_knn.ipynb`
- Máquinas de Vectores de Soporte (SVM)
  - Clasificación lineal y no lineal
  - Kernels y truco del kernel
  - Margen máximo
- K-Nearest Neighbors (KNN)
  - Métrica de distancia
  - Selección de K

### **Bloque 4: Redes Neuronales**
- `U4_nb04_redes.ipynb`
- Perceptrón y multicapa
- Funciones de activación
- Backpropagation
- Regularización y dropout
- Aplicaciones en clasificación

### **Bloque 5: Métricas de Evaluación**
- `U4_nb05_metricas.ipynb`
- Matriz de confusión
- Accuracy, Precisión, Recall, F1-Score
- Curva ROC y AUC
- Validación cruzada
- Selección del modelo óptimo

## 🛠️ Herramientas y Librerías

```python
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (confusion_matrix, classification_report, 
                            roc_curve, auc, cross_val_score)
from sklearn.model_selection import train_test_split, GridSearchCV
```

## 📋 Flujo de Trabajo Recomendado

1. **Preparación**: Cargar y preparar datos (ver Unidad 1)
2. **EDA**: Análisis exploratorio (ver Unidad 2)
3. **Train-Test Split**: Dividir datos en entrenamiento y prueba
4. **Entrenamiento**: Ajustar el modelo a los datos de entrenamiento
5. **Evaluación**: Evaluar en datos de prueba
6. **Ajuste**: Modificar hiperparámetros si es necesario
7. **Validación Cruzada**: Validar robustez del modelo
8. **Interpretación**: Analizar resultados y explicar decisiones

## 📊 Ejemplo Básico de Flujo

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entrenar
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# Predecir
y_pred = model.predict(X_test)

# Evaluar
accuracy = accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))
```

## ✅ Actividades Requeridas

Para completar esta unidad debes:

1. **Ejecutar todos los notebooks** siguiendo el orden propuesto
2. **Entender conceptos clave** de cada algoritmo
3. **Modificar hiperparámetros** y observar el impacto
4. **Comparar modelos** usando métricas apropiadas
5. **Documentar hallazgos** en comentarios dentro del código
6. **Resolver ejercicios propuestos** en cada notebook

## 🔍 Comparación de Algoritmos

| Algoritmo | Interpretabilidad | Velocidad | Complejidad | Mejor para |
|-----------|------------------|-----------|-------------|-----------|
| Árbol Simple | Alta | Muy rápido | Baja | Datos con relaciones simples |
| Random Forest | Media | Rápido | Media | Datasets balanceados |
| SVM | Baja | Lento | Alta | Datos complejos, lineal/no lineal |
| KNN | Media | Lento | Baja | Datos localmente similares |
| Redes Neuronales | Muy baja | Variable | Muy alta | Datos complejos, grandes |

## 📚 Recursos Adicionales

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Machine Learning Course](https://www.coursera.org/learn/machine-learning)
- Lecturas en PDFs teoría de Unidad 4

## 🤔 Preguntas Clave

Al finalizar esta unidad deberías poder responder:
- ¿Cuándo usar cada algoritmo?
- ¿Cómo interpretar métricas de clasificación?
- ¿Qué es overfitting y cómo detectarlo?
- ¿Cómo realizar validación cruzada correctamente?
- ¿Cuál es el mejor modelo para mi problema?

---

**Última actualización**: 2026-07-06
