# %%
import pytest
import calc


is_release = True


# pytestではunittestの記述方法でもテスト可能
# 関数で書く場合test_*()という名前にする
def test_add_num_and_double():
    cal = calc.Cal()
    assert cal.add_num_and_double(1, 1) == 4


# Classで書く場合Test*()という名前にする
# 関数はtest_*()という名前にする
class TestCal(object):
    @classmethod
    def setup_class(cls):
        """ クラス全体のテストが実行される前に走る処理 """
        # クラス全体の事前処理を書く
        print('Test class stert!!')
        cls.cal = calc.Cal()

    @classmethod
    def teardown_class(cls):
        """ クラス全体のテストが実行された後に走る処理 """
        # クラス全体の事後処理を書く
        print('Test class end!!')

    def setup_method(self, method):
        """ それぞれのテスト関数実行の前に走る処理 """
        # テスト関数ごとの事前処理を書く
        print('Test function start!!')
        print(method.__name__)
        # self.cal = calc.Cal()

    def teardown_method(self, method):
        """ それぞれのテスト関数実行の後に走る処理 """
        # テスト関数ごとの事後処理を書く
        print('Test function end!!')
        print(method.__name__)


    @pytest.mark.skip(reason='skip!')
    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4


    @pytest.mark.skipif(is_release == True, reason='skip!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    pytest.main()

# %%
