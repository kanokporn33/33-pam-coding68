score = float(input("กรอกคะแนน: "))

if score >= 80  :
   grade = "A"
elif score >= 70 :
   grade = "B"
elif score >= 60 :
   grade = "C"
elif score >= 50 :
  grade = "D"
else :
  grade = "F"
print ("เกรดที่ได้ =", grade)
