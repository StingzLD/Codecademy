#!/usr/bin/env python
# coding: utf-8

# # Off-Platform Project 1: Customer Service Bot

# In[1]:


name = input("What is your name? ")


# In[2]:


print(name)


# In[3]:


def cs_service_bot():
    print("Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer? \n[1] New Customer \n[2] Existing Customer")
    response = input("Please enter the number corresponding to your choice:")
    if response == "1":
        new_customer()
    if response == "2":
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection.")
        cs_service_bot()


# In[4]:


def existing_customer():
    print("What kind of support do you need?")
    response = input("[1] Television Support \n[2] Internet Support \n[3] Speak to a support representative.")
    if response == "1":
        television_support()
    if response == "2":
        internet_support()
    if response == "3":
        live_rep()
    else:
        print("Sorry, we didn't understand your selection.")
        existing_customer()


# In[5]:


def new_customer():
    print("What kind of support do you need?")
    response = input("[1] Sign up for service. \n[2] Schedule a home visit. \n[3] Speak to a sales representative.")
    if response == "1":
        sign_up()
    if response == "2":
        home_visit()
    if response == "3":
        live_rep(agent)
    else:
        print("Sorry, we didn't understand your selection.")
        new_customer()


# In[6]:


def television_support():
    print("What is the nature of your problem?")
    response = input("[1] I can't access certain channels. \n[2] My picture is blurry. \n[3] I keep losing service. \n[4] Other issues.")
    if response == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    if response == "2":
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    if response == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        dod_that_help()
    if response == "4":
        print("You are being redirection to Live Support.")
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        television_support()


# In[7]:


def internet_support():
    print("What is the nature of your problem?")
    response = input("[1] I can't connect to the internet. \n[2] My connection is very slow. \n[3] I can't access certain sites. \n[4] Other issues.")
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    if response == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.")
        did_that_help()
    if response == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    if response == "4":
        print("You are being redirection to Live Support.")
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        television_support()


# In[8]:


def did_that_help():
    response = input("[1] Yes \n[2] No")
    if response == "1":
        print("We are glad we could help you resolve your issue. Thank you for contacting support. Have a great day!")
    if response == "2":
        print("We are sorry that this solution did not resolve your issue. Would you like to speak to a Live Support Agent or schedule a home visit?")
        response2 = input("[1] Yes \n [2] No")
        if response2 == "1":
            live_rep("support")
        if response2 == "2":
            home_visit("support")
        else:
            print("Sorry, we didn't understand your selection.")
            did_that_help()
    else:
        print("Sorry, we didn't understand your selection.")
        did_that_help()


# In[9]:


def sign_up():
    print("Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for.")
    response = input("[1] Bundle Deal (Internet + Cable) \n[2] Internet \n[3] Cable")
    if response == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    if response == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    if response == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    else:
        print("Sorry, we didn't understand your selection.")
        sign_up()


# In[10]:


def home_visit(purpose = "none"):
    if purpose == "none":
        print("What is the reason for the home visit?")
        response = input("[1] New service installation. \n[2] Exisitng service repair. \n[3] Location scouting for unserviced region.")
        if response == "1":
            home_visit("new install")
        if response == "2":
            home_visit("support")
        if response == "3":
            home_visit("scout")
    if purpose == "new install":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and install your new service.")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")
    if purpose == "support":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home to troubleshoot and repair your service.")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")
    if purpose == "scout":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and scout out the area for new service.")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")


# In[11]:


def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    if purpose == "support":
        print("Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.")


# In[ ]:


cs_service_bot()


# ## Fin!