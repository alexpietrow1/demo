#This file was created by Alex Pietrow
# demo
A demo project from Kids Can Code
'''
**********What I changed about the game dynamics:
The character is constantly jumping
New player function (sink): When you press 's', the character sinks downward until you hit 
another spring and bounce up
New platform function (compress): When you jump on the springs, which are the new platforms,
the spring you jumped on compresses
Mobs spawn at a faster rate
When the player hits the side or bottom of the mob, it bounces off of it in the opposite direction
The screen size is larger so more platforms spawn in a larger location range
**********What I changed about the game cosmetics
The character is a different bunny
The platforms are springs and are compressed when jumped on
Mobs are spikeballs
Background color is different
**********Challenges I faced
I had trouble making the platform uncompress after it was jumped on:
I tried getting ticks from pygame, but I could not figure out how to create a time delay between
functions without making the game lag like crazy
I wasn't sure how to make the player bounce off the mobs in all directions, only 4 directions
Since the mob is recognized as a rectangle by pygame, I wasn't sure how to make pygame
recognize it like a circle
**********Bugs
Very rarely, when the player sinks, it sinks through a platform
If you press 's' right after the player dies, the pygame window crashes
It takes a long time for the mobs to die out once they are out of view of the screen
'''
