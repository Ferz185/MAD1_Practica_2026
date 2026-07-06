import pandas as pd
import numpy as np

np.random.seed(42)

n = 120

brands = [
    'ChocoDelight','DulceCasa','LaReina','SaborLocal','Artisanal','RicoBocado',
    'Tradicion','Merienda','Fabrica','Panaderia','Gourmet','Casero','Delicia','Mini','Premium'
]
fillings = ['dulce_de_leche','crema','fruta','ganache','manjar','mousse']

rows = []
for i in range(n):
    marca = np.random.choice(brands)
    rell = np.random.choice(fillings, p=[0.3,0.25,0.15,0.15,0.1,0.05])
    # base params by relleno
    if rell == 'dulce_de_leche':
        precio = np.random.normal(120,20)
        peso = np.random.normal(48,6)
        azucar = np.random.normal(32,4)
        cal = np.random.normal(4.4,0.3)
        ventas = np.random.poisson(220)
    elif rell == 'crema':
        precio = np.random.normal(100,18)
        peso = np.random.normal(43,5)
        azucar = np.random.normal(28,4)
        cal = np.random.normal(4.1,0.35)
        ventas = np.random.poisson(180)
    elif rell == 'fruta':
        precio = np.random.normal(80,15)
        peso = np.random.normal(38,4)
        azucar = np.random.normal(25,3)
        cal = np.random.normal(3.6,0.4)
        ventas = np.random.poisson(140)
    elif rell == 'ganache':
        precio = np.random.normal(210,30)
        peso = np.random.normal(62,7)
        azucar = np.random.normal(35,4)
        cal = np.random.normal(4.85,0.2)
        ventas = np.random.poisson(130)
    elif rell == 'manjar':
        precio = np.random.normal(110,15)
        peso = np.random.normal(46,5)
        azucar = np.random.normal(30,3)
        cal = np.random.normal(4.2,0.25)
        ventas = np.random.poisson(200)
    else: # mousse
        precio = np.random.normal(95,17)
        peso = np.random.normal(41,5)
        azucar = np.random.normal(27,3)
        cal = np.random.normal(4.0,0.3)
        ventas = np.random.poisson(160)

    # noise and bounds
    precio = max(30, round(precio,2))
    peso = max(20, round(peso,1))
    azucar = max(5, round(azucar,1))
    cal = min(5.0, max(1.0, round(cal,2)))
    ventas = max(5, int(ventas))

    rows.append([marca, precio, peso, azucar, rell, cal, ventas])

cols = ['marca','precio','peso_g','azucar_pct','relleno','calificacion','ventas_units']
df = pd.DataFrame(rows, columns=cols)
# save
df.to_csv('Unidad 5/alfajores_dataset.csv', index=False)
print('Generado Unidad 5/alfajores_dataset.csv con', len(df), 'filas')
