#!/usr/bin/env python
# coding: utf-8

# In[15]:


import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from PIL import Image
import numpy as np
import os
import pickle


# In[2]:


def img_to_vec(file_name):
    img = Image.open(file_name)
    return np.array(img).ravel()


target = []
data = []
for i, subdir in enumerate(os.listdir('data')):
    if subdir == '.DS_Store':
        continue
    for file in os.listdir('data/{}'.format(subdir)):
        if file[-3:] == 'jpg':
            file_name = 'data/{}/{}'.format(subdir, file)
            data.append(img_to_vec(file_name)[:64116])
            target.append(i)


# In[3]:


min(map(lambda x: len(x), data))


# In[4]:


svc_1 = SVC(kernel='linear')
print (svc_1)


# In[5]:


X_train, X_test, y_train, y_test = train_test_split(
        data, target, test_size=0.1, random_state=0)


# In[6]:


def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
    
    clf.fit(X_train, y_train)
    
    print ("Accuracy on training set:")
    print (clf.score(X_train, y_train))
    print ("Accuracy on testing set:")
    print (clf.score(X_test, y_test))
    
    y_pred = clf.predict(X_test)
    
    print ("Classification Report:")
    print (metrics.classification_report(y_test, y_pred))
    print ("Confusion Matrix:")
    print (metrics.confusion_matrix(y_test, y_pred))


# In[7]:


clf = SVC(kernel='linear', C=1).fit(X_train, y_train)


# In[13]:


clf.score(X_test, y_test)


# In[16]:


joblib.dump(clf, 'classifier.pkl') 


# In[18]:


clf.predict([X_test[0]])


# In[ ]:




