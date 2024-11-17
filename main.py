from src.load_dataset import load_data
from src.regression import apply_regression

# Carregar dados
X, y, metadata, variables = load_data()

# Aplicar regressão e visualizar resultados
apply_regression(X, y)
