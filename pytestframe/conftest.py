import pytest

@pytest.fixture()
def login():
    print("这是公共的方法")
    return "公共方法"