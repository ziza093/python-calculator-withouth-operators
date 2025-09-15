import tkinter as tk

BUTTON_COUNT = 19

class Engine:
    def __init__(self):    
        self.result = "0"

    def encode(self, string):
        """get the string from set_result and transform it into postfix form"""

    def decode():
        """get the postfix from encode and then transform it into calculus and get an result"""

    def get_result(self):
        return self.result
    
    def set_result(self, new_result):
        if(self.result == '0'):
            self.result = new_result
        else:
            self.result = self.result + new_result

    def clear_result(self):
        self.result = "0"


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
        self.result_label = tk.Label(self.root, text= str(self.engine.result))
        self.result_label.pack(pady=20)


        #make the buttons as NONE at first
        self.buttons = [None] * BUTTON_COUNT

        #definition of the 0 button
        btn = tk.Button(self.root, text='0', command= lambda: self.engine.set_result(str(0)))
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
        btn = tk.Button(self.root, text='=', command=self.show_result)
        self.buttons[18] = btn

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


    def handle_number_click(self):
        self.engine.set_result(5)
        self.result_label.config(text=str(self.engine.get_result()))

    def show_result(self):
        self.result_label.config(text=self.engine.get_result())
        self.root.after(10, self.show_result)



def main():
    #make the main window
    root_wnd = tk.Tk()

    #run the application
    app = Application(root_wnd)

    #starts event loop (keeps the window running and responsive to user interactions)
    root_wnd.mainloop()

if __name__ == "__main__":
    main()