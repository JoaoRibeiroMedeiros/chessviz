
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
from celluloid import Camera
import random


def get_first_plot(tabuleiro):
  """
  """
  fig = plt.figure()
  plt.imshow(tabuleiro)
  ax = plt.gca()
  ax.set_xticks(np.arange(-.5, 8, 1), minor=True)
  ax.set_yticks(np.arange(-.5, 8, 1), minor=True)
  ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
  return fig

def get_next_plot(tabuleiro):
  """
  """
  plt.imshow(tabuleiro)

def get_knight_shadow_gif(tabuleiro):
  """
  """

  fig = get_first_plot(tabuleiro)
  camera = Camera(fig)

  for i in range(300):
    tabuleiro = knight_moves(tabuleiro)
    get_next_plot( tabuleiro )
    camera.snap()

  animation = camera.animate()
  return animation
  # animation.save("KnightShadowMoves.gif", writer = "pillow")

def get_knight_limited_board_gif(tabuleiro):
  """
  """

  fig = get_first_plot(tabuleiro)
  camera = Camera(fig)

  for i in range(300):
    tabuleiro = knight_moves_limited(tabuleiro)
    get_next_plot( tabuleiro )
    camera.snap()

  animation = camera.animate()
  return animation

def get_bishop_shadow_gif(tabuleiro):
  """
  """

  fig = get_first_plot(tabuleiro)
  camera = Camera(fig)

  for i in range(300):
    tabuleiro = bishop_moves(tabuleiro)
    get_next_plot( tabuleiro )
    camera.snap()

  animation = camera.animate()
  return animation
  # animation.save("KnightShadowMoves.gif", writer = "pillow")

def get_bishop_limited_board_gif(tabuleiro):
  """
  """

  fig = get_first_plot(tabuleiro)
  camera = Camera(fig)

  for i in range(300):
    tabuleiro = bishop_moves_limited(tabuleiro)
    get_next_plot( tabuleiro )
    camera.snap()

  animation = camera.animate()
  return animation
  # animation.save("BishopShadowMoves.gif", writer = "pillow")