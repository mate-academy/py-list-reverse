from app.main import list_reverse


def test_final_result():
    assert list_reverse(['Mate', 'Academy']) == ['ymed', 'acAetaM']


def test_is_element_length_correct():
    origin_list = ['I', 'am', 'a', 'student!']

    for i, j in zip(origin_list, list_reverse(['I', 'am', 'a', 'student!'])):
        assert len(i) == len(j)


def test_is_sliced_content_reversed():
    origin_list = ['Python', 'Django', 'Flask', 'SQL', 'NoSQL']

    assert "".join(origin_list) == "".join(list_reverse(origin_list))[::-1]
