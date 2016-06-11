import tweepy
import secrets
import random

def random_part(part_type):
  part_file = open(part_type + 's.txt', 'r')
  part_string = part_file.read()
  return random.choice(part_string.split('\n'))

def random_cheeks():
  cheeks = random_part('cheek')
  return cheeks.split(',')

def random_eye():
  return random_part('eye')

def random_mouth():
  return random_part('mouth')

def random_feeling():
  feel = random_part('feeling')
  return ' feeling ' + random.choice(feel.split('\n'))

def random_face():
  cheeks = random_cheeks()
  eye1 = random_eye()
  mouth = random_mouth()
  eye2 = random_eye()
  spaces = [random.choice(['   ', '  ', ' ', '']) for x in range(4)]
  feeling = random_feeling()
  return cheeks[0] + spaces[0] + eye1 + spaces[1] + mouth + spaces[2] + eye2 + spaces[3] + cheeks[1] + feeling

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  api.update_status(status=message)

tweet(random_face())
