import csv
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
from sklearn.linear_model import LinearRegression

# Data Preprocessing
data = pd.read_csv('dataset1.csv',encoding='ISO-8859-1')
X = data.iloc[:,:2].values
Y = data.iloc[:,2:5].values
Xe = data.iloc[717:,:].values


# Encoding the string into binary numbers
l_x = LabelEncoder()
X[:,0] = l_x.fit_transform(X[:,0])
oneHotEncoder = OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray()

# Expenditure Prediction
xe_train = X[:-41,:]
ye_train = Y[:-41,:-2]
xe_test = X[717:,:]
ye_test = Y[717:,:-2]
regressor = LinearRegression()
regressor.fit(xe_train,ye_train)
ye_pred = regressor.predict(xe_test)

# Sales Prediction
xs_train = X[:-41,:]
ys_train = Y[:-41,1:-1]
xs_test = X[717:,:]
ys_test = Y[717:,1:-1]
regressor.fit(xs_train,ys_train)
ys_pred = regressor.predict(xs_test)

#profit Prediction
xp_train = X[:-41,:]
yp_train = Y[:-41,2:]
xp_test = X[717:,:]
yp_test = Y[717:,2:]
regressor.fit(xp_train,yp_train)
yp_pred = regressor.predict(xp_test)



#Creating CSV File for predicted crops details
l = ['Crop Name','Expected Expenditure','Expected Selling Price','Expected Profit %','Duration','Soil Type','Season']
with open('./predicted.csv','w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(l)
    for i in range(len(yp_pred)):
        filewriter.writerow([Xe[i][0],ye_pred[i][0],ys_pred[i][0],yp_pred[i][0]*100,Xe[i][5],Xe[i][6],Xe[i][7]])

