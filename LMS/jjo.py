from sklearn.ensemble import RandomForestClassifier
import pandas as pd
df=pd.read_csv('loan45.csv')
print(df.head())
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plot
from sklearn import metrics
from sklearn.metrics import accuracy_score,f1_score,recall_score,precision_score,confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df['Loan_Amount_Term'].fillna(df['LoanAmount'].mean(), inplace=True)
df.isna().sum()

label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
df['Married'] = label_encoder.fit_transform(df['Married'])

df['Education'] = label_encoder.fit_transform(df['Education'])
df['Self_Employed'] = label_encoder.fit_transform(df['Self_Employed'])
df['Property_Area'] = label_encoder.fit_transform(df['Property_Area'])
df['Loan_Status'] = label_encoder.fit_transform(df['Loan_Status'])



from sklearn.model_selection import train_test_split
X = df.drop(['Loan_Status'],axis=1)
Y = df['Loan_Status']
X.shape,Y.shape
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                    test_size=0.2,
                                                    random_state=1)
X_train.shape, X_test.shape, Y_train.shape, Y_test.shape
df['Loan_Amount_Term'].fillna(df['LoanAmount'].mean(), inplace=True)
rfc = RandomForestClassifier(n_estimators = 7, criterion = 'entropy', random_state =7,min_samples_leaf=3)
rfc.fit(X_train,Y_train)
print(rfc)

from skops import  io as sio
obj = sio.dump(rfc,'new.skops')
print(obj)
