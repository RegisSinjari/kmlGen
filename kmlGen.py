"""
Generates KML files
by intitiating a KML class
and calling Add point
options to add polygon by introducing coordinates in function
requires also context opener
"""
class kmlGen:
    def __init__(self,file_name=None):
        self.listPoints=[]
        if file_name is None:
            self.file_name='test'
        else:self.file_name=file_name

        self.intialXml="""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>test.kml</name>
	<Style id="s_ylw-pushpin_hl">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<StyleMap id="m_ylw-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#s_ylw-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#s_ylw-pushpin_hl</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="s_ylw-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
		"""
        self.endXml="""</Document></kml>"""
        self.final=''
    def constructor(self):
        pointsa=''.join([a for a in self.listPoints])
        self.final=self.intialXml+pointsa+self.endXml

    def addPoint(self,lat,long):
        """
        Adds new placemarks on the kml file
        :param lat:
        :param long:
        :return:
        """
        self.listPoints.append(f"<Placemark><name>test</name><styleUrl>#m_ylw-pushpin</styleUrl><Point><gx:drawOrder>1</gx:drawOrder><coordinates>{lat},{long},0</coordinates></Point></Placemark>")

    def save(self):
        self.constructor()
        with open(self.file_name+'.kml', 'w') as myFile:
            myFile.write(self.final)


