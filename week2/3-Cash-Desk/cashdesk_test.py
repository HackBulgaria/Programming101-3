# TDD
# 1. Write test that fails
# 2. Make it work.
# 3. Refactor while testing
# 4. Loop back to 1)
import unittest
from cashdesk import Bill


class CashDeskTest(unittest.TestCase):
    def test_create_new_bill_class(self):
        bill = Bill(10)
        self.assertTrue(isinstance(bill, Bill))

    def test_create_int_value_from_bill(self):
        bill = Bill(10)
        self.assertEqual(int(bill), 10)

    def test_amount_in_bill(self):
        bill = Bill(10)

        with self.assertRaises(AttributeError):
            bill.amount

    def test_str_dunder_for_bill(self):
        bill = Bill(10)

        self.assertEqual(str(bill), "A 10$ bill.")

    def test_repr_dunder_for_bill(self):
        bill = Bill(10)

        self.assertEqual(repr(bill), "A 10$ bill.")

    def test_eq_between_bills_when_not_same(self):
        bill1 = Bill(10)
        bill2 = Bill(11)

        self.assertTrue(bill1 != bill2)

    def test_eq_between_bills_when_same(self):
        bill1 = Bill(10)
        bill2 = Bill(10)

        self.assertTrue(bill1 == bill2)

    def test_can_hash_bill(self):
        bill = Bill(10)

        self.assertIsNotNone(hash(bill))

    def test_can_put_bill_in_dictionary(self):
        money_holder = {}
        bill = Bill(10)

        money_holder[bill] = 1

        self.assertTrue(bill in money_holder)

    def test_value_error_raises_from_negative_amount(self):
        with self.assertRaises(ValueError):
            bill = Bill(-10)

    def test_value_error_raises_from_zero_amount(self):
        with self.assertRaises(ValueError):
            bill = Bill(0)

    def test_type_error_raises_from_float_amount(self):
        with self.assertRaises(TypeError):
            bill = Bill(0.5)


if __name__ == '__main__':
    unittest.main()
