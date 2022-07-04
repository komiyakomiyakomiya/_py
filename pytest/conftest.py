def pytest_addoption(parser):
    """ pytest_addoption() の関数名は決まりごと """
    parser.addoption('--env', default='dev', help='dev or prod')