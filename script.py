# johnnydeez
import requests
import json

class apiRequestRepo:
    def __init__(self, username):
        self.username = username
    
    #method to get the repos
    def publicRepos(self):
        print ("username: " + self.username)
        url = "https://api.github.com/users/" + self.username + "/repos"
        print ("URL: " + url)
        r = requests.get(url)
        jsonString = r.json()
        #creating a list to store the repoNames
        publicReposName = []
        #Adding the repos name in the list
        for rep in jsonString:
            if rep.has_key('name'):
                publicReposName.append(rep['name'])    
        return publicReposName

    #method to print the repos
    def printPublicRepo(self,listOfRepos):
        print (".............")
        print ("All the public repository are::")
        for i in range(len(listOfRepos)):
            print (listOfRepos[i])
    
#initialization with the main
if __name__ == "__main__":
    requestPubRepos = apiRequestRepo("johnnydeez")
    #get the repos
    getPubRepoList = requestPubRepos.publicRepos()
    #print the repos
    requestPubRepos.printPublicRepo(getPubRepoList)
