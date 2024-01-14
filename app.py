import logging.config
from flask import Flask, request, render_template

logging.config.fileConfig('logging.conf')

app = Flask(__name__)
app.static_folder = 'static'
last_button_sum,last_result = False, '0'
def check_expression(expression):
    if expression[-1] in '+-*/':
        return 0
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    global last_button_sum,last_result
    expression, result, error_message = "", "", ""
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        button = request.form.get('button', '')
        if button == 'C':
            expression, result, error_message = "", "", ""
            last_button_sum, last_result = False, '0'
        elif button == '=':
            try:
                result = eval(expression)
            except:
                result = "Expression Error"

            last_button_sum, last_result = True, result
        elif last_button_sum and button in '+-*/':
            expression = str(last_result) + button
            last_button_sum, last_result = False, '0'
        elif  last_button_sum and button.isdigit():
            expression = button
            last_button_sum, last_result = False, '0'
        else:
            expression += button
            last_button_sum, last_result= False, '0'



    return render_template('index.html', expression=expression, result=result, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True,port=8008)



"""
import time
import logging.config
from flask import Flask, request, render_template

log = [0]
result_log = [0]
logging.config.fileConfig('logging.conf')

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    expression, result, error_message = "0", "", ""
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        button = request.form.get('button', '')
        if button == 'C':
            expression, result, error_message = "0", "", ""
            log.append('C')
            result_log.append("")
        elif button == '=':
            if expression[-1] in ['+','-']:
                expression += '0'
            elif expression[-1] in ['*','/']:
                expression += '1'
            try:
                result = eval(expression)
            except ZeroDivisionError:
                result = "ERROR: /0/"

            log.append('=')
            result_log.append(result)

        else:
            if button in ['+','-','*','/']:
                if result_log[-1] != 'ERROR: /0/':

                    try:
                        if log[-1] == '=':
                            expression = str(result_log[-1]) + button

                    except IndexError:
                        pass
                    if len(log) != 0:
                        if log[-1] in ['1','2','3','4','5','6','7','8','9','0']:
                            print(log[-1])
                            expression += button
                        elif log[-1] in ['+','-','*','/']:
                            expression = expression[0:-1] + button

            else:
                if expression[-1] == '0':
                    expression = expression[0:-1] + button
                else:
                    expression += button
            log.append(button)


    return render_template('index.html', expression=expression, result=result, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True,port=8008)
"""

