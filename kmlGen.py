
class kmlGen2:
    def __init__(self,file_name=None):
        if file_name is None:
            self.file_name='test'
        else:self.file_name=file_name
        self.baseFile={'kml':[]}
        self.initial="""<?xml version="1.0" encoding="UTF-8"?>
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
	</Style>"""
        self.endXml = """</Document></kml>"""
        self.finale=...
        self.folderPoints=''
    def mergeInit(self,name):
        # < Folder id = {id} >< name > {name} < / name >
        return f'<Folder><name>{name}</name>'
    def mergeEnd(self):
        return '</Folder>'

    def looper(self,dir):
        #idkeys=1
        pointsa = ''
        for key in dir:
            if isinstance(dir, dict):
                if len(dir[key]) > 0:
                    #print(f'added init{key}')
                    self.folderPoints+=self.mergeInit(key)
                    #idkeys+=1
                    pointsa = ''
                    for a in dir[key]:
                        if isinstance(a, dict):
                            self.looper(a)
                        elif isinstance(a, str):
                            pointsa += str(a)
                    #print(pointsa)
                    self.folderPoints+=pointsa
                    self.folderPoints +=self.mergeEnd()
                    #print(f'end{key}')
                else:
                    print(type(key))
            else:
                break
    def convert(self):
        ...

    def addPoint(self,lat,long,root,name):
        
        root.append(f"<Placemark><name>{name}</name><styleUrl>#m_ylw-pushpin</styleUrl><Point><gx:drawOrder>1</gx:drawOrder><coordinates>{lat},{long},0</coordinates></Point></Placemark>")
    def addShape(self,arr,root,name):
        ...

    def newfolder(self,leaf=None, root=None):
        if root is None:
            self.baseFile['kml'].append({leaf: []})
            return self.baseFile['kml'][-1][leaf]
        root.append({leaf: []})
        return root[-1][leaf]

    def constructor(self):
        self.looper(self.baseFile)
        self.final=self.initial+self.folderPoints+self.endXml

    def save(self):
        self.constructor()
        with open(self.file_name+'.kml', 'w') as myFile:
            myFile.write(self.final)
