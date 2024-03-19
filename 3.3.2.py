import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler
url='https://raw.githubusercontent.com/akmand/datasets/master/iris.csv'
dataframe=pd.read_csv(url)
sepal_length_cm=dataframe['sepal_length_cm']
sepal_length_cm=[[sepal_length_cm[i]] for i in range(len(sepal_length_cm))]
minmax_scale=MinMaxScaler(feature_range=(0,1))
scaled=minmax_scale.fit_transform(sepal_length_cm)
print(f'Нормализация первого числового признака (sepal_length_cm) с использованием минимаксного преобразования: \n{scaled}')
sepal_width_cm=dataframe['sepal_width_cm']
sepal_width_cm=np.array([sepal_length_cm[i] for i in range(len(sepal_length_cm))])
scaler=StandardScaler()
scalered=scaler.fit_transform(sepal_width_cm)
print(f'Нормализация второго числового признака (sepal_width_cm) с задействованием z-масштабирования: \n{scalered}')