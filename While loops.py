
print('done')
Guess_number=5
Guess_count=3
Guess_counter=0

while Guess_counter<Guess_count:
    Guess_counter=Guess_counter+1
    guess_Answer=int(input('Enter a number between 0-9 '))
    if guess_Answer == Guess_number:
        print("You win")
        break
