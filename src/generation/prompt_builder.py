def build_prompt(query: str, chunks: list) -> str:
    context = "\n\n".join([
        f"[Source: {c['source']} | Page {c['page']}]\n{c['text']}"
        for c in chunks
    ])
    return f"""You are a research assistant. Answer the question based only on the provided context.
If the answer is not in the context, say "I cannot find this in the provided documents."

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:"""


def build_summary_prompt(chunks: list, paper_name: str) -> str:
    context = "\n\n".join([c["text"] for c in chunks])
    return f"""You are a research assistant. Summarize the following research paper.
Cover: main objective, methodology, key findings, and conclusions.

PAPER: {paper_name}

CONTENT:
{context}

SUMMARY:"""
