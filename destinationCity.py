# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        edges = {}
        temp = ''
        temp2 = ''
        
        for i in paths:
            if i[1] not in edges:
                temp = i[1]
                edges[temp] = 0
        
        for j in paths:
            if j[0] in edges:
                temp2 = j[0]
                edges[temp2] += 1
        
        for k in edges:
            if edges[k] == 0:
                return k
