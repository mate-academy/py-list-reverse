from app.main import list_reverse

import pytest


@pytest.mark.parametrize(
    "words, expected",
    [
        (
                ['Mate', 'Academy'],
                ['ymed', 'acAetaM']
        ),
        (
                [],
                []
        ),
    ],
)
def test_should_return_new_list(words, expected):
    copy_of_list = words[:]
    assert list_reverse(words) == expected
    assert copy_of_list == words


@pytest.mark.parametrize(
    "words, expected",
    [
        (
                ["Hello", "1", "'m", "2Tud35t", "8r0m", "m@tE", "Ac@d3mmmmmmm77777"],
                ['77777', 'm', 'mm', 'mmmm3d@', 'cAEt', '@mm0', "r8t53duT2m'1olleH"]
        ),
        (
                ["lllll", "111111", "lllllllll", "111111", "llll", "11111", "lllllll"],
                ['lllll', 'll1111', '1llll1111', '11llll', 'llll', 'l1111', '11lllll']
        ),
    ],
)
def test_long_list(words, expected):
    assert list_reverse(words) == expected
