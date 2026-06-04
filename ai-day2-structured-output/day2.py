import ollama
import json

resume_text = """
Name: Nishanth Mekala

Education:

* Motilal Nehru National Institute of Technology Allahabad
  Degree: B.Tech in Electronics and Communication Engineering
  CGPA: 8.38/10
  Duration: August 2018 – May 2022

* Sri Chaitanya Educational Institutions
  Qualification: Class XII
  Percentage: 96.8%
  Duration: April 2016 – April 2018

Skills:

* React.js
* TypeScript
* AWS
* Java
* Next.js
* Redux
* Tailwind CSS
* Spring
* PostgreSQL
* React Native
* Flutter
* Kotlin
* Python
* Android
* CI/CD
* Linux
* Data Structures & Algorithms

Experience:

* Company: Capmint
  Role: Senior Software Engineer (frontend)

* Company: Tick2Trade
  Role: Full-stack Engineer (frontend focused)

* Company: Donatekart
  Role: React Native Developer Intern

* Company: Besseggen
  Role: Android Developer Intern

Projects:

* College User & Admin Android Apps
  Developed 2 fully functional Android applications using Kotlin and Firebase as a self-taught college project.
  Features included:

  * Student app with 10+ screens
  * Admin app managing 50+ mock records
  * MNNIT notices management
  * Faculty directory
  * 12 department modules
  * E-book listings system


"""

prompt = f"""
You are an expert resume parser.

Return ONLY valid JSON.

Schema:
{{
  "name": "",
  "skills": [],
  "experience": [
    {{
      "company": "",
      "role": ""
    }}`
  ],
  "education": {{
    "school": "",
    "passed out":"",
    "degree": "",
    "course": ""
  }},
  "projects": [
  {{
    "project": "",
    "summary": "",
    "tech": [],
    "features": [],

  }}],
}}

Resume:
{resume_text}
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

output = response["message"]["content"]

print("RAW OUTPUT:\n")
print(output)

print("\nPARSED JSON:\n")

try:
    parsed = json.loads(output)

    print(json.dumps(parsed, indent=2))

except Exception as e:
    print("JSON parsing failed")
    print(e)