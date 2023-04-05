import pandas as pd
import numpy as np
import math

from scipy.stats import norm


chat_id = 1182463770 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    time_92 = 92
    alpha = 1 - p
    loc = min(x)
    loc1 = loc - (math.log(alpha)/len(x))+1/2
    loc2 = loc + 1/2
    loc1 /= time_92*time_92
    loc2 /= time_92^2*time_92
    return loc1, \
           loc2
