import pytest

#Pytest uses automatic discovery to find this fixture and use it in your the tests.
#This fixture will create a new page for each test and close it after the test is done.
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
    