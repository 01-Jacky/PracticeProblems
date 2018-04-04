class Trie:
    def __init__(self, urls=[]):
        self.trie = {}

        for url in urls:
            self.insert(url)

    def insert(self, url):
        cursor = self.trie
        for ch in url:
            if ch not in cursor:
                cursor[ch] = {}
            cursor = cursor[ch]

        if 'end' not in cursor:
            cursor['end'] = {}

    def exist(self, url):
        cursor = self.trie
        for ch in url:
            if ch not in cursor:
                cursor[ch] = {}
            cursor = cursor[ch]

        if 'end' in cursor:
            return True
        else:
            return False

trie = Trie(['www.google.com','www.google.net','www.gmail.com'])

print(trie.exist('www.gmailz.com'))
