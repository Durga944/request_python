import requests
import json
print("########################>>>>>>>>>  <Welcome To The Saral Navgurukul course>  <<<<<<<<<<#####################")
web = requests.get("http://saral.navgurukul.org/api/courses")
data = web.text
print(data)
print(type(data))
print(web.status_code)
with open("data.json","w") as file:
    data1=json.loads(data)
    print(data1)
    print(type(data1))
    json.dump(data1,file,indent=4)
    course_list=(data1["availableCourses"])
    print(course_list)
    id_list=[]
    course1=[]
    course_index=0

    while course_index<len(course_list):
        course_name =  course_list[course_index]["name"]
        print((course_name))
        course_id =course_list[course_index]["id"]
        id_list.append(course_id)
        course1.append(course_name)
        print(course_index ,course_name,course_id)
        course_index=course_index+1
    print(id_list)
    print( course1)

print("\n")
print("#########################>>>>>>>>> <Welcome To Saral Exercise> <<<<<<<<<<######################################")
print("\n")
user_id = int(input("Enter any id No.:-"))
web1 =  "http://saral.navgurukul.org/api/courses/"+(id_list[user_id])+"/exercises"
req = requests .get(web1)
web_data = req.text
with open("exercises.json","w") as f:
    data2 = json.loads(web_data)
    json.dump(data2,f,indent=4)
exercises = (data2['data'])
print(exercises)

parent_index=0
while parent_index<len(exercises):
    parent_Exercises = exercises[parent_index]["name"]
    childExerciseslist = exercises[parent_index]["childExercises"]
    print(parent_index+1,parent_Exercises)
    child_index=0
    while child_index<len(childExerciseslist):
        if "parent_exercises_id" in childExerciseslist[child_index]:
            print(" ",child_index+1," ",childExerciseslist[child_index]['name'])
        else:
            print("[]")
        child_index=child_index+1
    parent_index=parent_index+1

    
    






