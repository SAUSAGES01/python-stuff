word = 'sausages'
letters = len(word)
lettersGuessed = []
howManyGuessed = len(lettersGuessed)
guess = input('guess a letter')
a = 0

    


def checkIfGuessed():
  global howManyGuessed, lettersGuessed, guess, letters, a
  guessed = False
  for i in range(howManyGuessed):
    if guess == lettersGuessed[a]:
      guessed = True
      a += 1

    else:
      a += 1

  if guessed == False:
    lettersGuessed.append(guess)

  else:
    print('you have already guessed that')


while True:
  for i in range(letters):
    print('_ ', end='')
  checkIfGuessed()
      