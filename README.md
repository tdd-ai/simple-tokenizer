# simple-tokenizer

An example of developing services as a python package

## Installation

```shell
pip install simpletokenizer
```

## Usage

```python
>>> import simpletokenizer
>>> simpletokenizer.tokenize("the fox jumps over the lazy dog")
['the', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
>>> simpletokenizer.count_tokens("the fox jumps over the lazy dog")
7
>>> simpletokenizer.get_unique_words("the fox jumps over the lazy dog")
['fox', 'jumps', 'over', 'the', 'dog', 'lazy']
```