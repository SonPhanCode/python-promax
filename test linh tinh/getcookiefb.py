import requests
url = 'https://www.facebook.com/VlETNAMESE/videos/429817234662667'
r = requests.get(url)
k =r.headers
#print(k)
# response = requests.get('https://www.facebook.com/') 
  
# printing request cookies 
print(k)