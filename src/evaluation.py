# Use this to manually evaluate answers

def qualitative_eval(questions, rag_func):
    eval_results = []
    for q in questions:
        context = retrieve_context(q)['documents'][0]  # assuming top-1
        answer = generate_answer(q, context)
        eval_results.append({
            'question': q,
            'context': context,
            'answer': answer,
            'score': None,  # Fill manually after review
            'comments': ''
        })
    return eval_results