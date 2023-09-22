#2.จงเขียนโปรแกรมPython ของโปรแกรมคำนวณหาค่าเฉลียของคะแนนจากการสอบ 3 ครั้ง 
#โดยรับค่า รหัสนักเรียน ชื่อนักเรียน และคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์ 
#แล้วแสดงผลค่าเฉลี่ยที่คำนวณได้ทางหน้าจอ


def inputdata ():
    user_password = int(input("ป้อนรหัสนักเรียน : "))
    user_name = str(input("ป้อนชื่อนักเรียน : "))
    user_score1 = int(input("ป้อนคะแนนสอบครั้งที่ 1 : "))
    user_score2 = int(input("ป้อนคะแนนสอบครั้งที่ 2 : "))
    user_score3 = int(input("ป้อนคะแนนสอบครั้งที่ 3 : "))
    return user_score1 , user_score2 , user_score3 , user_name , user_password

def cal (user_score1 , user_score2 , user_score3):
    score_all = (user_score1 + user_score2 + user_score3) / 3 
    return score_all

def calandshow ( user_score1 , user_score2 , user_score3 , user_name , user_password , score_all):
    print (f"รหัสนักเรียน : {user_password}")
    print (f"ชื่อนักเรียน : {user_name}")
    print (f"คะแนนลำดับที่ 1 : {user_score1} | คะแนนลำดับที่ 2 : {user_score2} | คะแนนลำดับที่ 3 : {user_score3}")
    print (f"คะแนนสอบ 3 ครั้งเฉลี่ยได้ : {score_all:.2f}")
    return score_all

print ("***---------------------------------------------------------------------***")
user_score1 , user_score2 , user_score3 , user_name , user_password = inputdata()
print ("***---------------------------------------------------------------------***")
calandshow (user_score1 , user_score2 , user_score3 , user_name , user_password , cal (user_score1 , user_score2 , user_score3))
print ("***---------------------------------------------------------------------***")

