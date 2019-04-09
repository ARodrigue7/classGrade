# 2 quizzes up to 10 points
# 1 midterm/1 final up to 100 points
# final exam = 50%, midterm = 25%, two quizzes = 25%
# 90+ = A
# 80 > 90 = B
# 70 > 80 = C
# 60 > 70 = D
# -60 = F

quizz1 = int(input('What was your grade for quizz 1?'))
while quizz1 != -1:
   quizz2 = int(input('What was your grade for quizz 2?'))
   midterm = int(input('What was your grade for the midterm?'))
   final = int(input('What was your grade for the final?'))

   #EQUATIONS
   quizzTotal = (quizz1 + quizz2) * 1.25
   midTotal = midterm/4
   finalTotal = final/2
   grade = (quizzTotal + midTotal + finalTotal)
   
   print 'Your scored for quizz 1 was:',quizz1
   print 'Your score for quizz 2 was:',quizz2
   print 'Your score for the midterm was:',midterm
   print 'Your score for the final was:',final

   if grade > 90:
      print 'Good job you got an A'
   elif grade > 80:
      print 'You got a B'
   elif grade > 70:
      print 'You got a C'
   elif grade >60:
      print 'You got a D'
   else:
      print 'You got an F'
      
   quizz1 = int(input('What was your grade for quizz 1 or enter -1 to quit'))