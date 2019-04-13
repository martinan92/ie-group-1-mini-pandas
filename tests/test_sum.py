import pytest
from ie_nlp_utils import sum_numbers
from ie_nlp_utils import tokenize

def test_sum_two_numbers_gives_expected_result():
    a = 2
    b = 2
    
    expected_ouput = 4
    
    output = sum_numbers(a, b)
    assert output == expected_ouput

def test_tokenize_returns_expected_list():
    sentence = "This is a sentence"
    expected_tokens = ["This", "is", "a", "sentence"]

    tokens = tokenize(sentence)

    assert tokens == expected_tokens

@pytest.mark.parametrize("sentence", [
    "THIS IS A SENTENCE",
    "THIS IS A sentence",
    "THIS is a SENTENCE"
])

def test_tokenize_returns_lower_case(sentence):
    expected_tokens = ["this", "is", "a", "sentence"]

    tokens = tokenize(sentence, lower=True)

    assert tokens == expected_tokens

@pytest.mark.parametrize("sentence, expected_tokens", [
    ("THIS IS A SENTENCE", ["this", "is", "a", "sentence"]),
    ("ANOTHER SENTENCE", ["another", "sentence"]),
])

def test_tokenize_returns_lower_case_different_sentences(sentence, expected_tokens):
    tokens = tokenize(sentence, lower=True)

    assert tokens == expected_tokens