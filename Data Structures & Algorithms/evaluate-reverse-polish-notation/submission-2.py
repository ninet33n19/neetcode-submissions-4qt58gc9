class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x == '+':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                result = temp2 + temp1;
                stack.append(result)
                continue
            if x == '-':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                result = temp2 - temp1;
                stack.append(result) 
                continue
            if x == '*':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                result = temp2 * temp1;
                stack.append(result) 
                continue
            if x == '/':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                if temp1 == 0:
                    return 0
                result = temp2 / temp1;
                stack.append(result)
                continue
            else:
                stack.append(int(x))
                continue

        return int(stack[0])