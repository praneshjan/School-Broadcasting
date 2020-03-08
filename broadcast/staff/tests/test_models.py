from django.test import TestCase, Client
from staff.models import Status, User, Staff, Grade

class StaffTestCase(TestCase):
    c = Client()
    def setUp(self):
        User.objects.create(
            username='testing_User',
            password='welcome123',
            is_staff=True,
            is_teacher=True,
            birth_date="1996-01-07",
            address='5,apple street, tnagar,chennai73',
            is_superuser=True)
        Grade.objects.create(
            garde_name='A1',
            description='A1 Class'
        )
    
    def test_user_creation(self):
        username = User.objects.get(username='testing_User')
        self.assertEqual(username.is_teacher,True)
    
    def test_mapping_user(self):
        username = User.objects.get(username='testing_User')
        grade = Grade.objects.get(id=1)
        staff = Staff.objects.create(
        staff_id=username,
        grade_id=grade, 
        date_of_joining= '1996-01-07', 
        subject_handling='history'
        )
    def test_homeurl_check(self):
        responce = self.c.get('')
        self.assertEqual(responce.status_code,200)
    def test_login(self):
        responce = self.c.post('/login/',{'username':'testing_user','password':'welcome123'})
        self.assertEqual(responce.status_code,200)
    def test_allurl_check(self):
        responce = self.c.post('/login/',{'username':'testing_user','password':'welcome123'})
        self.assertEqual(responce.status_code,200)
        responce = self.c.get('/staff/dashboard')
        self.assertEqual(responce.status_code,200)