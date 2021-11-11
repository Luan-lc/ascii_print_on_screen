import pygame
from time import sleep

img_text = r'''
                         ...                             |     |    |   |
    -`''-  _        ..########o...                       |     |    |   |
 _.'     `: \     ,##8#########8##o,,     (      (       `|    |    |   |
/ :  ___,-+-'   .#######8##8###8###8##,    )ailor )aturn  |    |    |   |
`-+-'     ;   ,#8###########8#8########,,                 `|   `|   |   `|
   `-...-'   :#88####8##8###########8###.,                 |    |  |'    |
            .HXX8X88X#8XX########XX8X8XX#;,                `|   |  |     |
           ,#O#X8888#88###########X####8X8,         _       `|  `\/'   ,/
          :8##88##X######8#8######X######8#:      _| |__     `|      ,/
         .######8##8####8)#)#(i#88####8####.:    |_   __|     `|    /
       .,#88##8#88###H8I~-_  _-~8+8##8####8#,:     | |___    __.----._
      :=#X##8#######,# ~-._()_.-~ ##########.,:    |  __ \   L__    __|
    .:I8##88####88#:;_--__    __--_,:#88#####),:   | |  \ |     |--|
   .:=8#XX#####88#LH =#O#\    /O##\i)##8######+:   | |  | \__  |'  `|
 .':###X888###8#8#O) \##@/    \##=/#H8###8####.,:  |_|  `\___| `|--|'
.':#####8####888L;;I,       |      #8###8##8###,.,              |  |
:.88Li######8#888#,H.     .__,    :8##88#####8##o:             |'  `|
:88X:##88##8##8#8##O8,           _8###########8#.8.           .|    |
8X#+#888#8##8#8#H.###8#,_      _-'8##=#####88#XX,o:           | \__/  _
X#..8#8##8##8888..8##8#8#-.__.-X#88##=8#####8#8#.,;           `.|__|-' |
'   HH8###;##8##,+888#L#|__  __|##88##;8###8##X'               ||(__- |'
_____                   |__()__|                _____          .|.:@#/_
\    `---.________.-----'      `-----._____.---'    /          ||._--' |
 \           oOOOOOOOOOOo__      ___oOOOOOOOOo    _/          | |(_----|
  \_.--_        oOOOOOOOOo -   --   oOOOOOOo __.-'            | |(_--__)
 _-:_-'           oOOOOOOOo        oOOOOOOo    `-_            | |.:(__ )
<::<_      _        oOOOOOOo       oOOOOo |       -_          `||.:@#_/
 ~-_:-__.-':'      xXXXxoOOOo ,|, oOOOoxXXXx _______\         |||.:@#|
    -_|    |        xXXXXXXXXx\|/.xXXXXXXXx  \ \             / `|.:@#|                  
      |   |'   _-.  xXXXXXxx--=O=--xxXXXXx|___| \           /  .|.:@#|
      |   |__-':/    xXXxxXXx'/|\`.XXxxxXX:.  '  \        ./  .:|.:@#|
      |     :::||    xxxXXXXx.'|`.xXXXXXxxx::.    \      /   .::|.:@#|
      |     :::||_  xxXXXXXXXx/'\_xXXXXXXXXx::.    \    /   .::/|.:@#|
      |    :::|' \`--xXXXXXXXx     xXXXXXx  \::.    \  /   .::/ |.:@#|
      |    :::|   \   xXXXXXX      xXXXx     \::.   /\/   .::/  |.:@#|
      |    ::|xx   \    xXx         xx        \::. /oO|  .::/   |.:@#|
     |'   .::|XXXXxx|    `          '|   xxxxx \::/OoOO\.::/    |.:@#|
     |    ::|XXXXXXX|                |xXXXXXx   \|oOOooOOOOo    |.:@#|
 ,-__|__ .::|XXXXXX/__              |_XXXXXx      OoooOoooooo   |.:@#|
 \ooooOOo::|XXXXXX/__ \,            | \XXXx       oOOOooOOOO    |.:@#|
  \OOOoooooo|XxoOOOo.\. \          / ./oOOoXXXXXx   oOOOoooo    |.:@#|
   |OOOOOOOO|oOOOOOOOo.\ \,       / /oOOOOOOoXXx       oOOo.    |.:@#|
   |oooooooo|OOOOOOOOOOo.\ \     / /oOOOOOOOOOOOo [ -Tim Park ] |.:@#|
'''


#Create a function that blit the text character by character to the screen with pygame
def blit_ascii_text(text, x, y, font, color):
    sleep(3)
    for char in text:
        if char == '\n':
            x = 0
            y += font.get_height()
        else:
            window.blit(font.render(char, True, color), (x, y))
            x += font.size(char)[0]
            pygame.display.update()


# init pygame
pygame.init()

# Set full screen window
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Font properties
text_height = 23
font = pygame.font.SysFont("Courier", text_height)

#Loop pygame
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
         
    #Calling the funcion
    blit_ascii_text(img_text, 0, 0, font, (255, 255, 0))

pygame.quit()

