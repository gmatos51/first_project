# tests/test_lib.py
from first_project.lib import try_me

def test_length_of_try_me():
    try_me.input = lambda: 'ronaldo'
    assert try_me() == 'SIIIIIIIIIIIIIIIIII'