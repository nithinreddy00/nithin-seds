#!/usr/bin/env python
# coding: utf-8

# # # python

# In[11]:


superhero='Ironman'
number='3000'
print(superhero+number)


# In[7]:


x= input('enter a:')
y= input( 'enter b: ')
print(x+y)


# In[6]:


x = 5
y = "John"
print(type(x))
print(type(y))


# In[1]:


x = "5"
y = "64"
print(x + y)


# In[3]:


import pandas as pd
music_data=pd.read_csv('music.csv')
music_data.head()


# # Nampy start

# In[1]:


import numpy as np
array=np.array([(1,2,3,4),(1,2,3,4)],dtype=float)
print(array)
array.shape


# In[76]:


from time import process_time
list=[i for i in range(99999)]
start_time=process_time()
list=[i / 5 for i in range(9999999)]
end_time=process_time()
print(end_time-start_time)


# In[75]:


np_array=np.array([ i for i in range(9999999)])
start_time=process_time()
np_array = np_array / 5
end_time=process_time()
print(end_time-start_time)


# In[56]:


c=np.random.randint(10,100,(3,3))
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)


# In[57]:


list=[1,2,3,4,5]
print(list)
type(list)
np_array=np.asarray(list)
print(np_array)
type(np_array)


# In[59]:


arr1=np.random.randint(0,10,(3,3))
arr2=np.random.randint(10,20,(3,3))
print(arr1,arr2)
print(arr1+arr2)
print(arr1*arr2)
print(arr1/arr2)


# In[63]:


n=np.random.randint(0,10,(2,3))
print(n)
m=(n.T) #T=transpose
print(m)


# In[68]:


k=np.random.randint(0,10,(2,3))
y=k.reshape(3,2)
print(k)
print(y)


# 
# # pandas strart 
# 

# #importing a dataset

# In[32]:


from sklearn.datasets import load_boston
cali_dataset=load_boston()
print(cali_dataset)


# In[20]:


import pandas as pd
boston_data=pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
boston_data.head()
boston_data.shape

#importing from a csv file
# In[21]:


import pandas as pd
music_data=pd.read_csv('music.csv')
music_data.head()
music_data.shape


# #Loading data from a excel file :
# #variable_name=pd.read_excel('file name' or 'fie path')
# converting a pandas file to a csv 
#variable_df.to_csv('filename.csv')

# In[19]:


import pandas as pd
import numpy as np
random_df=pd.DataFrame(np.random.randint(20,90,(6,6)))
random_df.head()


# In[40]:


from sklearn.datasets import load_boston
cali_dataset=load_boston()
boston_data = pd.DataFrame(cali_dataset.data,columns=cali_dataset.feature_names)
boston_data.info()


# In[42]:


boston_data.isnull().sum()


# In[55]:


dia_data=pd.read_csv('diabetes.csv')
#dia_data.info()
#dia_data.isnull
#dia_data.value_counts('Outcome')
#dia_data.groupby('Age').mean()


# In[2]:


#boston_data.mean()
#boston_data.std()
#boston_data.min()
#boston_data.max()
#boston_data.describe()


# In[65]:


#adding a column
#boston_data['Price']=boston_dataset.target


# In[66]:


#removing a column
boston_data.drop(index=0,axis=0)


# In[7]:


#removing a column
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
boston_dataset=load_boston()
boston_data=pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
boston_data.drop(columns='ZN',axis=1)


# In[8]:


boston_data.iloc[2]


# In[ ]:


print(boston_data.iloc[:,0]) #first column
print(boston_data.iloc[:,2]) #third column
print(boston_data.iloc[:,-1]) #last column


# In[10]:


boston_data.corr()

