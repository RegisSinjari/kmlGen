"""
Tani ktu kemi layers and layers
basically json file
which means
nje loop fillestar qe shikon ca dic ka
kto auto behen foldera
loopi vazhdon deri ne break rasti kur len brenda eshte 0

qe dmth for kte in keys
    if len>=0 #pse ta besh then?
    -Folder-
    for key in keys:
    .
    .
    .
    -/Folder-


"""
dicti={
   "kml":[
      {
         "kml3":[
            "ee"
         ]
      },
      {
         "kml2":[
            "ww"
         ]
      }
   ]
}

def looper(dir):
    print(type(dir))
    # if isinstance(dir, dict):
    #     for key in dir:
    #         print(f'added init{key}')
    for key in dir:
        if isinstance(dir,dict):
            #print(f'added init{key}')
            # print(dir[key])
            # print(len(dir[key]))
            # add folder initial
            if len(dir[key]) > 0:
                # print('len > 0')
                print(f'added init{key}')
                for a in dir[key]:
                    # print('a')
                    # print(a)
                    if isinstance(a, dict):
                        print('ktu')
                        looper(a)
                    elif isinstance(a, list):
                        print('lista?')
                        looper(a)
                print(f'end{key}')
                #folder end
            else:
                print(type(key))
                # just add /folder with dir name
        elif isinstance(dir,list):
            print('list')
            if len(dir) > 0:
                #loop all points and just append to filewrite
                #pointsa = ''.join([a for a in dir])
                print('added allpoints')
            else:
                print('break')
                print(type(dir))
                break
        else:
            print('break')
            print(type(key))
            break

looper(dicti)