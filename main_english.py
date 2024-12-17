class Teacher:
    teaches  = []
    def __init__(self, name, last_name, education, exp):
        self.name = name
        self.__last_name = last_name
        self.__education = education
        self.__exp = exp
        Teacher.teaches.append((name,last_name))
    @property
    def last_name(self):
        return self.__last_name

    @property
    def education(self):
        return self.__education

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        self.__exp = exp

    def get_teacher_data(self):
        return f"{self.name} {self.__last_name} Образование {self.__education}, опыт работы {self.__exp}"

    def add_mark(self, student, mark):
        return f"{self.name} {self.__last_name} поставил оценку {mark} студенту {student}"

    def remove_mark(self, student, mark):
        return f"{self.name} {self.__last_name} удалил оценку {mark} студенту {student}"

    def give_a_consultation(self, classwork):
        return f"{self.name} {self.__last_name} провел консультацию в классе {classwork}"

class DisciplineTeacher(Teacher):
    def __init__(self, name, last_name, education, exp, discipline, job_title):
        super().__init__(name, last_name, education, exp)
        self.__discipline = discipline
        self.__job_title = job_title
        Teacher.teaches.append((name,last_name))

    @property
    def discipline(self):
        return self.__discipline

    @property
    def job_title(self):
        return self.__job_title

    def get_teacher_data(self):
        return f"{super().get_teacher_data()}, Предмет {self.discipline}, Должность {self.job_title}"

    def add_mark(self, student, mark):
        return f"{super().add_mark(student, mark)} по Предмету {self.discipline}"

    def remove_mark(self, student, mark):
        return f"{super().remove_mark(student, mark)} по  Предмету {self.discipline}"

    def give_a_consultation(self, classwork):
        return f"{super().give_a_consultation(classwork)} Предмет {self.discipline}, Как {self.job_title}"

    def hire_teacher(self,nameTeacher,lastNameTeacher):
        if (nameTeacher,lastNameTeacher) not in Teacher.teaches:
            Teacher.teaches.append((nameTeacher,lastNameTeacher))
            return f"{nameTeacher} {lastNameTeacher} учитель успшено добавлен"
        else:
            return "не может быть добавлен такой учитель уже есть"
    def fire_teacher(self,nameTeacher,lastNameTeacher):
        if (nameTeacher,lastNameTeacher)  in Teacher.teaches:
            Teacher.teaches.remove((nameTeacher,lastNameTeacher))
            return f"{nameTeacher} {lastNameTeacher} успешно удален "
        else:
            return f"{nameTeacher} {lastNameTeacher} не найден в списке не может быть удален "
# вы мне впрошлый раз написали чтобы  я улучшил не переписывал методы полностью
# а использовал super()
# я исправил  теперь я использую суперкласс внутри методов
# я надеюсь я верно понял и именно это иммелось ввиду жду комментарий про этот момент



# вызовы коментирую чтобы не портить покрытие тестов

# # Создание объекта Teacher и отладка
# programer = Teacher("Дмитрий", "Сульжиц", 'МГУ', "10 лет")
# print(programer.get_teacher_data())
# print(programer.add_mark("Андрей Никанов", "12"))
# print(programer.remove_mark("Иван Иванов", "10"))
# print(programer.give_a_consultation("python426"))
#
#
# # Создание объекта DisciplineTeacher
# chemist = DisciplineTeacher("Волтер", "Вайт", "Высшее", "3", "Химия", "учитель")
# print(chemist.get_teacher_data())
# print(chemist.add_mark("джесси", "5"))
# print(chemist.remove_mark("джесси", "5"))
# print(chemist.give_a_consultation("сhemistry782"))
#
# # новые функции
#
# print(chemist.hire_teacher("иван","долгович"))
#
# print(chemist.fire_teacher("иван","долгович"))
