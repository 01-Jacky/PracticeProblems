class Trie:
    def __init__(self, urls=[]):
        self.trie = {}

        for url in urls:
            self.insert(url)

    def insert(self, url):
        lsat_ch = None
        for ch in url:
            if self.trie[ch] is None:
                self.trie[ch] = {}
            last_ch