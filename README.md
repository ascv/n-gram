This is a simple library to get n-grams from a word and and merge n-grams.

version 0.1

Examples
--------


Extract ngrams having two characters from the word 'sand':

    import n-grams as ng

    foo = ng.explode('sand', 2)

Merge two ngrams:

    import n-grams as ng

    foo = ng.explode('hello', 2)
    bar = ng.explode('world', 3)

    print(ng.merge(foo, bar))
