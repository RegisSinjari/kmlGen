dict1={'base':[]}
def newfolder(leaf=None,root=None):
    if root is None:
        dict1['base'].append({leaf: []})
        return dict1['base'][-1][leaf]
    root.append({leaf: []})
    return root[-1][leaf]

def newPoint(root=None,val=None):
    root.append(val)
a=newfolder('dd')
b=newfolder('pp',a)
c=newfolder('ppee',a)
d=newfolder('pdwp',b)
y=newfolder('wewew',d)
newPoint(y,'dsdasda')
newPoint(y,'dsdasda2')
print(dict1)
def returnName(x):
    return x
texttibosh=''
texttibosh+='ddd'
texttibosh+=returnName('aaa')
print(texttibosh)
