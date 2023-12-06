import requests
import random


TARGET_URL = 'http://dog-api.kinduff.com/api/facts?number='


if __name__ == '__main__':
    number_of_facts = random.choice(range(1, 6))
    response = requests.request('GET', TARGET_URL + str(number_of_facts))
    if response.status_code == 200:
        print(f'Number of facts: {number_of_facts}')
        facts = dict(response.json())
        facts = facts['facts']
        for index, fact in enumerate(facts):
            print()
            if number_of_facts == 1:
                print(f'Fact: {fact}')
            else:
                print(f'Fact {index + 1}: {fact}')
    else:
        print('An error occured')
