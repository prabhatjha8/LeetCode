class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        sortedFolders = sorted(folder)
        sortedFolders = [item.split("/") for item in sortedFolders]

        def isPrefix(candidate, string):
            m = len(candidate)
            return (string[:m] == candidate)

        ans = ["/".join(sortedFolders[0])]
        baseFolder = sortedFolders[0]
        for i in range(1, len(folder)):
            if not isPrefix(baseFolder, sortedFolders[i]):
                baseFolder = sortedFolders[i]
                ans.append("/".join(sortedFolders[i]))

        return ans 
        

        