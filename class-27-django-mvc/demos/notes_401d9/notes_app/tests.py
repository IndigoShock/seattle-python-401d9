from django.test import TestCase, RequestFactory
from .models import Note


class TestNoteModel(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Feed the cat', description='She is hangry')
        Note.objects.create(title='blarp', description='wat stick')
        Note.objects.create(title='Gnarf', description='wat dat')

    def test_note_titles(self):
        self.assertEqual(self.note.title, 'Feed the cat')

    def test_note_detail(self):
        note = Note.objects.get(title='Gnarf')

        self.assertEqual(note.description, 'wat dat')


class TestNoteViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.note_one = Note.objects.create(title='blarp', description='wat stick')
        self.note_two = Note.objects.create(title='Gnarf', description='wat dat')

    def test_note_detail_view(self):
        from .views import notes_detail_view
        request = self.request.get('')
        response = notes_detail_view(request, f'{self.note_one.id}')
        self.assertIn(b'wat stick', response.content)

    def test_note_detail_status(self):
        from .views import notes_detail_view
        request = self.request.get('')
        response = notes_detail_view(request, f'{self.note_one.id}')
        self.assertEqual(200, response.status_code)