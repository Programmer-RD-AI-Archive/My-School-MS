#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
"""


# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('./reviews.csv')


# In[3]:


data.head()


# In[4]:


data.drop(['Id'],axis=1,inplace=True)


# In[5]:


data.head()


# In[6]:


data.isna().sum()


# In[7]:


data.dropna(inplace=True)


# In[8]:


data['Label'].value_counts()


# In[9]:


import numpy as np
to_delete = np.random.choice(data[data['Label'] == 5].index,size=61000,replace=False)


# In[10]:


data.drop(to_delete,axis=0,inplace=True)


# In[11]:


data['Label'].value_counts()


# In[12]:


data.dtypes


# In[13]:


X = data['Review']
y = data['Label']


# In[14]:


from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
cv = CountVectorizer()
tv = TfidfVectorizer()
cv.fit(X)
X = cv.transform(X)
# X.reshape(-1,1)
# X = pd.DataFrame(X)
y = pd.DataFrame(y)


# In[15]:


from sklearn.metrics import *
from sklearn.model_selection import *
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)


# In[16]:


from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train,y_train)
model.score(X_test,y_test)


# In[17]:


text = input('Review : ')
text = cv.transform([text])
model.predict(text)


# In[18]:


grid = {
#     "n_estimators":[10,100,200,400,800,1600,125,250,500,1250,2500],
    "max_depth":[None,5,10,15,20,25],
    "criterion":["gini","entropy",],
    'splitter':['best','random'],
    "max_features":["auto","sqrt",'log2'],
    "min_samples_leaf":[1,2,4,6,8,10],
}
model_rs = DecisionTreeClassifier()
rs = RandomizedSearchCV(estimator=model_rs,param_distributions=grid,cv=5,n_iter=25,verbose=25)
rs.fit(X_train,y_train)
print(rs.best_estimator_)
print(rs.score(X_test,y_test))
print(rs.best_score_)
import pickle
pickle.dump(model_rs,open('./model_random.pkl','wb'))


# In[19]:


text = 'Worst course in the world the worst of the worst I hate the teacher of the course and the teacher is like a nerd and he sucks I hate him and the course the instructions are the worst in the world'
text = cv.transform([text])
rs.predict(text)


# In[ ]:


grid = {
    "max_depth":[None,5,10,15,20,25,30,35,40,45,50],
    "criterion":["gini","entropy",],
    'splitter':['best','random'],
    "max_features":["auto","sqrt",'log2'],
    "min_samples_leaf":[2,4,6,8,10],
}
model_gs = DecisionTreeClassifier()
gs = GridSearchCV(estimator=model_gs,param_grid=grid,cv=5,verbose=25)
gs.fit(X_train,y_train)
print(gs.best_estimator_)
print(gs.score(X_test,y_test))
print(gs.best_score_)
pickle.dump(model_gs,open('./model_grid.pkl','wb'))


# In[ ]:


text = 'Worst course in the world the worst of the worst I hate the teacher of the course and the teacher is like a nerd and he sucks I hate him and the course the instructions are the worst in the world'
text = cv.transform([text])
model_rs.predict(text)

