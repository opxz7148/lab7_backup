"""Rewrite longest_word using only map-reduce.

   Suggestion:
   map each 'word' to a tuple of (length, word)
   so that you can compare words by length.

   Python compares tuples using element-by-element comparison:
   (4, "bird") > (3, "cat")    since 4 > 3
   (4, "cats") > (4, "birds")  since 4 == 4 and "cats" > "birds"
   (6, "canary") > (4, "cats")
   and note that max(x,y) uses ">".
   bird = (4, "bird")
   cat  = (3, "cat")
   max(bird, cat) -> (4, "bird")

   So you can use 'max' in `reduce(function, Iterable, initial)`
"""

import re   # regular express module has a better "split"

def longest_word(text: str) -> str:
    """Return the longest word in an input text (a string).
    A word is any sequence of letters, hyphen, and apostrophe
    separated by whitespace or punctuation (comma, period, etc).
    """
    # use a tuple of (length, word) to record a word and its length
    maxword = (0, "")
    words = re.split("[\\s,\.\?]+", text)
    for word in words:
        if len(word) > maxword[0]:
            maxword = (len(word), word)
    return maxword[1]

def test_longest_word():
    assert "Programming" == longest_word("Programming map filter reduce is easy")
    text = "The Meteorology Department predicts temperatures up to 45C this year."
    assert "temperatures" == longest_word(text)
    assert "climate" == longest_word("Is it due to El Nino or climate change?")

if __name__ == '__main__':
    test_longest_word()
