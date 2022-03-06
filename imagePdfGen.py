dict1={'base':[]}
def newfolder(leaf=None,root=None):
    if root is None:
        dict1['base'].append({leaf: []})
        return dict1['base'][-1][leaf]
    root.append({leaf: []})
    return root[-1][leaf]
a=newfolder('dd')
b=newfolder('pp',a)
c=newfolder('ppee',a)
d=newfolder('pdwp',b)
newfolder('wewew',d)
print(dict1)