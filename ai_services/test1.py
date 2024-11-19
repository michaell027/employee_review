from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Define the prompt template
template = """Question: {question}

Answer: Let's think step by step."""

# Create the prompt template
prompt = ChatPromptTemplate.from_template(template)

# Define the model
model = OllamaLLM(model="llama3.2")

# Create the chain by combining the prompt with the model
chain = prompt | model

# Invoke the chain with a specific input and print the result
result = chain.invoke({"question": "What is LangChain?"})
print(result)
