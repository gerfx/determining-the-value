import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file1 = open("input", "r")


Y = list(map(float, file1.readline()[:-2].split(',')))
lines = file1.readlines()
i = 0
correlations = []
cor_lag1 = []
cor_lag2 = []
cor_lag3= []
mas = []
for line in lines:
    s = list(map(float, line[:-2].split(',')))
    mas.append(s)
    correlations.append(abs(pd.Series(Y).corr(pd.Series(s))))
    cor_lag1.append(abs(pd.Series(Y[:-1]).corr(pd.Series(s[1:]))))
    cor_lag2.append(abs(pd.Series(Y[:-2]).corr(pd.Series(s[2:]))))
    cor_lag3.append(abs(pd.Series(Y[:-3]).corr(pd.Series(s[3:]))))
    k_prog = []
for i in range(len(mas[0])-3):
    k_prog.append((mas[0][i+3]/mas[0][i]-1)*100*cor_lag3[0] + (mas[1][i+3]/mas[1][i+2]-1)*100*cor_lag1[1] + (mas[2][i+3]/mas[2][i+2]-1)*100*cor_lag1[2]+(mas[3][i+3]/mas[3][i+1]-1)*100*cor_lag2[3])
x = np.arange(0,19,1)
y=np.array(k_prog)
plt.plot(x,y)
plt.plot(x, np.array((([(Y[i+1]/Y[i]-1)*100 for i in range(len(Y)-3)]))))
print("Прогнозируемое значение на следующий день - " + str((1+k_prog[-1]/100)*Y[-1]))
plt.show()

