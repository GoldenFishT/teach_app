import unittest
from app import Lesson
from requests import put, get
class TestLessonClass(unittest.TestCase):
    def test_class(self):
        titles = ['title'+str(i) for i in range(3)]
        teachers = ['teacher'+str(i) for i in range(3)]
        contents = ['content'+str(i) for i in range(3)]

        lessons = []
        for i in range(3):
            l = Lesson(i, titles[i], teachers[i], contents[i])
            lessons.append(l)

        self.assertEqual(lessons[0].title, 'title0')
        self.assertEqual(lessons[0].teacher, 'teacher0')
        self.assertEqual(lessons[0].content, 'content0')


class TestAppInteraction(unittest.TestCase):

    def test_lesson_get(self):
        lesson0 = get('http://localhost:5000/0').json()
        self.assertEqual(lesson0['id'], 0)

    def test_lessons_get(self):
        lessons = get('http://localhost:5000/').json()
        self.assertTrue(len(lessons) > 0)
        self.assertEqual(lessons[0]['id'], 0)
        
if __name__ == '__main__':
    unittest.main()
