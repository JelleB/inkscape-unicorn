3Dprinter G-Code Output for Inkscape
===========================================

This is an Inkscape extension that allows you to save your Inkscape drawings as
G-Code files suitable for plotting with a reprap style 3D printer

Original Author: [Marty McGuire](http://github.com/martymcguire)
Modified by [Jelle at ProtoSpace](http://github.com/JelleB)

Website: [http://github.com/JelleB/inkscape-unicorn.git](http://github.com/JelleB/inkscape-unicorn.git)

Credits
=======

* Jelle at ProtoSpace converted this to a generig gcode exporter and ripped out all unicorn specific stuff
* Marty McGuire pulled this all together into an Inkscape extension.
* [Inkscape](http://www.inkscape.org/) is an awesome open source vector graphics app.
* [Scribbles](https://github.com/makerbot/Makerbot/tree/master/Unicorn/Scribbles%20Scripts) is the original DXF-to-Unicorn Python script.
* [The Egg-Bot Driver for Inkscape](http://code.google.com/p/eggbotcode/) provided inspiration and good examples for working with Inkscape's extensions API.

Install
=======

Copy the contents of `src/` to your Inkscape `extensions/` folder.

Typical locations include:

* OS X - `/Applications/Inkscape.app/Contents/Resources/extensions`
* Linux - `/usr/share/inkscape/extensions`
* Windows - `C:\Program Files\Inkscape\share\extensions`

Usage
=====

* Size and locate your image appropriately:
	* Most Reprap style 3D printers have a building platform of 200x200mm
	* Setting units to **mm** in Inkscape makes it easy to size your drawing.
	* The extension will automatically attempt to center everything.
* Convert all text to paths:
	* Select all text objects.
	* Choose **Path | Object to Path**.
* Save as G-Code:
	* **File | Save a Copy**.
	* Select **3D printer G-Code (\*.gcode)**.
	* Save your file.
* Preview
	* For OS X, [Pleasant3D](http://www.pleasantsoftware.com/developer/pleasant3d/index.shtml) is great for this.
	* Repetier Host offers gcode preview, as does Cura, if you trick it by offering an .stl with the same name and select the gcode view
* Print!
	* Open your `.gcode` file with printrun/pronterface, repetier host or Cura.
	* do the usual things you need to do to start your printer. Also adapt the start.gcode snippet in the gcode tab TODO!

TODOs
=====

* clean out the old unicorn specific stuff
* put back some new parameters and a tab for holding the start and stop gcode snippets
* Add a way to select different extruders by choosing different colour/ids/groups

* Rename `*PolyLine` stuff to `*Path` to be less misleading.
* Parameterize smoothness for curve approximation.
* Use native curve G-Codes instead of converting to paths?
* Include example templates?
