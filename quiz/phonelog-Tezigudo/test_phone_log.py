import unittest
from phone_log import PhoneLog


class TestPhoneLog(unittest.TestCase):

    def setUp(self) -> None:
        self.log = PhoneLog(3)

    def test_record_call(self):
        """basic record it just work!"""
        self.log.record_call("555-1212")
        self.assertEqual(self.log.get_calls(), ["555-1212"])

        self.log.record_call("123")
        self.assertEqual(self.log.get_calls(), ["123", "555-1212"])

    def test_record_call_with_trailing_and_leading_whitespace(self):
        """record call with trailing whitespace must be removed"""
        self.log.record_call("555-1212 ")
        self.log.record_call("  5011")
        self.assertEqual(self.log.get_calls(), ["5011", "555-1212"])

    def test_empty_record(self):
        """record call with empty string or whitespace must raise ValueError"""
        with self.assertRaises(ValueError):
            self.log.record_call('')

        with self.assertRaises(ValueError):
            self.log.record_call('   ')

    def test_deplicate_record(self):
        """duplicate number will keep the recent occurence only"""
        self.log.record_call("555-1212")
        self.log.record_call("123")
        self.log.record_call("555-1212")
        self.assertEqual(self.log.get_calls(), ["555-1212", "123"])

    def test_record_over_capacity(self):
        """record over the max capacity must remove the oldest number"""
        self.log.record_call("555-1212")
        self.log.record_call("123")
        self.log.record_call("456")
        self.log.record_call("789")
        self.log.record_call("123")
        self.assertEqual(self.log.get_calls(), ["123", "789", "456"])

    def test_log_with_capacity_one(self):
        """if the capacity is 1 log must be change everytime it recorded"""
        log_one = PhoneLog(1)
        log_one.record_call("555-1212")
        self.assertEqual(log_one.get_calls(), ["555-1212"])
        log_one.record_call("123")
        self.assertEqual(log_one.get_calls(), ["123"])

    def test_record_whitespace_in_number(self):
        """record number with whitespace inside and it must be orihinal one"""
        self.log.record_call("123 456")
        self.assertEqual(self.log.get_calls(), ["123 456"])


if __name__ == '__main__':
    unittest.main()
