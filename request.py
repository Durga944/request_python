import requests
import json
response = requests.get("http://saral.navgurukul.org/api/courses")
var = response.text
print(var)
print(type(var))

with open("courses.json","w") as f:
    data =json.loads(var)
    json.dump(data,f,indent=4)

availableCourses = (data["availableCourses"])
print(availableCourses)
index=0
empty1=[]
empty2=[]
for i in availableCourses:
    print((index)," ",i["name"],i["id"])
    empty1.append(i["id"])
    empty2.append(i["name"])
    index=index+1


user = int(input("enter any id:-"))
id=empty1[user]
resofexercise=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises")
var2=resofexercise.text
with open("exercises.json","w") as f:
    d=json.loads(var2)
    json.dump(d,f,indent=4)

req=(d["data"])
 
print("main courses",empty2[user])

c=0
empty_slug=[]
for i in req:
    print(c," ",i["name"])
    empty_slug.append(i["slug"])
    c=c+1
    if len(i["childExercises"]):
        c2=0
        for j in i["childExercises"]:
            print(c2," ",j["name"])
            c2=c2+1
    else:
        print("[]")
print(empty_slug)

user1=int(input("enter any slug:-"))
b=empty_slug[user1]
print(b)

slug = requests.get(" http://saral.navgurukul.org/api/courses/"+id+"75/exercise/getBySlug?slug=requests__using-json"+b)
z=(slug.text)
print(z)
with open("slug_id","w") as f:
    p=json.loads(z)
    json.dump(p,f,indent=4)
    print(p)

user_choise=int(input("enter what u want:- )\n1.next\n2.privious\n3.up\n4.stop"))
print(user_choise)

# if user_choise =="1" or user_choise =="next" or user_choise =="2" or user_choise == "privious" or user_choise == "3" or user_choise == "4" or user_choise == "stop":
