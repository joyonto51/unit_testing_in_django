from django.test import TestCase, Client, LiveServerTestCase
from django.urls import reverse

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from school.models import Student


class StudentListViewTest(TestCase):
    # test view
    def test_get_method(self):
        url = reverse("student_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class TestStudentAddView(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.student_add_url = reverse('student_add')

    def test_get_method(self):
        response = self.client.get(self.student_add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_add.html')

    def test_post_method(self):
        data = {
            'name': 'Akbar Ali',
            'roll': 34,
            'address': 'Dinajpur'
        }

        response = self.client.post(self.student_add_url, data)
        student = Student.objects.all().first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(student.name, "Akbar Ali")
        self.assertEqual(student.roll, 34)
        self.assertEqual(student.address, 'Dinajpur')

class TestStudentAddViewBySelenium(LiveServerTestCase):

    def setUp(self):
        # binary = FirefoxBinary('path/to/installed firefox binary')
        # self.driver = webdriver.Firefox()
        self.student_add_url = self.live_server_url + reverse('student_add')
        self.student_list_url = self.live_server_url + reverse('student_list')

        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_student_creation_form(self):
        self.driver.get(self.student_add_url)

        self.driver.find_element_by_name('class_id').send_keys('')
        self.driver.find_element_by_name('name').send_keys("test student")
        self.driver.find_element_by_name('roll').send_keys(1)
        self.driver.find_element_by_name('address').send_keys("test address")

        self.driver.find_element_by_id("submit").click()
        self.assertEqual(self.student_list_url, self.driver.current_url)

    def tearDown(self) -> None:
        self.driver.quit()
