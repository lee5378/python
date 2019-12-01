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
taxratelist = [ .10, .12, .22, .24, .32, .35, .37 ]
taxsinglelist = [ 9700, 39475, 84200, 160725, 204100, 510300 ]
taxmarriedlist = [ 19400, 78950, 168400, 321450, 408200, 6123550 ]
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
            taxrate = taxratelist [7]
    npy = dpylocal-(taxrate*dpylocal)
    print("Income tax will consume",taxrate,"of your salary.")
    print("You will net", npy, "dollars per year.")

# Function name: calcgrosal
# Purpose: Calculate the gross salary if only hourly is known

def calcgrosal():
    dph = float(input("What is your hourly wage (USD)?"))   # This program assumes you know hourly wage

    # Begin input validation for dph variable

    if dph < 0:
        print(dph, "is not a normal wage. You must have a strange job. Please enter a feasible wage.")
        dph = float(input("Dollars per hour?"))

    if dph == 0:
        print("You will gross 0 dollars per year if you earn", dph, "dollars per hour. Please enter a feasible wage.")
        dph = float(input("Dollars per hour?"))
        
    # Finish input validation for dph variable
        
    print("You make", dph, "dollars per hour.")

    hpw = float(input("Hours per week?"))
    wpy = 52        # wpy = Weeks per year
    dpw = dph*hpw   # dpw = Dollars per week
    dpylocal = dpw*wpy   # dpy = Dollars per year

    print("You work", hpw, "hours per week. Therefore you will gross", dpylocal, "dollars per year.")
    return dpylocal # Pass dpylocal value back out to the global variable dpy

print("Welcome to the annual income forecaster. \n This program was written by David Lee \n Version 1.0 \n Last revised 12-1-2019 \n")
print("NOTE: This program uses 2019 tax brackets. \n DISCLAIMER: By using this program you release the author from all legal liability \n") 

knowsal = str(input("Do you know your annual gross salary (Y/N)?"))
if knowsal == "N":
    dpy = calcgrosal()
elif knowsal == "Y":
    dpy = float(input("What is your annual gross salary (USD)?"))
else:
    print("Unacceptable value entered besides Y/N. I am assuming this means you do not know your annual gross salary. Let's calculate that.")
    dpy = float(calcgrosal())
print("How will you be filing taxes?")
print("  a) Single")
print("  b) Married filing jointly or qualifying widow/widower")
print("  c) Married filing separately")
taxtype = str(input("  d) Head of household"))

if taxtype == "a":
    calcnetsal(taxsinglelist, float(dpy))

if taxtype == "b":
    calcnetsal(taxmarriedlist, float(dpy))

print("DEBUG variable dpy =",dpy)

