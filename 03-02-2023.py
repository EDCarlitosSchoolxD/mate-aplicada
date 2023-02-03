import math


def run():
    tasaOrdinaria = float(input("Tasa Ordinaria: "))
    iva = float(input("IVA: "))
    deuda = float(input("Deuda: "))

    while(True):
        if(deuda <= 0):
            break
        abono = 2000

        if abono > deuda:
            abono = deuda


        psudoAbono = deuda - abono
        interes = (psudoAbono * tasaOrdinaria) / 100
        totalIva = round((interes * iva) / 100,2)

        deudaAntigua = deuda
        deuda = psudoAbono + interes + totalIva

        print(f"""
        ----------------------------------
            Deuda: {deudaAntigua}
            Abono: {abono}
            psudoAbono: {psudoAbono}
            interes = {interes}
            IVA = {totalIva}
            Deuda Nueva: {deuda}
    ------------------------------------------------------------
        """)


if __name__ == '__main__':
    run()