import requests as re
import bs4

req = re.get('https://www.youtube.com/watch?v=0_VZ7NpVw1Y')
print(req.text)

