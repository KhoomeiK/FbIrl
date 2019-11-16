#!/usr/bin/env python
# coding: utf-8

# In[172]:


import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from PIL import Image
import numpy as np
import os
import pickle
import random
# let's not drive ourselves crazy with fitting
random.seed(2)


# In[173]:


IMG_SIZE = 128

def img_to_vec(file_name):
    img = Image.open(file_name)
    img = img.resize((IMG_SIZE, IMG_SIZE))
    return np.array(img).ravel()


target = []
data = []
class_num = -1
for i, subdir in enumerate(os.listdir('data')):
    if subdir == '.DS_Store':
        continue
    class_num += 1
    for file in os.listdir('data/{}'.format(subdir)):
        if file[-3:] == 'jpg':
            file_name = 'data/{}/{}'.format(subdir, file)
            data.append(img_to_vec(file_name))
            target.append(class_num)
    print(subdir, class_num)


# In[174]:


min(map(lambda x: len(x), data))


# In[175]:


svc_1 = SVC(kernel='linear')
print (svc_1)


# In[176]:


X_train, X_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=0)


# In[177]:


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


# In[178]:


clf = SVC(kernel='linear').fit(X_train, y_train)


# In[179]:


clf.score(X_test, y_test)


# In[180]:


joblib.dump(clf, 'classifier.pkl') 


# In[181]:


clf.predict([X_test[0]])


# In[182]:


predictions = clf.predict(X_test)
for input, prediction, label in zip(X_test, predictions, y_test):
    if prediction != label:
        print(input, 'has been classified as ', prediction, 'and should be ', label) 


# In[183]:


predictions


# In[184]:


print(class_num)


# In[ ]:




