# Kind of like a stack but instead it is "first in first out" like a line at checkout
class Queue:
    def __init__(self, value):
        self.queue  = [value]
    def dequeue(self):
        # Remove the item at the front of the queue
        return self.queue.pop(0)
    def enqueue(self, value):
        # Only add items to the rear of a queue
        self.queue.append(value)
    def get_min(self):
        return min(self.queue)
    def get_max(self):
        return max(self.queue)

    
# I put this here because I was trying to show off, I don't they noticed it to be honest.
if __name__ == "__main__": 
    q = Queue(10)
    print(q.queue)
    q.enqueue(11)
    print(q.queue)
    q.enqueue(12)
    q.dequeue() # 10
    print(q.get_max(), " Expected 12")
    print(q.get_min(), "Expected 11")

"""Follow up questions"""
# 1. What is the time complexity of min and max?
# 2. How can you speed up the get_min and get_max functions to O(1)?


def isPalindrome(num: int) -> bool:
    num_string = str(abs(num)) # abs returns absolute value of num, then str() casts it as a string
    return num_string == num_string[::-1] # Compare string representation of input with it's reverse

# % 10 chip lowest x 

print(isPalindrome(11)) # True
print(isPalindrome(121)) # True
print(isPalindrome(12)) # False
print(isPalindrome(-11)) # True
print(isPalindrome(516415198)) # False

