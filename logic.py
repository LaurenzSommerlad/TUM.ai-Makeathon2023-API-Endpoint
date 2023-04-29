import openai
import os
from dotenv import load_dotenv

load_dotenv(".env")

openai.api_key = os.getenv("OPENAI_API_KEY")

'''
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "Why should DevOps engineer learn kubernetes?"},
        ]
)
result = ''
for choice in response.choices:
    result += choice.message.content
print(result)
'''

static_questions = []
static_questions.append("What is the name of the company?")
static_questions.append("Tell me more about the company? (e.g. company's mission and values)")
static_questions.append("Which industry is you company in? (Services, Manifacturing or Disposal. If there is an overlay, please focus on the aspect you want to imporve the most)")
static_questions.append("Can you please provide more information about that industry?")
static_questions.append("What are the main challenges faced by customers in these industries?")
static_questions.append("Are there any specific trends or opportunities in these industries that your company is focused on?")
static_questions.append("What are the biggest pain points and inefficiencies in your business operations?")
static_questions.append("Which areas of your business do you think could benefit most from process improvement?")
static_questions.append("Have you noticed any recurring issues or bottlenecks that are affecting your business operations?")
static_questions.append("What are the key trends and benchmarks in your industry?")
static_questions.append("How do you compare to your competitors in terms of performance, efficiency, and profitability?")
static_questions.append("What are your main operating expenses?")
static_questions.append("What are your largest expense categories?")
static_questions.append("How much do you spend on procurement, marketing, or maintenance?")
static_questions.append("what type of date is your company managing (records, reports, ...) and in what form are they available in (numbers, pictures, spreadsheets, ... )?  What about the consistency and completeness of the data?")

def generate_report():
    return "this is a report"

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
        report = 1
        new_question = generate_report()
    tmp = {"question": new_question
        , "response": new_response, "id": id}
    context.append(tmp)
    return report, context


def chat():
    pass