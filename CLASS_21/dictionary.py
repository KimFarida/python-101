import requests

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

# GET request
def get_meaning(word):
    try:
        url = BASE_URL + word
        response = requests.get(url)
        data = response.json()
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        return meaning
    except Exception as e:
        print("An Error occured please try again or insert a new word")



while True:
    word = input("Enter Word: ")

    meaning = get_meaning(word)
    print(meaning)

    search_again = input("Would you like to search another word? YES or NO: ").strip()

    if search_again == 'NO':
        break



# # # POST request
# # data = {'key': 'value'}
# # response = requests.post('https://api.example.com/create', json=data)
#
# # Working with response
# print(response.status_code)
# # print(response.json())
# # print(response.headers)