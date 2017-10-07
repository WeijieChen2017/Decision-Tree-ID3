#-*- coding: utf-8 -*-

import numpy as np

# Initialization
feature = dict()
data_flag = 0
data = []
n = -1 # Number of samples
p = 0 # Number of features without label

# Load ARFF file
with open('diabetes.arff', 'rt') as f:
    for line in f:
        # Find relation
        if line.find('@relation')>-1:
            relation = line[10:]
        
        # Find Attribute
        if line.find('@attribute')>-1:
            # Cut off '@attribute'
            att = line[11:]
            # Find space between feature name and type
            space = att.find(' ')
            # Get feature name
            fea = att[1:space-1]
            # Get feature type
            att_type = att[space+1:-1]
            # If feature type is a list
            x = att_type.find('{')
            if x>-1:
                x = x + 2
                fea_dic =[]
                i = att_type.find(',')
                # Loop for build up a dictionary to store feature value
                while i>-1:
                    fea_dic.append(att_type[x:i])
                    att_type = att_type[i+1:]
                    i = att_type.find(',')
                    x = 1
                fea_dic.append(att_type[x:-1])
                # Count total number of feature 
                p = len(fea_dic)
            else:
                # If feature is numeric, just store 'numeric'
                fea_dic = att_type
            # Build up the feature dictionary
            feature[fea] = fea_dic
            p = p - 1
        
        # Begin data loading
        if line.find('@data')>-1:
            data_flag = 1
            continue
            
        # Count of samples
        if data_flag == 1:
            n = n + 1
            # Store current sample
            data_row = [] 
            for key in feature:
                value = feature[key]
                i = line.find(',') 
                # Feature segementation
                # If the last feature is string, it will end up with '\n'
                # If the last featuer is number, it will end upwith number
                if i==-1 and isinstance(value, str):
                    info = line
                else:
                    info = line[:i]
                line = line[i+1:]
                # Convert current feature value
                if isinstance(value, list):
                    data_row.append(value.index(info))
                else:
                    data_row.append(float(info))
            # Add current sample to dataset
            data.append(data_row)

# Convert dataset into numpy array
data = np.array(data)

# ------End for .ARFF Loading------
