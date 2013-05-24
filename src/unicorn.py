#!/usr/bin/env python
'''
Copyright (c) 2010 MakerBot Industries

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''
import sys,os
import sys
sys.path.append("/usr/share/inkscape/extensions")
import inkex
from math import *
import getopt
from unicorn.context import GCodeContext
from unicorn.svg_parser import SvgParser

class MyEffect(inkex.Effect):
  def __init__(self):
    inkex.Effect.__init__(self)
    self.OptionParser.add_option("--xy-feedrate",
                      action="store", type="float",
                      dest="xy_feedrate", default="10.0",
                      help="XY axes feedrate in mm/min")
    self.OptionParser.add_option("--z-feedrate",
                      action="store", type="float",
                      dest="z_feedrate", default="10.0",
                      help="Z axis feedrate in mm/min")
    self.OptionParser.add_option("--z-height",
                      action="store", type="float",
                      dest="z_height", default="0.0",
                      help="Z axis print height in mm")
    self.OptionParser.add_option("--thread-width",
                      action="store", type="float",
                      dest="thread_width", default="0.6",
                      help="default stroke width of a single line, when no stroke width is given.")
    self.OptionParser.add_option("--temp",
                      action="store", type="int",
                      dest="temp", default="220",
                      help="Printing temperature")
    self.OptionParser.add_option("--startGcode",
                      action="store", type="string",
                      dest="startGcode", default="0.0",
                      help="Start gcode routine")
    self.OptionParser.add_option("--g28",
                      action="store", type="string",
                      dest="g28", default="false",
                      help="home before printing.")
    self.OptionParser.add_option("--pause-on-layer-change",
                      action="store", type="string",
                      dest="pause_on_layer_change", default="false",
                      help="Pause on layer changes.")
    self.OptionParser.add_option("--filament",
                      action="store", type="float",
                      dest="filament", default="38",
                      help="Filament diameter.")  
    self.OptionParser.add_option("--ex1color",
                      action="store", type="string",
                      dest="ex1color", default="#000000",
                      help="color for the 1st(default) extruder.")                                       
    self.OptionParser.add_option("--ex2color",
                      action="store", type="string",
                      dest="ex2color", default="#000000",
                      help="color for the 2nd extruder.") 
    self.OptionParser.add_option("--ex2offsetX",
                      action="store", type="float",
                      dest="ex2offsetX", default="0",
                      help="X offset for the 2nd extruder.") 
    self.OptionParser.add_option("--ex2offsetY",
                      action="store", type="float",
                      dest="ex2offsetY", default="0",
                      help="Y offset for the 2nd extruder.")                                            
    self.OptionParser.add_option("--tab",
                      action="store", type="string",
                      dest="tab")

  def output(self):
    self.context.generate()

  def effect(self):
    self.context = GCodeContext(self.options.xy_feedrate, 
                           self.options.z_feedrate, 
                           self.options.z_height, 
                           self.options.thread_width,
                           self.options.temp, 
                           self.options.g28,
                           self.options.startGcode,
                           self.options.filament,
                           self.options.ex2color,
                           self.options.ex2offsetX,
                           self.options.ex2offsetY,
                           self.svg_file)
    parser = SvgParser(self.document.getroot(), self.options.pause_on_layer_change)
    parser.parse()
    for entity in parser.entities:
      if entity :
        entity.get_gcode(self.context)

if __name__ == '__main__':   #pragma: no cover
  e = MyEffect()
  e.affect()
