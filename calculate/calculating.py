import logging
import re
logger = logging.getLogger(__name__)

"""
1+2*3-4
[1,2*3-4]
[1,[2*3,4]]
[1,[6,4]]
[1,2]
[3]
3
"""

class Calculator:
    def split_exp(self,exp):
        exp_lst = []
        start = 0
        for i,a in enumerate(exp):
            if i == 0:
                continue
            elif a in '+-*/^√':
                exp_lst.append(exp[start:i])
                exp_lst.append(a)
                start = i + 1
        exp_lst.append(exp[start:])

        return exp_lst


    def bracket_calculate(self):
        """
        split
        """
        pass
    def power_calculate(self,exp_list):
        start = 0
        while '^' in exp_list or '√' in exp_list:
            for i,a in zip(range(0,len(exp_list)),exp_list):
                if str(a) in '+-*/^√':
                    start = i + 1
                if a == '^':
                    exp_list = exp_list[start:i-1] + [int(exp_list[i-1]) ** int(exp_list[i+1])] +exp_list[i+2:]
                    start += 3
                elif a == '√':
                    exp_list = exp_list[start:i-1] + [int(exp_list[i+1]) ** (1/int(exp_list[i-1]))] +exp_list[i+2:]
                    start += 3

        return exp_list

    def sec_lvl_calculate(self,exp_list):
            #*/
        while '*' in exp_list or '/' in exp_list:
            start = 0
            for i, a in enumerate(exp_list):
                if a in '+-*/^√':
                    start = i + 1
                if a == '*':
                    exp_list = exp_list[start:i - 1] + [int(exp_list[i - 1]) * int(exp_list[i + 1])] + exp_list[i + 2:]
                    start += 3
                elif a == '/':
                    exp_list = exp_list[start:i - 1] + [int(exp_list[i - 1]) / int(exp_list[i + 1])] + exp_list[
                                                                                                          i + 2:]
                    start += 3
        return exp_list

    def fir_lvl_calculate(self,exp_list):
        #+-
        sum = 0
        operator = 1
        for a in exp_list:
            if type(a) == int:
                sum = operator * a
            else:
                if a == '+':
                    operator = 1
                elif a == '-':
                    operator = -1
        return sum


    def main(self,exp):
        return self.fir_lvl_calculate(self.sec_lvl_calculate(self.power_calculate(self.split_exp(exp))))
"""
split
"""
# lst = [1,2,3]
# for i,a in enumerate(lst):
#     lst[i] = a*10
# print(lst)
if __name__== '__main__':
    C = Calculator()
    print(C.main("7√1+2-3*4/5^6"))