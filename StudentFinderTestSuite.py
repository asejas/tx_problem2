import unittest
import DataLoader
import StudentFinder


class MyTestCase(unittest.TestCase):
    def setUp(self):
        if not hasattr(self, 'students'):
            self.students = DataLoader.load_students_from_file('resources/students.json')
            self.classes = DataLoader.load_classes_from_file('resources/classes.json')
            self.students2 = DataLoader.load_students_from_file('resources/students2.json')
            self.classes2 = DataLoader.load_classes_from_file('resources/classes2.json')
            self.students3 = DataLoader.load_students_from_file('resources/students3.json')

    def test_students_in_classes_1(self):
        """First scenario for the Problem 2"""
        students_in_classes = StudentFinder.students_in_classes(self.students, self.classes)
        self.assertIsNotNone(students_in_classes)
        self.assertEqual(3, len(students_in_classes))
        self.assertIn(self.students[0], students_in_classes)
        self.assertIn(self.students[1], students_in_classes)
        self.assertIn(self.students[2], students_in_classes)
        print('==============================First scenario for the Problem 2==========================')
        print('Students: {}'.format(students_in_classes))
        print('========================================================================================')

    def test_students_in_classes_2(self):
        """Second scenario for the Problem 2"""
        students_in_classes = StudentFinder.students_in_classes(self.students2, self.classes)
        self.assertIsNotNone(students_in_classes)
        self.assertEqual(1, len(students_in_classes))
        self.assertIn(self.students2[2], students_in_classes)
        print('==============================Second scenario for the Problem 2=========================')
        print('Students: {}'.format(students_in_classes))
        print('========================================================================================')

    def test_students_in_classes_empty(self):
        """Scenario for empty result (no students in classrooms)"""
        students_in_classes = StudentFinder.students_in_classes(self.students2, self.classes2)
        self.assertIsNotNone(students_in_classes)
        self.assertEqual(0, len(students_in_classes))

    def test_student_clusters_in_classes(self):
        """Bonus scenario for Problem 2"""
        students_in_classes = StudentFinder.student_clusters_in_classes(self.students3, self.classes, 2)
        self.assertIsNotNone(students_in_classes)
        self.assertEqual(4, len(students_in_classes))
        self.assertIn(self.students3[1], students_in_classes)
        self.assertIn(self.students3[2], students_in_classes)
        self.assertIn(self.students3[3], students_in_classes)
        self.assertIn(self.students3[4], students_in_classes)
        print('==============================Bonus scenario for the Problem 2==========================')
        print('Students: {}'.format(students_in_classes))
        print('=========================================================================================')

    def test_student_clusters_in_classes_empty(self):
        """Bonus scenario with empty result (classes with less than minimum attendance) for Problem 2"""
        students_in_classes = StudentFinder.student_clusters_in_classes(self.students, self.classes, 2)
        self.assertIsNotNone(students_in_classes)
        self.assertEqual(0, len(students_in_classes))


if __name__ == '__main__':
    unittest.main()
