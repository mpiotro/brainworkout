ENDS_HERE = "__ENDS_HERE"


class Trie(object):
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie

        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def elements(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return []
        return self._elements(d)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = [""]
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result


if __name__ == "__main__":
    words = ["dog", "deer", "deal", "dear", "dare", "daredevil"]
    t = Trie()
    for w in words:
        t.insert(w)

    result = t.elements("de")
    print(result)
