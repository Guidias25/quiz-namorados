import streamlit as st
import time

# Configuração da página para ficar legal no celular
st.set_page_config(page_title="Surpresa para Bruna ❤️", page_icon="🎁")

# --- INÍCIO DA MUDANÇA DE VISUAL COM CORAÇÕES ---
st.markdown("""
    <style>
    /* Fundo rosa clarinho com estampa de corações suaves em SVG */
    .stApp {
        background-color: #FFF0F5; 
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 50 50'%3E%3Cpath d='M25 39.7l-1.5-1.5C14.3 29.2 8 23.6 8 16.5 8 11.8 11.8 8 16.5 8c2.7 0 5.3 1.3 6.9 3.3L25 13.5l1.6-2.2C28.2 9.3 30.8 8 33.5 8 38.2 8 42 11.8 42 16.5c0 7.1-6.3 12.7-15.5 21.7L25 39.7z' fill='%23ffc0cb' fill-opacity='0.6'/%3E%3C/svg%3E");
    }
    
    /* Muda a cor dos textos principais para um tom de vermelho/vinho */
    h1, h2, h3, p, .stRadio label {
        color: #8B0000 !important;
    }
    
    /* Dá um destaque no botão */
    .stButton>button {
        background-color: #FF1493;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
# --- FIM DA MUDANÇA DE VISUAL ---

# Estilo básico
st.title("Quiz do Nosso Amor 💘")
st.write("Bem-vinda, Bruninha! Responda corretamente para desbloquear sua surpresa.")

# --- PLAYER DE MÚSICA ---
st.write("🎧 **Aperte o play para entrar no clima antes de começar:**")
try:
    st.audio("musica.mp3", format="audio/mp3")
except:
    st.write("*(Música não encontrada. Certifique-se de que o arquivo musica.mp3 está na mesma pasta e no GitHub!)*")
st.divider()

# Usando session_state para guardar a pontuação e a etapa
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0
if 'pontos' not in st.session_state:
    st.session_state.pontos = 0

# Perguntas 
perguntas = [
    {
        "pergunta": "Quem disse eu te amo primeiro??", 
        "opcoes": ["Guilherme", "Bruna", "Simon"], 
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
    },
    {
        "pergunta": "Quando a gente senta para jogar alguma coisa juntos, quem é o mais competitivo?", 
        "opcoes": ["Bruna", "Guilherme", "Simon"], 
        "resposta": "Bruna"
    },
    {
        "pergunta": "O que me faz ter a certeza absoluta de que você é a parceira ideal para a minha vida?", 
        "opcoes": ["O seu sorriso incrível", "A nossa parceria em todos os momentos", "A paciência que você tem comigo", "Todas as alternativas anteriores"], 
        "resposta": "Todas as alternativas anteriores"
    },
    {
        "pergunta": "Quando bate aquele TDH fortíssimo, quem é a pessoa mais provável de esquecer onde colocou o controle remoto ou o celular?", 
        "opcoes": ["Guilherme","Bruna","Os dois","A gente é muito organizado, isso nunca acontece"], 
        "resposta": "Os dois"
    },
    {
        "pergunta": "Quem mais dorme nas viagens de carro?", 
        "opcoes": ["Bruna", "Guilherme", "Ninguém dorme"], 
        "resposta": "Bruna"
    },
    {
        "pergunta": "Quem é mais provável de tirar um cochilinho à tarde?", 
        "opcoes": ["Bruna", "Guilherme", "Nenhum dos dois"], 
        "resposta": "Bruna"
    },
    {
        "pergunta": "Qual a cor branca do cavalo de Gilson Katatau?", 
        "opcoes": ["Branco", "Preto", "Vermelho"], 
        "resposta": "Branco"
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
    
    st.divider() # Linha para separar e deixar o visual bonito
    
    # Mensagem personalizada de acordo com a pontuação
    if st.session_state.pontos == len(perguntas):
        st.success("Nota 10 de outubro, para combinar com você, meu amor! Parabéns pela sua inteligência de outro universo. Te amo! ❤️")
    else:
        st.warning("Não tirou nota 10, mas o que importa é o amor! ❤️ Te amo demais!")
    
    st.divider()
    
    # A Charada com Suspense
    st.subheader("🕵️‍♀️ O Desafio Final: Onde está o seu presente?")
    st.write("Para descobrir o seu prêmio, resolva este último enigma:")
    
    st.info("Sou o esconderijo oficial da bagunça, onde as blusas se multiplicam sozinhas e os sapatos formam uma montanha que a gente sempre promete arrumar no fim de semana. Onde o seu presente te espera?")
    
    # O botão de suspense para revelar o Closet
    if st.button("Revelar o esconderijo!"):
        st.success("O seu presente está escondido na bagunça do **CLOSET**! Corre lá! 🎁🏃‍♀️💨")
    
    st.write("") # Espaço em branco
    if st.button("Tentar de novo"):
        st.session_state.etapa = 0
        st.session_state.pontos = 0
        st.rerun()
