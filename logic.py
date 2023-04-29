# implement the logic of the discussion
def build_question(context):
    report = 0
    id = len(context)
    tmp =  {"question": "this is a question"
            , "response": "this is a response"}
    context.append({id: tmp})
    return report, context

def chat():
    pass