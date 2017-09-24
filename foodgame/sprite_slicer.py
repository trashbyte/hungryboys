import pygame
from .asset_manager import AssetManager
from math import ceil

## The size in pixels of the tile's corner segments.
TILE_CORNER_SIZE = 12
## The width of the blank wall segments.
TILE_WALL_SIZE = 13
## The width/height of the source sprite.
TILE_BASE_DIMENSIONS = 48


## A sprite generated from sliced images.
class SpriteSlicer():


    ## Draws a sliced sprite.
    # @param game The game to draw in.
    # @param tile The specific tile/file from AssetManager to use.
    # @param x_size The width of the desired sprite.
    # @param y_size The height of the desired sprite.
    # @param x_position The x position of the sprite's top-left corner.
    # @param y_position The y position of the sprite's top-left corner.
    @staticmethod
    def draw(game, tile, x_position, y_position, x_size, y_size, ):
        ## The saved image for cutting.
        # Used instead of AssetManager.get_ui for speed.
        tile_block = AssetManager.get_ui(tile)
        ## blit to the game's screen, to avoid reevaluating game.screen.blit each time
        draw_to_screen = game.screen.blit
        ## The size in pixels of the "empty" middle segment
        middle_block_size = TILE_BASE_DIMENSIONS-TILE_CORNER_SIZE*2
        ## How many rows of whole middle blocks fit
        whole_middle_rows = int((y_size-TILE_CORNER_SIZE*2)/middle_block_size)
        ## How many columns fit
        whole_middle_columns = int((x_size-TILE_CORNER_SIZE*2)/middle_block_size)
        ## How many pixels to make the last partial row
        extra_bottom_pixels = (y_size-TILE_CORNER_SIZE*2-whole_middle_rows*middle_block_size)
        ## How many partial pixels to put at the end of each row
        extra_right_pixels = (x_size-TILE_CORNER_SIZE*2-whole_middle_columns*middle_block_size)

        #Draw top strip
        #Top left corner
        draw_to_screen(
            tile_block,
            (x_position, y_position),
            (0,0,TILE_CORNER_SIZE,TILE_CORNER_SIZE) )
        #If width is greater than the two corners, go over the middle and fill with wall.
        if x_size > TILE_CORNER_SIZE*2:
            for i in range(ceil((x_size-2*TILE_CORNER_SIZE)/TILE_WALL_SIZE)):
                draw_to_screen(
                    tile_block,
                    (i*TILE_WALL_SIZE+TILE_CORNER_SIZE+x_position, y_position),
                    (TILE_CORNER_SIZE,0,TILE_WALL_SIZE,TILE_CORNER_SIZE) )
        #Top right corner
        draw_to_screen(
            tile_block,
            (x_position+(x_size-TILE_CORNER_SIZE), y_position),
            (TILE_BASE_DIMENSIONS-TILE_CORNER_SIZE,0,TILE_CORNER_SIZE,TILE_CORNER_SIZE) )

        #Draw middle strip... If there is a middle strip.
        if y_size > TILE_CORNER_SIZE*2:
            #Draw left wall
            for i in range(ceil((y_size-2*TILE_CORNER_SIZE)/TILE_WALL_SIZE) ):
                draw_to_screen(
                    tile_block,
                    (x_position, y_position+TILE_CORNER_SIZE+TILE_WALL_SIZE*i),
                    (0, TILE_CORNER_SIZE, TILE_CORNER_SIZE, TILE_WALL_SIZE) )
            #Draw middle fill. Only drawn if there is actually any middle to fill.
            ## The number of complete rows of filler in the middle of the desired box.
            if x_size > TILE_CORNER_SIZE*2:
                #For each complete middle row
                for i in range(whole_middle_rows):
                    #Draw full-size boxes until there's no longer enough width for another
                    for j in range(whole_middle_columns):
                        draw_to_screen(
                            tile_block,
                            (x_position+TILE_CORNER_SIZE+j*middle_block_size,
                                y_position+TILE_CORNER_SIZE+i*middle_block_size),
                            (TILE_CORNER_SIZE,TILE_CORNER_SIZE,middle_block_size,middle_block_size) )
                    #Draw vertical strip to cover remainder, if there's a remaining bit
                    if extra_right_pixels > 0:
                        draw_to_screen(
                            tile_block,
                            (x_position+TILE_CORNER_SIZE+whole_middle_columns*middle_block_size,
                                y_position+TILE_CORNER_SIZE+i*middle_block_size),
                            (TILE_CORNER_SIZE,TILE_CORNER_SIZE,
                                extra_right_pixels,middle_block_size))

                #Remaining bottom strip
                if extra_bottom_pixels > 0:
                    #for each full-block-wide segment
                    for i in range(whole_middle_columns):
                        draw_to_screen(
                            tile_block,
                            (x_position+TILE_CORNER_SIZE+i*middle_block_size,
                                y_position+TILE_CORNER_SIZE+whole_middle_rows*middle_block_size),
                            (TILE_CORNER_SIZE,TILE_CORNER_SIZE,middle_block_size,extra_bottom_pixels) )
                #for the last bottom-right corner of the middle fill
                    draw_to_screen(
                        tile_block,
                        (x_position+TILE_CORNER_SIZE+whole_middle_columns*middle_block_size,
                            y_position+TILE_CORNER_SIZE+whole_middle_rows*middle_block_size),
                        (TILE_CORNER_SIZE,TILE_CORNER_SIZE,extra_right_pixels,extra_bottom_pixels) )

        #Draw the right wall if it exists
        for i in range(ceil((y_size-TILE_CORNER_SIZE*2)/TILE_WALL_SIZE) ):
            draw_to_screen(
                tile_block,
                (x_position+TILE_CORNER_SIZE+whole_middle_columns*middle_block_size+extra_right_pixels,
                    y_position+TILE_CORNER_SIZE+i*TILE_WALL_SIZE),
                (TILE_BASE_DIMENSIONS-TILE_CORNER_SIZE,TILE_CORNER_SIZE,
                    TILE_CORNER_SIZE,TILE_WALL_SIZE))

        #Draw bottom
        #Bottom left corner
        draw_to_screen(
            tile_block,
            (x_position, y_position+y_size-TILE_CORNER_SIZE),
            (0, TILE_BASE_DIMENSIONS-TILE_CORNER_SIZE, TILE_CORNER_SIZE, TILE_CORNER_SIZE) )
        #If bottom wall exists, print it
        if x_size > TILE_CORNER_SIZE*2:
            for i in range(ceil((x_size-2*TILE_CORNER_SIZE)/TILE_WALL_SIZE)):
                draw_to_screen(
                    tile_block,
                    (i*TILE_WALL_SIZE+TILE_CORNER_SIZE+x_position, y_position+y_size-TILE_CORNER_SIZE),
                    (TILE_CORNER_SIZE,TILE_BASE_DIMENSIONS-TILE_CORNER_SIZE,
                        TILE_WALL_SIZE,TILE_CORNER_SIZE) )
        #Bottom right corner
        draw_to_screen(
            tile_block,
            (x_position+x_size-TILE_CORNER_SIZE,y_position+y_size-TILE_CORNER_SIZE),
            (TILE_BASE_DIMENSIONS-TILE_CORNER_SIZE,TILE_BASE_DIMENSIONS-TILE_CORNER_SIZE,
                TILE_CORNER_SIZE,TILE_CORNER_SIZE))