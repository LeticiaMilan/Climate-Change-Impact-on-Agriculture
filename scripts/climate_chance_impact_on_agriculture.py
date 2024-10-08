import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo o arquivo CSV
file_path = 'https://www.kaggle.com/datasets/waqi786/climate-change-impact-on-agriculture?select=climate_change_impact_on_agriculture_2024.csv'
data = pd.read_csv(file_path)

# Visualizando as primeiras linhas do arquivo
data.head()