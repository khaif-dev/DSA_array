
# # Let us say your expense for every month are listed below,
# # January - 2200
# # February - 2350
# # March - 2600
# # April - 2130
# # May - 2190
# # Create a list to store these monthly expenses and using that find out,
# monthlyExpense = [2200,2350,2600,2130,2190]
# print(monthlyExpense)

# # 1. In Feb, how many dollars you spent extra compare to January?
# febExtra = monthlyExpense[1]- monthlyExpense[0] #o(1): its a direct index access
# print(febExtra)

# # 2. Find out your total expense in first quarter (first three months) of the year.
# Q1Expense = monthlyExpense[0] + monthlyExpense[1] + monthlyExpense[2] #o(1): its a direct index access
# print(Q1Expense)

# # 3. Find out if you spent exactly 2000 dollars in any month
# checkFor2000 = 2000 in monthlyExpense 

# #in is like a for loop having to iterate through the list therefore a o(n) notation
# print(f"Is 2k expenses in any month?: {checkFor2000}")

# # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# monthlyExpense.append(1980) #o(1)
# print(monthlyExpense)

# # 5. You returned an item that you bought in a month of April and
# # got a refund of 200$. Make a correction to your monthly expense list
# # based on this
# monthlyExpense[3] = monthlyExpense[3] - 200 #o(1)
# print(f"Final expenses: {monthlyExpense}") 

# #You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']

# # Using this find out,
# # 1. Length of the list
# print(len(heros)) #o(1): Python lists store their length internally
# # 2. Add 'black panther' at the end of this list
# heros.append('black panther') 
# print(heros)
# # 3. You realize that you need to add 'black panther' after 'hulk',
# #    so remove it from the list first and then add it after 'hulk'
# heros.remove("black panther")#o(n): has to iterate the list to find the element before removing it.
# heros.insert(3,"black panther")#o(n): have to shift elements in the list to the right
# # 4. Now you don't like thor and hulk because they get angry easily :)
# #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# #    Do that with one line of code.
# heros[1:3]=['doctor strange'] #o(n): shifts items to the left
# # 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
# #print(dir(heros))
# heros.sort() #o(logn) 
# print(heros)

max_Num = int(input("Max number:"))
odd_Nums = [num 
            for num in range(1, max_Num) 
            if num % 2 != 0]
print("Odd numbers between 1 and", max_Num, "are :", odd_Nums)

