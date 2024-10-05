import random as rd
word_list=['python', 'hangman', 'programming', 'challenge', 'developer','apple','butterfly','rainbow','Rhino','Diamond','Lily','xylophone','watermellon','zebra','australia']
chosen=rd.choice(word_list)
disp=[]
for i in chosen:
     disp.append('_')
print(disp)
count=0
count1=0
flag1=0
while flag1==0:
 
  player=input("Enter your letter : ")
  for i in range(0,len(chosen),1):
    if(player==chosen[i] and chosen[i]!=disp[i]):
        print("Correct letter  guessed")
        disp[i]=player
        count1+=1
        flag=0
        print(disp)
        break
    else:
      flag=1
  if flag==1:
        print("wrong letter guessed")
        print("number of chances left : ",(5-count))
        count+=1
        if(count==1):
            print('     |')
            print('     0')
        elif(count==2):
            print('     |')
            print('     0')
            print('    / ')
        elif(count==3):
            print('     |')
            print('     0')
            print('    /|')  
            
        elif(count==4):
            print('     |')
            print('     0')
            print('    /|\ ')
        elif(count==5):
            print('     |')
            print('     0')
            print('    /|\ ')  
            print('    /   ')
        elif(count==6):
            print('     |')
            print('     0')
            print('    /|\ ')  
            print('    / \ ')
  if(count==6):
            print("You lose")
            print("correct word is : ",chosen)
            flag1=1
  elif(count1==(len(chosen))):
            print("You won")
            flag1=1
        
         
