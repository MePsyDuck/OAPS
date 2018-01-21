from django.test import TestCase

from api.models import Faculty, Student, Letter, Inbox, User, Remark


class ModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='new_user', email='new@user.com', password='secret',
                                        acc_type=User.FACULTY)
        user2 = User.objects.create_user(username='new_user_student', email='new2@user.com', password='secrettop',
                                         acc_type=User.STUDENT)
        faculty = Faculty.objects.create(user=user, tts_id=5214)
        Student.objects.create(user=user2, reg_id='15bats3201', vtu_id=7362, mentor=faculty)
        letter = Letter.objects.create(body='Hi this is first email',
                                       subject='Test subject',
                                       sender=user2,
                                       receiver=user,
                                       )
        letter2 = Letter.objects.create(body='Hi this is second email',
                                        subject='Test subject second',
                                        sender=user2,
                                        receiver=user,
                                        is_read=True,
                                        )
        Inbox.objects.create(user=user, letter=letter, is_starred=True)
        Inbox.objects.create(user=user, letter=letter2)
        Remark.objects.create(letter=letter, user=user2, action=Remark.APPROVED, message='Go on')

    def test_models(self):
        # check user
        user = User.objects.get(username='new_user')
        user2 = User.objects.get(username='new_user_student')
        self.assertTrue(user.check_password('secret'))
        self.assertFalse(user.check_password('secrettop'))
        self.assertFalse(user2.check_password('secret'))
        self.assertTrue(user2.check_password('secrettop'))

        # check faculty
        self.assertTrue(user.is_faculty())
        self.assertFalse(user.is_student())
        self.assertEqual(str(user.faculty), 'TTS5214')

        # check student
        self.assertTrue(user2.is_student())
        self.assertFalse(user2.is_faculty())
        self.assertEqual(str(user2.student), 'VTU7362')
        self.assertEqual(user2.student.reg_id, '15bats3201')
        self.assertEqual(user2.student.mentor, user.faculty)

        # check letter
        letter = Letter.objects.get(pk=1)
        letter2 = Letter.objects.get(pk=2)
        self.assertEqual(letter.body, 'Hi this is first email')
        self.assertEqual(letter.subject, 'Test subject')
        self.assertFalse(letter.is_read)
        self.assertEqual(letter.sender, user2)
        self.assertEqual(letter.receiver, user)
        self.assertEqual(letter2.body, 'Hi this is second email')
        self.assertEqual(letter2.subject, 'Test subject second')
        self.assertTrue(letter2.is_read)
        self.assertEqual(letter2.sender, user2)
        self.assertEqual(letter2.receiver, user)

        # check inbox
        self.assertEqual(user.inbox.count(), 2)
        self.assertTrue(user.inbox.first().is_starred)
        self.assertFalse(user.inbox.filter(user=user, letter=letter2).first().is_starred)

        # check remarks
        remarks = Remark.objects.filter(letter=letter).all()
        remarks2 = Remark.objects.filter(letter=letter2).all()
        self.assertEqual(remarks.count(), 1)
        self.assertEqual(remarks2.count(), 0)
        self.assertEqual(str(remarks.first()), '%s : Go on' % Remark.APPROVED)
