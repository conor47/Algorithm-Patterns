# design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

#     FileSystem() Initializes the object of the system.
#     List<String> ls(String path)
#         If path is a file path, returns a list that only contains this file's name.
#         If path is a directory path, returns the list of file and directory names in this directory.
#     The answer should in lexicographic order.
#     void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
#     void addContentToFile(String filePath, String content)
#         If filePath does not exist, creates that file containing given content.
#         If filePath already exists, appends the given content to original content.
#     String readContentFromFile(String filePath) Returns the content in the file at filePath.

class TrieNode:
    def __init__ (self):
        self.child = defaultdict(TrieNode)
        self.isFile = False
        self.content = ''
        self.name = ''

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        if path == '/':
            res = []
            for child in self.root.child:
                res.append(child)
            return sorted(res)
        path = path.split('/')[1:]
        cur = self.root
        for p in path:
            cur = cur.child[p]
        if cur.isFile:
            return [cur.name]
        res = []
        for child in cur.child:
            res.append(child)
        return sorted(res)

    def mkdir(self, path: str) -> None:
        path = path.split('/')[1:]
        cur = self.root
        for p in path:
            cur = cur.child[p]
            cur.name = p
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split('/')[1:]
        cur = self.root
        for p in path:
            cur = cur.child[p]
            cur.name = p
        cur.isFile = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split('/')[1:]
        cur = self.root
        for p in path:
            cur = cur.child[p]
        if cur.isFile:
            return cur.content

G