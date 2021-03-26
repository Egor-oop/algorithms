def chr_row(ascci_val=32):
    if ascci_val == 128:
        return True
    print(f' {ascci_val} - {chr(ascci_val)}', end='')
    if (ascci_val - 31) % 10 == 0:
        print()

    chr_row(ascci_val + 1)


chr_row()
