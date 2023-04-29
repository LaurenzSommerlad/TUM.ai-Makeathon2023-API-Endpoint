# implement the logic of the discussion
def build_question(context):
    print("inside logic", context)
    report = 0
    id = len(context)
    tmp = {"question": "this is a question"
            , "response": "this is a response", "id": id}
    context.add(tmp)
    return report, context

def chat():
    pass