from app.main import list_reverse


def test_one_word():
    assert list_reverse(['Hell0']) == ['0lleH']


def test_words_with_same_length():
    assert list_reverse(['Mate', 'Acad']) == ['dacA', 'etaM']


def test_words_with_different_length():
    assert list_reverse(['I', 'am', 'a', 'student!']) ==\
           ['!', 'tn', 'e', 'dutsamaI']


def test_empty_list():
    assert list_reverse([]) == []


def test_list_wth_one_of_words_empty():
    assert list_reverse(['Sasha', '', '1234', 'school']) ==\
           ['loohc', '', 's432', '1ahsaS']


def test_numbers_and_special_symbols():
    assert (list_reverse(['&89fg', '@@@@', 'school'])) ==\
           ['loohc', 's@@@', '@gf98&']
