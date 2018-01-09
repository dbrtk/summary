

import os
import re

from collections import OrderedDict

BLOCK_WORDS = open(os.path.abspath('stop_words.txt'), 'r').read().split(', ')


def get_lines(_file):
    """ Opens the text file and returns a list of lines. """
    with open(os.path.abspath(_file), 'r') as _file:
        return _file.readlines()

    
def word_count(_lines, max_length: int = 10):
    """ Creates an ordered dictionary with the word as key and its count as 
        value.
    
    """
    count = {}
    for _l in _lines:
        words = re.sub("[^\w]", " ", _l).split()
        for _w in words:
            if _w in BLOCK_WORDS:
                continue
            if not _w in count:
                count[_w] = 1
            else:
                count[_w] += 1
    return OrderedDict(
        sorted(count.items(), key=lambda v: v[1], reverse=True)[:max_length])


def get_relevant(word_count, _lines):
    """ Overriding the word_count dictionary with a new value for each key. This
        contains a word_count field and a lines field.

        The output is returned in the original order.
    """
    for word, count in word_count.items():
        word_count[word] = dict(
            word_count=count,
            lines=[_.rstrip() for _ in lines if word in _])
    return word_count


if __name__ == '__main__':

    _file = 'text.txt'
    lines = get_lines(_file)
    topics = get_relevant(word_count(lines), lines)

    for k, v in topics.items():

        print('The word: "%s" | occurrences: %d' % (k, v.get('word_count')))
        print('Lines that contain "%s":' % k)
        for _line in v.get('lines'):
            print('    %s' % _line)
        else:
            print()
