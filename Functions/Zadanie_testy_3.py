def test_policz_znaki_bez_znacznikow():
    assert policz_znaki("ala ma kotaa ko ma ale") == 0


def test_policz_jeden_poziom_zalgebienia_standardowe_znaczniki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_policz_znaki_wiele_poziomow_zaglebienia_niestandardowe_znaki():
    assert policz_znaki()