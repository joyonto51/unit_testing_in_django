from rest_framework.test import APISimpleTestCase, APIRequestFactory, APIClient

class TestAPIView(APISimpleTestCase):
    def test_get_json_api(self):
        response = self.client.get('/sample-crud/student-add/api/', format='json')
        self.assertEqual(response.data, {
            'message':'API is Okay',
        })
