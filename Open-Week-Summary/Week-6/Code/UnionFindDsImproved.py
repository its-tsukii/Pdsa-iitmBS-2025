class MakeUnionFind:
    def __init__(self):
        self.components = {}
        self.members = {}
        self.size = {}
    def make_union_find(self,vertices):
        for vertex in range(vertices):
            self.components[vertex] = vertex
            self.members[vertex] = [vertex]
            self.size[vertex] = 1
    def find(self,vertex):
        return self.components[vertex]
    def union(self,u,v):
        c_old = self.components[u]
        c_new = self.components[v]
        # Always add member in components which have greater size
        if self.size[c_new] >= self.size[c_old]:            
            for x in self.members[c_old]:
                self.components[x] = c_new
                self.members[c_new].append(x)
                self.size[c_new] += 1
        else:
            for x in self.members[c_new]:
                self.components[x] = c_old
                self.members[c_old].append(x)
                self.size[c_old] += 1
    

uf = MakeUnionFind()
uf.make_union_find(5)  # vertices = 0,1,2,3,4

uf.union(0, 1)
uf.union(3, 4)
uf.union(1, 4)

print("Component of each vertex:", uf.components)
print("Members of each component:", uf.members)
print("Sizes:", uf.size)

# Test finds
print(uf.find(0), uf.find(4))
