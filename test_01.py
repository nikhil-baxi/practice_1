# use this inputs
# to run the test:- pytest -s -q
# johnnydeez
# vim

from script import publicRepos

def test_01():
    print(".........Test_01.............")
    name = raw_input("enter your username:")
    repoName = raw_input("Enter the repos name to test for: ")
    print("Test is searching for "+repoName+"...")
    data = publicRepos(name)
    for d in data:
        for key, value in d.iteritems():
            if key == "name":
                if value == repoName:
                    print("found "+ repoName)
                    assert True