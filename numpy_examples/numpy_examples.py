height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# bmi = weight / height ** 2
bmi = []
for i in range(len(height)):
    bmi.append(round(weight[i] / height[i] ** 2, 2))

print(bmi)

# 1D - line (x)
# "2D (dimensional) - plane (x, y)"
# 3D - space (x, y, z)

users = [[1.73, 1.68, 1.71, 1.89, 1.79],
         [65.4, 59.2, 63.6, 88.4, 68.7]]

# 1. how to calc bmi of user1 (index 0)
bmi_user1 = round(users[1][0] / users[0][0] ** 2, 2)
print(bmi_user1)

# 2. how to calc bmi of user2 (index 1)
bmi_user2 = round(users[1][1] / users[0][1] ** 2, 2)
print(bmi_user2)

# 3. calculate bmi for all users using 2D list
bmi_2d = []
for i in range(len(users[0])):
    bmi_2d.append(round(users[1][i] / users[0][i] ** 2, 2))

print(bmi_2d)
