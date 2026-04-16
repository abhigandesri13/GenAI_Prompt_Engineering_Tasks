# AI Resume Screening System with Tracing

## Project Overview

This project is part of the internship assignment **"GenAI Task 3 – AI Resume Screening System with Tracing"**.

The system evaluates candidate resumes based on a given job description using an LLM-powered pipeline.

---

## Features

* Skill Extraction from resumes
* Resume vs Job Description Matching
* Candidate Scoring (0–100)
* Explanation for each score
* Modular pipeline using LangChain

---

##  Tech Stack

* Python
* LangChain
* OpenRouter (LLM API)
* LangSmith (for tracing - configured)

---

##  Project Structure

```
project/
│
├── prompts/
├── chains/
├── resumes/
├── main.py
├── job_description.txt
├── output.png
```

---

## Note on Folder Structure

The main implementation of **Task 3 (AI Resume Screening System)** is placed inside the `project/` folder.

👉 This is done to maintain a clean and modular structure as per the assignment requirements (separating prompts, chains, and main pipeline logic).

All relevant files for Task 3 are located within this folder.

---

## How to Run

1. Install dependencies:

```
pip install langchain langchain-openai
```

2. Add your API key inside `main.py`

3. Run the project:

```
python main.py
```

---

## Output

The system processes:

* Strong resume
* Average resume
* Weak resume

And returns:

* Score
* Explanation

---


##  Final Note

This project demonstrates a complete LLM pipeline including extraction, matching, scoring, and explainability.

## Done by Gandesri Abhilash
## Submitted to Innomatics Research Labs
