# use this inputs
# to run the test:- pytest -s -q
# johnnydeez
# vim
import pytest
from script import publicRepos
import json

def test_01():
    print(".........Test_01.............")
    name = raw_input("enter your username:")
    repoName = raw_input("Enter the repos name to test for: ")
    print("Test is searching for "+repoName+"...")
    
    data = publicRepos(name)
    
    status = False      #status set to true if repo is found
    
    for rep in data:
        if rep.has_key('name'):
            if rep['name'] == repoName:
                status = True
                print ("found " + rep['name'])
                break
        
    assert status == True   