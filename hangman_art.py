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
def displayt_hint(hint):
    pass
def display_hint(answer):
    pass
def main():
    answer= random.choice(danhsach)
    hint=["_"]*len(answer)
    print("|".join(hint))

if __name__ == "__main__":
    main()