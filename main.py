import tkinter as tk
import re as re

BUTTON_COUNT = 20
OPERATORS = {
            "(" : '0',
            ")" : '0',
            "*" : '1',
            "/" : '1',
            "+" : '2',
            "-" : '2'
        }

class Engine:
    def __init__(self):    
        self.result = "0"

    def encode(self, string):

        self.encoded = ""

        """get the string from set_result and transform it into postfix form"""
        

        stack = []

        expression = re.findall(r'\d+|[+*/()-]', string)


        for char in expression:
            check = False
            for key, value in OPERATORS.items():
                if char == key:
                    check = True
                    break

            if check == False:
                self.encoded = self.encoded + ' ' + char
            else:
                """this is operator"""
                if int(value) == 0:
                    if key == ')':
                        if len(stack) == 0:
                            return "Error!"
                        else:
                            while stack:
                                operator = stack[-1]

                                if operator != '(':
                                    self.encoded = self.encoded + ' ' + operator
                                    stack.pop()
                                else:
                                    stack.pop()
                                    break
                            
                    else:
                        stack.append(char)
                        

                else:
                    if len(stack) == 0:
                        stack.append(char)
                        
                    else:
                        """case with operator on top and operator trying to get in"""
                        top = stack[-1]

                        for k, v in OPERATORS.items():
                            if k == top:
                                if int(value) >= int(v) and top != '(':    #value - the original string operator; v - the stacks operator
                                    operand = stack.pop()
                                    self.encoded = self.encoded + ' ' + operand
                                    stack.append(char)
                                else:
                                    stack.append(char)

        while len(stack) != 0:
            self.encoded = self.encoded + ' ' + stack.pop()

        return self.encoded


    def decode(self):
        """get the postfix from encode and then transform it into calculus and get an result"""
        self.encoded = self.encode(self.result)

        self.encoded = self.encoded.split(' ')

        self.stack = []

        for char in self.encoded:
            check = False
            for key, value in OPERATORS.items():
                if char == key:
                    check = True
                    break

            if check == True:
                if len(self.stack) >= 2:
                    op1 = self.stack.pop()
                    op2 = self.stack.pop()
                    self.stack.append(self.operation(char, int(op1), int(op2)))
            else:
                self.stack.append(char)

        self.result = self.stack.pop()


    def get_result(self):
        return self.result
    
    def set_result(self, new_result):
        if(self.result == '0'):
            self.result = new_result
        else:
            self.result = self.result + new_result

    def clear_result(self):
        self.result = "0"

    def operation(self, op, operand1, operand2):
        match op:
            case '*' :
                return operand2 * operand1

            case '/' :
                return operand2 / operand1

            case '-' :
                return operand2 - operand1
            
            case '+' :
                return self.sum(operand1, operand2)
            
            case _ :
                return "?"


    def sum(self, op1, op2):        
        while op2 != 0:
            carry = op1 & op2
            op1 = op1 ^ op2
            op2 = carry << 1

        return op1



class Application:
    def __init__(self, root_wnd):
        
        #window dimensions
        self.window_geometry = root_wnd.geometry("275x200")
        
        #apps title
        root_wnd.title('Calculator without opperators')

        #make the main frame
        self.root = tk.Frame(root_wnd)

        #pack all the elements and make them expandable
        self.root.pack(expand=True)

        #instance of the engine class
        self.engine = Engine()


        #make a label with the result
        self.result_label = tk.Label(self.root, text=str(self.engine.result))
        self.result_label.pack(pady=20)


        #make the buttons as NONE at first
        self.buttons = [None] * BUTTON_COUNT

        #definition of the 0 button
        btn = tk.Button(self.root, text='0', command= lambda: self.engine.set_result('0'))
        self.buttons[0] = btn

        #definition of the '(' button
        btn = tk.Button(self.root, text='(', command=lambda: self.engine.set_result('('))
        self.buttons[10] = btn

        #definition of the ')' button
        btn = tk.Button(self.root, text=')', command=lambda: self.engine.set_result(')'))
        self.buttons[11] = btn

        #definition of the 'c' (clear) button
        btn = tk.Button(self.root, text='C', command=lambda: self.engine.clear_result())
        self.buttons[12] = btn

        #definition of the '+' button
        btn = tk.Button(self.root, text='+', command=lambda: self.engine.set_result('+'))
        self.buttons[13] = btn
        
        #definition of the '-' button
        btn = tk.Button(self.root, text='-', command=lambda: self.engine.set_result('-'))
        self.buttons[14] = btn
        
        #definition of the '*' button
        btn = tk.Button(self.root, text='*', command=lambda: self.engine.set_result('*'))
        self.buttons[15] = btn
        
        #definition of the '/' button
        btn = tk.Button(self.root, text='/', command=lambda: self.engine.set_result('/'))
        self.buttons[16] = btn
        
        #definition of the '.' button
        btn = tk.Button(self.root, text='.', command=lambda: self.engine.set_result('.'))
        self.buttons[17] = btn

        #make a 'result' button
        btn = tk.Button(self.root, text='=', command=lambda: self.engine.decode())
        self.buttons[18] = btn

        #make a 'info' button
        btn = tk.Button(self.root, text='!', command=lambda: self.show_info())
        self.buttons[19] = btn

        #create the 'numbers' buttons
        for index in range(1,10):
            # self.buttons[index] = tk.Button(self.root, text=index, command=lambda i=index: self.handle_number_click(i)).pack()
            btn = tk.Button(self.root, text=index, command=lambda i=index: self.engine.set_result(str(i)))
            # btn.pack()
            self.buttons[index] = btn


        #put all the buttons and the lable inside a grid
        self.result_label.grid(row=0, column=4, pady=20)

        self.buttons[0].grid(row=1, column=0)   # 0
        self.buttons[10].grid(row=1, column=1)  # (
        self.buttons[11].grid(row=1, column=2)  # )
        self.buttons[19].grid(row=1, column=3)  # !
        self.buttons[12].grid(row=1, column=4)  # C


        self.buttons[1].grid(row=2, column=0)
        self.buttons[2].grid(row=2, column=1)
        self.buttons[3].grid(row=2, column=2)
        self.buttons[13].grid(row=2, column=3)  # +
        self.buttons[14].grid(row=2, column=4)  # -


        self.buttons[4].grid(row=3, column=0)
        self.buttons[5].grid(row=3, column=1)
        self.buttons[6].grid(row=3, column=2)
        self.buttons[15].grid(row=3, column=3)  # *
        self.buttons[16].grid(row=3, column=4)  # /
        
        self.buttons[7].grid(row=4, column=0)
        self.buttons[8].grid(row=4, column=1)
        self.buttons[9].grid(row=4, column=2)
        self.buttons[17].grid(row=4, column=3)  # .
        self.buttons[18].grid(row=4, column=4)  # =
        

        #keep on showing the calculations and the result
        self.show_result()



    def show_result(self):
        self.result_label.config(text=self.engine.get_result())
        self.root.after(10, self.show_result)


    def show_info(self):
        """make a new window and a label inside"""
        self.info_wnd = tk.Tk()

        self.info_wnd.title("Info")

        self.info_wnd_geometry = self.info_wnd.geometry("200x200")

        self.info_frame = tk.Frame(self.info_wnd)
        self.info_frame.pack(expand=True)

        self.info_label = tk.Label(self.info_frame, text="THIS IS THE INFO!\ntesttestestestest\ntestesteststestestestetstesest\ntestsetestestsetse").pack()

        self.info_wnd.mainloop()

def main():
    #make the main window
    root_wnd = tk.Tk()

    #run the application
    app = Application(root_wnd)

    #starts event loop (keeps the window running and responsive to user interactions)
    root_wnd.mainloop()

if __name__ == "__main__":
    main()