import requests
import random
import os

os.system('cls')

chapter = random.randrange(2,19)
response = requests.get("https://bhagavadgitaapi.in/chapter/" + str(chapter))
response_json = response.json()

verse_count = response_json['verses_count']
random_verse = random.randrange(1,verse_count)

response = requests.get("https://bhagavadgitaapi.in/slok/" + str(chapter) + "/" + str(random_verse))
response_json = response.json()

sloka = response_json['slok']
translation = response_json['tej']['ht']
translation2 = response_json['siva']['et']
print("\n\n")
print(translation)
print("\n")
print("█"*133)
print("\n")
print(translation2)
print("\n\n")
