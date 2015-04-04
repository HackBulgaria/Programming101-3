from bank import BankAccount
import unittest


class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.currency = "BGN"
        self.account = BankAccount("Rado", 0, self.currency)

    def test_can_create_bank_account(self):
        self.assertTrue(isinstance(self.account, BankAccount))

    def test_initial_zero_balance(self):
        self.assertEqual(self.account.balance(), 0)

    def test_initial_non_zero_balance(self):
        initial_balance = 100
        account = BankAccount("Test", initial_balance, "$")

        self.assertEqual(account.balance(), initial_balance)

    def test_negative_initial_amount(self):
        with self.assertRaises(ValueError):
            BankAccount("Test", -100, "$")

    def test_get_name(self):
        name = "Test"
        account = BankAccount(name, 0, "$")

        self.assertEqual(account.holder(), name)

    def test_get_name_when_name_not_string_but_object(self):
        name = ("Radoslav", "Georgiev")
        account = BankAccount(name, 0, "%")

        self.assertEqual(str(name), account.holder())

    def test_get_currency(self):
        self.assertEqual(self.account.currency(), self.currency)

    def test_currency_always_string(self):
        currency = 1

        account = BankAccount("Test", 0, currency)

        self.assertEqual(str(currency), account.currency())

    def test_deposit_in_empty_account(self):
        self.account.deposit(100)

        self.assertEqual(100, self.account.balance())

    def test_deposit_in_not_empty_account(self):
        account = BankAccount("Test", 50, "$")
        account.deposit(50)

        self.assertEqual(account.balance(), 100)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_from_non_empty_account(self):
        self.account.deposit(100)
        result = self.account.withdraw(50)

        self.assertTrue(result)
        self.assertEqual(self.account.balance(), 50)

    def test_withdraw_from_empty_account(self):
        result = self.account.withdraw(50)

        self.assertIsNotNone(result)
        self.assertFalse(result)

    def test_history_when_account_is_created(self):
        account = BankAccount("Test", 0, "$")
        expected = ["Account was created"]

        self.assertEqual(account.history(), expected)

    def test_history_with_balance_check(self):
        account = BankAccount("Test", 0, "$")
        expected = ["Account was created", "Balance check -> 0$"]

        self.assertEqual(account.history(), expected)
if __name__ == '__main__':
    unittest.main()
