def add_to_list(x):
    list1=[{"name": "Kanat", "last_name": "Erbolov", "age": 20},
    {"name": "Askar", "last_name": "Paivich", "age": 15},
    {"name": "Kairat", "last_name": "Sadva", "age": 45}
    ]     
    list1.append(x)
    return list1
print(add_to_list({"name": "jonibek", "last_name": "senimovich", "age":30}))