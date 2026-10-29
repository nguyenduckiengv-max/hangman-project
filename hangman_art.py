import random
danhsach=["apple","banana","peanut","coconut","pinapple"]
hangman_art={0:("   ",
               "   ",
               "   "),
            1:(" O ",
               "   ",
               "   "),
            2:(" O ",
               " | ",
               "   "),
            3:(" O ",
               " | ",
               "/  "),
            4:(" O ",
               "/|\\ ",
               "   "),
            2:(" O ",
               "/|\\",
               "/  "),
            3:(" O ",
               "/|\\",
               "/ \\ ")}
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
def display_hint(hint):
    print("|".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer= random.choice(danhsach)
    hint=["_"]*len(answer)
    wrong_guesses= 0
    guessed_letter= ()
    is_running=True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess= input("Enter a letter : ").lower()
        if guess in answer:
            for i in range(len(answer)):
                if guess== answer[i]:
                    hint[i]=guess

if __name__ == "__main__":
    main()