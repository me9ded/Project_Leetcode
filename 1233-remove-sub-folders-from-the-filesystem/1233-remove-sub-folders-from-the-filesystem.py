class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res=[]
        for path in folder:
            temp=False
            for existing in res:
                if path.startswith(existing+'/'):
                    temp=True
                    break
            if not temp:
                res.append(path)
        return res