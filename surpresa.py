import streamlit as st
import time

# Configuração da página para ficar legal no celular
st.set_page_config(page_title="Surpresa para Bruna ❤️", page_icon="🎁")

# Estilo básico
st.title("Quiz do Nosso Amor 💘")
st.write("Bem-vinda, Bruninha! Responda corretamente para desbloquear sua surpresa.")

# Usando session_state para guardar a pontuação e a etapa
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0
if 'pontos' not in st.session_state:
    st.session_state.pontos = 0

# Perguntas (Substitua pelas histórias de vocês!)
perguntas = [
    {
        "pergunta": "Quem disse eu te amo primeiro??", 
        "opcoes": ["Guilherme", "Bruna", "o Simon"], 
        "resposta": "Guilherme"
    },
    {
        "pergunta": "Onde foi o nosso primeiro encontro?", 
        "opcoes": ["No cinema", "No parque", "No restaurante", "Em casa"], 
        "resposta": "No restaurante"
    },
    {
        "pergunta": "Quem é mais bagunceiro?", 
        "opcoes": ["Guilherme", "Bruna", "Nós dois", "Nenhum de nós"], 
        "resposta": "Bruna"
    },
    {
        "pergunta": "Qual é o momento que eu mais gosto no meu dia?", 
        "opcoes": ["Jogar videogame", "Quando estou com você", "Dormir", "Comer"], 
        "resposta": "Quando estou com você"
    }
]

# Lógica do Quiz
if st.session_state.etapa < len(perguntas):
    q = perguntas[st.session_state.etapa]
    st.subheader(f"Pergunta {st.session_state.etapa + 1} de {len(perguntas)}:")
    st.write(q["pergunta"])
    
    # Exibe as opções como botões de rádio
    resposta_usuario = st.radio("Escolha a alternativa correta:", q["opcoes"], key=f"radio_{st.session_state.etapa}")
    
    if st.button("Confirmar Resposta"):
        if resposta_usuario == q["resposta"]:
            st.success("Acertou! 🥰")
            st.session_state.pontos += 1
        else:
            st.error("Errou... mas eu te amo mesmo assim! 😂")
        
        time.sleep(1.5) # Pequena pausa para ela ler a mensagem
        st.session_state.etapa += 1
        st.rerun() # Recarrega a página para a próxima pergunta

else:
    st.balloons() # Animação de balões na tela
    st.header("Fim do Quiz! 🎉")
    st.write(f"Você acertou **{st.session_state.pontos}** de **{len(perguntas)}** perguntas.")
    
    if st.session_state.pontos == len(perguntas):
        st.success("Nota máxima! O seu presente está escondido em [insira o local aqui]. Te amo!")
    else:
        st.warning("Não tirou nota 10, mas o que importa é o amor! ❤️ O seu presente te aguarda em [insira o local].")
    
    if st.button("Tentar de novo"):
        st.session_state.etapa = 0
        st.session_state.pontos = 0
        st.rerun()