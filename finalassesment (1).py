# -*- coding: utf-8 -*-
"""finalAssesment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Ui2ngNhoqCScMK0EnnpaGkOIUJD8v11
"""



#loading training dataset
import pandas as pd
data=pd.read_csv('/content/train_LZdllcl.csv')
data.head()

data.info()
data.describe()

#checking for null values
data.isnull().sum()

data.columns

#handling null values by taking mean and mod
data['education']=data['education'].fillna(data['education'].mode()[0])
data['previous_year_rating']=data['previous_year_rating'].fillna(data['previous_year_rating'].mean())
#check for null
data.isnull().sum()



#encoding the columns using one-hot encoder
data=pd.get_dummies(data,columns=['department','education','gender','recruitment_channel'])
data.head()

data.shape

data.columns

#splitting x and y
X=data.drop(['is_promoted','employee_id','region'],axis=1)
y=data['is_promoted']

X.shape,y.shape

#splitting train and test data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#scale the columns
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

#loading the model
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
pred=model.predict(X_test)
accuracy = accuracy_score(y_test, pred)
ac

f1 = f1_score(pred, y_test)
f1

#loading dataset for testing
import pandas as pd
data2=pd.read_csv('/content/test_2umaH9m.csv')
data2.head()

data2.info()
data2.describe()

data2.shape

#checking for null values in test dataset
data2.isnull().sum()

data2.columns

#handling null values by taking mean and mod
data2['education']=data2['education'].fillna(data2['education'].mode()[0])
data2['previous_year_rating']=data2['previous_year_rating'].fillna(data2['previous_year_rating'].mean())
#check for null
data2.isnull().sum()

#encoding the columns using one-hot encoder
data2=pd.get_dummies(data2,columns=['department','education','gender','recruitment_channel'])
data2.head()

data2.columns

test=data2.drop(['employee_id','region'],axis=1)
test.head()

#scale the columns
from sklearn.preprocessing import StandardScaler
sc2=StandardScaler()
test=sc2.fit_transform(test)

result=model.predict(test)
len(result),result

sample=pd.read_csv('/content/sample_submission_M0L0uXE.csv')

sample['is_promoted']=result
sample.to_csv('solution1.csv',index=False)

