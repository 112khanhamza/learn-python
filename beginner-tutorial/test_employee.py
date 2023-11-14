import unittest
from unittest.mock import patch
from employee import Employee

# all tests should be isolated
class TestEmployee(unittest.TestCase):

	# runs at the start of test
	@classmethod
	def setUpClass(cls):
		print('setUpClass\n')

	# runs at the end of test
	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	# runs at the start of every method
	def setUp(self):
		print('setUp')
		self.e1 = Employee('Hamza', 'Khan', 60000)
		self.e2 = Employee('Talha', 'Khan', 55000)

	# runs at the end of every test
	def tearDown(self):
		print('teardown\n')
		pass

	def test_email(self):
		print('test_email')
		self.assertEqual(self.e1.email, 'Hamza.Khan@email.com')
		self.assertEqual(self.e2.email, 'Talha.Khan@email.com')

		self.e1.first = 'Maaz'

		self.assertEqual(self.e1.email, 'Maaz.Khan@email.com')

	def test_fullname(self):
		print('test_fullname')
		self.assertEqual(self.e1.fullname, 'Hamza Khan')

		self.e1.last = 'Ansari'
		self.assertEqual(self.e1.fullname, 'Hamza Ansari')

	def test_raise(self):
		print('test_raise')
		self.e1.apply_raise()
		self.assertEqual(self.e1.pay, 63000)

	def test_monthly_schedule(self):
		with patch('employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.e1.monthly_schedule('May')
			mocked_get.assert_called_with('https://company.com/Khan/May')
			self.assertEqual(schedule, 'Success')


			mocked_get.return_value.ok = False

			schedule = self.e2.monthly_schedule('June')
			mocked_get.assert_called_with('https://company.com/Khan/June')
			self.assertEqual(schedule, 'Bad Request')

if __name__ == '__main__':
	unittest.main()