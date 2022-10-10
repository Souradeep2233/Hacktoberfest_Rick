secret_number=2003
guess_count=0
guess_limit=3
while guess_count< guess_limit :
    guess=int(input('GUESS: '))
    guess_count+=1
    if guess==secret_number:
     print('you win')
     break
    if guess_count==3:
     print('THE SECRET NUMBER IS 2003')
     break
    else:
        print('YOU FAILED')



