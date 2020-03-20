# This Source Code Form is subject to the terms of the Mozilla
# Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

dictionary = ["agony", "avoid", "ape", "angel", "answer", "address", "airplane", "all","awake", "across", "airplane", "air", "agnostic"]                                                #A
dictionary += ["beta", "bomb", "battle", "bazaar", "bike", "board", "blade", "bus", "bundle", "ballad"]                                                                                 #B
dictionary += ["cancer", "capsule", "code", "central", "chamber", "car", "call", "combat", "costume", "corn", "cow", "crawl", "costume", "crushboard", "cocktail", "crown"]             #C
dictionary += ["deliveryman", "dawn", "demarcate", "daughter", "definitively", "disc", "divinity", "dogmatist", "doubt", "duel"]                                                        #D
dictionary += ["eater", "eat", "eye", "emoji", "essential", "exercise", "elevator", "end", "escape", "exit", "exam", "everybody", "echo"]                                               #E
dictionary += ["factory", "fall", "fake", "front", "font", "face", "fear", "folk", "food", "flavour", "false", "found", "flash", "fate", "frame", "fury"]                               #F
dictionary += ["gas", "goodbye", "good", "grid", "gate", "game", "god", "global", "graphic", "growth", "group"]                                                                         #G
dictionary += ["hero", "hot", "hate", "hope", "heat", "home", "honey", "hunt", "health", "head", "hard" ]                                                                               #H
dictionary += ["iron", "idea", "influence", "intensive", "irony", "indie"]                                                                                                              #I
dictionary += ["job", "joy", "judge"]                                                                                                                                                   #J
dictionary += ["kid", "keep", "know"]                                                                                                                                                   #K
dictionary += ["labour", "law", "lane", "laser", "late", "lenght", "light", "link"]                                                                                                     #L
dictionary += ["mask", "make", "moon", "mate", "mint", "mess", "mass", "mistake"]                                                                                                       #M
dictionary += ["nature", "nose", "near", "nothing", "note", "name", "naive", "noble", "nice", "new"]                                                                                    #N
dictionary += ["obstacle", "open", "orbite", "old", "odd", "operator"]                                                                                                                  #O
dictionary += ["paradox", "pay", "pale", "premium", "power", "print", "product", "pulse", "public"]                                                                                     #P
dictionary += ["quit", "quick", "quad"]                                                                                                                                                 #Q
dictionary += ["race", "rose", "rate", "real", "risk", "run", "reporter", "right"]                                                                                                      #R
dictionary += ["song", "snow", "shame", "show", "snippet", "snake", "silver", "strategy", "social"]                                                                                     #S
dictionary += ["time", "town", "trick", "tough", "test", "throw", "tron", "type", "toaster"]                                                                                            #T
dictionary += ["user", "upcast", "union", "use"]                                                                                                                                        #U
dictionary += ["valley", "vendetta", "violin", "visa", "void"]                                                                                                                          #V
dictionary += ["want", "wave", "weather", "work"]                                                                                                                                       #W
dictionary += ["xylophone"]                                                                                                                                                             #X
dictionary += ["yard"]                                                                                                                                                                  #Y
dictionary += ["zero", "zone", "zenith"]                                                                                                                                                #Z

def ReturnRandomWord():
    global dictionary
    return dictionary

def AddWordToDictionary(word):
    global dictionary
    dictionary += [word]
    return dictionary

# For TailWord:
PreviousWord = [""]
DejaVu = []

def PreviousWordIs(word, text):
    global PreviousWord
    del PreviousWord[0:len(PreviousWord)-1]
    del PreviousWord[0]
    global DejaVu
    DejaVu += [text]
    DejaVu += [word]
    PreviousWord += word
    return PreviousWord