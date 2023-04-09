import pandas as data, numpy as np
import load, stats
from scipy.stats import ttest_1samp

def t_test(bet):
    logs = stats.Variables()
    prop = load.CSV.prop
    gamelog = logs.gamelog

    type = prop['type']
    arr = np.array(gamelog[type])
    num = float(prop['num'])

    if bet == 'over':
        alt = 'greater'
    elif bet == 'under':
        alt = 'less'

    test = ttest_1samp(arr, popmean=num)
    conf = test.confidence_interval(confidence_level=0.95)
    t_stat = test.statistic
    p_value = test.pvalue
    print(arr)
    print(t_stat)
    print(p_value)
    print(conf)








t_test('over')