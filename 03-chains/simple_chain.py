from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    prompt = ChatPromptTemplate.from_template(
        "Explain the concept of {topic} in simple terms."
    )

    parser = StrOutputParser()

    chain = prompt | model | parser

    response = chain.invoke({
        "topic": "LangChain chains"
    })

    print(response)


if __name__ == "__main__":
    main()
