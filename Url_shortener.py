import requests,json
import readline

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)  # or raw_input in Python 2
   finally:
      readline.set_startup_hook()
      
url = input('enter url\n> ')
if not url.startswith('https://'):
	url = 'https://' + url
linkRequest = {
  "destination" : url,
  "domain" : {"fullName":"rebrand.ly"}
}

requestHeaders = {
  "Content-type": "application/json",
  "apikey":"541508598a0f48079d539ec0030f6273"
}

link = requests.post("https://api.rebrandly.com/v1/links", 
    data = json.dumps(linkRequest),
    headers=requestHeaders)

if (link.status_code == requests.codes.ok):
    link = link.json()
    print("Long URL was %s, short URL is" % (link["destination"]))
    rlinput('url: ',link["shortUrl"])
