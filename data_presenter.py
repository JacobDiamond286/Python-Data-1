cupcake_invoices = open("CupcakeInvoices.csv")

for row in cupcake_invoices:
    print(row)

for cupcakes in cupcake_invoices:
    cupcakes = cupcakes.rstrip().split(',')
    print(cupcakes[2])

invoiceAll = 0

for invoice in cupcake_invoices:
    invoice = invoice.rstrip().split(',')
    invoiceIndexThree = float(invoice[3])
    invoiceIndexFour = float(invoice[4])
    invoiceTotals = invoiceIndexThree * invoiceIndexFour
    print(invoiceTotals)
    if invoiceTotals > 0:
        invoiceAll += invoiceTotals

print(invoiceAll)

cupcake_invoices.close()