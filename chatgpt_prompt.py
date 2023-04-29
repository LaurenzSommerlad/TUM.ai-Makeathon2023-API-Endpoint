
prompt_header = '''Output a use case where AI can be applied that must contains:
1. Problem Description: A specific description of the problem
2. Solutions being used so far: 
3. Expected Business Value: include number, be specific in numbers! include concrete numbers like tracking key performance indicators (KPIs) such as revenue growth, cost savings, and return on investment (ROI)  etc.
4. How AI can be Applied: explain where AI can be applied, provide the examples and tools that can be used
5. Potential Costs and Risks:  Include Financial Costs, Time Costs, Reputation Costs, Legal and Regulatory Costs, Operational Risks and Strategic Risks.
6. Data sources required by this use case: write which data should be providet by company 

Case: '''
from functools import cmp_to_key
def generate_prompt(context):
    prompt = "" + prompt_header
    def compare(elem1, elem2):
        id1 = elem1["response"]
        id2 = elem2["response"]
        if id1 < id2: return -1
        elif id1 == id2: return 0
        else: return 1
         
    sorted_context = context.copy()

    # sorted_context = context.sort(key=compare)
    sorted(sorted_context, key = cmp_to_key(compare))
    print("inside generate prompt", sorted_context)

    prompt += sorted_context[0]["response"] + '\n'
    for x in sorted_context[1:]:
        prompt += x["response"] + '\n'
    return prompt
