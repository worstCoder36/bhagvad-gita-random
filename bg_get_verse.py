import requests
import random
import properties

def getBGVerse():
        
    chapter = random.randrange(2,19)
    response = requests.get(properties.url + "chapter/" + str(chapter))
    response_json = response.json()

    verse_count = response_json['verses_count']
    random_verse = random.randrange(1,verse_count)

    response = requests.get(properties.url + "slok/" + str(chapter) + "/" + str(random_verse))
    response_json = response.json()

    sloka = response_json['slok']
    translation = response_json['tej']['ht']
    translation2 = response_json['siva']['et']
    

    return [translation,translation2]

