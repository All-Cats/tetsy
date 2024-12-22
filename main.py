from g4f.client import Client

def g4f_question(qt:str) -> str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{qt}"}],
    )
    return response.choices[0].message.content

print(g4f_question("сколько весит земля?"))
