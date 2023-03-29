# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
from functions import puasson
from functions import bernulli

n = 144
m = 70
p = 0.5

print (f'Вероятность того, что орел выпадет 70 раз из 144 подпросов = {round(bernulli(p, m, n)*100,2)}%')
print(puasson(p,m,n))


