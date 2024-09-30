import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats 

# 母平均の区間推定の関数
def popmean_confidence_interval(mean, U, n, confidence=0.95):
    """
    母平均の区間推定を行う関数（母分散未知の場合）
    - mean: 標本平均 (x̄)
    - U: 不偏分散から求めた標本標準偏差 (U)
    - n: 標本サイズ (n)
    - confidence: 信頼区間 (デフォルト: 95%)

    Returns:
    - 区間の下限値と上限値
    """
    
    # t分布のt値を求める (自由度 n-1 の t分布)
    t_value = stats.t(df=n-1).ppf((1 + confidence) / 2)
    
    # 標準誤差の計算
    standard_error = U / np.sqrt(n)
    
    # 信頼区間の計算
    error = t_value * standard_error
    lower_bound = mean - error
    upper_bound = mean + error
    
    return lower_bound, upper_bound
