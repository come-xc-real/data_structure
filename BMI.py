stature = float(input("请输入你的身高(单位m):"))
weight = float(input("请输入你的体重(单位kg):"))
try:
    BMI = float(weight / stature ** 2)
except:
    print("除零错误")
if BMI < 0:
    print("数据非法")
elif BMI < 18.5:
    print("体重过小")
elif 18.5 <= BMI < 24:
    print("体重正常")
elif 24 <= BMI < 28:
    print("体重过大")
elif 28 <= BMI < 32:
    print("体重肥胖")
else:
    print("体重过胖")
print(BMI)

