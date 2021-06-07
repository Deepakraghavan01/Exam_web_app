from django.shortcuts import render
import pyrebase
from django.http import HttpResponse



config = {
  'apiKey': "AIzaSyCNplQAjux1Ul8HiZ0e_q1qOV3rn3PnnFs",
  'authDomain': "web-app-b12fc.firebaseapp.com",
  'databaseURL': "https://web-app-b12fc-default-rtdb.firebaseio.com",
  'projectId': "web-app-b12fc",
  'storageBucket': "web-app-b12fc.appspot.com",
  'messagingSenderId': "620345277790",
  'appId': "1:620345277790:web:c9e476e9c920392e5ea3cf",
  'measurementId': "G-3NHQF2YBQH"

}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
database = firebase.database()

# Create your views here.
def home(request):
     return render(request,'home.html')
def Admin(request):
     return render(request,'Admin/login.html')
def question_dash(request):
    return render(request,'Admin/question_dash.html')
def add_student(request):
     return render(request,'Admin/add_student.html')
def Exam(request):
     return render(request,'Admin/Exam.html')
def save_exam(request):
     course = request.POST.get('course')
     tot_qus = request.POST.get('tot_question')
     tot_mark = request.POST.get('tot_mark')
     data={
          "course":course,
          "tot_question":tot_qus,
          "tot_mark":tot_mark,
     }
     database.child("Exam_det").push(data)
     return render(request,'Admin/question_add.html')
def question_add(request):
     return render(request,'Admin/question_add.html')
def add(request):
     return render(request,'Admin/add.html')
def db(request):
     course = request.POST.get('course')
     question = request.POST.get('question')
     mark = request.POST.get('mark')
     option1 = request.POST.get('option1')
     option2 = request.POST.get('option2')
     option3 = request.POST.get('option3')
     option4 = request.POST.get('option4')
     answer = request.POST.get('ans')

     data={
       "course":course,
       "question":question,
       "mark":mark,
       "option1":option1,
       "option2":option2,
       "option3":option3,
       "option4":option4,
       "answer":answer
       }
     database.child("Question_list").push(data)
     return render(request,'Admin/question_add.html')

def view_question(request):
     list1 = []
     list2 = []
     list3 = []
     res = database.child("Question_list").get()
     for data in res.each():
          dic = data.val()
          question = dic["question"]
          mark = dic["mark"]
          course = dic["course"]
          list1.append(question)
          list2.append(mark)
          list3.append(course)
     tot = zip(list1,list2,list3)

     return render(request,'Admin/view_question.html',{"tot":tot})

def stu_det(request):
     email = request.POST.get('stu_mail')
     data = {
          "email":email
     }
     database.child("stu_list").push(data)
     return render(request,'Admin/question_dash.html')

def Student(request):
     return render(request,'Student/student.html')
def student_dash(request):
          list1 =[]
          email = request.POST.get("email")
          mail = database.child('stu_list').get()
          for data in mail.each():
              dic = data.val()
              email_db = dic["email"]
              list1.append(email_db)
          if(email in list1):
              course_det = database.child("Exam_det").get()
              list2 = []
              list3 = []
              for i in course_det.each():
                   course = i.val()
                   course_name = course["course"]
                   tot_mark = course["tot_mark"]
                   list2.append(course_name)
                   list3.append(tot_mark)
              course = zip(list2,list3)
              return render(request,'Student/student_dash.html',{"course":course})
          else:
              message = "Invalid User"
              print("Invalid User")
              return render(request,'Student/student.html',{"messages":message})
def student_exam(request):
     list1 = []
     list2 = []
     list3 = []
     list4 = []
     list5 = []
     data = database.child("Question_list").get()
     for i in data.each():
          dic = i.val()
          list1.append(dic["question"])
          list2.append(dic["option1"])
          list3.append(dic["option2"])
          list4.append(dic["option3"])
          list5.append(dic["option4"])
     value = zip(list1,list2,list3,list4,list5)
     return render(request,'Student/student_exam.html',{"val":value})
def student_mark(request):
     mark = 0
     list1 = []
     data = database.child("Question_list").get()
     for i in data.each():
          dic = i.val()
          list1.append(dic["answer"])
     for i in range(len(list1)):
         val = request.POST.get("option")
         if(val == list1[i]):
             mark+=1
     return render(request,'Student/student_mark.html',{"mark":mark})



     