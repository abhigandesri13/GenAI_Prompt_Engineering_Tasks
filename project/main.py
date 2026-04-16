from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.match_prompt import match_prompt
from prompts.score_prompt import score_prompt
from prompts.explain_prompt import explain_prompt
from chains.extract_chain import extract_chain

# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",   
    temperature=0.3,
    google_api_key=""
)
def run_pipeline(resume, job):

    # Step 1: Extract
    extracted = extract_chain(llm, resume)

    # Step 2: Match
    match = (match_prompt | llm).invoke({
        "resume_data": extracted.content,
        "job": job
    })

    # Step 3: Score
    score = (score_prompt | llm).invoke({
        "match": match.content
    })

    # Step 4: Explain
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

    score, explanation = run_pipeline(resume, job)

    print("\n====================")
    print("Resume:", file)
    print("Score:", score)
    print("Explanation:", explanation)