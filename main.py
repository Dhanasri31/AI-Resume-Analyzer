def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def find_skills(text, skills_list):
    found = []
    for skill in skills_list:
        if skill in text.lower():
            found.append(skill)
    return found


def compare_skills(resume_skills, required_skills):
    matched = []
    missing = []

    for skill in required_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(required_skills)) * 100
    return matched, missing, score


def show_result(matched, missing, score):
    print("Matched skills:", matched)
    print("Missing skills:", missing)
    print("Match score:", round(score), "%")


def show_suggestions(missing, suggestions):
    if len(missing) == 0:
        print("Great! Your resume has all the required skills.")
        return

    print("\nWhat to learn next:")
    for skill in missing:
        if skill in suggestions:
            print("-", skill.upper(), ":", suggestions[skill])


all_skills = [
    "python", "django", "html", "css", "javascript",
    "react", "sql", "mysql", "git", "github"
]

suggestions = {
    "python": "Practice loops, functions and file handling, then build small programs.",
    "django": "Learn models, views and templates, then build a simple blog.",
    "html": "Practice page structure, forms and tables.",
    "css": "Practice Flexbox, Grid and responsive design.",
    "javascript": "Learn DOM, events and functions, then build a to-do list.",
    "react": "Learn components, props and state, then build a small app.",
    "sql": "Learn SELECT, WHERE, JOIN and GROUP BY on a sample table.",
    "mysql": "Install MySQL and practice creating tables and queries.",
    "git": "Learn init, add, commit, push and branches.",
    "github": "Upload your projects and write a clear README for each."
}

resume_text = read_file("resume.txt")
job_text = read_file("job.txt")

resume_skills = find_skills(resume_text, all_skills)
required_skills = find_skills(job_text, all_skills)

matched, missing, score = compare_skills(resume_skills, required_skills)
show_result(matched, missing, score)
show_suggestions(missing, suggestions)

from google import genai


def get_ai_feedback(resume_text, job_text):
    client = genai.Client()

    prompt = (
        "You are a helpful career coach for a fresher. "
        "Read the resume and the job description below. "
        "Give feedback in simple English in 5 short bullet points: "
        "what is good, what is missing, and how to improve the resume.\n\n"
        "RESUME:\n" + resume_text + "\n\n"
        "JOB DESCRIPTION:\n" + job_text
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    return response.text


print("\nAI Feedback:")
print(get_ai_feedback(resume_text, job_text))