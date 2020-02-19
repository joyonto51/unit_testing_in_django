from django.contrib.auth.models import User
from django.test import TestCase, Client, LiveServerTestCase
from django.urls import reverse

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from school.models import Student, SchoolClass


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
        # create class
        SchoolClass.objects.create(class_name="one", numeric_value=1)
        SchoolClass.objects.create(class_name="Two", numeric_value=2)

        # student add urls
        self.student_add_url = self.live_server_url + reverse('student_add')
        self.student_list_url = self.live_server_url + reverse('student_list')

        # initializing browser
        self.browser = webdriver.Firefox()

    def test_student_creation_form(self):
        self.browser.get(self.student_add_url)

        class_select_field = self.browser.find_element_by_name("class_id")

        # for option in class_select_field.find_elements_by_tag_name('option'):
        #     if option.text == 'Two':
        #         option.click()

        self.browser.find_element_by_xpath("//select[@name='class_id']/option[text()='Two']").click()

        self.browser.find_element_by_name('name').send_keys("test student")
        self.browser.find_element_by_name('roll').send_keys(1)
        self.browser.find_element_by_name('address').send_keys("test address")

        self.browser.find_element_by_id("submit").click()
        self.assertEqual(self.student_list_url, self.browser.current_url)

    def tearDown(self) -> None:
        self.browser.quit()


from selenium.webdriver.common.keys import Keys as KEY


class TestAdmin(LiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', email='admin@gmail.com', password='admin123')

        self.browser = webdriver.Firefox()
        self.url = self.live_server_url + '/admin/'

    def test_admin_panel(self):
        self.browser.get(self.url)

        username = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')

        username.send_keys('admin')
        password.send_keys("admin123")
        password.send_keys(KEY.RETURN)

        self.browser.find_element_by_name('submit').click()

        self.assertEqual(self.url, self.browser.current_url)

    def tearDown(self):
        self.browser.quit()
        self.user.delete()