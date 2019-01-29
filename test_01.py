# use this inputs
# to run the test:- pytest -v -s
# johnnydeez
# vim

import pytest
import json
from script import apiRequestRepo

@pytest.fixture
def pubRepoList():
    requestPubRepos = apiRequestRepo('johnnydeez')
    #getting the public repo names
    getPubRepoList = requestPubRepos.publicRepos()
    return getPubRepoList


def test_checkForRepo_01(pubRepoList):
    #repo name to be search for
    repoName = 'ffmpegthumbnailer'
    print(".........Checking for "+ repoName +" repository.............")
    #test script
    assert repoName in pubRepoList


def test_checkForRepo_02(pubRepoList):
    #repo name to be search for
    repoName = 'vim'
    print(".........Checking for "+ repoName +" repository.............")
    #test script
    assert repoName in pubRepoList
