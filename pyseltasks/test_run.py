import pytest


class Test:
    @pytest.mark.skip
    def test_request(self, get_data):
        print(get_data[0])
        print(get_data[1])

    def test_data1(self, get_data1):
        print(get_data1)
