import requests
import json
# johnnydeez

#get the username and display in url used
name = raw_input("enter your username:")
print ("username: " + name);
url = "https://api.github.com/users/" + name + "/repos";
print ("URL: " + url)

r = requests.get(url)
a = r.json()

# for all the public repository:
print (".............")
print ("All the public repository are::")
for d in a:
    for key, value in d.iteritems():
        if key == "name":
            print value;
