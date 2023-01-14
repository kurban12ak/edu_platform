from django.db import models

# Create your models here.


# Таблица для категорий
class Category(models.Model):
    # СОздание столбца
    category_name = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


# Таблица для продуктов (курсы)
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_price = models.FloatField()
    course_period = models.FloatField()
    course_description = models.TextField()
    course_photo = models.ImageField(upload_to='media', null=True, blank=True)
    course_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


# Таблица корзина
class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Course, on_delete=models.CASCADE)


# Таблица для личного кабинета
class Cabinet(models.Model):
    user_id = models.IntegerField()
    user_courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True)


# Таблица акций
class Sale(models.Model):
    sale_name = models.CharField(max_length=75, null=True, blank=True)
    courses = models.ManyToManyField(Course)
    sale_start_date = models.DateField()
    sale_end_date = models.DateField()

    def __str__(self):
        return self.sale_name


# ТЕмы урока
class Programs(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    tema_uroka = models.CharField(max_length=150)
    opisaniye_tema = models.TextField()


    def __str__(self):
        return self.tema_uroka


# Таблица уровней курса
class CourseLevel(models.Model):
    course = models.ManyToManyField(Course)

    chices = (('junior', 'Начинающий'), ('middle', 'Продолжающий'), ('pro', 'Продвинутый'))

    choice = models.CharField(max_length=15, choices=chices)

    def __str__(self):
        return self.choice