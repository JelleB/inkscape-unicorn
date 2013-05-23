from math import *
import sys

class GCodeContext:
    def __init__(self, xy_feedrate, z_feedrate, z_height, thread_width, temp, home, startGcode, file):
      self.xy_feedrate = xy_feedrate
      self.z_feedrate = z_feedrate
      self.zHeight = z_height
      self.threadWidth = thread_width
      self.temp = temp
      self.home = home
      self.startGcode = startGcode
      self.file = file    
      self.drawing = False
      self.retracted = False
      self.last = None
      self.e = 0.0
      self.z = 0.0

      self.preamble = [
        ";(3D printer gcode generated from %s )" % (self.file),
        ";( %s )" % " ".join(sys.argv).replace('\n','/'),
        ";G21 ;(metric ftw)",
        "G90 ;(absolute mode)",
        ""
      ]
      if startGcode != "" :
        self.preamble.append(startGcode + "\n")   
      
      if home == "true" :
        self.preamble.append("G28 X0 Y0 Z0 ; move to the endstops and call that position 0,0,0 \n")

      self.postscript = [
        "",
        ";(end of print job)",
        "M104 S0",
        "G91",
        "G1 X10 Y10 Z5 E-5",
        "G90",
        "G28 X0 Y0" ,
        "G84 ;(drives off)",
        ""
      ]

      self.registration = [
         ""
      ]

      self.sheet_header = [
        ";(start of sheet header)",
        ""
      ]

      self.sheet_footer = [
        ""
        ]

      self.loop_forever = [ "M30 ;(Plot again?)" ]

      self.codes = []

    def start(self):
      if (self.retracted):
        self.e += 5
        self.codes.append("G1 E%0.4f ;(de-retract some)" %(self.e))
        self.retracted = False
      self.drawing = True

    def stop(self):
      if (self.retracted == False):
        self.e += -5
        self.codes.append("G1 E%0.4f ;(retract some)" %(self.e))
        self.retracted = True
      self.drawing = False

    def go_to_point(self, x, y, stop=False):
      if self.last == (x,y):
        return
      if stop:
        return
      else:
        if self.drawing: 
          self.stop(self)
        self.codes.append("G0 X%.2f Y%.2f F%.2f" % (x,y, self.xy_feedrate * 60))
      self.last = (x,y)
	
    def draw_to_point(self, x, y, width, layerHeight, stop=False):
      if self.last == (x,y):
          return
      if stop:
        return
      else:
        if self.drawing == False:
          self.start(self)
        lx = x - self.last[0]
        ly = y - self.last[1]  
        self.e += self.calculateE( lx , ly , self.zHeight, self.threadWidth)  
        self.codes.append("G1 X%0.2f Y%0.2f E%0.3f F%0.2f" % (x,y,self.e, self.xy_feedrate * 60))
      self.last = (x,y)
      
    def calculateE(self, x, y, z, thread, radius=1.45):
      #"calculate the relative E component based on x y z vector and thread width"
      l = hypot(x,y)
      return (l * z * thread ) / (pi * radius * radius)
      
      
    def generate(self):
    
      codesets = [self.codes]
      
      for line in self.preamble:
        print line

      for codeset in codesets:
        for line in codeset:
            print line
        if codeset :    
          for line in self.postscript:
              print line
