'''def Is_not_empty_list(values):
  return (isinstance(values, list) and (len(values)!=0))'''

def  Consecutive_Values_Difference_is_less_Than_maxDelta(value, nextValue, maxDelta):
  return(nextValue - value < maxDelta)

def reports_sudden_jump_in_reading(values,maxDelta):
  #if(Is_not_empty_list(values)):
  if(values!=None):
    last_but_one_reading = len(values) - 1
    for i in range(last_but_one_reading):
      if(not Consecutive_Values_Difference_is_less_Than_maxDelta(values[i], values[i + 1], maxDelta)):
        return False
    return True


