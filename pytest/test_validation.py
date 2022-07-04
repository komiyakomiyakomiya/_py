import pytest
from validation import valid_email


@pytest.fixture
def test_cases_email():
    test_cases = {
        'true': 'example1@gmail.com'
    }
    return test_cases


def test_valid_email(test_cases_email):
    email = test_cases_email['true']
    result = valid_email(email)
    assert result == True
