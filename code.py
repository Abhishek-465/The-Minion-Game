def minion_game(string):
    vowel = 'AEIOU'
    StuartScore = 0
    KevinScore = 0
    l = 0
    l = len(string)
    for i in range(l):
        if string[i] not in vowel:
            
            StuartScore += l - i
        else:
            
            KevinScore += l - i
    if StuartScore > KevinScore:
        print("Stuart", StuartScore)
    elif StuartScore < KevinScore:
        print("Kevin", KevinScore)
    else:
        print("Draw") 
    return
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
