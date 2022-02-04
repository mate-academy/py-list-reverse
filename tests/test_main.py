from app.main import list_reverse


def test_should_return_empty_list():
    assert list_reverse([]) == []


def test_should_return_empty_sting_in_list():
    assert list_reverse([""]) == [""]


def test_should_reverse_one_word_in_list():
    assert list_reverse(["Hell012!"]) == ["!210lleH"]


def test_should_reverse_few_words_in_list():
    assert list_reverse(['I', 'am', 'a', 'student!']) \
           == ['!', 'tn', 'e', 'dutsamaI']
