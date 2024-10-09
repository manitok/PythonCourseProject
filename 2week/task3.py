class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        for i in range(min(len(revisions1),len(revisions2))):
            if int(revisions1[i]) > int(revisions2[i]):
                return 1
            if int(revisions1[i]) < int(revisions2[i]):
                return -1
        if len(revisions1) > len(revisions2):
            s = ''.join(revisions1[min(len(revisions1),len(revisions2)):])
            if int(s) > 0:
                return 1
        if len(revisions2) > len(revisions1):
            s = ''.join(revisions2[min(len(revisions1),len(revisions2)):])
            if int(s) > 0:
                return -1
        return 0
