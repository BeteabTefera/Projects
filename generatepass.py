'''
challenge: write a python function to generate passpharses
INput: Number of words in passphrase
OUtput: string of random words, seberated by spaces

so you roll a dice to get a sequence of five random numbers
in my case i don't have all 7000 of em but what i know is that 
they all are 6sided 5x dice outcomes
    - i need to randomize 5x and look for that
'''
import random
phraselist = [ (16655,"clause"),
 (16656,"claw"),
 (16661,"clay"),
 (16662,"clean"),
 (16663,"clear"),
 (16664,"cleat"),
 (16665,"cleft"),
 (16666,"clerk"),
 (21111,"clich"),
 (21112,"click"),
 (21113,"cliff"),
 (21114,"climb"),
 (21115,"clime"),
 (21116,"cling"),
 (21121,"clink"),
 (21122,"clint"),
 (21123,"clio"),
 (21124,"clip"),
 (21125,"clive"),
 (21126,"cloak"),
 (21131,"clock"),
 (11111,"a"),
(11112,	"a&p"),
(11113,	"a's"),
(11142,	"abc"),
(11143,	"abe"),
(11144,	"abed"),
(11145,	"abel"),
(11146,	"abet"),
(11151,	"abide"),
(11152,	"abjec"),
(11153,	"ablaz"),
(11154,	"able"),
(11155,	"abner"),
(11156,	"abo"),
(11161,	"abode"),
(11162,	"abort"),
(11163,	"about"),
(11164,	"above"),
(11165,	"abrad")]
phraselist = dict(phraselist)
def generate_passpharase(num:int):
    ans = ""
    while num:
        randomDiceDigit = ('').join([str(random.randint(1,6)) for x in range(5)])
        randomDiceDigit = int(randomDiceDigit)
        if randomDiceDigit in phraselist:
            ans += phraselist[randomDiceDigit] + " "
            num -=1
    return ans[:-1]
print(generate_passpharase(10))
