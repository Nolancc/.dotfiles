import maces.macosessental as es
import scripts.macospersonal
import scripts.windowsessental
import scripts.windowspersonal
import scripts.archpersonal
import scripts.archlightweight
print('''select your os:
        1 = windows
        2 = macos
        3 = arch linux(btw)''')
os = input("> ")
if int(os) == 1:
    print("you chose windows")
    print('''select your profile:
            1 = personal
            2 = essental''')
    profilewindows = input("> ")
if int(os) == 2:
    print("you chose macos")
    print('''select your profile:
            1 = personal
            2 = essental''')
    macprofile = input("> ")
    if int(macprofile) == 2:
        es.run()
if int(os) == 1:
    print("you chose arch(btw)")
    print('''select your profile:
            1 = personal
            2 = lightweight''')
    archprofile = input("> ")