"""
first test is a class thats serializes data into nested
qe dmth
fillon dhe mbaron me ####
dhe ne cdo instance qe incializohet
ben 1111 ose 2222
which can basically be implemented with dictonaryes

'kml':{'base':[]}   #intiated
first step is to translate this to xml
if you want folder you append new dictonaries

{point:(lat:x,long:y,name:'d')},{point:(lat:x,long:y,name:'y')}

'kml':{'base':['second':[{point:(lat:x,long:y,name:'y')}]]}

#####
    1111
    fff
        2222
        rrr
        2222
    1111
#####
dict1={'base':[]}
def newfolder(leaf=None,root=None):
    if root is None:
        dict1['base'].append({leaf: []})
        return dict1['base'][-1][leaf]
    root.append({leaf: []})
    return root[-1][leaf]
"""
sa={'kml':[]}
print(type(sa))
sa['kml'].append({'kml3': ['ee']})
#print(sa)
sa['kml'].append({'kml2': ['ww']})
# sa['kml'].append({'kml2': ['ww']})
print(sa)
print(sa['kml'][0]['kml3'])
print('----------')
# >>> for key in a_dict:
# ...     print(key, '->', a_dict[key])
atexti=''



def looper(dir):
    for key in dir:
        print(dir[key])
        print(len(dir[key]))
        if len(dir[key]) > 0:
            print('len > 0')
            for a in dir[key]:
                print('a')
                print(a)
                if isinstance(a, dict):
                    looper(a)
        else:
            break
looper(sa)

# for key in sa:# loop kap vtm kml dhe t con n list
#     print('kti')
#     print(sa[key])#kjo gjen listen boshe
#     #nqs eshte list boshe ska nevoje te shtoje foldera, direkt pika ama nqs gjen dicta
#     if len(sa[key])>0:
#         looper(sa[key])
#     else : break
#
#     for a in sa.get(key):
#         if isinstance(a, dict):
#         #     print(a)
#         #     print('a is dic') #ktu posto x folder
#         #     atexti += 'elostart'
#         #     atexti += 'eloend'
#             for key in a:
#                 print(a.get(key))

def inserter(base,path,what):
    for a in base:
        b=a.get(path,False)
        if b:
            print(b)

def newfolder(root,leaf=None):
    if leaf is None:
        #just append to root
        ...
    #else append leaf to root
    #then return ku vete
    return eval('dictLocation')
#make it so that initiated first will just append to base
#but if calling it again it will append to the
a=newfolder('name')#appends to base

b=newfolder(a,'ds')
c=newfolder(b,'ui')
newfolder(a,'dd')
print(a)
print('^^^^^^^^^')
for a in sa['kml']:
    ee=a.get('kml3')
    print(ee)
    print(a)
inserter(sa['kml'],'kml3','eeeeppp')
print('--*-*-*-*-*-')
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
    def mergeInit(self,name,id):
        # < Folder id = {id} >< name > {name} < / name >
        return f'<Folder id = {id}><name>{name}</name>'
    def mergeEnd(self,name):
        return '</Folder>'

    def convert(self):
        ...

    def addPoint(self,name,lat,long,folder='kml'):
        #self.baseFile[folder].append({point:(lat:x,long:y,name:'d')})
        self.baseFile[folder].append(f"<Placemark><name>{name}</name><styleUrl>#m_ylw-pushpin</styleUrl><Point><gx:drawOrder>1</gx:drawOrder><coordinates>{lat},{long},0</coordinates></Point></Placemark>")

    def addFolder(self,name,folder='kml'):
        self.baseFile[folder].append({name:[]})

    def constructor(self):
        #pointsa=''.join([a for a in self.listPoints])
        pointsa=''
        #loop all elements in dict


        self.final=self.initial+pointsa+self.endXml

    def save(self):
        self.constructor()
        with open(self.file_name+'.kml', 'w') as myFile:
            myFile.write(self.final)