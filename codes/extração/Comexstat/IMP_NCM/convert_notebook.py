import nbconvert
import nbformat

# Load the notebook
with open('Baixa_Extrai.ipynb') as f:
    notebook = nbformat.read(f, as_version=4)

# Convert to Python script
exporter = nbconvert.PythonExporter()
script, _ = exporter.from_notebook_node(notebook)

# Save the script
with open('Baixa_Extrai.py', 'w') as f:
    f.write(script)