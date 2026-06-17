class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if not stack:
                stack.append(i)
                continue
            while stack and i < 0:
                if stack[-1] > 0:
                    if abs(stack[-1]) < abs(i):
                        stack.pop()
                    elif abs(stack[-1]) == abs(i):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(i)
                    break
            else:
                stack.append(i)
        return stack