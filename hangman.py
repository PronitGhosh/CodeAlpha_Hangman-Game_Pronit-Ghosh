import random as rd
word_list=['python', 'hangman', 'programming']
chosen=rd.choice(word_list)
disp=[]
for i in chosen:
     disp.append('_')
for i in disp:
     print(i,end=" ")
print("\n")
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
        for i in disp:
             print(i,end=" ")
        print("\n") 
        break
    else:
      flag=1
  if flag==1:
        print("wrong letter guessed")
        print("number of chances left : ",(5-count))
        count+=1
        if(count==1):
            print('  |_____')
            print('  |   |')
            print('  |   0')
            print('  |_____')
        elif(count==2):
            print('  |_____')
            print('  |   |')
            print('  |   0')
            print('  |  / ')
            print('  |_____')
        elif(count==3):
            print('  |_____')
            print('  |   |')
            print('  |   0')
            print('  |  /|')
            print('  |_____')
            
        elif(count==4):
            print('  |_____')
            print('  |   |')
            print('  |   0')
            print('  |  /|\ ')
            print('  |_____')
        elif(count==5):
            print('  |_____')
            print('  |   |')
            print('  |   0')
            print('  |  /|\ ')
            print('  |  /   ')
            print('  |_____')

        elif(count==6):
            print('  |_____')
            print('  |   |')
            print('  |   0')
            print('  |  /|\ ')
            print('  |  / \  ')
            print('  |_____')

           
  if(count==6):
            print("You lose")
            print("correct word is : ",chosen)
            flag1=1
  elif(count1==(len(chosen))):
            print("You won")
            flag1=1
        
         
