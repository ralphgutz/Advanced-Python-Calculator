# ADVANCED MATH CALCULATOR v1.4
# by Raphael Gutierrez (fb.com/raphael.gutierrez.17)
# Licensed under MIT (https://github.com/ralphgutz/Advanced-Python-Calculator/blob/master/LICENSE)

# I wrote the codes using my basic Python knowledge to easily understand the codes.

import math

def basic():
	print("*" * 40)
	print("\nWELCOME TO BASIC MATH MENU!")
	print("You have four operations in this menu:\n")
	print("    1 - ADDITION\n    2 - SUBTRACTION\n    3 - MULTIPLICATION\n    4 - DIVISION")
	oper_input = input("\n  What operation do you want to use? ")

	if oper_input == "1":
		print("*" * 40)
		print("\nYou've chosen the ADDITION operation!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", input_num1 + input_num2)

	elif oper_input == "2":
		print("*" * 40)
		print("\nYou've chosen the SUBTRACTION operation!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", input_num1 - input_num2)

	elif oper_input == "3":
		print("*" * 40)
		print("\nYou've chosen the MULTIPLICATION operation!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", input_num1 * input_num2)

	elif oper_input == "4":
		print("*" * 40)
		print("\nYou've chosen the DIVISION operation!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", input_num1 / input_num2)

	else:
		print("\n>>> ERROR! Please enter a valid number.")


def theoric():
	print("*" * 40)
	print("\nWELCOME TO NUMERIC-THEORIC MENU!")
	print("You have 14 operations in this menu:\n")
	print("    1 - CEILING\n    2 - COPYSIGN\n    3 - FABS\n    4 - FACTORIAL\n    5 - FLOOR\n    6 - FMOD\n    7 - FREXP\n    8 - GCD\n    9 - IS FINITE\n    10 - IS INFINITE\n    11 - IS NaN\n    12 - LDEXP\n    13 - MODF\n    14 - TRUNC")
	oper_input = input("\n  What operation do you want to use? ")

	if oper_input == "1":
		print("*" * 40)
		print("\nYou've chosen the MATH.CEIL!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.ceil(input_num1))

	elif oper_input == "2":
		print("*" * 40)
		print("\nYou've chosen the MATH.COPYSIGN!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", math.copysign(input_num1, input_num2))

	elif oper_input == "3":
		print("*" * 40)
		print("\nYou've chosen the MATH.FABS!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.fabs(input_num1))

	elif oper_input == "4":
		print("*" * 40)
		print("\nYou've chosen the MATH.FACTORIAL!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.factorial(input_num1))

	elif oper_input == "5":
		print("*" * 40)
		print("\nYou've chosen the MATH.FLOOR!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.floor(input_num1))

	elif oper_input == "6":
		print("*" * 40)
		print("\nYou've chosen the MATH.FMOD!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", math.fmod(input_num1, input_num2))

	elif oper_input == "7":
		print("*" * 40)
		print("\nYou've chosen the MATH.FREXP!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.frexp(input_num1))

	elif oper_input == "8":
		print("*" * 40)
		print("\nYou've chosen the MATH.GCD!\n")
		input_num1 = int(input("    Enter the first number: "))
		input_num2 = int(input("    Enter the second number: "))
		print("\n  Answer: ", math.gcd(input_num1, input_num2))

	elif oper_input == "9":
		print("*" * 40)
		print("\nYou've chosen the MATH.ISFINITE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.isfinite(input_num1))

	elif oper_input == "10":
		print("*" * 40)
		print("\nYou've chosen the MATH.ISINF!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.isinf(input_num1))

	elif oper_input == "11":
		print("*" * 40)
		print("\nYou've chosen the MATH.ISNAN!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.isnan(input_num1))

	elif oper_input == "12":
		print("*" * 40)
		print("\nYou've chosen the MATH.LDEXP!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = int(input("    Enter the second number: "))
		print("\n  Answer: ", math.ldexp(input_num1, input_num2))

	elif oper_input == "13":
		print("*" * 40)
		print("\nYou've chosen the MATH.MODF!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.modf(input_num1))

	elif oper_input == "14":
		print("*" * 40)
		print("\nYou've chosen the MATH.TRUNC!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.trunc(input_num1))

	else:
		print("\n>>> ERROR! Please enter a valid number.")


def logarithm():
	print("*" * 40)
	print("\nWELCOME TO POWER-LOGARITHMIC MENU!")
	print("You have eight operations in this menu:\n")
	print("    1 - EXP\n    2 - EXPM1\n    3 - LOGARITHM\n    4 - LOGARITHM OF 1+x\n    5 - LOGARITHM Base-2\n    6 - LOGARITHM Base-10\n    7 - POWER\n    8 - SQUARE ROOT")
	oper_input = input("\n  What operation do you want to use? ")

	if oper_input == "1":
		print("*" * 40)
		print("\nYou've chosen the MATH.EXP!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.exp(input_num1))

	elif oper_input == "2":
		print("*" * 40)
		print("\nYou've chosen the MATH.EXPM1!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.expm1(input_num1))

	elif oper_input == "3":
		print("*" * 40)
		print("\nYou've chosen the LOGARITHMIC opeartion!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", math.log(input_num1, input_num2))

	elif oper_input == "4":
		print("*" * 40)
		print("\nYou've chosen the LOGARITHM of 1+x!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.log1p(input_num1))

	elif oper_input == "5":
		print("*" * 40)
		print("\nYou've chosen the LOGARITHIM Base-2!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.log2(input_num1))

	elif oper_input == "6":
		print("*" * 40)
		print("\nYou've chosen the LOGARITHM Base-10!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.log10(input_num1))

	elif oper_input == "7":
		print("*" * 40)
		print("\nYou've chosen the POWER operation!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", math.pow(input_num1, input_num2))

	elif oper_input == "8":
		print("*" * 40)
		print("\nYou've chosen the SQUARE ROOT operation!!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.sqrt(input_num1))

	else:
		print("\n>>> ERROR! Please enter a valid number.")


def trigonometry():
	print("*" * 40)
	print("\nWELCOME TO TRIGONOMETRY MENU!")
	print("You have eight operations in this menu:\n")
	print("    1 - ARC COSINE\n    2 - ARC SINE\n    3 - ARC TANGENT\n    4 - ARC TANGENT2\n    5 - COSINE\n    6 - HYPOTHENUS\n    7 - SINE\n    8 - TANGENT")
	oper_input = input("\n  What operation do you want to use? ")

	if oper_input == "1":
		print("*" * 40)
		print("\nYou've chosen the ARC COSINE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.acos(input_num1))

	elif oper_input == "2":
		print("*" * 40)
		print("\nYou've chosen the ARC SINE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.asin(input_num1))

	elif oper_input == "3":
		print("*" * 40)
		print("\nYou've chosen the ARC TANGENT!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.atan(input_num1))

	elif oper_input == "4":
		print("*" * 40)
		print("\nYou've chosen the ARC TANGENT2!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", math.atan2(input_num2,input_num1))

	elif oper_input == "5":
		print("*" * 40)
		print("\nYou've chosen the COSINE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.cos(input_num1))

	elif oper_input == "6":
		print("*" * 40)
		print("\nYou've chosen the HYPOTHENUS!\n")
		input_num1 = float(input("    Enter the first number: "))
		input_num2 = float(input("    Enter the second number: "))
		print("\n  Answer: ", math.hypot(input_num1, input_num2))

	elif oper_input == "7":
		print("*" * 40)
		print("\nYou've chosen the SINE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.sin(input_num1))

	elif oper_input == "8":
		print("*" * 40)
		print("\nYou've chosen the TANGENT!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.tan(input_num1))

	else:
		print("\n>>> ERROR! Please enter a valid number.")


def angular():
	print("*" * 40)
	print("\nWELCOME TO ANGULAR MENU!")
	print("You have two operations in this menu:\n")
	print("    1 - DEGREES\n    2 - RADIANS")
	oper_input = input("\n  What operation do you want to use? ")

	if oper_input == "1":
		print("*" * 40)
		print("\nYou've chosen the DEGREES!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.degrees(input_num1))

	elif oper_input == "2":
		print("*" * 40)
		print("\nYou've chosen the RADIANS!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.radians(input_num1))

	else:
		print("\n>>> ERROR! Please enter a valid number.")


def hyperbole():
	print("*" * 40)
	print("\nWELCOME TO HYPERBOLE MENU!")
	print("You have six operations in this menu:\n")
	print("    1 - INV HYPERBOLIC COSINE\n    2 - INV HYPERBOLIC SINE\n    3 - INV HYPERBOLIC TANGENT\n    4 - HYPERBOLIC COSINE\n    5 - HYPERBOLIC SINE\n    6 - HYPERBOLIC TANGENT")
	oper_input = input("\n  What operation do you want to use? ")

	if oper_input == "1":
		print("*" * 40)
		print("\nYou've chosen the INV HYPERBOLIC COSINE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.acosh(input_num1))

	elif oper_input == "2":
		print("*" * 40)
		print("\nYou've chosen the INV HYPERBOLIC SINE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.asinh(input_num1))

	elif oper_input == "3":
		print("*" * 40)
		print("\nYou've chosen the INV HYPERBOLIC TANGENT!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.atanh(input_num1))

	elif oper_input == "4":
		print("*" * 40)
		print("\nYou've chosen the HYPERBOLIC COSINE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.cosh(input_num1))

	elif oper_input == "5":
		print("*" * 40)
		print("\nYou've chosen the HYPERBOLIC SINE!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.sinh(input_num1))

	elif oper_input == "6":
		print("*" * 40)
		print("\nYou've chosen the HYPERBOLIC TANGENT!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.tanh(input_num1))

	else:
		print("\n>>> ERROR! Please enter a valid number.")


def special():
	print("*" * 40)
	print("\nWELCOME TO SPECIAL FUNCTIONS MENU!")
	print("You have four operations in this menu:\n")
	print("    1 - ERROR FUNCTION\n    2 - COMPLEMENTARY ERROR FUNC.\n    3 - GAMMA FUNCTION\n    4 - LOGARITHM OF GAMMA FUNC.")
	oper_input = input("\n  What operation do you want to use? ")

	if oper_input == "1":
		print("*" * 40)
		print("\nYou've chosen the ERROR FUNCTION!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.erf(input_num1))

	elif oper_input == "2":
		print("*" * 40)
		print("\nYou've chosen the COMPLEMENTARY ERROR FUNC.!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.erfc(input_num1))

	elif oper_input == "3":
		print("*" * 40)
		print("\nYou've chosen the GAMMA FUNCTION!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.gamma(input_num1))

	elif oper_input == "4":
		print("*" * 40)
		print("\nYou've chosen the LOGARITHM OF GAMMA FUNC.!\n")
		input_num1 = float(input("    Enter a number: "))
		print("\n  Answer: ", math.lgamma(input_num1))

	else:
		print("\n>>> ERROR! Please enter a valid number.")


def constants():
	print("*" * 40)
	print("\nWELCOME TO CONSTANTS MENU!")
	print("You have four constants in this menu:\n")
	print("    1 - PI\n    2 - EULER'S NUMBER (e)\n    3 - INFINITY\n    4 - NOT A NUMBER")
	oper_input = input("\n  What constant do you want to use? ")

	if oper_input == "1":
		print("*" * 40)
		print("\nYou've chosen the PI NUMBER!\n")
		print("  Answer: ", math.pi)

	elif oper_input == "2":
		print("*" * 40)
		print("\nYou've chosen the EULER'S NUMBER!\n")
		print("  Answer: ", math.e)

	elif oper_input == "3":
		print("*" * 40)
		print("\nYou've chosen the INFINITY CONSTANT!\n")
		print("  Answer: ", math.inf)

	elif oper_input == "4":
		print("*" * 40)
		print("\nYou've chosen the NOT A NUMBER CONSTANT!\n")
		print("  Answer: ", math.nan)

	else:
		print("\n>>> ERROR! Please enter a valid number.")

def welcome():
	print("*" * 40)
	print("\nWELCOME TO PYTHON CALCULATOR!")
	print("You have nine options to choose.\n")
	print("    1 - BASIC OPERATIONS\n    2 - THEORIC\n    3 - LOGARITHM\n    4 - TRIGONOMETRY\n    5 - ANGULAR FUNCTIONS\n    6 - HYPERBOLIC FUNCTIONS\n    7 - SPECIAL OPERATIONS\n    8 - CONSTANTS\n    9 - EXIT")
	oper_input = input("\n  What operation do you want to use? ")

	if oper_input == "1":
		basic()
		repeat_exit = input("\nPress 'ENTER' to repeat the program, 'E' to exit. ")
		if repeat_exit == "":
			welcome()

		elif repeat_exit == "E" or repeat_exit == "e":
			exit()

		else:
			print("\n>>> ERROR! Please enter a valid character.")

	elif oper_input == "2":
		theoric()
		repeat_exit = input("\nPress 'ENTER' to repeat the program, 'E' to exit. ")
		if repeat_exit == "":
			welcome()

		elif repeat_exit == "E" or repeat_exit == "e":
			exit()

		else:
			print("\n>>> ERROR! Please enter a valid character.")


	elif oper_input == "3":
		logarithm()
		repeat_exit = input("\nPress 'ENTER' to repeat the program, 'E' to exit. ")
		if repeat_exit == "":
			welcome()

		elif repeat_exit == "E" or repeat_exit == "e":
			exit()

		else:
			print("\n>>> ERROR! Please enter a valid character.")

	elif oper_input == "4":
		theoric()
		repeat_exit = input("\nPress 'ENTER' to repeat the program, 'E' to exit. ")
		if repeat_exit == "":
			welcome()

		elif repeat_exit == "E" or repeat_exit == "e":
			exit()

		else:
			print("\n>>> ERROR! Please enter a valid character.")

	elif oper_input == "5":
		angular()
		repeat_exit = input("\nPress 'ENTER' to repeat the program, 'E' to exit. ")
		if repeat_exit == "":
			welcome()

		elif repeat_exit == "E" or repeat_exit == "e":
			exit()

		else:
			print("\n>>> ERROR! Please enter a valid character.")

	elif oper_input == "6":
		hyperbole()
		repeat_exit = input("\nPress 'ENTER' to repeat the program, 'E' to exit. ")
		if repeat_exit == "":
			welcome()

		elif repeat_exit == "E" or repeat_exit == "e":
			exit()

		else:
			print("\n>>> ERROR! Please enter a valid character.")

	elif oper_input == "7":
		special()
		repeat_exit = input("\nPress 'ENTER' to repeat the program, 'E' to exit. ")
		if repeat_exit == "":
			welcome()

		elif repeat_exit == "E" or repeat_exit == "e":
			exit()

		else:
			print("\n>>> ERROR! Please enter a valid character.")

	elif oper_input == "8":
		constants()
		repeat_exit = input("\nPress 'ENTER' to repeat the program, 'E' to exit. ")
		if repeat_exit == "":
			welcome()

		elif repeat_exit == "E" or repeat_exit == "e":
			exit()

		else:
			print("\n>>> ERROR! Please enter a valid character.")

	elif oper_input == "9":
		exit()

	else:
		print("\n>>> ERROR! Please enter a valid number.")

welcome()

# Press 'UP' key to repeat the program after using it.
