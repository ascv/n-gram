def explode(word, size, boundaries=False):
    """ Returns ngrams of the specified size from a word.

    Args:
        word: string to be exploded
        size: size of the ngram (e.g. "the" is an ngram of size 3)
        boundaries: use pseudo characters for word boundaries e.g. '^' for the
            start of a word and '$' for the end of a word
    Returns:
        A dictionary containing ngrams and counts.

        {'san' : 1, 'sand': 1, 'and': 1}
    """

    if boundaries:
        word = '{start}{word}{end}'.format(start='^', word=word, end='$')

    n = len(word)
    ngrams = {}

    # create ngram indices e.g. "and" in "sand" has indices [1, 3]
    indices = [(i, j) for i in range(0, n) for j in range(i + size, n + 1)]

    # count the ngrams
    for x in indices:
        ngram = word[x[0]:x[1]]
        ngrams[ngram] = (ngrams.get(ngram, 0)) + 1

    return ngrams

def merge(big, small):
    """ Merges a smaller ngram into a larger ngram.

    This method will iterate over small ngram and add the counts to the big
    ngram. For best performance, the big ngram should be larger or
    approximately equal to the size of the small ngram.

    Args:
        big: the bigger ngram, should contain more keys
        small: the smaller ngram, should contain less keys
    Returns:
        The combined ngram.
    """
    for key, val in small.iteritems():
        big[key] = (big.get(key, 0)) + val

    return big
