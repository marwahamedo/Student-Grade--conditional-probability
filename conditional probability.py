#!/usr/bin/env python
# coding: utf-8

# In[12]:


# We’re going to calculate the probability a student gets an A (80%+) in math, given they miss 10 or more classes.
import pandas as pd
import numpy as np
df = pd.read_csv (r'C:\Users\marwa\Downloads\students.csv')
df.head(3)


# In[14]:


# We’re only concerned with the columns, absences (number of absences), and G3 (final grade).
# Let’s create a couple new boolean columns based on these columns (number of absences & final grade[G3])to make our lives easier.
df['absences_rate']=np.where(df['absences'] >=10,1,0)
df['grade_A']= np.where(df['G3']*5 >=80,1,0)
# Add one more column to make building a pivot table easier.
df['count'] = 1


# In[15]:


df = df[['grade_A','absences_rate','count']]
df.head()


# In[22]:


pd.pivot_table(df,
               values=['count'], 
               index=['grade_A'], 
               columns=['absences_rate'], 
               aggfunc= np.size, 
               fill_value=0
              )


# In[33]:


#P_A is the probability of a grade of 80% or greater.
#P_B is the probability of missing 10 or more classes.
#P_A|B is the probability of a 80%+ grade, given missing 10 or more classes.
na= 35 + 5
nb= 78 + 5
na_b= 5
nt= 277+78+35+5
p_A = na/nt
p_B =nb/nt
p_A_B =na_b/nt
result = (p_A_B /p_B) 
print("the probability a student gets an A (80%+) in math, given they miss 10 or more classes is", result)


# In[ ]:




