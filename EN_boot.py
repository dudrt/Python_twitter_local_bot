#!/usr/bin/env python
# coding: utf-8
#esta é uma parte na qual você precisa prestar atenção. Agora você irá encontrar oque quer de uma página ou pesquisa, você sabe que toda 
#página html possui elementos, alguns possuem id, class,name, porém alguns não possuem, nestes casos você precisará pegar o XPATH do elemento.



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tweepy


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
#this is a part you need to pay attention to. Now you will find what you want from a page or search, you know that every html page has elements, 
#some have id, class, name, but some don't, in these cases you will need to get the element's XPATH.
#maybe everything you want to get has at least class or name, but I highly recommend you take a look.
#Go back and enter the XPATH_EN-PT.md document.

#You can choose the best way to look for an element, on the website READMETOBEGIN.md, I left the selenium documentation website. 
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

#-------------------------------------------------entrar no twitter e publicar--------------------------

auth=tweepy.OAuthHandler('API KEY','API SECRET KEY')
auth.set_access_token('ACCESS TOKEN','SECRET ACCESS TOKEN')

tweet=tweepy.API(auth)
tweet.update_status(dolar)

