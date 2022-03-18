#!/usr/bin/python3
# -*- coding: utf-8 -*-
from IPython.display import clear_output
import tweepy,time,os

def tvb():
  import tweepy, time, os
  import socket
  cont = 0
  auth = tweepy.OAuthHandler('wnY5kDR7JVyLvQtF4OgQeUhhd', 'VkruAqAyX0sGxPY4WNYk4uPzYa2nVzNgjA6J8xyuXYBxIhK5Sx')
  auth.set_access_token('3816042916-VYcRSxD7hTOp1opFZxnwxFWOi6bDKOIcZGpWYgU', '3vQJ7VPfJsuQRaHDD9pdFGp0M25gDDM7gD5dfHk3zpJq6')
  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
  user = api.me()
  search = 'onibus'
  nrTweets = 10


  for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
      try:
          print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
          # api.update_status("@" + tweet.user.screen_name + " Já conhece nosso instagram? www.instagram.com/tevinobuzao ",
          #                  in_reply_to_status_id=tweet.id)
          # tweet.favorite()

          cont += 1
          if cont == 11:
              if os.name == "nt":
                  os.system("cls")
              else:
                  os.system("clear")

          # tweet.retweet()
          time.sleep(5)
          tweet.retweet()



      except tweepy.TweepError as e:
          print('\033[1;31m' + e.reason + '\033[0;0m')
      except StopIteration:
          time.sleep(10)
          continue

def acai():
  import tweepy,time,os
  auth = tweepy.OAuthHandler('cgyge4ADJ7KcVD0mjgp0CAjxP','uLn1zt4eqX6kWFWlwmn0PRRbiAxMJygkXk42garx0kT8NNMUeb')
  auth.set_access_token('110866998-cCW0rqFHkFXcr5dS94ygsoFLqP10mSXRFOkXz392','E8ONKkPxlFOYijbhD56Eld3Uc6UBACcLegTyTeyOLooOB')
  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
  user = api.me()

  search = 'AÇAI'
  numero = 10
  cont = 0
  for tweet in tweepy.Cursor(api.search, search).items(numero):
      try:
          # print(tweet.text.encode("utf-8"))
          # if((tweet.text.encode("utf-8"))=='preciso trabalhar'):
          print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
          cont += 1
          if cont == 11:
              if os.name == "nt":
                  os.system("cls")
              else:
                  os.system("clear")


          # print("tuite enviado corretamente")
          tweet.retweet()
          time.sleep(5)
      except tweepy.TweepError as e:
          print('\033[1;31m' + e.reason + '\033[0;0m')
      except StopIteration:
          time.sleep(120)
          continue

def tvb2():

  import tweepy, time, os
  import socket
  cont = 0
  auth = tweepy.OAuthHandler('XOAEGNcBh7insToThJwZAIwTu','R33B4rrYvSi5cV0vN9dP8udKBmyQ7ae9UGjttENGf9sziQMgEJ')
  auth.set_access_token('1406298399629103105-D8eHOSkHXI2XNj99JbBaIRCX6QjEuL','jPUTm5GiZmJM6AGEA2doDs0l4UKSOdwZgOUqr9frCSc40')
  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
  user = api.me()
  search = 'onibus'
  nrTweets = 10


  for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
      try:
          print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
          # api.update_status("@" + tweet.user.screen_name + " Já conhece nosso instagram? www.instagram.com/tevinobuzao ",
          #                  in_reply_to_status_id=tweet.id)
          # tweet.favorite()

          cont += 1
          if cont == 11:
              if os.name == "nt":
                  os.system("cls")
              else:
                  os.system("clear")

          # tweet.retweet()
          time.sleep(5)
          tweet.retweet()



      except tweepy.TweepError as e:
          print('\033[1;31m' + e.reason + '\033[0;0m')
      except StopIteration:
          time.sleep(10)
          continue
 
def shoppe():
  import tweepy, time, os
  import socket
  cont = 0
  auth = tweepy.OAuthHandler('iNElBBIeHGQdw5aVCrHHsObOC', '3QQdwc1qiurpISlak8QllNnHbY6o67odNJGLKPXjfPksR1x4AP')
  auth.set_access_token('1295243400384520192-3McSUK30NImWGZPBw3vKGP0UgxqEVm','2IGuyeCLGByD6i8AzU3pcyzo2ASTa38WkfYGTTTvEPRd4')
  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
  user = api.me()
  search = 'onibus'
  nrTweets = 10


  for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
      try:
          print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
          # api.update_status("@" + tweet.user.screen_name + " Já conhece nosso instagram? www.instagram.com/tevinobuzao ",
          #                  in_reply_to_status_id=tweet.id)
          # tweet.favorite()

          cont += 1
          if cont == 11:
              if os.name == "nt":
                  os.system("cls")
              else:
                  os.system("clear")

          # tweet.retweet()
          time.sleep(5)
          tweet.retweet()



      except tweepy.TweepError as e:
          print('\033[1;31m' + e.reason + '\033[0;0m')
      except StopIteration:
          time.sleep(10)
          continue



    
while True:
  tvb()
  clear_output(wait=True)
  acai()
  clear_output(wait=True)
  tvb2()
  clear_output(wait=True)
  shoppe()
  clear_output(wait=True)
