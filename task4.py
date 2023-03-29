# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
#
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?
from progress.colors import white

from functions import combinations

total1 = 10
white1 = 7
black1 = total1 - white1
total2 = 11
white2 = 9
black2 = total2 - white2
take = 2

# Какова вероятность того, что все мячи белые?
res_white_combination = combinations(take, white1) * combinations(take, white2)
total_white_combination = combinations(take, total1) * combinations(take, total2)
res = res_white_combination / total_white_combination
print(res)

# Какова вероятность того, что ровно два мяча белые?

p1 = (7/10 * 6/9) * (2/11 * 1/10) + (7/10 * 3/9) * (9/11 * 2/10) + (3/10 * 2/9) * (9/11 * 8/10)
print(p1)

# Какова вероятность того, что хотя бы один мяч белый?
p2 =  1 - (3/10 * 2/9 * 2/11 * 1/10)
print(p2)