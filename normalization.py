# -*- coding: utf-8 -*-


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.preprocessing as sp



path = "*.*"
pathnew = "*.*"

os.chdir(path)


#path, directory, file
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        #
        if os.path.splitext(name)[1] == '.txt':  
            #print(root)
            print(os.path.join(root, name))
            #open file
            train = pd.read_csv(os.path.join(root, name), sep=" ",header=None)
            datazscore = train[4]
            dataminmax = train[4]
            standard = sp.StandardScaler()
            standard_scaled = standard.fit_transform(datazscore.values.reshape(-1,1))
            train[4]=standard_scaled
            #write file
            filenamezscore=os.path.join(pathnew,os.path.join(root, os.path.splitext(name)[0]+'.zscore'+os.path.splitext(name)[1]).replace('.\\',''))
            filenameminmax=os.path.join(pathnew,os.path.join(root, os.path.splitext(name)[0]+'.minmax'+os.path.splitext(name)[1]).replace('.\\',''))
            if not os.path.exists(os.path.dirname(filenamezscore)):
                try:
                    os.makedirs(os.path.dirname(filenamezscore))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            #save file
            train.to_csv(filenamezscore, sep=" ",header=None, index=False)
            
            #normalization
            minmax = sp.MinMaxScaler()
            minmax_scaled = minmax.fit_transform(dataminmax.values.reshape(-1,1))
            train[4]=minmax_scaled
            train.to_csv(filenameminmax, sep=" ",header=None, index=False)
            