
# 1) შევქმნათ სია რომელშიც გვექნება რომელშიც გვექნება დადებითი და უარყოფითი რიცხვები. გავფილტროთ, უნდა დავაბრუნოთ ორი სია ერთში მხოლოდ დადებითი რიცხვები მეორეში მხოლოდ უარყოფითი რიცხვები



numbers = [-1 , 5 , -6 , 7 , -43 , -87 , -32, 92]
positive_numbers = []
negative_numbers = []
for i in range (len(numbers)):
    if numbers[i] == 0:
      continue
    elif   numbers[i] < 0:
      negative_numbers.append(numbers[i])
    else : 
      positive_numbers.append(numbers[i])
print("this is positive numbers:" , positive_numbers)
print("this is negative numbers:" , negative_numbers )