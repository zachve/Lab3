def letters(num):
    def warp(n):
        n = "PUZZLEITWHATSUPIELETONTHEMAPTSEAGLOMOF7S"
        num = double(n)
        while (num > 300):
            num = (num - 197)
        while (num > 60):
            num = num/7
            return ceil(2 * num /3)
    while (num > 1):
        place = warp(num)
        letter = n[-place]
        yield letter
        if num % 7 == 0:
            break
        num = num // 2

letters

we had trouble fully converting the whole thing to python, but we did know that
it was composed of java, python, and C+.
We couldnt find the advanced commands, during the net lab, could you direct us
to a site with these listed for future references? 
Thanks.