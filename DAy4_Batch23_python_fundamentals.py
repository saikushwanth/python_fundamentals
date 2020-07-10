#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list


# In[2]:


students = ['sai','kushwanth','ravi','kiran']

print(students)


# In[3]:


type(students)


# In[4]:


#access ravi name

print(students[2])


# In[5]:


print(students[2].title())


# In[7]:


print(students[2].upper())


# In[8]:


print(students)


# In[11]:


#replace ravi with sajid


# In[12]:


students[2] = 'sajid'


# In[13]:


print(students)


# In[16]:


#req: to add swapna to the list above list.....

students.append('swapna')


# In[17]:


print(students)


# In[18]:


students.append('joshi')


# In[19]:


print(students)


# In[20]:


#req: to add laxmi at the 3rd index

students.insert(3,'laxmi')


# In[21]:


print(students)


# In[22]:


#req: remove sai from the above list 

del students[0]


# In[23]:


print(students)


# In[24]:


#pop method


# In[25]:


x = students.pop()


# In[26]:


print(students)


# In[27]:


print(x)


# In[28]:


y = students.pop(3)


# In[29]:


print(students)


# In[30]:


print(y)


# In[ ]:




