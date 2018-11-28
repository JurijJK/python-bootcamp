
class CashMachine:

    def __init__(self):
        self._money = []

    @property
    def is_avaiable(self):
        if self._money:
            return True
        return False

    def put_money(self, money):
        self._money.extend(money)

    def withdraw_money(self, to_withdraw):
        bills_to_withdraw = []
        for bill in sorted(self._money, reverse=True):
            if sum(bills_to_withdraw) + bill <= to_withdraw:
                bills_to_withdraw.append(bill)

        if sum(bills_to_withdraw) != to_withdraw:
            return []

        for bill in bills_to_withdraw:
            self._money.remove(bill)

        return bills_to_withdraw


def main():
    bankomat = CashMachine()
    operacja = input("Podaj typ operacji w - wpłata, y - wypłata: ")

    if operacja == "w":
        banknoty = input("Podaj banknoty do wpłaty - wpisz je rozdzielając spacją ")
        banknoty = banknoty.split()
        banknoty = [int(x) for x in banknoty]
        bankomat.put_money(banknoty)

    if operacja == "y":
        kwota_do_wypłaty = int(input("Jaką kwotę chcesz wypłacić? "))
        wyplacone = kwota_do_wypłaty






main()




# testy

def test_cash_machine_not_avaiable():
    cash_machine = CashMachine()
    assert not cash_machine.is_avaiable

def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([50])
    cash_machine.put_money([50])
    assert cash_machine.is_avaiable

def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]