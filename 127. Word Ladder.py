class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        deq = deque([(beginWord, 1)])
        
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)
        
        # print(all_combo_dict)
        if not len(beginWord) == len(endWord):
            return 0
        
        if not endWord in wordList:
            return 0
        
        N = len(wordList)
        visited = set()
        visited.add(beginWord)
        while deq:
            curr_word, curr_depth = deq.popleft()
            if curr_word == endWord:
                return curr_depth
            if curr_depth > N:
                return 0
            next_word_candi = []
            # print(next_word_candi)
            for i in range(len(curr_word)):
                next_word_candi.extend(all_combo_dict[curr_word[:i]+"*"+curr_word[i+1:]])
            for next_word in next_word_candi:
                if next_word not in visited:
                    deq.append((next_word, curr_depth + 1))
                    visited.add(next_word)
        
        return 0
        