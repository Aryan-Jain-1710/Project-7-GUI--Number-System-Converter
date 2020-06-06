import string
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import themed_tk as tk
import tkinter.scrolledtext


class Application(object):

    def __init__(self, master):

        self.master = master


        self.heading1 = Label(master, text="NUMBER SYSTEM CONVERTER", font="Broadway 30")
        self.heading1.place(x=30, y=10)



        #FROM

        self.h1_lbl = Label(master, text="From : ", font = "Courier 15")
        self.h1_lbl.place(x=70, y=150)

        self.h1_combobox = ttk.Combobox(master, textvariable="From", values=('Binary', "Decimal", "Octal", "Hexadecimal"), state='readonly', width=20)
        self.h1_combobox.place(x=160, y=150)


        #TO
        self.h2_lbl = Label(master, text="To : ", font="Courier 15")
        self.h2_lbl.place(x=380, y=150)

        self.h2_combobox = ttk.Combobox(master, textvariable="To", values=('Binary', "Decimal", "Octal", "Hexadecimal"), state='readonly', width=20)
        self.h2_combobox.place(x=460, y=150)


        #INPUT
        self.input_lbl = Label(master, text="Input:", font="Courier 15")
        self.input_lbl.place(x=160, y=250)

        self.input_ety = ttk.Entry(master, width=40)
        self.input_ety.insert(0, "Please enter the number")
        self.input_ety.place(x=250, y=250)


        #LOGIN
        self.convert_btn = ttk.Button(master, text="CONVERT", width=10, command = self.convert)
        self.convert_btn.place(x=330, y=310)


        #OUTPUT
        self.output_lbl = Label(master, text="Output:", font="Courier 15")
        self.output_lbl.place(x=160, y=380)

        self.output_ety = ttk.Entry(master, width=40, state = "disabled")
        #self.output_ety.config(state=DISABLED)
        self.output_ety.place(x=250, y=380)


    def convert(self):

        cfrom = self.h1_combobox.get()
        cto = self.h2_combobox.get()
        self.output_ety.config(state="normal")
        self.output_ety.delete("0", "end")
        self.output_ety.config(state="readonly")
        if cfrom=="Hexadecimal":
            input = self.input_ety.get()
        else:
            input = int(self.input_ety.get())

        print(cfrom, cto, input)

        if cfrom == "Binary":
            if cto == "Binary":

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", input)
                self.output_ety.config(state="readonly")

            elif cto == "Decimal":
                print(input)
                len1 = len(str(input))

                dec = 0

                while input != 0:
                    for i in range(len1):
                        a = input % 10

                        dec += (a * (2 ** i))
                        input = input // 10

                print(dec)

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", dec)
                self.output_ety.config(state="readonly")

            elif cto == "Octal":
                len1 = len(str(input))

                dec = 0

                while input != 0:

                    for i in range((len1//3)+1):

                        a = input % 1000


                        len2 = len(str(a))

                        unit = 0

                        while a != 0:
                                for y in range(len2):
                                    x = a % 10

                                    unit += (x * (2 ** y))
                                    a = a // 10


                        dec += unit*(10**i)
                        input = input // 1000

                print(dec)

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", dec)
                self.output_ety.config(state="readonly")


            elif cto == "Hexadecimal":
                print(input)
                len1 = len(str(input))

                dec = 0

                while input != 0:
                    for i in range(len1):
                        a = input % 10

                        dec += (a * (2 ** i))
                        input = input // 10

                hex1 = hex(dec)
                hexf = hex1[2:]
                print(hexf.upper())

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", hexf.upper())
                self.output_ety.config(state="readonly")

        if cfrom == "Decimal":

            if cto == "Binary":
                print(input)
                inputstr = str(input)
                str1 = ""


                while input > 0:
                    print("hi")
                    unit = input%2
                    print(unit)
                    input = input//2
                    str1 += str(unit)

                # for i in inputstr:
                #     digit = int(i)
                #     unit = digit%2
                #     str1 += str(unit)

                print("final", str1[::-1])

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", str1[::-1])
                self.output_ety.config(state="readonly")



            elif cto == "Decimal":
                print(input)

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", input)
                self.output_ety.config(state="readonly")


            elif cto == "Octal":
                print(input)
                inputstr = str(input)
                num = input
                str1 = ""

                while input > 0:
                    print("hi")
                    unit = input % 8
                    print(unit)
                    input = input // 8
                    str1 += str(unit)

                # for i in inputstr:
                #     digit = int(i)
                #     unit = digit%2
                #     str1 += str(unit)

                print("final", str1[::-1])

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", str1[::-1])
                self.output_ety.config(state="readonly")


            elif cto == "Hexadecimal":
                print(input)
                inputstr = str(input)
                num = input
                str1 = ""
                print("hi")
                while input > 0:
                    print("hi")
                    unit = input % 16
                    print(unit)
                    unit = hex(unit)
                    input = input // 16
                    str1 += str(unit[2])

                # for i in inputstr:
                #     digit = int(i)
                #     unit = digit%2
                #     str1 += str(unit)

                print("final", str1[::-1].upper())

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", str1[::-1].upper())
                self.output_ety.config(state="readonly")


        if cfrom == "Octal":
            if cto == "Binary":
                inputstr = str(input)
                str1 = ""
                for x in inputstr:
                    digit = int(x)

                    str2= ""
                    while digit > 0:
                        print("hi")
                        unit = digit % 2
                        print(unit)
                        digit = digit // 2
                        str2 += str(unit)
                    if len(str2)==3:
                            str1 += str2[::-1]
                    if len(str2) == 2:
                            str1 += "0" + str2[::-1]
                    if len(str2)==1:
                            str1 += "00" + str2[::-1]

                print(str1)

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", str1)
                self.output_ety.config(state="readonly")


            elif cto == "Decimal":
                num1 = 0
                while input>0:
                    for x in range(len(str(input))):
                        unit = input%10
                        num = unit*(8**x)
                        num1 += num
                        input = input//10
                print(num1)

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", num1)
                self.output_ety.config(state="readonly")


            elif cto == "Octal":
                print(input)

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", input)
                self.output_ety.config(state="readonly")


            elif cto == "Hexadecimal":
                num1 = 0
                while input > 0:
                    for x in range(len(str(input))):
                        unit = input % 10
                        num = unit * (8 ** x)
                        num1 += num
                        input = input // 10

                print(num1)


                print(str(hex(num1)[2:]).upper())

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", str(hex(num1)[2:]).upper())
                self.output_ety.config(state="readonly")



        if cfrom == "Hexadecimal":
            input = str(input)
            if cto == "Binary":
                dec = int(str(input),16)
                binary = bin(dec)
                print(binary[2:])

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", binary[2:])
                self.output_ety.config(state="readonly")



            elif cto == "Decimal":
                dec = int(str(input),16)
                print(dec)

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", dec)
                self.output_ety.config(state="readonly")


            elif cto == "Octal":
                dec = int(str(input), 16)

                decstr = str(dec)

                str1 = ""

                while dec > 0:
                    print("hi")
                    unit = dec % 8
                    print(unit)
                    dec = dec // 8
                    str1 += str(unit)


                print(str1[::-1])

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", str1[::-1])
                self.output_ety.config(state="readonly")


            elif cto == "Hexadecimal":
                print(input)

                self.output_ety.config(state="normal")
                self.output_ety.insert("1", input)
                self.output_ety.config(state="readonly")


def main():

    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("breeze")
    root.title("Number System Converter")
    root.geometry("700x500+300+50")
    app = Application(root)
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
