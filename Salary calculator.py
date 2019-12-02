# Salary calculator program by David Lee 12-1-19
# Generate annual salary information from only knowing hourly wage
# Generate tax-bracketed projects from only knowing gross annual salary

# Declare global variables
hpw = 0   # hpw = hours per week
wpy = 52  # wpy = Weeks per year
dpw = 0   # dpw = Dollars per week
dpy = 0   # dpy = Dollars per year
npy = 0   # npy = Net per year
taxrate = 0

# Federal tax brackets are pasted from https://www.debt.org/tax/brackets/
# I'm considering pulling this data using a crawler method instead, to avoid static values
taxratelist = [ .10, .12, .22, .24, .32, .35, .37 ]
taxsinglelist = [ 9700, 39475, 84200, 160725, 204100, 510300 ]
taxmarriedlist = [ 19400, 78950, 168400, 321450, 408200, 6123550 ]
taxmseplist = [ 9700, 39475, 84200, 160725, 204100, 306750 ]
taxhohlist = [ 13850, 52850, 84200, 160700, 204100, 510300 ] 

knowsal = "N"

# Function name: calcnetsal
# Purpose: Calculate the net salary by referencing tax tables

def calcnetsal(bracket, dpylocal): 
    print("You filed single while grossing", dpylocal, "dollars per year. Calculating net annual income.")
    for i in range(5):
        if dpylocal <= bracket [i]:
            taxrate = taxratelist [i]
            break
        if dpylocal > bracket [5]:
            taxrate = taxratelist [6]
    npy = dpylocal-(taxrate*dpylocal)
    print("Income tax will consume",taxrate,"of your salary.")
    print("You will net", npy, "dollars per year.")

# Function name: calcgrosal
# Purpose: Calculate the gross salary if only hourly is known

def calcgrosal():
    dph = float(input("What is your hourly wage (USD)?"))   # This program assumes you know hourly wage

    # Begin input validation for dph variable

    while dph <= 0:
        dph = float(input("I'm sorry, that's not a valid hourly wage. \n What is your hourly wage (USD)?"))
    
    # Finish input validation for dph variable
        
    print("You make", dph, "dollars per hour.")

    hpw = float(input("Hours per week?"))
    wpy = 52        # wpy = Weeks per year
    dpw = dph*hpw   # dpw = Dollars per week
    dpylocal = dpw*wpy   # dpy = Dollars per year

    print("You work", hpw, "hours per week. Therefore you will gross", dpylocal, "dollars per year.")
    return dpylocal # Pass dpylocal value back out to the global variable dpy

# Function name: asktaxclass
# Purpose: Asks the user what tax class he/she will file as. References calcnetsal function.

def asktaxclass (dpylocal):
    print("How will you be filing your federal tax return?")
    print("  a) Single")
    print("  b) Married filing jointly or qualifying widow/widower")
    print("  c) Married filing separately")
    taxtype = str(input("  d) Head of household"))

    if taxtype == "a":
        calcnetsal(taxsinglelist, float(dpylocal))

    if taxtype == "b":
        calcnetsal(taxmarriedlist, float(dpylocal))

    if taxtype == "c":
        calcnetsal(taxmseplist, float(dpylocal))

    if taxtype == "d":
        calcnetsal(taxhohlist, float(dpylocal))

print("Welcome to the annual income forecaster. \n This program was written by David Lee \n Version 1.0 \n Last revised 12-1-2019 \n")
print("NOTE: This program uses 2019 tax brackets. \n DISCLAIMER: By using this program you release the author from all legal liability \n") 

knowsal = str(input("Do you know your annual gross salary (Y/N)?"))
if knowsal == "N":
    while dpy <= 0:
        dpy = float(calcgrosal())
elif knowsal == "Y":
    dpy = float(input("What is your annual gross salary (USD)?"))
else:
    print("Unacceptable value entered besides Y/N. I am assuming this means you do not know your annual gross salary. Let's calculate that.")
    while dpy <= 0:
        dpy = float(calcgrosal())
        
if dpy > 0:
    asktaxclass(dpy)
else:
    print("Cannot generate valid annual income with information provided. Please re-run the program. \n")

print("\nThanks for using my Python program. I would love to make this a powerful financial planning tool.")
print("I have made this code available at https://github.com/lee5378/python. Please email me at lee5378@alumni.uidaho.edu, I would welcome feedback.")
print("-David")
