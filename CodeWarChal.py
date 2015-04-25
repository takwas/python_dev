def solution(number):
  #return sum_mul_3(number) + sum_mul_5(number) + sum_mul_15(number)
  return sum_mul_all(number)
  
  
def sum_mul_all(number):
  return sum([x for x in range(number) if x%3==0 or x%5==0])
  
  
def sum_mul_3(number):
  return sum([x for x in range(number+1) if x%3==0 and x%15 != 0])
  
  
def sum_mul_5(number):
  return sum([x for x in range(number+1) if x%5==0 and x%15 != 0])
  
  
def sum_mul_15(number):
  return sum([x for x in range(number+1) if x%15==0])



print "Solution is {0}".format(solution(10))
