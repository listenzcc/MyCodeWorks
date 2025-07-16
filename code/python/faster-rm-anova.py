"""
File: faster-rm-anova.py
Author: Chuncheng Zhang
Date: 2025-07-16
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Compute rm-anova (repeated measures ANOVA) faster.
    The script only applies to the matrix, the dimensions are
    (n_subjects, n_conditions, ...),
    which means the subjects of conditions are the same.
    The following dimensions are independently computed.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2025-07-16 ------------------------
# Requirements and constants
import numpy as np
import pandas as pd
import pingouin as pg

from rich import print
from scipy import stats
from tqdm.auto import tqdm


# %% ---- 2025-07-16 ------------------------
# Function and class
class Option:
    n_subject = 10
    n_cond = 4
    data = np.random.rand(n_subject, n_cond)


def rm_anova_with_pingouin(data):
    '''
    Compute the repeated measures ANOVA using pingouin as ground truth.
    '''
    n_subject, n_cond = data.shape
    # Build df and convert into long format.
    df = pd.DataFrame(data, columns=[f'cond{e}' for e in range(n_cond)])
    df['subject'] = range(1, 1+n_subject)
    df_long = df.melt(id_vars='subject',
                      var_name='condition', value_name='value')
    # Compute ANOVA
    aov = pg.rm_anova(data=df_long, dv='value', within='condition',
                      subject='subject', detailed=False, correction=False)
    return aov


def fast_rm_anova(data):
    """
    Fast repeated measures ANOVA to data matrix.
    The following dimensions are independently computed.

    The script only applies to the matrix, the dimensions are
    (n_subjects, n_conditions, ...),
    which means the subjects of conditions are the same.

    :param data np.array: (At least) 2D numpy matrix (n_subjects x n_conditions x ...)

    :return F float or np.array: The F value.
    :return p float or np.array: The uncorrelated p value.
    """
    n, k = data.shape[:2]  # n=受试者数, k=条件数

    # 计算各项均值
    grand_mean = np.mean(np.mean(data, axis=0), axis=0)
    subj_means = np.mean(data, axis=1)
    cond_means = np.mean(data, axis=0)

    # 计算平方和 (SS)
    SS_total = np.sum(np.sum((data - grand_mean)**2, axis=0), axis=0)
    SS_subj = np.sum((subj_means - grand_mean)**2, axis=0) * k
    SS_cond = np.sum((cond_means - grand_mean)**2, axis=0) * n
    SS_error = SS_total - SS_subj - SS_cond

    # 计算自由度
    df_cond = k - 1
    df_error = (n - 1) * (k - 1)

    # 计算均方和F值
    MS_cond = SS_cond / df_cond
    MS_error = SS_error / df_error
    F = MS_cond / MS_error

    # 计算自由度
    df_cond = k - 1
    df_error = (n - 1) * (k - 1)

    # 计算均方和F值
    MS_cond = SS_cond / df_cond
    MS_error = SS_error / df_error
    F = MS_cond / MS_error

    # 未校正p值
    p_uncorrected = stats.f.sf(F, df_cond, df_error)

    return F, p_uncorrected


# %% ---- 2025-07-16 ------------------------
# Play ground
if __name__ == '__main__':
    print('\n-- gp method (ground truth, slow) --')
    for _ in tqdm(range(100)):
        anova_pg = rm_anova_with_pingouin(Option.data)
    print(anova_pg)

    print('\n-- fast method (with single matrix, fast) --')
    for _ in tqdm(range(100)):
        F, p = fast_rm_anova(Option.data)
    print(F, p)

    print('\n-- fast method (with stacked matrix, fast with multiple dimensions) --')
    data2 = np.stack([Option.data.copy() for _ in range(20)], axis=2)
    print(data2.shape)
    for _ in tqdm(range(100)):
        F, p = fast_rm_anova(data2)
    print(F, p)

# %% ---- 2025-07-16 ------------------------
# Pending


# %% ---- 2025-07-16 ------------------------
# Pending
