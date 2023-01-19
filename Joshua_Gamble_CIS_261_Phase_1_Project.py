#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#write the GetHoursWorked function
def GetHoursWorked():
    hours = float(input("Enter hours worked: "))
    return hours
#write the GetHourlyRate function
def GetHourlyRate(): 
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate
# write the GetTaxRate function
def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print()
    print("Name:  ", empname)
    print(f"Hours Worked: {hours:,.2f}")
    print(f"Hourly Rate: {hourlyrate:,.2f}")
    print(f"Gross Pay: {grosspay:,.2f}")
    print(f"Tax Rate: {taxrate:,.1%}")
    print(f"Income Tax: {incometax:,.2f}")
    print(f"Net Pay: {netpay:,.2f}")

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    print(f"Total Tax: {TotTax:,.2f}")
    print(f"Total Net Pay: {TotNetPay:,.2f}")
    

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
        hours = GetHoursWorked()
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        hourlyrate = GetHourlyRate()
        # write the code to assign to taxrate the return value from GetTaxRate
        taxrate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        # write the code to increment the other total variables with the appropriate values
        TotGrossPay = TotGrossPay + grosspay
        TotTax = TotTax + taxrate
        TotNetPay = TotNetPay + netpay
        

    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)



