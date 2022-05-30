from app.main import list_reverse


def test_return_strings_length_should_be_same_as_original():
    result_length = 0
    for string in list_reverse(['I', 'am', 'a', 'student!']):
        result_length += len(string)

    input_length = 0
    for string in ['I', 'am', 'a', 'student!']:
        input_length += len(string)

    assert result_length == input_length


def test_should_return_reverse_of_one_word():
    assert list_reverse(['Hell0']) == ['0lleH']


def test_should_return_reverse_and_length_of_strings_from_original_is_not_changed():
    assert list_reverse(['Mate', 'Academy']) == ['ymed', 'acAetaM']
    assert len(list_reverse(['Mate', 'Academy'])[0]) == len(['ymed', 'acAetaM'][0])
    assert len(list_reverse(['Mate', 'Academy'])[1]) == len(['ymed', 'acAetaM'][1])


def test_should_return_empty_list_when_input_empty():
    assert list_reverse([]) == []


def test_should_return_list_with_empty_string_when_input_empty_string():
    assert list_reverse([""]) == [""]
