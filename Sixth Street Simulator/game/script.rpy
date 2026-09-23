define y = Character("You", colour ="#d397a1")
define tk = Character("Truk-tan", colour="#ADC2D6")
define b = Character("Belle", colour="#0B1964")
define w = Character("Wise", colour="#90959B")


transform slide_in:
    xalign -0.5
    yalign 1.0
    linear 0.5 xalign 0.0

label start:

    scene bg beforeisekai1
    
    show you malemaincharacter default:
        xalign 1.0
        yalign 1.0

    y "It's late again. \n{w}{i} Sigh... {/i} \n{w}..."

    y "Another day at work just to aford some groceries... {w}\n... {w}\nand buy some pulls, I guess... "

    y "Damn, I suck... Shakespear said that once I believe"

    show traktan default at slide_in

    tk "Hello"

    y "{i}Oh.{/i} {w}Hi. Is it what I think it is?"
    
    show traktan happy:
        xalign 0.0
        yalign 1.0

    tk "Yeah"

    y "...{w} \nFuck"

    show traktan happy:
        linear 0.5 xalign 1.0  

    scene bg sixthstreetnearrp with fade

    y "Agh... Fuck... {w}\n It's realy painful..."

    y "I thought it wouldn be... like that"

    show you malemaincharacter default:
        xalign 1.0
        yalign 10.0
        linear 0.2 yalign 1.0

    y "Wow... I can't believe my eyes"

    y "It's a ZZZ"

    show bele default at slide_in

    b "Hey, everything alright?"

    y "...Eh... {w}\n ...No?"

    return