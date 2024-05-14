#!/usr/bin/env python
# coding: utf-8

# In[3]:


name = input("Enter your name: ")

weight = int(input("Enter your weight: "))

height = int(input("Enter your height: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name +", you are underweight. ")
    elif (BMI<=24.9):
        print(name +", you are normal weight. ")
    elif (BMI<=29.9):
        print(name +", you are overweight. ")
    elif (BMI<=34.9):
        print(name +", you are obese. ")
    elif (BMI<39.9):
        print(name +", You are severely obese. ")
else:
    print(name +", You are morbidly obese. " )
        

        


# In[ ]:





# In[ ]:





# In[ ]:


#BMI = (weight in pounds x 703) / (height in inches x height in inches)


# In[ ]:


# BMI Range

Under 18.5	Underweight	Minimal
18.5 - 24.9	Normal Weight	Minimal
25 - 29.9	Overweight	Increased
30 - 34.9	Obese	High
35 - 39.9	Severely Obese	Very High
40 and over	Morbidly Obese	Extremely High


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




