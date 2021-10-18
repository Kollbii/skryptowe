import unittest
import subs

class Test_Subscribing(unittest.TestCase):
    global acc1, acc2, ch1, ch2, ch3, ch4
    acc1 = subs.Account("User1")
    acc2 = subs.Account("User2")

    ch1 = subs.Channel("One chan", 0, "Blank description in here")
    ch2 = subs.Channel("Two chan", 0, "Lorem ipsum dos semit")
    ch3 = subs.Channel("Simple chan", 0, "")
    ch4 = subs.Channel("4 chan", 0, "Very short desc in here")

    acc1.subscribe(ch1)
    acc1.subscribe(ch2)
    acc1.subscribe(ch4)

    def test_subscriber(self):
        self.assertEqual(acc1.subscribe(ch1), False) # Already subscribed
        self.assertEqual(acc1.subscribe(ch3), True)
        self.assertEqual(acc2.subscribe(ch4), True)
        with self.assertRaises(Exception):
            self.assertEqual(acc1.subscribe("channel5"), False) # There is no channel no. 5

    def test_unsubscribe(self):
        self.assertEqual(acc1.unsubscribe(ch1), True)
        self.assertEqual(acc2.unsubscribe(ch4), True)
        self.assertEqual(acc1.unsubscribe(ch2), True)

    def test_change_description(self):
        ch1.add_description(" more text XYZ.")
        self.assertEqual(ch1.description, "Blank description in here more text XYZ.")

    def test_remove_description(self):
        self.assertEqual(ch1.rm_description(), True)
        self.assertEqual(ch2.rm_description(), True)
        self.assertEqual(ch3.rm_description(), True)
        self.assertNotEqual(ch4.rm_description(), False)


if __name__ == '__main__':
    unittest.main()