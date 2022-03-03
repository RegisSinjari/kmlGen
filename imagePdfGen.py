dict1={'base':[]}
def newfolder(leaf=None,root=None):
    if root is None:
        dict1['base'].append({leaf: []})
        return dict1['base'][-1][leaf]
    root.append({leaf: []})
    return root[-1][leaf]
# a=newfolder(dict1['base'],'dd')
# b=newfolder(a,'cc')
# newfolder(a,'ee')
# print(a)
# print(b)
# print(dict1)
a=newfolder('dd')
print(a)
b=newfolder('pp',a)
print(b)
print(dict1)