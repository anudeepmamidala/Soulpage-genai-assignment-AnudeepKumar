from transformers import pipeline
from tools import web_search


class ConversationalKnowledgeBot:
    """
    Conversational bot with:
    - Memory (conversation history)
    - External knowledge (Wikipedia)
    - Context-aware responses
    """

    def __init__(self):
        print("[⚙️ Loading LLM: google/flan-t5-base]")
        self.llm = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            device=-1
        )
        self.chat_history = []

    def build_prompt(self, user_input, context=""):
        history_text = ""
        if self.chat_history:
            recent = self.chat_history[-2:]
            history_text = "\n".join(
                [f"Q: {h['user']}\nA: {h['bot']}" for h in recent]
            )

        prompt = f"""
Context:
{context}

Conversation History:
{history_text}

Answer the question clearly and factually.

Question: {user_input}
Answer:
"""
        return prompt.strip()

    def respond(self, user_input):
        needs_search = any(
            kw in user_input.lower()
            for kw in ["who", "what", "when", "where", "ceo", "founder", "capital"]
        )

        context = ""
        if needs_search:
            context = web_search(user_input)

        prompt = self.build_prompt(user_input, context)

        print("[💭 Generating response...]")
        output = self.llm(
            prompt,
            max_new_tokens=120,
            do_sample=False
        )

        answer = output[0]["generated_text"].strip()
        if not answer:
            answer = "I'm not sure about that."

        self.chat_history.append({
            "user": user_input,
            "bot": answer
        })

        return answer


def main():
    print("=" * 50)
    print("🤖 Conversational Knowledge Bot")
    print("=" * 50)
    print("• Remembers conversation")
    print("• Uses Wikipedia for facts")
    print("• Context-aware answers")
    print("Type 'exit' to quit")
    print("=" * 50)

    bot = ConversationalKnowledgeBot()

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye 👋")
            break

        response = bot.respond(user_input)
        print(f"\nBot: {response}")


if __name__ == "__main__":
    main()
