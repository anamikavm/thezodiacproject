
# In[1]:


def zodiac(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    d = int(birthdate.strftime("%e"))
    m = birthdate.strftime("%b")

    if (m == "Mar" and 21 <= d <= 31) or (m == "Apr" and 1 <= d <= 19):
        print("""Zodiac sign:  \033[1mAries\033[0m 
              You are the embodiment of bravery, springing with life and energy; you radiate that around you. As a cardinal sign 
              and the youngest of them all, you have quite the mischief. But that nasty temper of yours can maybe sting others
              and yourself. After all, fire burns all!! Learn to keep it cool and you're irresistible!""")
    elif (m == "Apr" and 20 <= d <= 30) or (m == "May" and 1 <= d <= 20):
        print("""Zodiac sign: \033[1mTaurus\033[0m
        You are the embodiment of protection, a true protector of your loved ones. The blessings of Venus, beauty and war,
        reside in you. You are a bit attracted to comfort and are too stubborn till you breathe on this planet. 
        Maybe ease up a little and get comfortable in the high road and you're unstoppable!""")
    elif (m == "May" and 21 <= d <= 31) or (m == "Jun" and 1 <= d <= 20):
        print("""Zodiac sign: \033[1mGemini\033[0m
        You are the embodiment of communication, air sign. You have two sides: a side known to all and a side oblivious to all.
        You are brilliant in what you choose to excel and are quite intelligent, but you may self-sabotage by over-communicating,
        underrepresenting, or simply revealing your plans early. But you know all the fixes, be nice and you're truly admirable!""")
    elif (m == "Jun" and 21 <= d <= 30) or (m == "Jul" and 1 <= d <= 22):
        print("""Zodiac sign: \033[1mCancer\033[0m
        You are the embodiment of healing, the mother of all zodiac signs. But don't let that fool others, you can be quite ahead at 
        what you like doing. You're just as ambitious as Capricorns, your opposite sign. You can be emotionally intuitive and can play
        people's emotions and keep 'em rollin if you choose to. But healing others is what makes you, you. Don't let that die!""")
    elif (m == "Jul" and 23 <= d <= 31) or (m == "Aug" and 1 <= d <= 22):
        print("""Zodiac sign: \033[1mLeo\033[0m
        You are the embodiment of leadership. A lion always rules the jungle! But don't be swept by your ego and fire, as it can push
        all your loved ones away from you. You are the spotlight anywhere you go and are more steady in your stance, so nobody pushes
        your buttons. Have gratitude, and there's no stopping your aura! Too magnetic and loyal!""")
    elif (m == "Aug" and 23 <= d <= 31) or (m == "Sep" and 1 <= d <= 22):
        print("""Zodiac sign: \033[1mVirgo\033[0m
        You are the embodiment of perfection. You plan steps and are actually very grounded during tough times, even for your
        loved ones. You can be a pillar of support during times of crisis. Don't put away your emotions while trying to achieve practicality
        in all aspects of life. Embrace the imperfections and keep things easy, you're really cool and you know that!""")
    elif (m == "Sep" and 23 <= d <= 30) or (m == "Oct" and 1 <= d <= 22):
        print("""Zodiac sign: \033[1mLibra\033[0m
        You are the embodiment of justice, air sign. You see fairness and balance in all aspects of life. Your morals are your true 
        strength. You are diplomatic when you have to be and quite revolting when things go against you're beliefs and ideals. You are
        just as fiery and mischievous as your opposite, Aries, but you know how to keep it together. Trust the process and be inspiring!""")
    elif (m == "Oct" and 23 <= d <= 31) or (m == "Nov" and 1 <= d <= 21):
        print("""Zodiac sign: \033[1mScorpio\033[0m
        You are the embodiment of Intensity. No one argues with the mysterious Scorpio! You can make a whole room yours just
        by existing. But you have a soft guy in you, who  wishes to cuddle and cross the length of the earth. You are a
        water sign, making you intuitive, but you explore the depths and can trigger people into transformation. Don't kill the
        soft guy in you and make room to trust people, you're a true lover!""")
    elif (m == "Nov" and 22 <= d <= 30) or (m == "Dec" and 1 <= d <= 21):
        print("""Zodiac sign: \033[1mSagittarius\033[0m
        You are the embodiment of Wisdom. You are a seeker of the truth, going on adventures, exploring, and playing the eternal optimist
        You're like a wise old owl when it comes to your passion and knowledge about the world. You're fiery passion is often 
        unmatched by those around you, you're a  natural charmer, and your enthusiasm towards life always draws people in. Keep it going, growing!""")
    elif (m == "Dec" and 22 <= d <= 31) or (m == "Jan" and 1 <= d <= 20):
        print("""Zodiac sign: \033[1mCapricorn\033[0m
        You are the embodiment of Ambition, earth sign. Characterized by a hardworking, pragmatic nature focused on achieving goals through perseverance 
        and dedication, you are an authority! You can be too focused on achieving that, and you may be behind on working out your emotions. It is 
        important to understand and release emotions and be just as vulnerable as your dedication to your work. Be soft and you'll transcend boundaries!""")
    elif (m == "Jan" and 21 <= d <= 31) or (m == "Feb" and 1 <= d <= 18):
        print("""Zodiac sign: \033[1mAquarius\033[0m
        You are the embodiment of Innovation, air sign. Often seen as a rebel or visionary who challenges the status quo for the betterment of society.
        You are individualistic and humanitarian with a relentless pursuit of progress. You are the change people wish to see, but you
        can also lose your way if you are misunderstood or curbed for too long. Be kind but don't lose yourself!""")
    elif (m == "Feb" and 19 <= d <= 29) or (m == "Mar" and 1 <= d <= 20):
        print("""Zodiac sign: \033[1mPisces\033[0m
        You are the embodiment of expression. As the last sign of the zodiac, it represents the dissolution of boundaries and absorption of all
        life lessons, leading to a profound connection with the unseen realms of emotion, spirituality, and the collective consciousness. They are all
        about fantasy and reality, and can be just as intuitive as other water signs. Be yourself, express more, and spread your wisdom to others!""")
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




