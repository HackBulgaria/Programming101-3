# TDD
# 1. Write test that fails
# 2. Make it work.
# 3. Refactor while testing
# 4. Loop back to 1)
import unittest
from cashdesk import Bill, BillBatch, CashDesk


class CashDeskTest(unittest.TestCase):

    def setUp(self):
        self.test_bill = Bill(10)

    def test_create_new_bill_class(self):
        self.assertTrue(isinstance(self.test_bill, Bill))

    def test_create_int_value_from_bill(self):
        self.assertEqual(int(self.test_bill), 10)

    def test_amount_in_bill(self):

        with self.assertRaises(AttributeError):
            self.test_bill.amount

    def test_str_dunder_for_bill(self):
        self.assertEqual(str(self.test_bill), "A 10$ bill.")

    def test_repr_dunder_for_bill(self):
        self.assertEqual(repr(self.test_bill), "A 10$ bill.")

    def test_eq_between_bills_when_not_same(self):
        bill1 = Bill(10)
        bill2 = Bill(11)

        self.assertTrue(bill1 != bill2)

    def test_eq_between_bills_when_same(self):
        bill1 = Bill(10)
        bill2 = Bill(10)

        self.assertTrue(bill1 == bill2)

    def test_bills_are_orderable(self):
        self.assertTrue(Bill(5) < Bill(10))

    def test_can_hash_bill(self):
        self.assertIsNotNone(hash(self.test_bill))

    def test_can_put_bill_in_dictionary(self):
        money_holder = {}
        bill = Bill(10)

        money_holder[bill] = 1

        self.assertTrue(bill in money_holder)

    def test_value_error_raises_from_negative_amount(self):
        with self.assertRaises(ValueError):
            Bill(-10)

    def test_value_error_raises_from_zero_amount(self):
        with self.assertRaises(ValueError):
            Bill(0)

    def test_type_error_raises_from_float_amount(self):
        with self.assertRaises(TypeError):
            Bill(0.5)

    def test_can_create_billbatch(self):
        batch = BillBatch([])
        self.assertTrue(isinstance(batch, BillBatch))

    def test_can_create_billbatch_with_bills(self):
        bills = [Bill(value) for value in range(1, 10)]
        batch = BillBatch(bills)

        self.assertEqual(len(batch), len(range(1, 10)))
        self.assertEqual(batch.total(), sum(range(10)))

    def test_can_for_loop_a_billbatch(self):
        bills = [Bill(value) for value in range(1, 10)]
        batch = BillBatch(bills)
        total = 0

        for bill in batch:
            total += int(bill)

        self.assertEqual(total, sum(range(1, 10)))

    def test_can_create_cashdesh(self):
        desk = CashDesk()
        self.assertTrue(isinstance(desk, CashDesk))

    def test_cashdesk_take_only_bills(self):
        desk = CashDesk()

        desk.take_money(Bill(10))
        desk.take_money(Bill(5))

        self.assertEqual(desk.total(), 15)

    def test_cashdesk_take_only_batch(self):
        desk = CashDesk()
        batch = BillBatch([Bill(10), Bill(5)])

        desk.take_money(batch)

        self.assertEqual(desk.total(), 15)

    def test_inspect_on_empty_desk(self):
        desk = CashDesk()
        expected = "We have 0$ in the desk."

        self.assertEqual(desk.inspect(), expected)

    def test_inspect_with_full_desk(self):
        desk = CashDesk()

        desk.take_money(Bill(1))
        desk.take_money(Bill(2))
        desk.take_money(Bill(10))

        expected = ["We have 13$ in the desk."]
        expected.append("Bills are:")
        expected.append("$1 - 1")
        expected.append("$2 - 1")
        expected.append("$10 - 1")

        self.assertEqual("\n".join(expected), desk.inspect())

if __name__ == '__main__':
    unittest.main()
