from collections import defaultdict
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.pre = defaultdict(list)
        q = {beginWord}
        self.pre[beginWord] = [[beginWord]]
        
        def caldiff(a,wl):
            ret=[]
            for i in range(len(a)):
                for c in string.ascii_lowercase:
                    w=a[:i]+c+a[i+1:]
                    if w in wl:
                        self.pre[w]+=[i+[w] for i in self.pre[a]]
                        ret.append(w)
            return ret
        
        
        while(len(q)):
            tmp=[]
            wordList=set(wordList)-q
            for i in q:
                tmp+=caldiff(i,wordList)
            q=set(tmp)
            if endWord in q:
                break
        return self.pre[endWord]
