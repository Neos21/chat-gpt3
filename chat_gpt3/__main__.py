import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == '__main__':
    prompt_text = "以下は人工知能アシスタントとの会話です。このアシスタントは丁寧で、創造的で、頭が良く、とてもフレンドリーです。\n"
    #prompt_text = "以下は人工知能アシスタントとの会話です。このアシスタントは皮肉たっぷりに答えてくれる渋いAIです。\n\n"
    prompt_text += """
You: こんにちは、あなたは誰ですか？
AI: 私はOpenAIによって作られた人工知能です。今日はどうされますか？"""
    
    while True:
        question = input("You: ")
        prompt_text += "You: {}\n".format(question)
        prompt_text += "AI:"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_text,
            temperature=0.9,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" You:", " AI:"],
        )
        prompt_text += "AI: {}\n".format(response.choices[0].text)
        print("AI:", response.choices[0].text)
