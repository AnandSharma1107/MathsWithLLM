🔢 Maths & Knowledge AI Assistant

This is a small AI tool which can help you solve math questions, think logically, and find information from Wikipedia. It’s powered by a GPT-OSS-120B model from Groq.

🛠️ What it can do
Maths Calculator: Solve simple and complex maths questions like 2+2, sqrt(16), etc.
Reasoning Tool: Gives step-by-step explanation for logic or reasoning questions.
Wikipedia Search: Finds quick information about any topic from Wikipedia.
Interactive Web App: You can ask questions directly and get instant answers.
📦 Packages Used
langchain_groq – For connecting to GPT-OSS-120B
langchain – To make chains and agents
langchain_community – For Wikipedia search
streamlit – To make a simple web app
math – For safe math calculations
⚡ How to Run
Clone the project:
git clone https://github.com/your-username/MathsWithLLM.git
cd MathsWithLLM
Install packages:
pip install -r requirements.txt
Run the app:
streamlit run app.py
Enter your Groq API Key in the sidebar and ask your question.
💡 Example Questions
What is 25 + 17?
Solve: If x + 5 = 12, what is x?
Who discovered India’s first satellite?
Integrate x^2 dx
