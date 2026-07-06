import json
import os

notebooks_dir = r'Unidad 5'
notebook_files = ['U5_bloque1_clustering.ipynb', 'U5_bloque2_representacion.ipynb', 'U5_bloque3_densidad.ipynb', 'U5_bloque4_autoencoders.ipynb']

for nb_file in notebook_files:
    path = os.path.join(notebooks_dir, nb_file)
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    print(f'\n{"="*60}')
    print(f'{nb_file}')
    print(f'{"="*60}')
    print(f'Total cells: {len(nb["cells"])}')
    
    # Buscar celdas con preguntas/ejercicios
    exercise_cells = []
    for i, cell in enumerate(nb['cells']):
        content = cell.get('source', [])
        if isinstance(content, list):
            content = ''.join(content)
        
        keywords = ['Ejercicio', 'Pregunta', 'TODO', 'Complete', 'Responda', 'PREGUNTA', 'EJERCICIO']
        if any(kw.lower() in content.lower() for kw in keywords):
            exercise_cells.append((i, cell['cell_type'], content[:150]))
    
    print(f'Exercise/Question cells found: {len(exercise_cells)}')
    for idx, cell_type, content in exercise_cells:
        print(f'  Cell {idx} ({cell_type}): {content.strip()}...')
