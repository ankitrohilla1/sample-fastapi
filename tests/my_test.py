import pytest
from app.calculations import add, InsufficientFunds, BankAccount


@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    print('testing add func')
    assert add(num1,num2) == expected



def test_bank_set_initial_amount(bank_account):
    # bank_account = BankAccount(50)
    # assert bank_account.balance == 50
    assert bank_account.balance == 50


def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_collect_interest():
    bank_account = BankAccount(10)
    bank_account.collect_interest()
    assert bank_account.balance == 11


def test_insufficient(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
        # assert bank_account.balance == -150