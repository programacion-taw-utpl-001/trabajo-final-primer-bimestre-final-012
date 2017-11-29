Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data_dir ="C:\Users\lenovo\OneDrive\universidad\programacion de algoritmo\git hub\trabajo-final-primer-bimestre-final-012\proyecto final\datos\CPV2010M_Poblacion.csv"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> data_dir="C:\Users\lenovo\OneDrive\universidad\programacion de algoritmo\git hub\trabajo-final-primer-bimestre-final-012\proyecto final\datos\CPV2010M_Poblacion.csv"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> datos=pd.red_csv('CPV2010M_Poblacion.csv',header=0)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    datos=pd.red_csv('CPV2010M_Poblacion.csv',header=0)
AttributeError: module 'pandas' has no attribute 'red_csv'
>>> datos=pd.red_csv('CPV2010M_Poblacion.csv',header=0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    datos=pd.red_csv('CPV2010M_Poblacion.csv',header=0)
AttributeError: module 'pandas' has no attribute 'red_csv'
>>> data_dir = 'C:\Users\lenovo\OneDrive\universidad\programacion de algoritmo\git hub\trabajo-final-primer-bimestre-final-012\proyecto final\datos'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> data_dir ='C:\Users\lenovo\OneDrive\universidad\programacion de algoritmo\git hub\trabajo-final-primer-bimestre-final-012\proyecto final\datos'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> data_dir='C:\Users\lenovo\OneDrive\universidad\programacion de algoritmo\git hub\trabajo-final-primer-bimestre-final-012\proyecto final\datos'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> data_dir=='C:\Users\lenovo\OneDrive\universidad\programacion de algoritmo\git hub\trabajo-final-primer-bimestre-final-012\proyecto final\datos'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
