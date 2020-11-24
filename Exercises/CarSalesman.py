#Car Salesman
#This program makes some calculations for Subaru purchase.
#
#It factors in tax, license, dealer prep, and destination charge.
#Tax and license are a percentage.
#Dealprep and destcharge are flatrate.

basecharge = int(input("What is the base price of the vehicle? "))

tax = .20 * basecharge

licensefee = .10 * basecharge

dealprep = 500

destcharge = 200

total = basecharge + tax + licensefee + dealprep + destcharge

print("\nThe total including tax is:$", basecharge + tax),"."
print("\nThe total including tax AND license fees is:$", basecharge + tax + licensefee),"."
print("\nThe grand total with all the bells and whistles is:$", total)
