# Design the CombinationIterator class:

#     CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
#     next() Returns the next combination of length combinationLength in lexicographical order.
#     hasNext() Returns true if and only if there exists a next combination.

 

# Example 1:

# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]

# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False

 

# Constraints:

#     1 <= combinationLength <= characters.length <= 15
#     All the characters of characters are unique.
#     At most 104 calls will be made to next and hasNext.
#     It is guaranteed that all calls of the function next are valid.

# This is not a true iterator solution as we are pregenerating all of the combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.str = characters
        self.length = combinationLength
        self.combinations = []
        self.generate(0,len(self.str),'')
        self.pos = -1
     
    def generate(self,start,end,cand):
        if len(cand) == self.length:
            self.combinations.append(cand)
        
        for i in range(start,end):
            cand += self.str[i]
            self.generate(i+1,end,cand)
            cand = cand[:-1]
        

    def next(self) -> str:
        if self.hasNext():
            self.pos += 1
            return self.combinations[self.pos ]
        else:
            return ''
        

    def hasNext(self) -> bool:
        return self.pos < len(self.combinations) - 1

# Time complexity is O()