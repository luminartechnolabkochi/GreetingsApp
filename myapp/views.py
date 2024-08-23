from django.shortcuts import render

from django.views.generic import View


# url:localhost:8000/helloworld
# method:get
# response=>helloworld.html


class HelloWorldView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"helloworld.html")


class GoodMorningView(View):

    def get(self,request,*args,**kwrags):

        return render(request,"morning.html")


class GoodAfternoonView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"afternoon.html")





def greetings_view(request,*args,**kwargs):

    return render(request,"greetings.html")



class SelfIntroView(View):

    def get(self,request,*args,**kwargs):

        data={
            "name":"sarath Babu",
            "age":21,
            "qualification":"bsc",
            "contact":4567890,
            "course":"cs"
        }

        return render(request,"selfintro.html",data)


# localhost:8000/mammooty/
# method:get

# 5Actors

class ActorView(View):

    def get(self,request,*args,**kwargs):

        data={
            "name":"Mammoty",
            "profile_pic":"https://images.indianexpress.com/2024/05/mammootty-fb.jpg",
            "age":"70",
            "dob":"345678"
        }

        return render(request,"actor_detail.html",data)




# Coursename:DjangoReactFullstack
# backendframework:pythondjango
# frontend:react
# duration:7month
   
class CourseDetailView(View):

    def get(self,request,*args,**kwargs):

        data={
            "title":"DjangoReactFullStack",
            "backend":"python django",
            "frontend":"react",
            "duration":"7month"
        }


        return render(request,"course_detail.html",data)

