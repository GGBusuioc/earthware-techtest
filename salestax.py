from math import ceil


def basicSalesTax(line):
    terms = ["book", "pills", "chocolate", "chocolates"]
    return True if len(set(line).intersection(terms)) == 0 else False


def importDutyTax(line):
    terms = ["imported"]
    return False if len(set(line).intersection(terms)) == 0 else True


def round_to_05(n):
    return ceil(n * 20) / 20


with open("scenarios/scenario1.txt", encoding="utf-8") as f:
    total = 0
    salesTaxTotal = 0
    for line in f:
        print(line, end="")

        # item bought
        item = line.split()[1:-1]

        # keep the price which is the last element from the line
        originalItemPrice = float(line.split()[-1][1:])
        currentItemPrice = float(line.split()[-1][1:])
        salesTax = 0

        # check if basic sales tax is applicable
        if basicSalesTax(item) == True:
            salesTax = (10 / 100) * originalItemPrice
            currentItemPrice = originalItemPrice + salesTax

        # check if import tax duty is applicable
        if importDutyTax(item) == True:
            salesTax = salesTax + ((5 / 100) * originalItemPrice)
            currentItemPrice = currentItemPrice + ((5 / 100) * originalItemPrice)

        salesTaxTotal += salesTax
        total = total + currentItemPrice

    salesTaxTotal = round_to_05(salesTaxTotal)
    print("\nSales Taxes: £%.2f" % salesTaxTotal)
    print("Total: £%.2f" % total)
