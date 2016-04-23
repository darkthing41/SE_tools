# SE_tools
Space Engineers: Tools common to all SE projects.

> This is a collection of utilities designed to be used alongside or incoporated into other SE projects.

##Description
File | Description
---- | -----------
Template.cs	| Template SE script to be used in an IDE
export.py	| Python script to convert `.cs` files into raw text suitable for copying into the SE editor. Extracts `#region`, strips out documentation comments, removes extra indentation, and replaces tab characters with spaces. When executed in the project directory (e.g. after a project build), will convert all `.cs` files into `.txt` files.