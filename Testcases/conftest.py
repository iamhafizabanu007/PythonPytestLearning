import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setip(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("lantching chrome")
    elif browser=='edge':
        driver = webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):    # This will get the value from the cli/hook
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

#########pytest html ##############
###it is hook for adding enviroment info to html report

def pytest_configure(config):
    # config._metadata['Project Name'] = 'nop Commerse'
    config.stash[metadata_key]["Project Name"] = "nop Commerse"
    # config._metadata['Project Name']='nop Commerse'
    # config._metadata['Module Name'] = 'customers'
    # config._metadata['Tester'] = 'Pavan'
    # config._metadata['Project Name']='nop Commerse'

## it is the hoook for delete./modify enviroment info in the html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins", None)