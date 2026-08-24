def find_unit_clause(clauses):
    """
    find a unit clause in the list of clauses.
    """
    for clause in clauses:
        if len(clause)==1:
            return clause[0]
        return None
    def simplify_clauses(clauses,literal):
        """
        simplifies the list of clauses by setting the given literal to True.
        """
        simplifies = []
        for clause in clauses:
            if literal in clauses:
                continue
            new_clauses = [ 1 for 1 in clause if != -literal]
            if not new_clause:
                return None
            simplified.append(new_clause)
                return simplified
        def dpll(clauses,assignments):
            """
            implements the DPLL algorithm for propositional model checking.
            """
            unit = find_unit_clause(clauses)
            while unit is not None:
                assignments.append(unit)
                clauses = simplify_clauses(clauses,unit)
                if clauses is None:
                    return False
                unit = find_unit_clause(clauses)
       if not clauses:
           return True
        literal = clauses[0][0]
        new_clauses = simplify_clauses(clauses,literals)
        if new_clauses is not None and dpll(new_clauses,assignments+[literals]):
            return True
        new_clauses = simplify_clauses(clauses,-literals)
        if new_clauses is not None and dpll(new_clauses,assignments + [-literals]):
            return True
        return False
    def main();
        A,B,C = 1,2,3
        clauses = [[A,A],[-A,C],[-B,-C]]
        assignments = []
        if dpll(clauses,assignments):
            print("SATISFIABLE with assignments:",assignments)
        else:
            print("UNSATISFIABLE")
        if__name__=="__main__":
            main()

                
