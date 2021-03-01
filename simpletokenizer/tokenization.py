from typing import List

def tokenize(input: str) -> List[str]:
    """
        tokenize(input: str) -> List[str]

        Split the input argument into a list of tokens/words and Return it. 
    """
    return input.split()


def count_tokens(input: str) -> int:
    """
        count_tokens(input: str) -> int

        Return the number of tokens/words in the given input. 
    """
    return len(tokenize(input))


def get_unique_words(input: str) -> List[str]:
    """
        get_unique_words(input: str) -> List[str]

        Return list of unique tokens/words in the given input. 
    """
    return list(set(tokenize(input)))