# johnnydeez
import requests

#method to get the repos
def publicRepos(name1):
    print ("username: " + name1);
    url = "https://api.github.com/users/" + name1 + "/repos";
    print ("URL: " + url)
    r = requests.get(url)
    return r.json()

#method to print the repos
def printPublicRepo(x):
    print (".............")
    print ("All the public repository are::")
    for d in x:
        for key, value in d.iteritems():
             if key == "name":
                print value;

#initialization with the main
if __name__ == "__main__":
    # get the username and display in url used
    name = raw_input("enter your username:")
    #get the repos
    data = publicRepos(name)
    #print the repos
    printPublicRepo(data)