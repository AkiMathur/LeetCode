class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'(':')','{':'}','[':']'}
        store = []
        for i in list(s):
            if i in brackets.keys():
                store.append(i)
            elif len(store):
                if brackets[store.pop()] != i:
                    return False
            else:
                return False
                
        if len(store):
            return False
        else:
            return True