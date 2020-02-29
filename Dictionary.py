# This Source Code Form is subject to the terms of the Mozilla
# Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

dictionary = ["agony", "avoid", "ape", "angel", "answer", "address", "airplane", "all","awake", "across", "airplane", "air", "agnostic"] #A
dictionary += ["beta", "bomb", "battle", "bazaar", "bike", "board", "blade", "bus", "bundle", "ballad"] #B
dictionary += ["cancer", "capsule", "code", "central", "chamber", "car", "call", "combat", "costume", "corn", "cow", "crawl", "costume", "crushboard", "cocktail"] #C
dictionary += ["deliveryman", "dawn", "demarcate", "daughter", "definitively", "disc", "divinity", "dogmatist", "doubt", "duel"] #D
dictionary += ["eater", "eat", "eye", "emoji", "essential", "exercise", "elevator", "end", "escape", "exit", "exam", "everybody", "echo"] #E

def ReturnRandomWord():
    global dictionary
    return dictionary

def AddWordToDictionary(word):
    global dictionary
    dictionary += [word]
    return dictionary