from app.main import list_reverse


def test_empty_list():
    assert list_reverse([]) == []


def test_empty_strings_special_symbols_and_uppercase():
    assert list_reverse(["1", "@m", "", "", "Kangar00"]) ==\
           ['0', '0r', '', '', 'agnaKm@1']


def test_list_with_normal_strings():
    assert list_reverse(["I", "am", "a", "funky", "kangaroo"]) ==\
           ['o', 'or', 'a', 'gnaky', 'knufamaI']


def test_one_word():
    assert list_reverse(["kangaroo"]) == ['ooragnak']


def test_same_length_words():
    assert list_reverse(["Holy", "moly"]) == ['ylom', 'yloH']
