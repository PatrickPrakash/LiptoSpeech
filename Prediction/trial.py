# from ffpyplayer.player import MediaPlayer
# import time
#
# player = MediaPlayer('PredictVideo/bbaf2n.mpg')
# while 1:
#     frame, val = player.get_frame()
#     if val == 'eof':
#         break
#     elif frame is None:
#         time.sleep(0.01)
#     else:
#         img, t = frame
#         print (val, t, img.get_pixel_format(), img.get_buffer_size())
#         time.sleep(val)

'''
import matplotlib
matplotlib.use('Agg')

from moviepy.editor import *
from tkinter import *
root = Tk()
'''

import pyglet

vidPath = 'PredictVideo/bbaf2n.mpg'
window = pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)
#
# player.queue(MediaLoad)
# player.play()
#
# @window.event
# def on_draw():
#     if player.source and player.video_format:
#         player.get_texture().blit(50,50)
#
# pyglet.app.run()
