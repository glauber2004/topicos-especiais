import numpy as np

def load_data():
    # Dados fictícios (expandido para mais moluscos)
    X = np.array([
        [0.5, 0.35, 0.1, 0.2, 0.3, 0.15, 0.07],  # Molusco 1
        [0.6, 0.4, 0.2, 0.25, 0.4, 0.2, 0.08],   # Molusco 2
        [0.7, 0.5, 0.15, 0.3, 0.35, 0.18, 0.09], # Molusco 3
        [0.8, 0.6, 0.25, 0.4, 0.5, 0.3, 0.1],    # Molusco 4
        [0.9, 0.7, 0.2, 0.5, 0.6, 0.4, 0.12],    # Molusco 5
        [1.0, 0.75, 0.3, 0.6, 0.65, 0.45, 0.15], # Molusco 6
        [0.85, 0.65, 0.35, 0.55, 0.55, 0.4, 0.13],# Molusco 7
        [0.95, 0.8, 0.28, 0.65, 0.7, 0.5, 0.14],  # Molusco 8
        [1.1, 0.85, 0.4, 0.75, 0.8, 0.6, 0.2],    # Molusco 9
        [1.2, 0.9, 0.45, 0.85, 0.9, 0.7, 0.25]    # Molusco 10
    ])
    
    # Idades dos moluscos (alvo)
    y = np.array([3, 6, 8, 10, 12, 15, 14, 16, 18, 20])  # Idades fictícias

    # Metadados
    metadata = "Dados fictícios para testes ampliados"
    variables = [
        "Length", "Diameter", "Height",
        "Whole Weight", "Shucked Weight",
        "Viscera Weight", "Shell Weight"
    ]
    
    return X, y, metadata, variables
