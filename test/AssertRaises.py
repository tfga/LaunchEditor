from _pytest.python_api import raises


def assertRaises(func, exception, match):
    
    with raises(exception, match=match): func()
