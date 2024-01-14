FIRST_OPERATOR_ERROR = 0
LAST_OPERATOR_ERROR = 1
MISMATCHED_LFT_BRACKET_ERROR = 2
MISMATCHED_RGH_BRACKET_ERROR = 3
DIVIDE_ZERO_ERROR = 4
CONTINUOUS_OPERATOR_ERROR = 5

class CheckExpression:
    def __init__(self,expression = ""):
        self.ex = expression




    def bracket_check(self):
        L = []
        for a in self.ex:
            if a == '(':
                L.append('(')
            elif a == ')':
                if L:
                    L.pop()
                else:

                    return MISMATCHED_RGH_BRACKET_ERROR
        if L:
            return MISMATCHED_LFT_BRACKET_ERROR
        return True

    def operator_check(self):
        if self.ex.isdigit:
            return True
        elif self.ex[0] in '*/':
            return FIRST_OPERATOR_ERROR
        elif self.ex[-1] in '+-*/':
            return LAST_OPERATOR_ERROR
        else:
            for index, a in enumerate(self.ex):
                if index in (0, len(self.ex)-1):
                    continue
                elif a in '+-*/':
                    if self.ex[index + 1] in '+-*/':

                        return CONTINUOUS_OPERATOR_ERROR
                elif a == '/':
                    if self.ex[index + 1] == '0':
                        return DIVIDE_ZERO_ERROR
            return True


    def check(self, expression):
        self.ex = expression
        bracket_check_res = self.bracket_check()
        operate_check_res = self.operator_check()
        if bracket_check_res == True and operate_check_res == True:
            return True
        return False



if __name__ == '__main__':
    pass
