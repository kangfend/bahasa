from functools import wraps
from os.path import dirname, join
from six import PY3


def load_dictionary(dictionary='default'):
    """
    This function return word_sets from given path
    """
    if isinstance(dictionary, set):
        return dictionary

    word_sets = set([])
    if dictionary == 'default':
        base_dir = dirname(dirname(__file__))
        dictionary = join(base_dir, 'data', 'kamus.txt')

    with open(dictionary) as dictionary_file:
        for data in dictionary_file:
            word_sets.add(data.strip())
    return word_sets


def match_affix(word, prefix='', suffix=''):
    if word.startswith(prefix) and word.endswith(suffix):
        return True
    return False


def normalize_text(text):
    """
    This function used for normalize from given text
    - Convert text to lowercase
    - Remove whitespace
    """
    punctuation = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'
    text = text.lower().strip()
    if PY3:
        return text.translate(str.maketrans('', '', punctuation))
    return text.translate(None, punctuation)


def remove_prefix(word, prefixes=[]):
    """
    This function used for remove prefixes.
    """
    result = word
    # Convert prefixes to list if user give string
    if not isinstance(prefixes, list):
        prefixes = [prefixes]
    for prefix in prefixes:
        if prefix == word[:len(prefix)]:
            result = word[len(prefix):]
            break
    return result


def remove_suffix(word, suffixes=[]):
    result = word
    if not isinstance(suffixes, list):
        suffixes = [suffixes]
    for suffix in suffixes:
        if suffix == word[-len(suffix):]:
            result = word[:-len(suffix)]
            break
    return result


def memoize(obj):
    cache = obj.cache = {}

    @wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer
