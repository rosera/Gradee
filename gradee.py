# Name: 	Gradee
# Author: Richard Rose
# Date: 	Sept 2015
# Description: Calculate R&D Benefit

print ""
print "  ________                  .___     ___________"
print "/  _____/___________     __| _/____ \_   _____/"
print "/   \  __\_  __ \__  \   / __ |/ __ \ |    __)_ "
print "\    \_\  \  | \// __ \_/ /_/ \  ___/ |        \\"
print " \______  /__|  (____  /\____ |\___  >_______  /"
print "        \/           \/      \/    \/        \/ "
print "Calculate SME R&D Benefit"
print ""
print "--------------------------------------------------------------------"
uplift = input("Uplift %: \t\t\t")
staff_costs = input ("Staff costs: \t\t\t")
staff_restrict = input("Percentage allowable 0-100: \t")
sub_costs = input ("Subcontractor costs: \t\t")
apportion_costs = input("Apportioned costs: \t\t")
apportion_restrict = input("Percentage allowable 0-100: \t")
print "--------------------------------------------------------------------"


###################################################
# Staff calc
###################################################
# Restrict staff costs
staff_total = staff_costs * (float(staff_restrict)/100)
#print "Apply %"
#print staff_costs
# Multiply staff by uplift %
staff_total = staff_total * (float(uplift)/100)
#print "Apply 225%"
#print staff_costs

###################################################
# Subcontractor calc
###################################################
# Restrict sub_costs by 65%
sub_total = sub_costs * .65
#print "sub costs @ 65%"

# Multiple sub_costs by uplift %
sub_total = sub_total * (float(uplift)/100)
#print "sub costs @ 225%"
#print sub_costs

###################################################
# Apportion calc
###################################################
# Restrict apportion cost
apportion_total = apportion_costs * (float(apportion_restrict)/100)

# Multiply apportion costs by 225%
apportion_total = float(apportion_total) * (float(uplift)/100)


###################################################
# Calculate tax credit
###################################################
# Sum available costs
#Tax_credit = staff_costs
Tax_credit = staff_total + sub_total + apportion_total

# Apply tax credit rate - 14.5%
Tax_credit = Tax_credit * 0.145


###################################################
# Output the tax credit
###################################################
print "R&D Tax Credit - SME"
print "--------------------------------------------------------------------"
print "Employee costs:\t\t %.2f \t%d%% \t%.2f" % (staff_costs, staff_restrict, staff_total)
print "Sub contrator costs:\t %.2f \t65%% \t%.2f" % (sub_costs, sub_total)
print "Apportion costs:\t %.2f \t%d%% \t%.2f" % (apportion_costs, apportion_restrict, apportion_total) 
print "--------------------------------------------------------------------"
print "Tax Credit:\t\t\t\t\t%.2f" % (Tax_credit)
print "--------------------------------------------------------------------"
 
