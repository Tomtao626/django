from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Score, Student, Course
from django.db.models import Avg, Count, Sum, Q
from django.db import connection


def index(request):
    # 查询平均成绩大于60分的同学的id和平均成绩；
    students = Student.objects.annotate(score_avg=Avg("score__number")).filter(score_avg__gt=60).values('id', 'score_avg')
    student_score = [dict(id=student['id'], score_avg=student['score_avg']) for student in students]
    print(student_score)
    print(connection.queries[4]['sql'])
    return HttpResponse("successfully")


def index2(request):
    # 查询所有同学的id、姓名、选课的数量、总成绩；
    students = Student.objects.annotate(course_nums=Count("score__id"), total=Sum("score__number")).values('id',
                                                                                                        'name', 'course_nums', 'total')
    student_score = [
        dict(id=student['id'],
             name=student['name'],
             course_nums=student['course_nums'],
             total=student['total']) for student in students]
    print(student_score)
    print(connection.queries)
    return HttpResponse("successfully")


def index3(request):
    # 查询姓“李”的老师的个数；
    teacher_count = Teacher.objects.filter(name__startswith='李').count()
    print(teacher_count)
    return HttpResponse("successfully")


def index4(request):
    # 查询没学过“李老师”课的同学的id、姓名；
    students = Student.objects.exclude(score__course__teacher__name='李老师').values('id', 'name')
    for student in students:
        print(student)
    return HttpResponse("successfully")


def index5(request):
    # 查询学过课程id为1和2的所有同学的id、姓名
    students = Student.objects.filter(score__course__id__in=[1, 2]).values('id', 'name').distinct()
    for student in students:
        print(student)
    return HttpResponse("successfully")


def index6(request):
    # 查询学过“黄老师”所教的“所有课”的同学的id、姓名；
    # 先查询出每位学生学习的黄老师课程的数量
    # 在课程表中查询出黄老师教的课程的数量
    students = Student.objects.annotate(learn_nums=Count("score__course", filter=Q(score__course__teacher__name='黄老师'))
                                        ).filter(learn_nums=Course.objects.filter(teacher__name='黄老师').count()).values('id', 'name')
    for student in students:
        print(student)
    return HttpResponse("successfully")


def index7(request):
    # 查询所有课程成绩小于60分的同学的id和姓名；
    students = Student.objects.filter(score__number__lt=60).values('id', 'name').distinct()
    for student in students:
        print(student)
    return HttpResponse("successfully")


    # 查询没有学全所有课的同学的id、姓名；
    #
    # 查询所有学生的姓名、平均分，并且按照平均分从高到低排序；
    #
    # 查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分；
    #
    # 查询没门课程的平均成绩，按照平均成绩进行排序；
    #
    # 统计总共有多少女生，多少男生；
    #
    # 将“黄老师”的每一门课程都在原来的基础之上加5分；
    #
    # 查询两门以上不及格的同学的id、姓名、以及不及格课程数；
    #
    # 查询每门课的选课人数；

