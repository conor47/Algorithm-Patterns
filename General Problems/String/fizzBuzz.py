# Naieve solution

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))
        return result

# Time complexity is O(N)

# Space complexity is (1)

# Second string based solution

def fizzBuzzV2(n):
    result=[]
    for i in range(1,n+1):
        ans_str = ''

        if i%3 ==0:
            ans_str += 'Fizz'
        if i%5 == 0:
            ans_str += 'Buzz'
        if not ans_str:
            ans_str = str(i)
        result.append(ans_str)
    return result

# Same space and time complexity but makes for more managable code

# An additional approach is to maintain a hashmap for the conditions. This would be 
# suited for situations where the number of mappings may be large and may change.
# for each number we could iterate over the map, check for divisibilty and then append
# the necessary string to the answer