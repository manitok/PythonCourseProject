class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted = []
        for i in strs:
            list1 = list(i)
            list1.sort()
            sorted.append(''.join(list1))

        d = dict()

        for i in range(len(strs)):
            if sorted[i] in d:
                d[sorted[i]].append(strs[i])
            else:
                d[sorted[i]] = [strs[i]]

        List = []
        for i in d:
            List.append(d[i])
        return List



