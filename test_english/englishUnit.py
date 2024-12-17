import unittest
from symtable import Class

from main_english import Teacher,DisciplineTeacher


class TestTeacher(unittest.TestCase):
    teacher_test = Teacher("Антон", "Алексеевич", "высшее", "3 года")
    disp_teacher = DisciplineTeacher("Сергей", "Краснов", "высшее", "3 года","литература","стажер")
    def test_teacher_init(self):
        self.assertEqual(Teacher.teaches[0], ('Антон', 'Алексеевич'))

    def test_last_name(self):
        self.assertEqual(self.teacher_test.last_name, "Алексеевич")

    def test_education(self):
        self.assertEqual(self.teacher_test.education, "высшее")

    def test_exp(self):
        self.assertEqual(self.teacher_test.exp, "3 года")

    def test_exp_set(self):
        self.teacher_test.exp = 10
        self.assertEqual(self.teacher_test.exp, 10)

    def test_get_teacher_data(self):
        self.assertEqual(self.teacher_test.get_teacher_data(), "Антон Алексеевич Образование высшее, опыт работы 10")

    def test_add_mark(self):
        self.assertEqual(self.teacher_test.add_mark("Андрей",11), "Антон Алексеевич поставил оценку 11 студенту Андрей")


    def test_remove_mark(self):
        self.assertEqual(self.teacher_test.remove_mark("Андрей",11), "Антон Алексеевич удалил оценку 11 студенту Андрей")

    def test_give_a_consultation(self):
        self.assertEqual(self.teacher_test.give_a_consultation("654"),"Антон Алексеевич провел консультацию в классе 654")

    def test_disp_teacher_init(self):
        print(Teacher.teaches)
        self.assertEqual(len(Teacher.teaches),2)


