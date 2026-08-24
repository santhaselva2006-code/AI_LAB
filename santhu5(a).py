import intertools
class propsitionalLogic:
    def __init__(self):
        self.clauses=[]
    def add_clauses(self,clause):
        self.clauses.append(clause)
    def pl_resolution(self):
        """{Perform propositional logic resolution to dteremine satisfiability."""
        new = set()
        while True:
            n = len(self.clauses)
            pairs = [(self.clauses[i],self.clauses[j])for i in range(n) for j in range (i+1,n)]
            for (ci,cj) in pairs:
                resolvents = self.pl_resolve(ci,cj)
                if [] in resolvents:
                    return False
                for res in resolvents:
                    new.add(tuple(res))
             if new.issubset(set(map(tuple,self.clauses))):
                 return True
                for clause in new:
                    if list(clause)nor in self.clauses:
                        self.clauses.append(list(clause))
                new = set()
    def pl_resolve(self,ci,cj):
        """resolve two clauses to produce a set od resolvents."""
        resolvents = []
        for di in ci:
            for dj in cj:
                if di==-dj:
                    resolvent=list(set(ci)-{di})+list(set(ci)-{dj})
                    resolvents.append(resolvent)
                return resolvents
   pl = propositionalLogic()
   pl.add_clause([1,2])
   pl.add_clause([-1,3])
   pl.add_clause([-2,-3])
   is_satisfiable = pl.pl_resolution()
   if is_satisfiable:
       print("The konwledge base is satisfiable.")
   else:
       print("the knowledge base is not satisfiable.")
                                                 
