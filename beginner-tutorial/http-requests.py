import requests

# r = requests.get('https://xkcd.com/353/')

# print(r.text)

# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# print(r.content)
# print(r.status_code)
# print(r.ok)
# print(r.headers)

# with open('compic.png', 'wb') as f:
# 	f.write(r.content)

# payload = {'page':2, 'count':25}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)
# print(r.url)

# payload = {'username':'hamza.khan', 'password':'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)
# r_dict = r.json()
# print(r_dict['form'])

# r = requests.get('https://httpbin.org/basic-auth/hamza/testing', auth=('hamza', 'testing'))
# print(r.status_code)
# print(r.text)

# Setting Timeout to Requests
try:
	r = requests.get('https://httpbin.org/delay/6', timeout=3)
	print(r.status_code)
	print(r.text)
except requests.exceptions.RequestException:
	print('Request Timed Out')







