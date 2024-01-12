# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드
class School:
    def __init__(self, school_name, school_region, student_number=0, teacher_number=0):
        self.school_name = school_name
        self.school_region = school_region
        self.student_number = student_number
        self.teacher_number = teacher_number


# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드
class Teacher:
    def __init__(self, teacher_name, subject, school):
        self.teacher_name = teacher_name
        self.subject = subject
        self.school = school
        self.school.teacher_number += 1
    def teacher_info(self):
        print(f'teacher name: {self.teacher_name}, subject: {self.subject}, school: {self.school.school_name}')
    def teach(self, student):
        student.ability += 1

# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드
class Student:
    def __init__(self, student_name, grade, school, teacher, ability=0):
        self.student_name = student_name
        self.grade = grade
        self.school = school
        self.ability = ability
        self.teacher = teacher
        self.school.student_number += 1

    def student_info(self):
        print(f"Student: {self.student_name}, Grade: {self.grade}, School: {self.school.school_name}, Ability: {self.ability}")


school = School("dankook", "jukjeon")
teacher = Teacher("jang", 'computer', school)
student = Student("zzoneddeock", 2, school, teacher)

student.student_info()
teacher.teacher_info()

teacher.teach(student)

student.student_info()