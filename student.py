class Student:
    def __init__(self, name, student_id, age, grade):
        """
        Initialize a Student object
        
        Args:
            name (str): Name of the student
            student_id (str): Student ID
            age (int): Age of the student
            grade (str): Grade/Class of the student
        """
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grade = grade
        self.subjects = []  # List to store subjects
        self.gpa = 0.0      # Grade Point Average
    
    def get_name(self):
        """Get student name"""
        return self.name
    
    def get_student_id(self):
        """Get student ID"""
        return self.student_id
    
    def get_age(self):
        """Get student age"""
        return self.age
    
    def get_grade(self):
        """Get student grade"""
        return self.grade
    
    def add_subject(self, subject):
        """Add a subject to student's subjects list"""
        self.subjects.append(subject)
    
    def get_subjects(self):
        """Get all subjects"""
        return self.subjects
    
    def set_gpa(self, gpa):
        """Set student's GPA"""
        self.gpa = gpa
    
    def get_gpa(self):
        """Get student's GPA"""
        return self.gpa
    
    def study(self, subject):
        """Student studies a subject"""
        return f"{self.name} is studying {subject}"
    
    def __str__(self):
        """String representation of the Student object"""
        return f"Student: {self.name} (ID: {self.student_id}, Age: {self.age}, Grade: {self.grade}, GPA: {self.gpa})"


# สร้าง Object student1 จาก Class Student (ของจริงใน RAM)
if __name__ == "__main__":
    # สร้าง student1 object
    student1 = Student("สมชาย ใจดี", "S001", 18, "ม.6")
    
    # ตั้งค่าเพิ่มเติม
    student1.add_subject("คณิตศาสตร์")
    student1.add_subject("วิทยาศาสตร์")
    student1.add_subject("ภาษาอังกฤษ")
    student1.set_gpa(3.5)
    
    # แสดงข้อมูล student1
    print("=== ข้อมูล Student1 ===")
    print(student1)
    print(f"วิชาที่เรียน: {student1.get_subjects()}")
    print(student1.study("คณิตศาสตร์"))
    
    # สร้าง student2 เพิ่มเติม
    student2 = Student("สมหญิง รักเรียน", "S002", 17, "ม.5")
    student2.add_subject("ภาษาไทย")
    student2.add_subject("สังคมศึกษา")
    student2.set_gpa(3.8)
    
    print("\n=== ข้อมูล Student2 ===")
    print(student2)
    print(f"วิชาที่เรียน: {student2.get_subjects()}")
    print(student2.study("ภาษาไทย"))
