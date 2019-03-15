# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from skfeature.function.statistical_based import CFS
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import scale, MinMaxScaler

from imblearn.over_sampling import SMOTE, ADASYN
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

from sklearn.metrics import auc, roc_curve, roc_auc_score, recall_score, f1_score, precision_score

from sklearn.feature_selection import SelectKBest, chi2, f_classif, f_regression


fpr1=[0.,0.00748727,0.00808625,0.00808625,0.00868524,0.00898473
,0.00898473,0.00928422,0.00928422,0.0098832,0.0098832,0.01018269
,0.01018269,0.01078167,0.01078167,0.01168014,0.01168014,0.01227913
,0.01227913,0.01437556,0.01437556,0.01617251,0.01737047,0.01737047
,0.01916742,0.01916742,0.01946691,0.01946691,0.02276131,0.02276131
,0.0230608,0.0230608,0.02425876,0.02425876,0.02545672,0.02605571
,0.02665469,0.02665469,0.02755316,0.02755316,0.0296496,0.0296496
,0.03234501,0.03234501,0.03504043,0.03563941,0.03623839,0.03683738
,0.03683738,0.03713687,0.03713687,0.03743636,0.03743636,0.03773585
,0.03773585,0.03803534,0.03863432,0.03953279,0.03953279,0.03983229
,0.03983229,0.04552261,0.0458221,0.04761905,0.04851752,0.04851752
,0.0491165,0.0491165,0.04941599,0.05091345,0.05151243,0.05151243
,0.0524109,0.0524109,0.05300988,0.05360886,0.05690326,0.05690326
,0.05750225,0.05750225,0.05780174,0.06049715,0.0622941,0.06349206
,0.06349206,0.06439054,0.06439054,0.06528901,0.06708595,0.06708595
,0.06738544,0.06858341,0.06918239,0.0721773,0.07247679,0.07247679
,0.07337526,0.07337526,0.07487272,0.07517221,0.07577119,0.07607068
,0.07607068,0.07786763,0.0787661,0.07936508,0.07936508,0.07996406
,0.09224319,0.09404013,0.09793351,0.098233,0.098233,0.09883199
,0.10182689,0.10212639,0.10362384,0.10422282,0.11320755,0.11350704
,0.11440551,0.11620246,0.11680144,0.11710093,0.11919736,0.12309075
,0.12339024,0.1245882,0.12728362,0.12818209,0.12848158,0.13057802
,0.13147649,0.13387242,0.1344714,0.13566936,0.13956274,0.14315663
,0.1443546,0.1572327,0.1575322,0.15873016,0.15932914,0.16172507
,0.16771488,0.16951183,0.17400419,0.1868823,0.18718179,0.18987721
,0.19886193,0.20515124,0.2066487,0.20724768,0.20844564,0.23180593
,0.23869422,0.2392932,0.24049117,0.24528302,0.24707996,0.24857742
,0.25037436,0.25067385,0.25067385,0.25127284,0.25217131,0.26924229
,0.2722372,0.27253669,0.27403414,0.27523211,0.27643007,0.27672956
,0.28391734,0.28571429,0.28601378,0.33033842,0.35609464,0.36507937
,0.36597784,0.36597784,0.36687631,0.36807427,0.36837376,0.36837376
,0.36867326,0.36927224,0.36957173,0.36957173,0.37226715,0.37466307
,0.37526205,0.37646002,0.37765798,0.37945493,0.39802336,0.40101827
,0.40131776,0.4064091,0.4067086,0.40730758,0.40760707,0.41419587
,0.41479485,0.41808925,0.41838874,0.4195867,0.42198263,0.42407907
,0.42437856,0.42527703,0.42557652,0.43006888,0.44654088,0.45163223
,0.67804732,0.67834681,0.68104223,0.74483378,0.74782869,0.75561545
,0.76939203,0.7738844,0.7801737,0.78706199,0.90895478,1.]


tpr1=[0.,0.29292929,0.29292929,0.3030303,0.3030303,0.3030303
,0.31313131,0.31313131,0.34343434,0.34343434,0.36363636,0.36363636
,0.37373737,0.37373737,0.4040404,0.4040404,0.41414141,0.41414141
,0.43434343,0.43434343,0.45454545,0.45454545,0.45454545,0.47474747
,0.47474747,0.49494949,0.49494949,0.50505051,0.50505051,0.51515152
,0.51515152,0.53535354,0.53535354,0.55555556,0.55555556,0.55555556
,0.55555556,0.56565657,0.56565657,0.57575758,0.57575758,0.58585859
,0.58585859,0.60606061,0.60606061,0.60606061,0.60606061,0.60606061
,0.63636364,0.63636364,0.64646465,0.64646465,0.66666667,0.66666667
,0.68686869,0.68686869,0.68686869,0.68686869,0.6969697,0.6969697
,0.70707071,0.70707071,0.70707071,0.70707071,0.70707071,0.71717172
,0.71717172,0.73737374,0.73737374,0.73737374,0.73737374,0.74747475
,0.74747475,0.75757576,0.75757576,0.75757576,0.75757576,0.76767677
,0.76767677,0.77777778,0.77777778,0.77777778,0.77777778,0.77777778
,0.78787879,0.78787879,0.80808081,0.80808081,0.80808081,0.81818182
,0.81818182,0.81818182,0.81818182,0.81818182,0.81818182,0.82828283
,0.82828283,0.85858586,0.85858586,0.85858586,0.85858586,0.85858586
,0.87878788,0.87878788,0.87878788,0.87878788,0.88888889,0.88888889
,0.88888889,0.88888889,0.88888889,0.88888889,0.8989899,0.8989899
,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899
,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899
,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899
,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899
,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899,0.8989899
,0.8989899,0.8989899,0.8989899,0.8989899,0.90909091,0.90909091
,0.90909091,0.90909091,0.90909091,0.90909091,0.90909091,0.90909091
,0.90909091,0.90909091,0.90909091,0.90909091,0.90909091,0.90909091
,0.90909091,0.90909091,0.91919192,0.91919192,0.91919192,0.91919192
,0.91919192,0.92929293,0.92929293,0.92929293,0.92929293,0.92929293
,0.92929293,0.92929293,0.92929293,0.92929293,0.92929293,0.93939394
,0.93939394,0.94949495,0.94949495,0.94949495,0.94949495,0.96969697
,0.96969697,0.96969697,0.96969697,0.97979798,0.97979798,0.97979798
,0.97979798,0.97979798,0.97979798,0.97979798,0.97979798,0.97979798
,0.97979798,0.97979798,0.97979798,0.97979798,0.97979798,0.97979798
,0.97979798,0.97979798,0.97979798,0.97979798,0.97979798,0.97979798
,0.97979798,0.97979798,0.97979798,0.97979798,0.97979798,0.97979798
,1.,1.,1.,1.,1.,1.
,1.,1.,1.,1.,1.,1.]

fpr2=[0.,0.01080432,0.01260504,0.01260504,0.01290516,0.01290516
,0.01410564,0.01410564,0.01590636,0.01590636,0.0165066,0.0165066
,0.01680672,0.01680672,0.01860744,0.01860744,0.01920768,0.01920768
,0.0195078,0.0195078,0.02040816,0.02160864,0.02190876,0.02190876
,0.022509,0.02310924,0.02310924,0.02430972,0.02430972,0.02521008
,0.02521008,0.0255102,0.0285114,0.02941176,0.02941176,0.03031212
,0.03031212,0.03181273,0.03181273,0.03271309,0.03271309,0.03331333
,0.03331333,0.03541417,0.03541417,0.03631453,0.03691477,0.03691477
,0.03871549,0.03871549,0.04201681,0.04231693,0.04231693,0.04321729
,0.04381753,0.04381753,0.04471789,0.04471789,0.04501801,0.04501801
,0.04561825,0.04921969,0.04981993,0.05042017,0.05162065,0.05222089
,0.05222089,0.05282113,0.05282113,0.05342137,0.05342137,0.05402161
,0.05822329,0.05852341,0.05852341,0.05882353,0.06212485,0.06332533
,0.06332533,0.06362545,0.06422569,0.06482593,0.06722689,0.06752701
,0.06752701,0.06782713,0.06782713,0.06842737,0.06842737,0.06902761
,0.07082833,0.07142857,0.07142857,0.07292917,0.07292917,0.07322929
,0.07322929,0.07352941,0.07352941,0.07412965,0.07412965,0.07442977
,0.07442977,0.07503001,0.07503001,0.07623049,0.07623049,0.07653061
,0.07653061,0.07713085,0.07773109,0.07923169,0.07953181,0.07953181
,0.07983193,0.08103241,0.08193277,0.08313325,0.08373349,0.08373349
,0.08493397,0.08613445,0.08673469,0.08883553,0.08943577,0.10084034
,0.10144058,0.1017407,0.1017407,0.10234094,0.10654262,0.10954382
,0.11014406,0.11164466,0.11254502,0.11434574,0.1197479,0.12785114
,0.12965186,0.12995198,0.1317527,0.13265306,0.1332533,0.13565426
,0.13685474,0.13745498,0.13895558,0.13955582,0.14015606,0.14135654
,0.14165666,0.14285714,0.14315726,0.1452581,0.1467587,0.14885954
,0.16326531,0.16356543,0.16476591,0.16566627,0.16596639,0.16986795
,0.17527011,0.17707083,0.17737095,0.19357743,0.20828331,0.20858343
,0.23109244,0.23229292,0.24039616,0.24069628,0.25270108,0.25510204
,0.26320528,0.2635054,0.26560624,0.26590636,0.27130852,0.27160864
,0.27280912,0.27430972,0.27490996,0.27671068,0.27731092,0.28241297
,0.28451381,0.28571429,0.29201681,0.29711885,0.29771909,0.29861945
,0.30282113,0.32563025,0.33103241,0.33703481,0.33733493,0.33973589
,0.34033613,0.34063625,0.34183673,0.65366146,0.65396158,0.65636255
,0.66266507,0.66986795,0.67046819,0.93157263,0.9879952,0.98889556
,0.99009604,0.99039616,0.9954982,1.]

tpr2=[0.,0.35849057,0.35849057,0.36792453,0.36792453,0.37735849
,0.37735849,0.38679245,0.38679245,0.39622642,0.39622642,0.41509434
,0.41509434,0.4245283,0.4245283,0.44339623,0.44339623,0.45283019
,0.45283019,0.46226415,0.46226415,0.46226415,0.46226415,0.47169811
,0.47169811,0.47169811,0.49056604,0.49056604,0.50943396,0.50943396
,0.52830189,0.52830189,0.52830189,0.52830189,0.53773585,0.53773585
,0.55660377,0.55660377,0.5754717,0.5754717,0.58490566,0.58490566
,0.60377358,0.60377358,0.62264151,0.62264151,0.62264151,0.63207547
,0.63207547,0.64150943,0.64150943,0.64150943,0.6509434,0.6509434
,0.6509434,0.66037736,0.66037736,0.66981132,0.66981132,0.67924528
,0.67924528,0.67924528,0.67924528,0.67924528,0.67924528,0.67924528
,0.68867925,0.68867925,0.70754717,0.70754717,0.71698113,0.71698113
,0.71698113,0.71698113,0.72641509,0.72641509,0.72641509,0.72641509
,0.74528302,0.74528302,0.74528302,0.74528302,0.74528302,0.74528302
,0.75471698,0.75471698,0.76415094,0.76415094,0.78301887,0.78301887
,0.78301887,0.78301887,0.79245283,0.79245283,0.80188679,0.80188679
,0.81132075,0.81132075,0.82075472,0.82075472,0.83018868,0.83018868
,0.83962264,0.83962264,0.85849057,0.85849057,0.86792453,0.86792453
,0.87735849,0.87735849,0.87735849,0.87735849,0.87735849,0.9245283
,0.9245283,0.9245283,0.9245283,0.9245283,0.9245283,0.94339623
,0.94339623,0.94339623,0.94339623,0.94339623,0.94339623,0.94339623
,0.94339623,0.94339623,0.95283019,0.95283019,0.95283019,0.95283019
,0.95283019,0.95283019,0.95283019,0.95283019,0.95283019,0.95283019
,0.95283019,0.95283019,0.95283019,0.95283019,0.95283019,0.95283019
,0.95283019,0.95283019,0.95283019,0.95283019,0.95283019,0.95283019
,0.96226415,0.96226415,0.96226415,0.96226415,0.96226415,0.96226415
,0.96226415,0.96226415,0.96226415,0.96226415,0.97169811,0.97169811
,0.97169811,0.97169811,0.98113208,0.98113208,0.99056604,0.99056604
,0.99056604,0.99056604,0.99056604,0.99056604,0.99056604,0.99056604
,0.99056604,0.99056604,0.99056604,0.99056604,0.99056604,0.99056604
,0.99056604,0.99056604,0.99056604,0.99056604,0.99056604,0.99056604
,0.99056604,0.99056604,0.99056604,0.99056604,0.99056604,0.99056604
,0.99056604,1.,1.,1.,1.,1.
,1.,1.,1.,1.,1.,1.
,1.,1.,1.,1.,1.,1.
,1.,1.,1.,1.]

# plot ROC
lw = 2
_, ax = plt.subplots(figsize=(7, 7))
#设置字体大小
# 设置刻度字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 设置坐标标签字体大小
ax.set_xlabel('PF',fontsize=20)
ax.set_ylabel('recall',fontsize=20)
# 设置图例字体大小
# line, = plt.plot(fpr, tpr, color='darkorange',
#                  lw=lw, label='ROC curve (AUC=%.2f)'%auc1)  ###假正率为横坐标，真正率为纵坐标做曲线
line, = plt.plot(fpr1, tpr1, color='darkorange',
                     lw=lw, label='CFS')
line.set_antialiased(False)
line2 = plt.plot(fpr2, tpr2, color='black',
                     lw=lw, label='chi-square',linestyle='--')
# line2.set_antialiased(False)
# plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
# plt.xlabel('PF')
# plt.ylabel('recall')
plt.title('PC5_ROC',fontsize=20)
plt.legend(loc="lower right",fontsize=20)
# plt.savefig('figure.eps')
plt.show()


#pc5
# chisquare:[0.7121891946059147,,0.7579842962989832,,0.9603133706312713,,0.5943396226415094,,0.03331332533013205]
# CFS:[0.,,0.8180512216745801,,0.9400398111089935,,0.696969696969697,,0.039832285115303984]7838820050387473