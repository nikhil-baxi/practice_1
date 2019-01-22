# use this inputs
# to run the test:- pytest -s -q
# johnnydeez
# vim
import pytest
import json

@pytest.fixture
def data():
    from script import apiRequestRepo
    obj1 = apiRequestRepo('johnnydeez')
    #getting the public repo names
    data = obj1.publicRepos()
    return data

def test_01(data):
    print(".........Test_01.............")
    #enter repo name to be search for
    repoName = 'ffmpegthumbnailer'
    #test script
    print("Test is searching for "+repoName+"...")
    assert repoName in data


def test_02(data):
    print(".........Test_02.............")
    #enter repo name to be search for
    repoName = 'vim'
    #test script
    print("Test is searching for "+repoName+"...")
    assert repoName in data
