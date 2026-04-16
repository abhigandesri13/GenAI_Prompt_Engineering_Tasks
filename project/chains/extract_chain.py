from prompts.extract_prompt import extract_prompt

def extract_chain(llm, resume):
    return (extract_prompt | llm).invoke({"resume": resume})