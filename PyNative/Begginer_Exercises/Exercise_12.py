def taxCollector(x: float) -> float:
    tax_total = 0
    block = 10000

    if x < block:
        return tax_total
    elif x > block and x < block*2:
        tax_total = ((x-block)/10)
        return tax_total
    else:
        x_taxed_20 = x - block*2
        x_taxed_10 = x - x_taxed_20 - block
        tax_total = (x_taxed_10/10) + ((x_taxed_20/10)*2)
        return tax_total
    

if __name__ == '__main__':
    
    x = 45000
    print(taxCollector(x))