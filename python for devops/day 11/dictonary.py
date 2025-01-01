# studemt_info = {
#     'name': "tejas",
#     'age': 23,
#     'class': 'btech',
#     'city':'Loni'
# }
# print(studemt_info["name"], studemt_info["class"])

ec2_instance_info =[
    {"id":"instance-001",
      "type":"t2.micro" 
    },
    {"id":"instance-002",
      "type":"t2.medium" 
    },
    {"id":"instance-003",
      "type":"t2.xlarge" 
    }
]
print(ec2_instance_info[1]["type"])