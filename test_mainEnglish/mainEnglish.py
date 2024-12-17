import unittest

from mainEnglish import Teacher


class TestTeacher(unittest.TestCase):
    teacher_test = Teacher( "Антон","Алексеевич","высшее","3 года")

    def test