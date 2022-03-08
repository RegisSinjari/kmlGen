# kmlGen
Just a simple KML file generator 
example usage :

kml=kmlGen(file_name='test')
a=kml.newfolder('folder1') #new root folder
b=kml.newfolder('folder2',a) #new folder named folder2 inside folder1
c=kml.newfolder('folder3') #new root folder
kml.addPoint(3.816419857518891, 47.67153553396173,b,'name') #point inside 
kml.addPoint(3.816419857518891, 47.67153553396173,a,'name2')
kml.save()

