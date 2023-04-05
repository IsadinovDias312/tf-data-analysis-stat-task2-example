import pandas as pd
import numpy as np
import math

import scipy.stats


chat_id = 1182463770 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    time_92 = 92
    alpha = 1 - p
    semians = 0
    for i in range(len(x)):
      semians += x[i]
    semians /= len(x)
    left = semians - 1/2 - scipy.stats.gamma.ppf((1+alpha)/2, len(x))/len(x)
    right = semians - 1/2 - scipy.stats.gamma.ppf((1-alpha)/2, len(x))/len(x)
    left /= (time_92*time_92)
    right /= (time_92*time_92)
    left *= 2
    right *= 2

    return left, \
           right
