import pygame
from .asset_manager import AssetManager
from math import floor

## Utility for drawing dynamically-scaled sprites
class SpriteSlicer():
    ## A dictionary of tileset names and their individual block sizes-
    # This way we could have sprites at different resolutions or scales or somethin
    tile_sizes = {"white-line": 12}

    ## Draws a sprite from pieces.
    #@param game The game being drawn to.
    #@param tile The tileset to use.
    # @param x_position The x coordinate to use as the sprite's top-left corner
    # @param y_position The sprite's y coordinate
    # @param width The sprite's desired width in tiles
    # @param height The sprite's height in tiles
    def draw(game, tile, x_position, y_position, width, height):
        #Blit sprite to received game- Saved here to avoid constantly evaluating
        #game.screen
        draw_to_screen = game.screen.blit
        #Similar, to avoid pestering the asset manager
        sprite_image = AssetManager.get_ui(tile)
        #The size of individual tiles in that unsliced image.
        tile_size = SpriteSlicer.tile_sizes[tile]

        width=int(width)
        height=int(height)


        #If 1x1, draw single tile
        if width<=1 and height<=1:
            draw_to_screen(sprite_image, (x_position,y_position),
                (tile_size*3,tile_size*3, tile_size,tile_size))

        #If horizontal line
        elif height<=1 and width>1:
            #draw left cap
            draw_to_screen(sprite_image, (x_position,y_position),
                (0,tile_size*3,tile_size,tile_size))
            #draw right cap
            draw_to_screen(sprite_image, (x_position+tile_size*(width-1),y_position),
                (tile_size*2,tile_size*3,tile_size,tile_size))
            #draw middle strip
            for i in range(width-2):
                draw_to_screen(sprite_image, (x_position+tile_size*(i+1), y_position),
                    (tile_size,tile_size*3,tile_size,tile_size))


        #If vertical line
        elif height>1 and width<=1:
            #draw top cap
            draw_to_screen(sprite_image, (x_position,y_position),
                (tile_size*3,0,tile_size,tile_size))
            #draw bottom cap
            draw_to_screen(sprite_image, (x_position,y_position+tile_size*(height-1)),
                (tile_size*3,tile_size*2,tile_size,tile_size))
            #draw middle strip
            for i in range(height-2):
                draw_to_screen(sprite_image, (x_position, y_position+tile_size*(i+1)),
                    (tile_size*3,tile_size,tile_size,tile_size))

        #If multidimensional
        else:
            #First, draw corners
            #top left
            draw_to_screen(sprite_image, (x_position,y_position),
                (0,0,tile_size,tile_size))
            #top right
            draw_to_screen(sprite_image, (x_position+tile_size*(width-1),y_position),
                (tile_size*2,0,tile_size,tile_size))
            #bottom left
            draw_to_screen(sprite_image, (x_position,y_position+tile_size*(height-1)),
                (0,tile_size*2,tile_size,tile_size))
            #bottom right
            draw_to_screen(sprite_image, (x_position+tile_size*(width-1),
                y_position+tile_size*(height-1)),
                (tile_size*2,tile_size*2,tile_size,tile_size))

            #Next do the edges- Use long bar as much as possible, fill gaps with singles.
            #Top side
            whole_fourwalls=floor((width-2)/4)
            for i in range(whole_fourwalls):
                draw_to_screen(sprite_image, 
                    (x_position+tile_size+tile_size*i*4,y_position),
                    (0,tile_size*5,tile_size*4,tile_size))
            for i in range(int((width-2)-whole_fourwalls*4)):
                draw_to_screen(sprite_image,
                    (x_position+tile_size*((whole_fourwalls*4)+i+1), y_position),
                    (tile_size,0,tile_size,tile_size))
            #Bottom side
            for i in range(whole_fourwalls):
                draw_to_screen(sprite_image, (x_position+tile_size+tile_size*i*4,
                    y_position+tile_size*(height-1)),
                    (0,tile_size*4,tile_size*4,tile_size))
            for i in range(int((width-2)-whole_fourwalls*4)):
                draw_to_screen(sprite_image,
                    (x_position+tile_size*((whole_fourwalls*4)+i+1),
                        y_position+tile_size*(height-1)),
                    (tile_size,tile_size*2,tile_size,tile_size))
            #Left side
            whole_fourwalls=floor((height-2)/4)
            for i in range(whole_fourwalls):
                draw_to_screen(sprite_image, 
                    (x_position,y_position+tile_size+tile_size*i*4),
                    (tile_size*5,0,tile_size,tile_size*4))
            for i in range(int((height-2)-whole_fourwalls*4)):
                draw_to_screen(sprite_image,
                    (x_position, y_position+tile_size*((whole_fourwalls*4)+i+1)),
                    (0,tile_size,tile_size,tile_size))
            #Right side
            for i in range(whole_fourwalls):
                draw_to_screen(sprite_image, (x_position+tile_size*(width-1),
                    y_position+tile_size+tile_size*i*4),
                    (tile_size*4,0,tile_size,tile_size*4))
            for i in range(int((height-2)-whole_fourwalls*4)):
                draw_to_screen(sprite_image, (x_position+tile_size*(width-1),
                    y_position+tile_size*((whole_fourwalls*4)+i+1)),
                    (tile_size*2,tile_size,tile_size,tile_size))

            #Middle fill
            #How many rows of 2x2 fill blocks fit
            double_rows = floor((height-2)/2)
            #How many extra one-block rows
            double_columns = floor((width-2)/2)
            for i in range(double_rows):
                for j in range(double_columns):
                    #Draw 2x2 sections
                    draw_to_screen(sprite_image,
                        (x_position+tile_size+tile_size*(j*2),
                            y_position+tile_size+tile_size*(i*2)),
                        (tile_size*4,tile_size*4,tile_size*2,tile_size*2))
                #Draw extra bit to fill in the right side- It's a 1x2 chunk of that 2x2
                if width%2==1:
                    draw_to_screen(sprite_image,
                        (x_position+tile_size*(width-2),
                            y_position+tile_size+tile_size*i*2),
                        (tile_size*4,tile_size*4,tile_size,tile_size*2))
            #Draw extra row at bottom
            if height%2==1:
                #First if the fillspace is 2 wide, draw in 2x1 chunks
                for i in range(double_columns):
                    draw_to_screen(sprite_image,
                        (x_position+tile_size+tile_size*i*2,
                            y_position+tile_size*(height-2)),
                        (tile_size*4,tile_size*4,tile_size*2,tile_size))
                #If there's another corner bit add a 1x1 there
                if width%2==1:
                    draw_to_screen(sprite_image,
                        (x_position+tile_size*(width-2),
                            y_position+tile_size*(height-2)),
                        (tile_size,tile_size,tile_size,tile_size))
        #JOB DONE

'''
The last rect in all the blits is the position on the spritesheet of the required chunk.
Here's a list of all those, for future use, because I couldn't get slick variables to work.
top_left_corner = (0,0,tile_size,tile_size)
top_right_corner = (tile_size*2,0,tile_size,tile_size)
bottom_left_corner = (0,tile_size*2,tile_size,tile_size)
bottom_right_corner = (tile_size*2,tile_size*2,tile_size,tile_size)
top_single = (tile_size,0,tile_size,tile_size)
left_single = (0,tile_size,tile_size,tile_size)
right_single = (tile_size*2,tile_size,tile_size,tile_size)
bottom_single = (tile_size,tile_size*2,tile_size,tile_size)
left_cap = (0,tile_size*3,tile_size,tile_size)
right_cap = (tile_size*2,tile_size*3,tile_size,tile_size)
top_cap = (tile_size*3,0,tile_size,tile_size)
bottom_cap = (tile_size*3,tile_size*2,tile_size,tile_size)
horizontal_single = (tile_size,tile_size*3,tile_size,tile_size)
vertical_single = (tile_size*3,tile_size,tile_size,tile_size)
top_long_wall = (0,tile_size*5,tile_size*4,tile_size)
left_long_wall = (tile_size*5,0,tile_size,tile_size*4)
right_long_wall = (tile_size*4,0,tile_size,tile_size*4)
bottom_long_wall = (0,tile_size*4,tile_size*4,tile_size)
single_block = (tile_size*3,tile_size*3,tile_size,tile_size)
single_empty = (tile_size,tile_size,tile_size,tile_size)
quad_empty = (tile_size*4,tile_size*4,tile_size*2,tile_size*2)
'''