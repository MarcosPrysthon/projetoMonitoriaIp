from graphics import Graphics
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import PIL

data = ''
graphics = Graphics()

for i in range (15):
    with open('test' + str(i+1) + '.txt', 'r', errors='ignore') as f:
        data += f.read()

data = data.split()

graphics.set_final_nums(data)
graphics.set_engines(data)
graphics.set_doors(data)
graphics.set_years(data)

final_nums = graphics.get_final_nums()
engines = graphics.get_engines()
doors = graphics.get_doors()
years = graphics.get_years()

print(years, engines, doors, years, sep='\n')

df1 = pd.DataFrame({ 'Motor': engines })
df2 = pd.DataFrame({ 'Final de placa': final_nums })
df3 = pd.DataFrame({ 'Ano': years })
df4 = pd.DataFrame({ 'Nº de portas': doors })

df1.plot(kind='bar')
df2.plot(kind='area')
df3.plot(kind='hist')
df4.plot(kind='line')
plt.show()