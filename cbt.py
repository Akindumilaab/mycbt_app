import time as tm
num_students =int(input(f'Input the number of registered student: '))
students = []
for each in range(num_students):
    user =input(f'Enter student {each + 1} name: ')
    students.append(user)
print(students)
score = 0
for stud in students:
    print(f"{stud} take your test")
    question1 = '1. What is the capital of osun state\na.) Oshogbo b.) Ife c.)Ilesha'
    print(question1)
    ans = input('Answer: ').strip().lower()
    if ans == 'a':
        print('Correct')
        score += 5
    else:
        print('Incorrect')
    question2 = "2. What year did Nigeria gain independent. \n a. 1920 \n b. 1940\n c.1960 "
    print(question2)
    ans = input('Answer: ').strip().lower()
    if ans == 'c':
        print('Correct')
        score += 5
    else:
        print('Incorrect')
    question3 = "3. What is the colour of Nigeria flag?\n a. White\n b. Green\n c. Green nd white "
    print(question3)
    ans = input('Answer: ').strip().lower()
    if ans == 'c':
        print('Correct')
        score += 5
    else:
        print('Incorrect')
    question4 = "4. Who designed the Nigeria flag\n a. Titi Olayemi\n b. Taiwo Akinkunmi\n c. You\nans: "
    print(question4)
    ans = input('Answer: ').strip().lower()
    if ans == 'b':
        print('Correct')
        score += 5
    else:
        print('Incorrect')
    print(f"your final score is {score}/20")
    print(score)
    if score == 20:
     print(f'what an excellent result')
     tm.sleep(2)
     print('Congratulation, keep it up')
    else:
     print(f'You tried but you can do better!')