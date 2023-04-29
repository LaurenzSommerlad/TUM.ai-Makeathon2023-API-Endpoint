import openai
import os
from dotenv import load_dotenv
import cohere
from static_questions import *
from chatgpt_prompt import generate_prompt

load_dotenv(".env")
openai.api_key = os.getenv("OPENAI_API_KEY")
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# implement the logic of the discussion
def build_question(context):
    print("inside logic", context)
    report = 0
    new_question = ""
    new_response = ""
    context = list(context)
    id = len(context)
    if id < len(static_questions):
        new_question = static_questions[id]

    else:
        for i in range(len(context)):
            j = context[i]['id']
            if len(context[i]["response"]) < 40:
                continue
            else: 
                summary = co.summarize(
                    text=context[i]["response"],
                    length='auto',
                    format='paragraph',
                    model='summarize-xlarge',
                    additional_command=extra_commands[j],
                    temperature=0.2,
                )
                context[i]["response"] = summary.summary
        prompt = generate_prompt(context)
        print(prompt)
        gptResponse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "Act as a MCKinsey AI consultant."},
                {"role": "user", "content": prompt},
            ]
        )
        reportText = ''
        for choice in gptResponse.choices:
            reportText += choice.message.content
        print(reportText)
        report = 1
        new_question = reportText
    tmp = {"question": new_question
        , "response": new_response, "id": id}
    context.append(tmp)
    return report, context


def chat():
    pass