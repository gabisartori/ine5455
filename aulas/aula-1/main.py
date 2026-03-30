import unittest
import datetime

class Tester(unittest.TestCase):
	def test_1_value_attribuition(self):
		"""Testa atribuição de valores"""
		# Fixture Setup
		# Exercise SUT
		birthday = datetime.date(2003, 12, 15)
		# Result Verificiation
		self.assertEqual(2003, birthday.year)
		self.assertEqual(12, birthday.month)
		self.assertEqual(15, birthday.day)
		# Fixture Teardown

	def test_2_capture_negative_day(self):
		"""Testa se valores negativos são capturados"""
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			negative_day = datetime.date(2026, 3, -20)
		# Result Verificiation
		# Fixture Teardown

	def test_3_capture_strings(self):
		"""Testa se strings são capturadas"""
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(TypeError):
			string_month = datetime.date(2026, "March", 20)
		# Result Verificiation
		# Fixture Teardown

	def test_4_capture_higher_months(self):
		"""Testa se meses além de Dezembro são capturados"""
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			onzembro = datetime.date(2026, 13, 30)
		# Result Verificiation
		# Fixture Teardown

	def test_5_allow_february_29_in_leap_year(self):
		"""Testa se Fevereiro tem 29 dias num ano bissexto"""
		# Fixture Setup
		# Exercise SUT
		feb29 = datetime.date(2024, 2, 29)
		# Result Verificiation
		self.assertEqual(feb29.year, 2024)
		self.assertEqual(feb29.month, 2)
		self.assertEqual(feb29.day, 29)
		# Fixture Teardown

	def test_6_catch_february_29_in_common_yeay(self):
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			feb29 = datetime.date(2025, 2, 29)
		# Result Verificiation
		# Fixture Teardown

	def test_7_common_year_multiple_of_100(self):
		"""Anos múltiplos de 100 não são bissextos"""
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			feb29 = datetime.date(2100, 2, 29)
		# Result Verificiation
		# Fixture Teardown

	def test_8_leap_year_multiple_of_400(self):
		"""Mas múltiplos de 400 são :)"""
		# Fixture Setup
		# Exercise SUT
		feb29 = datetime.date(2000, 2, 29)
		# Result Verificiation
		self.assertEqual(feb29.year, 2000)
		self.assertEqual(feb29.month, 2)
		self.assertEqual(feb29.day, 29)
		# Fixture Teardown

	def test_9_to_ordinal_day_1(self):
		# Fixture Setup
		day_1 = datetime.date(1, 1, 1)
		# Exercise SUT
		ordinal_day_1 = day_1.toordinal()
		# Result Verificiation
		self.assertEqual(ordinal_day_1, 1)
		# Fixture Teardown

	def test_10_ordinal_day_366(self):
		# Fixture Setup
		day_366 = datetime.date(2, 1, 1)
		# Exercise SUT
		ordinal_day_366 = day_366.toordinal()
		# Result Verificiation
		self.assertEqual(ordinal_day_366, 366)
		# Fixture Teardown

	def test_11_to_ordinal_counts_leap_year(self):
		# Fixture Setup
		day_365_times_4_plus_1 = datetime.date(4, 12, 31)
		# Exercise SUT
		day_1461_ordinal = day_365_times_4_plus_1.toordinal()
		# Result Verificiation
		self.assertEqual(day_1461_ordinal, 4*365+1)
		# Fixture Teardown

	def test_12_catch_november_with_31_days(self):
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			nov31 = datetime.date(2026, 11, 31)
		# Result Verificiation
		# Fixture Teardown

	def test_13_time_creation_invalid_24_hours(self):
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			day = datetime.time(24, 0, 0)
		# Result Verificiation
		# Fixture Teardown

	def test_14_time_creation_invalid_minute(self):
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			day = datetime.time(20, 60, 0)
		# Result Verificiation
		# Fixture Teardown

	def test_15_time_creation_valid_time(self):
		# Fixture Setup
		# Exercise SUT
		bedtime = datetime.time(23, 59, 59)
		# Result Verificiation
		self.assertEqual(bedtime.hour, 23)
		self.assertEqual(bedtime.minute, 59)
		self.assertEqual(bedtime.second, 59)
		# Fixture Teardown

	def test_16_timedelta_creation_24_hours_is_one_day(self):
		# Fixture Setup
		# Exercise SUT
		day = datetime.timedelta(hours=24)
		# Result Verificiation
		self.assertEqual(day.days, 1)
		# Fixture Teardown

	def test_17_timedelta_correct_difference_between_two_dates(self):
		# Fixture Setup
		day1 = datetime.date(1, 1, 1)
		day2 = datetime.date(1, 1, 2)
		# Exercise SUT
		delta = day2 - day1
		# Result Verificiation
		self.assertEqual(delta.days, 1)
		# Fixture Teardown

	def test_18_negative_timedelta(self):
		# Fixture Setup
		day1 = datetime.date(1,1,1)
		day2 = datetime.date(1,1,2)
		# Exercise SUT
		delta = day1-day2
		# Result Verificiation
		self.assertEqual(delta.days, -1)
		# Fixture Teardown

	def test_19_datetime_creation_valid_input(self):
		# Fixture Setup
		# Exercise SUT
		appointment = datetime.datetime(2026, 5, 26, 15, 0, 0)
		# Result Verificiation
		self.assertEqual(appointment.year, 2026)
		self.assertEqual(appointment.month, 5)
		self.assertEqual(appointment.day, 26)
		self.assertEqual(appointment.hour, 15)
		self.assertEqual(appointment.minute, 0)
		self.assertEqual(appointment.second, 0)
		# Fixture Teardown

	def test_20_datetime_creation_negative_values(self):
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			negative_day = datetime.datetime(2026, 30, -26, 0, 0, 0)
		# Result Verificiation
		# Fixture Teardown

	def test_21_datetime_creation_invalid_string_as_month(self):
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(TypeError):
			string_month = datetime.datetime(2026, "hii", 26, 15, 30, 0)
		# Result Verificiation
		# Fixture Teardown

	def test_22_datetime_creation_numeric_string_as_month(self):
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(TypeError):
			string_month = datetime.datetime(2025, "3", 30, 0, 0, 0)
		# Result Verificiation
		# Fixture Teardown

	def test_23_leap_second_of_december_31st_2016(self):
		"""31 de dezembro de 2016"""
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			leap_second = datetime.datetime(2016, 12, 31, 23, 59, 60)
		# Result Verificiation
		# Fixture Teardown

	def test_24_check_weekday_is_correct_monday(self):
		"""Weekdays are returned as numbers, starting from mondays as 0 and going up to sundays as 6"""
		# Fixture Setup
		monday = datetime.date(2026, 3, 16)
		# Exercise SUT
		weekday = monday.weekday()
		# Result Verificiation
		self.assertEqual(weekday, 0)
		# Fixture Teardown

	def test_24_1_check_weekday_is_correct_sunday(self):
		"""Weekdays are returned as numbers, starting from mondays as 0 and going up to sundays as 6"""
		# Fixture Setup
		monday = datetime.date(2026, 3, 15)
		# Exercise SUT
		weekday = monday.weekday()
		# Result Verificiation
		self.assertEqual(weekday, 6)
		# Fixture Teardown

	def test_25_replace_leap_year_with_common_year_on_february_29th(self):
		# Fixture Setup
		feb29_2024 = datetime.date(2024, 2, 29)
		# Exercise SUT
		with self.assertRaises(ValueError):
			feb29_2024.replace(year=2025)
		# Result Verificiation
		# Fixture Teardown

	def test_26_replace_time_valid_input(self):
		# Fixture Setup
		appointment = datetime.datetime(2026, 5, 26, 15, 0, 0)
		# Exercise SUT
		appointment = appointment.replace(minute=30)
		# Result Verification
		self.assertEqual(appointment.minute, 30)
		# Fixture Teardown

if __name__ == '__main__': unittest.main()
