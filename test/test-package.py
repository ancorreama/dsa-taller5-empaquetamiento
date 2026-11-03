from pathlib import Path

import pandas as pd
from model.predict import make_prediction

# Se lee el CSV de la misma carpeta del script (la ruta original "~/test/" apuntaba a /home/ubuntu/test,
# que no existe porque la carpeta test quedó dentro del repositorio)
sample_input_data = pd.read_csv(Path(__file__).resolve().parent / "bankchurn_test.csv")
result = make_prediction(input_data=sample_input_data)
print(result)
