from langchain_ollama import OllamaLLM
from langchain_core.callbacks import StreamingStdOutCallbackHandler

# Configuração atualizada do modelo
llm = OllamaLLM(
    model="llama2",
    # No LangChain 0.3+, passamos uma lista diretamente para 'callbacks'
    callbacks=[StreamingStdOutCallbackHandler()]
)

def gerar_insights_sobre_filmes(pergunta):
    prompt = f"Responda a seguinte pergunta sobre filmes: {pergunta}\n"
    prompt += "Por favor, forneça um resumo detalhado e quaisquer informações relevantes."
    
    # O método invoke continua o mesmo
    insights = llm.invoke(prompt)
    return insights

def responder_pergunta(pergunta):
    return gerar_insights_sobre_filmes(pergunta)

def main():
    pergunta = input("Sobre qual filme você deseja saber informações? ")
    resposta = responder_pergunta(pergunta)
    # Como o streaming já imprime no terminal, este print final pode ser opcional 
    # ou apenas para pular uma linha.
    print(f"\nConcluído.")

if __name__ == "__main__":
    main()