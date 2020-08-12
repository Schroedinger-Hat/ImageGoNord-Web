# -*- coding: utf-8 -*-

class ConvertUtility:
  def color_difference (self, color1, color2):
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

  def get_avg_color (self, pixels, w=-2, h=3):
    average_sum = []
    for k in range(w, h):
      for l in range(w, h):
        try:
          average_sum.append(pixels[i+k, j+l])
          n += 1
        except:
          pass

    size = len(average_sum)
    r = 0
    g = 0
    b = 0
    for x in average_sum:
      r += x[0]
      g += x[1]
      b += x[2]

    return (r/size, g/size, b/size)
