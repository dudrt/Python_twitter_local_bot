#To start we will need to import at least three libraries.

from selenium import webdriver
#Selenium webdriver will be our browser.
from selenium.webdriver.common.keys import Keys
#Keys will be used by our browser to understand the keyboard keys such as return.
import tweepy
#tweepy is the library we will use to connect to twitter.


#To start, we need to set a variable that will be our browser.Here I created it as "Chrome" because it will be the browser that I will use.
chrome=webdriver.Chrome()
#now we will pass the site that our browser should open.
chrome.get("https://www.google.com.br/")


#In this case, I want to search on google so I will look for the element that has its name 'q'
#which is the place where google searches are carried out.
#And on the same line, I can specify which word or phrase I want to search for.
chrome.find_element_by_name('q').send_keys("dolar")
#think as if the bot were you, right after writing your research, you need confirm in this case it is called .ENTER
chrome.find_element_by_name('q').send_keys(Keys.ENTER)
#right after that it will search and find on a page.
#----------------------------------------------------IMPORTANT-------------------------------------------------------------------------------------
#This is a part you need to pay attention to. Now you will find what you want from a page or search, you know that every html page has elements, 
#some have id, class, name, but some don't, in these cases you will need to get the element's XPATH.
#maybe everything you want to get has at least class or name, but I highly recommend you take a look.
#Go back and enter the XPATH_EN-PT.md document.

#You can choose the best way to look for an element(on the documment READMETOBEGIN.md, I left the selenium documentation website).
#By xpath, id, class, name, whatever you prefer.
#On the same line you can give the command get_attribute("whatever you want to get").

dolar=chrome.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute("data-value")

#And the basics are ready, you can already do cool things with it. Look for more commands on the official selenium website.

#Now the most complicated part begins, which is connecting tweepy with twitter. For this part I recommend that you research 
#some videos on how to get your keys and tokens.

#Basically you must enter the twitter developer website https://developer.twitter.com, connect and login with your bot's twitter 
#account and get the type 2 authentication level.

#-------------------------------------------------Join twitter and post--------------------------

#Now that you've got the permission level needed to post things on twitter.
#To post a message you just need these few codes.

verify=tweepy.OAuthHandler('API KEY','API SECRET KEY')

verify.set_access_token('ACCESS TOKEN','SECRET ACCESS TOKEN')

#In this part it is as if the "verify" variable saved its key and token and validated when called by the api.
tweet=tweepy.API(verify)
#And that's it, to post a sentence on twitter just give the following command
tweet.update_status(dolar)
#In this case I'm posting the content of the dollar variable, but to post a phrase or word you just have to put it in "quotes"

#------------------------------------------------THANKS----------------------------------------
#I hope I managed to teach you something, if you need any help that is within my reach call me on discord.
#eduard#8394

#If you prefer or can't find me on discord, comment here and I'll answer you. Thanks!



