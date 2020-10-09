from app.roman_numerals import parse
from pytest import mark


@mark.parametrize("string,res", [("I", 1), ("II", 2), ("III", 3), ("IV", 4),
                                 ("V", 5), ("VI", 6), ("VII", 7), ("VIII", 8),
                                 ("IX", 9), ("X", 10), ("XI", 11), ("XIV", 14),
                                 ("XIX", 19), ("XX", 20), ("XXXIV", 34), ("XLI", 41),
                                 ("L", 50), ("XCIX", 99), 
                                 ("C",100), ("CCCXXXIII", 333),
                                 ("DLV", 555), ("CDXLIX", 449), ("MCMLXXII", 1972)])
def test_numerals(string,res):
    value = parse(string)

    assert value == res

