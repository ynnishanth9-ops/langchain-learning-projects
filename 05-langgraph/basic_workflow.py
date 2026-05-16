from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class WorkflowState(TypedDict):
    topic: str
    explanation: str


def generate_explanation(state: WorkflowState):
    topic = state["topic"]

    return {
        "explanation": f"This is a simple LangGraph workflow about {topic}."
    }


def main():
    graph_builder = StateGraph(WorkflowState)

    graph_builder.add_node("generate_explanation", generate_explanation)

    graph_builder.add_edge(START, "generate_explanation")
    graph_builder.add_edge("generate_explanation", END)

    graph = graph_builder.compile()

    result = graph.invoke({
        "topic": "AI automation"
    })

    print(result["explanation"])


if __name__ == "__main__":
    main()
