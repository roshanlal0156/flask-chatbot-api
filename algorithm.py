import json

class Algo:
    def __init__(self):
        pass
    def read(self):
        f = open('./qna.json')
        data = json.load(f)
        return data
    def qna(self,question):
        return self.SearchAns(question)
    
    def getPoints(self, listQ, d):
        points = 0
        listD = d.split()
        for v in listQ:
            for u in listD:
                if(u == v):
                    points+=1
        return points
            
    def SearchAns(self,q):
        data = self.read()
        if q in data[0].keys():
            return data[0][q]
        
        matchingPoint = {}
        
        listQ = q.split()
        
        for d in data[0]:
            points = self.getPoints(listQ, d)
            matchingPoint[d] = points
        maxMatch = 0
        ans = "xxxx"
        for match in matchingPoint:
            if(matchingPoint[match] > maxMatch):
                ans = match
        return data[0][ans]
            
        
        
        
