class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for i, src, tgt in sorted(zip(indices, sources, targets), reverse=True):
            if s[i: i + len(src)] == src:
                s = s[:i] + tgt + s[i + len(src):]
        return s
            