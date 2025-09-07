#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def aries(n):
    if m = Mar,d= (21,31) or m = Apr, d = (1,19):
        print("zodiac sign : aries")
    else:
        print("you are not an aries")


# In[7]:


from datetime import datetime

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

print("Birthdate:", birthdate)
d= birthdate.strftime("%e")
m=birthdate.strftime("%b")


# In[9]:


def aries(birthdate_str):
    if m = Mar & d= (21,31) or m = Apr & d = (1,19):
        print("zodiac sign : aries")
    else:
        print("you are not an aries")
    return aries(birthdate_str)

from datetime import datetime

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

print("Birthdate:", birthdate)
d= birthdate.strftime("%e")
m=birthdate.strftime("%b")


# In[1]:


def zodiac(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    d = int(birthdate.strftime("%e"))
    m = birthdate.strftime("%b")

    if (m == "Mar" and 21 <= d <= 31) or (m == "Apr" and 1 <= d <= 19):
        print("Zodiac sign: Aries")
    elif (m == "Apr" and 20 <= d <= 30) or (m == "May" and 1 <= d <= 20):
        print("Zodiac sign: Taurus")
    elif (m == "May" and 21 <= d <= 31) or (m == "Jun" and 1 <= d <= 20):
        print("Zodiac sign: Gemini")
    elif (m == "Jun" and 21 <= d <= 30) or (m == "Jul" and 1 <= d <= 22):
        print("Zodiac sign: Cancer")
    elif (m == "Jul" and 23 <= d <= 31) or (m == "Aug" and 1 <= d <= 22):
        print("Zodiac sign:Leo")
    elif (m == "Aug" and 23 <= d <= 31) or (m == "Sep" and 1 <= d <= 22):
        print("Zodiac sign:Virgo")
    elif (m == "Sep" and 23 <= d <= 30) or (m == "Oct" and 1 <= d <= 22):
        print("Zodiac sign: Libra")
    elif (m == "Oct" and 23 <= d <= 31) or (m == "Nov" and 1 <= d <= 21):
        print("Zodiac sign: Scorpio")
    elif (m == "Nov" and 22 <= d <= 30) or (m == "Dec" and 1 <= d <= 21):
        print("Zodiac sign: Sagittarius")
    elif (m == "Dec" and 22 <= d <= 31) or (m == "Jan" and 1 <= d <= 20):
        print("Zodiac sign:Capricorn")
    elif (m == "Jan" and 21 <= d <= 31) or (m == "Feb" and 1 <= d <= 18):
        print("Zodiac sign: Aquarius")
    elif (m == "Feb" and 19 <= d <= 29) or (m == "Mar" and 1 <= d <= 20):
        print("Zodiac sign:Pisces")
    else:
        print("Invalid date")
    
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
zodiac(birthdate_str)


# In[1]:


def zodiac(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    d = int(birthdate.strftime("%e"))
    m = birthdate.strftime("%b")

    if (m == "Mar" and 21 <= d <= 31) or (m == "Apr" and 1 <= d <= 19):
        print("Zodiac sign: Aries")
    elif (m == "Apr" and 20 <= d <= 30) or (m == "May" and 1 <= d <= 20):
        print("Zodiac sign: Taurus")
    elif (m == "May" and 21 <= d <= 31) or (m == "Jun" and 1 <= d <= 20):
        print("Zodiac sign: Gemini")
    elif (m == "Jun" and 21 <= d <= 30) or (m == "Jul" and 1 <= d <= 22):
        print("Zodiac sign: Cancer")
    elif (m == "Jul" and 23 <= d <= 31) or (m == "Aug" and 1 <= d <= 22):
        print("Zodiac sign:Leo")
    elif (m == "Aug" and 23 <= d <= 31) or (m == "Sep" and 1 <= d <= 22):
        print("Zodiac sign:Virgo")
    elif (m == "Sep" and 23 <= d <= 30) or (m == "Oct" and 1 <= d <= 22):
        print("Zodiac sign: Libra")
    elif (m == "Oct" and 23 <= d <= 31) or (m == "Nov" and 1 <= d <= 21):
        print("Zodiac sign: Scorpio")
    elif (m == "Nov" and 22 <= d <= 30) or (m == "Dec" and 1 <= d <= 21):
        print("Zodiac sign: Sagittarius")
    elif (m == "Dec" and 22 <= d <= 31) or (m == "Jan" and 1 <= d <= 20):
        print("Zodiac sign:Capricorn")
    elif (m == "Jan" and 21 <= d <= 31) or (m == "Feb" and 1 <= d <= 18):
        print("Zodiac sign: Aquarius")
    elif (m == "Feb" and 19 <= d <= 29) or (m == "Mar" and 1 <= d <= 20):
        print("Zodiac sign:Pisces")
    else:
        print("Invalid date")
        

from datetime import datetime

while True:
    try:
        birthdate_str = input("Enter your birthdate (DD-MM-YYYY): ")
        birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
        if birthdate.month > 12:
            raise ValueError("Invalid month. Please enter a valid month (1-12).")
        break
    except ValueError:
        print("Invalid date, check again ")

zodiac(birthdate_str)


# In[ ]:





# In[ ]:




