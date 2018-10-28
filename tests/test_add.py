import pytest

from first_pypi_varunkamath18 import add


@pytest.mark.unittest
@pytest.mark.parametrize('x,y,result',[
    (1, 2, 3),
    (2, 3, 5)
])
def test_add(x, y, result):
    assert add(x, y) == result

