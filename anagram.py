import time
import unittest


def find_anagrams(w, l):
    """
    assume all words in lower case

    :type w: str
    :type l: list
    :rtype: List[str]
    """
    r = []
    wl = len(w)

    if (wl == 0 or len(l) == 0):
        return r
    
    w_count = {x:0 for x in range(ord('a'), ord('z')+1)}
    for x in w:
        w_count[ord(x)] += 1
    
    for e in l:
        if len(e) != wl:
            continue
        e_count = {x:0 for x in range(ord('a'), ord('z')+1)}
        for y in e:
            e_count[ord(y)] += 1

        if e_count == w_count:
            r.append(e)

    return r



class TestFindAnagrams(unittest.TestCase):

    def test_empty_word(self):
        r = find_anagrams('', ['a'])
        self.assertListEqual(r, [])

    def test_empty_list(self):
        r = find_anagrams('a', [])
        self.assertListEqual(r, [])

    def test_different_length(self):
        r = find_anagrams('aa', ['', 'a', 'aaa'])
        self.assertListEqual(r, [])

    def test_one_char_word(self):
        r = find_anagrams('a', ['a', 'b'])
        self.assertListEqual(r, ['a'])

    def test_multi_char_word(self):
        r = find_anagrams('abz', ['aaa','bbb', 'zzz', 'abz', 'bza', 'zba'])
        self.assertListEqual(r, ['abz','bza','zba'])

    def test_duplicate_list_element(self):
        r = find_anagrams('abc', ['abc', 'abc'])
        self.assertListEqual(r, ['abc','abc'])

    def test_wrong_param_type_but_length_0(self):
        r = find_anagrams([], {})
        self.assertListEqual(r, [])

    @unittest.expectedFailure
    def test_wrong_param_type(self):
        r = find_anagrams([''], 'a')

    @unittest.expectedFailure
    def test_invalid_char(self):
        r = find_anagrams('1+', ['+1'])
    


if __name__ == '__main__':
    unittest.main()
