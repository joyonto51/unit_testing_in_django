from django.test import TestCase
from django.urls import reverse

import unittest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from school.models import SchoolClass
from school.tests.test_model import StudentTest


class StudentViewTest(TestCase):
    # test view
    def test_student_list_view(self):
        url = reverse("student_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class TestStudentCreation(TestCase):
    def setUp(self):
        # binary = FirefoxBinary('path/to/installed firefox binary')
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_student_creation_form(self):
        self.driver.get("http://127.0.0.1:8500/sample-crud/student/add/")

        self.driver.find_element_by_name('class_id').send_keys(1)
        self.driver.find_element_by_name('name').send_keys("test student")
        self.driver.find_element_by_name('roll').send_keys(1)
        self.driver.find_element_by_name('address').send_keys("test address")

        self.driver.find_element_by_id("submit").click()
        self.assertEqual("http://127.0.0.1:8500/sample-crud/student/list/", self.driver.current_url)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()