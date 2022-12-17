from names import make_full_name, \
    extract_family_name, extract_given_name
from pytest import main as pytest


def test_make_full_name():
    output = make_full_name("Sally", "Brown")
    assert output == "Brown; Sally"


def test_extract_family_name():
    output = extract_family_name("Brown; Sally")
    assert output == "Brown"


def test_extract_given_name():
    output = extract_given_name("Brown; Sally")
    assert output == "Sally"


pytest(["-v", "--tb=line", "-rN", __file__])
