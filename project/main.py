import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your_api_key"
os.environ["LANGCHAIN_PROJECT"] = "My First App"

from prompts.match_prompt import match_prompt
from prompts.score_prompt import score_prompt
from prompts.explain_prompt import explain_prompt
from chains.extract_chain import extract_chain
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    openai_api_key="your_api_key",
    openai_api_base="https://openrouter.ai/api/v1"
)

def run_pipeline(resume, job, name):

        extracted = extract_chain(llm, resume)

        match = (match_prompt | llm).invoke({
            "resume_data": extracted.content,
            "job": job
        })

        score = (score_prompt | llm).invoke({
            "match": match.content
        })

        explanation = (explain_prompt | llm).invoke({
            "score": score.content,
            "match": match.content
        })

        return score.content, explanation.content

# Load job
with open("job_description.txt") as f:
    job = f.read()

# Run for all resumes
files = ["strong.txt", "average.txt", "weak.txt"]

for file in files:
    with open(f"resumes/{file}") as f:
        resume = f.read()

    score, explanation = run_pipeline(resume, job, file)

    print("\n====================")
    print("Resume:", file)
    print("Score:", score)
    print("Explanation:", explanation)