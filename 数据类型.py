height =float(input("请输入你的身高（米）："))    # input 给的是文字，要转换成数字，用什么函数？
weight =float(input("请输入你的体重（公斤）："))
bmi = bmi = weight / height ** 2          # 填两个运算符：除号和乘号（也可以用 ** 乘方写法）
print("你的 BMI 是：" + str(bmi))                  # ⚠️ 灵魂考点在这里：bmi 是数字，加号左边是文字，怎么办？
