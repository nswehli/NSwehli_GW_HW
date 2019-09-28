# @TODO: Your code here
name={
      "name": "Nedal",
      "Age": "42",
      "Hobbies": " None",
      "Waking_up":{
              "Weekdays":"7am",
              "Weekends":"8am" 
      }
}
#print(f'{name["name"]} is {name["Age"]} years old. He wakes up at {name["Waking_up"][2]} in weekends')

#print(f'{another_actor["name"]} was in {another_actor["best movies"][2]}')
      
print(f'{name["name"]} is {name["Age"]} years old. He wakes up at {name["Waking_up"]["Weekdays"]}')