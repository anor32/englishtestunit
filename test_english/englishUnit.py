import unittest
from symtable import Class

from main_english import Teacher, DisciplineTeacher


class TestTeacher(unittest.TestCase):
    teacher_test = Teacher("Антон", "Алексеевич", "высшее", "3 года")
    disp_teacher = DisciplineTeacher("Сергей", "Краснов", "высшее", "3 года", "литература", "стажер")

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
        self.assertEqual(self.teacher_test.add_mark("Андрей", 11),
                         "Антон Алексеевич поставил оценку 11 студенту Андрей")

    def test_remove_mark(self):
        self.assertEqual(self.teacher_test.remove_mark("Андрей", 11),
                         "Антон Алексеевич удалил оценку 11 студенту Андрей")

    def test_give_a_consultation(self):
        self.assertEqual(self.teacher_test.give_a_consultation("654"),
                         "Антон Алексеевич провел консультацию в классе 654")

    def test_disp_teacher_init(self):
        self.assertEqual(len(Teacher.teaches), 2)

    def test_dicipline(self):
        self.assertEqual(self.disp_teacher.discipline, "литература")

    def test_job_title(self):
        self.assertEqual(self.disp_teacher.job_title, "стажер")

    def test_disp_teacher_data(self):
        self.assertEqual(self.disp_teacher.get_teacher_data(),"Сергей Краснов Образование высшее, опыт работы 3 года, Предмет литература, Должность стажер")

    def test_disp_add_mark(self):
        self.assertEqual(self.disp_teacher.add_mark("барамалей",10),"Сергей Краснов поставил оценку 10 студенту барамалей по Предмету литература")

    def test_disp_remove_mark(self):
        self.assertEqual(self.disp_teacher.remove_mark("барамалей",10),"Сергей Краснов удалил оценку 10 студенту барамалей по  Предмету литература")

    def test_disp_give_a_consultation(self):
            self.assertEqual(self.disp_teacher.give_a_consultation("230"), "Сергей Краснов провел консультацию в классе 230 Предмет литература, Как стажер")



    def test_hire_teacher(self):
        print(self.disp_teacher.teaches)
        self.assertEqual(self.disp_teacher.hire_teacher("Cтепан","Долгоруков"),"Cтепан Долгоруков учитель успшено добавлен")
        self.assertEqual(self.disp_teacher.hire_teacher("Cтепан","Долгоруков"),"не может быть добавлен такой учитель уже есть")

    def test_fire_teacher(self):
        self.disp_teacher.hire_teacher("Cтепан","Долгоруков")
        self.assertEqual(self.disp_teacher.fire_teacher("Cтепан", "Долгоруков"),"Cтепан Долгоруков успешно удален ")
        self.assertEqual(self.disp_teacher.fire_teacher("Cтепан", "Долгоруков"),"Cтепан Долгоруков не найден в списке не может быть удален ")





