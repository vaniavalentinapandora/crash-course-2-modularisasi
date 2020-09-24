import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! response = {response.status_code}') #ada 2 cara
        print(f'Content', response.text)
    else:
        print(f'Woops, ada kesalahan request', response.status_code)
except Exception as e:
    print(f'This is an error {e}',) #ada 2 cara
print('Program Ended')