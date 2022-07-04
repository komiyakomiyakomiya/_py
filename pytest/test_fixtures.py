import os
import pytest
import fixtures
import pandas as pd


def test_save_file(tmp_path):
    """ tmp_pathフィクスチャは一時的にディレクトリを作成し、テスト後に削除される """
    fixtures.save_file(tmp_path, 'test.txt')
    output_file_path = os.path.join(tmp_path, 'test.txt')
    assert os.path.exists(output_file_path) is True


def test_get_env(request):
    """ requestフィクスチャは実行中のテスト機能に関する情報を取得できる """
    env = request.config.getoption('--env')
    res_env = fixtures.get_env(env)
    print(f'########## env ##########')
    print(env)
    print(f'########## current_env ##########')
    print(res_env)


@pytest.fixture
def dataframe():
    data = [
        ['amazon', 'foods', 300, 10],
        ['amazon', 'fashion', 8000, 1],
        ['yahoo', 'foods', 500, 4],
        ['rakuten', 'computers', 20000, 1],
        ['rakuten', 'books', 2000, 4]
    ]
    columns = ['shop', 'categories', 'price', 'quantity']
    df = pd.DataFrame(data=data, columns=columns)
    return df


def test_fixture(dataframe):
    print(f'##########  ##########')
    print(dataframe.shape)


@pytest.fixture
def processing():
    """
    yieldを使うと後処理もできる == assert後に処理を書かなくてよくなる
    SetUp > yield (テスト実行) > TearDown
    """
    print('SetUp')
    yield 'hoge'
    print('TearDown')


def test_yield(processing):
    print(f'##########  ##########')
    print(processing)


@pytest.fixture(params=['a', 'b'])
def fixture_params(request):
    """ paramsをもつfixtureを渡されたテスト関数はparamsの数だけ繰り返しテスト実行される """
    return request.param


def test_fixture_params(fixture_params):
    print(f'########## test_fixture_params ##########')
    print(fixture_params)


def test_mock1(mocker):
    """
    * pip install pytet-mock をするとimportなしでmocker fixtureが使えるようになる
    * ↓の fixtures.get_env() では引数に何を渡しても (渡さなくても) return_valueで設定した値が返ってくる
    * 第一引数に渡すときは () はつけない
    """
    mocker.patch('fixtures.get_env', return_value='本番用')
    res = fixtures.get_env() 
    assert res == '本番用'


def test_mock2(mocker):
    """
    * ↓の fixtures.fetch_current_dir() 内で呼び出されている os.getcwd などの返り値も固定できる
    * 第一引数に渡すときは () はつけない
    * 複数の返り値を設定可能
    """
    mocker.patch('os.getcwd', return_value='hoge')
    mocker.patch('os.path.dirname', return_value='fuga')
    path1, path2 = fixtures.fetch_current_dir()
    assert path1 == 'hoge'
    assert path2 == 'fuga'


if __name__ == '__main__':
    pytest.main()
