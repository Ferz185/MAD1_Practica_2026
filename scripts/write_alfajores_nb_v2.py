import nbformat as nbf
nb = nbf.v4.new_notebook()

cells = []

cells.append(nbf.v4.new_markdown_cell('# Análisis completo de Alfajores (Unidad 5)\n\nNotebook replicando el análisis realizado para chocolates, pero usando el dataset ficticio de alfajores.'))

cells.append(nbf.v4.new_code_cell("""# Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
sns.set(style="whitegrid")

# Cargar dataset
df = pd.read_csv('alfajores_dataset.csv')
df.head()
"""))

cells.append(nbf.v4.new_code_cell("""# Información y estadísticos
print('Shape:', df.shape)
print('\n--- Info ---')
ch = df.info()
print('\n--- Describe ---')
desc = df.describe(include='all')
desc
"""))

cells.append(nbf.v4.new_code_cell("""# Limpieza rápida y preparación
df = df.copy()
# Asegurar tipos
df['marca'] = df['marca'].astype('category')
df['relleno'] = df['relleno'].astype('category')
# codificar relleno para análisis numérico
df['relleno_code'] = df['relleno'].cat.codes
df.head()
"""))

cells.append(nbf.v4.new_code_cell("""# Visualizaciones exploratorias
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='precio', y='ventas_units', hue='relleno', s=100)
plt.title('Precio vs Ventas por tipo de relleno')
plt.show()

plt.figure(figsize=(8,4))
sns.histplot(df['calificacion'], bins=6, kde=False)
plt.title('Distribución de calificaciones')
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(data=df, x='relleno', y='ventas_units')
plt.title('Ventas por tipo de relleno')
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')
plt.title('Correlación entre variables numéricas')
plt.show()
"""))

cells.append(nbf.v4.new_markdown_cell('## Clustering (KMeans)\nSe usa escalado y se prueba el codo para seleccionar k'))

cells.append(nbf.v4.new_code_cell("""# Selección de features numéricas para clustering
features = ['precio','peso_g','azucar_pct','calificacion','ventas_units']
X = df[features].values
scaler = StandardScaler()
Xs = scaler.fit_transform(X)

# Codo (inertia)
ks = range(1,7)
inertias = []
for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(Xs)
    inertias.append(km.inertia_)

plt.figure(figsize=(6,4))
plt.plot(list(ks), inertias, '-o')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('Método del codo')
plt.xticks(ks)
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""# Elegir k (ej: 3) y entrenar KMeans
k = 3
km = KMeans(n_clusters=k, random_state=42, n_init=10)
df['cluster'] = km.fit_predict(Xs)
print('Silhouette score:', silhouette_score(Xs, df['cluster']))
print('\nCluster counts:')
print(df['cluster'].value_counts())
"""))

cells.append(nbf.v4.new_code_cell("""# Mostrar centroide en escala original (inversa)
centers = scaler.inverse_transform(km.cluster_centers_)
centers_df = pd.DataFrame(centers, columns=features)
centers_df
"""))

cells.append(nbf.v4.new_code_cell("""# Comparar clusters vs relleno
ct = pd.crosstab(df['cluster'], df['relleno'])
ct
"""))

cells.append(nbf.v4.new_code_cell("""# Visualizar clusters en 2D con PCA
pca = PCA(n_components=2, random_state=42)
Xp = pca.fit_transform(Xs)
df['pca1'] = Xp[:,0]
df['pca2'] = Xp[:,1]
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='pca1', y='pca2', hue='cluster', palette='tab10', s=100)
plt.title('Clusters (PCA 2D)')
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""# Exportar resultados agregados y asignaciones
df.to_csv('alfajores_analisis_resultados.csv', index=False)
print('Exportado alfajores_analisis_resultados.csv')
"""))

cells.append(nbf.v4.new_markdown_cell('## Conclusiones breves\nSe observaron agrupamientos que correlacionan parcialmente con el tipo de relleno. El análisis repetible está guardado en alfajores_analisis_resultados.csv.'))

nb['cells'] = cells
nb['metadata'] = {"kernelspec": {"display_name": "Python 3","language": "python","name": "python3"}, "language_info": {"name": "python","version": "3.8"}}

nbf.write(nb, 'Unidad 5/U5_alfajores_analisis.ipynb')
print('Notebook creado: Unidad 5/U5_alfajores_analisis.ipynb')
