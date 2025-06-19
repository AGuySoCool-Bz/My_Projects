# CURVE FITTING , FITTING STRAIGHT LINE BY LEAST SQUARE METHOD

# $ ---> Summation
# $y = a$x + nb
# $xy = a$x^2 + b$x

import numpy as np

def square(a):
    return a * a 

amp = [7.3, 7.2, 6.4, 6.1, 6.3, 6.2, 5.1, 5.0, 5.4, 4.9, 4.0, 3.5, 4.4, 3.7, 2.8, 2.8, 3.5, 2.9, 2.1, 1.8, 1.9, 1.6, 1.8, 1.5, 1.7, 1.4, 1.4, 1.3]
time = [2.08,3.15,4.22, 6.04, 7.10, 8.16,9.22,11.00, 12.01, 13.13, 14.13, 15.22, 17.06,18.11, 19.15, 20.20, 22.04, 23.09, 24.12, 25.19, 27.03, 28.08, 29.14, 30.18, 31.24, 33.05, 34.11, 35.17]
log_a = [1.99, 1.97, 1.86, 1.81, 1.84, 1.82, 1.63, 1.61, 1.69, 1.59, 1.39, 1.25, 1.48, 1.31, 1.03, 1.03, 1.25, 1.06, 0.74, 0.59, 0.64, 0.47, 0.59, 0.41, 0.53, 0.34, 0.34, 0.26]
# y = log_a
Vw = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
Vo = [
0 
,
1.8 
,
2.8 
,
3.2 
,
4.8 
,
5.5 
,
6.4 
,
8.3, 

9.2 
,
9.6 
,
10.6 
,
11.6 
,
12.7 
,
13.5 
,
14.1

]
y = Vo
# x = time
x = Vw
sqx = list(map(square,x))
xy = []
for i in range(0,len(x)):
    s = x[i] * y[i]
    xy.append(s)

summ_x = sum(x)
summ_y = sum(y)
summ_sqx = sum(sqx)
summ_xy = sum(xy)

a = np.array([[summ_x,len(x)], [summ_sqx, summ_x]])
b = np.array([summ_y,summ_xy])

soln = np.linalg.solve(a,b)

lol = round(soln[0], 4)
lols = round(soln[1], 4)
 
print(soln)
print(f"y = {lol}x + {lols}")

