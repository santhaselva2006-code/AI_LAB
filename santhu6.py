rules = [
    (["A","B"],"C"),
    (["c"],"D"),
    (["D","E"],"F")
    ]
facts = {"A","B","E"}
def forward_chaining(rules,facts,goal):
    inferred = set(facts)
    changed = True


    while changed:
        changed = False
        for premises,conclusion in rules:
            if all(p in inferred for p in premises) and conclusion not in inferred:
                inferred.add(conclusion)
                changed = True
                if conclusion == goal:
                    return True,inferred
                return goal in inferred,inferred
def backward_chaining(rules,facts,goal):
    if goal in facts:
        return True
    for premises,conclusion in rules:
        if conclusion == goal:
           if all(backward_chaining(rules,facts,p)for p in premises):
               return True
            return False



    goal = "F"


    fc_results,fc_facts = forward_chaining(rules,facts,goal)
    print("Forward chaining:Goal",goal,"->",fc_results,"|FActs:",fc_facts)


    bc_result = backward_chaining(rules,facts,goal)
    print("Backward chaining: Goal",goal,"->",bc_result)
