import pytest
from bank import Bank, Account, Transaction

@pytest.fixture
def bank():
    return Bank()

def test_create_account(bank):
    bank.create_account('123', balance=1000)
    assert bank.get_account_balance('123') == 1000

def test_create_duplicate_account(bank):
    bank.create_account('123', balance=1000)
    with pytest.raises(ValueError):
        bank.create_account('123')

def test_get_balance_non_existing_account(bank):
    with pytest.raises(ValueError):
        bank.get_account_balance('456')

def test_deposit_and_withdraw(bank):
    account = Account('123', balance=1000)
    account.deposit(500)
    assert account.balance == 1500
    account.withdraw(300)
    assert account.balance == 1200

def test_insufficient_balance(bank):
    account = Account('123', balance=1000)
    with pytest.raises(ValueError):
        account.withdraw(1500)

def test_transaction_successful(bank):
    source_account = Account('123', balance=1000)
    target_account = Account('456', balance=500)
    transaction = Transaction(source_account, target_account, 300)
    transaction.execute()
    assert source_account.balance == 700
    assert target_account.balance == 800

def test_transaction_insufficient_balance(bank):
    source_account = Account('123', balance=100)
    target_account = Account('456', balance=500)
    transaction = Transaction(source_account, target_account, 300)
    with pytest.raises(ValueError):
        transaction.execute()

def test_transaction_negative_amount(bank):
    source_account = Account('123', balance=1000)
    target_account = Account('456', balance=500)
    transaction = Transaction(source_account, target_account, -300)
    with pytest.raises(ValueError):
        transaction.execute()
