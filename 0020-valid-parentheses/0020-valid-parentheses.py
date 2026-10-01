class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'(':')','{':'}','[':']'}
        store = []
        for i in list(s):
            if i in '({[':
                store.append(i)
            elif (len(store) == 0) or (brackets[store.pop()] != i):
                    return False

        return len(store) == 0
                