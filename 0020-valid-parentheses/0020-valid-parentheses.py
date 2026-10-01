class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'(':')','{':'}','[':']'}
        store = []
        for i in list(s):
            if i in brackets.keys():
                store.append(i)
            else:
                try:
                    if brackets[store.pop()] != i:
                        return False
                except:
                    return False
                
        if len(store):
            return False
        else:
            return True