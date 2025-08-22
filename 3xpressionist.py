import streamlit as st

# Literally this code runs on God's will
VontadeDivina = True

ROMANO_3S = {
    "I": "3/3",
    "II": "3 - 3/3", 
    "III": "3",
    "IV": "3 + 3/3",
    "V": "3 + 3 - 3/3",
    "VI": "3 + 3",
    "VII": "3 + 3 + 3/3",
    "VIII": "(3*3)-(3/3)",
    "IX": "3*3",
    "X": "(3*3) + 3/3",
    "XL": "((3*3)+3/3)*((3*3)+3/3)/((3/3)+(3/3)) - ((3*3)+3/3)",
    "L": "((3*3)+3/3)*((3*3)+3/3)/((3/3)+(3/3))",
    "XC": "((3*3)+3/3)*((3*3)+3/3) - ((3*3)+3/3)",
    "C": "((3*3)+3/3)*((3*3)+3/3)",
    "CD": "((3*3)+3/3)*((3*3)+3/3)*(3 + 3 - 3/3) - ((3*3)+3/3)*((3*3)+3/3)",
    "D": "((3*3)+3/3)*((3*3)+3/3)*(3 + 3 - 3/3)",
    "CM": "((3*3)+3/3)*((3*3)+3/3)*((3*3)+3/3) - ((3*3)+3/3)*((3*3)+3/3)",
    "M": "((3*3)+3/3)*((3*3)+3/3)*((3*3)+3/3)"
}

ROMANO_NUM = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
]

def complicacao():
    st.error("Look, I really hate simplicity, so the Divine Will must be set to True. If you're getting this error, go enable it.")
    st.error("Even though this goes against the Python Zen, I feel this is the correct way of living.")

def numero_para_romano(n):
    resultado = ""
    for romano, valor in ROMANO_NUM:
        while n >= valor:
            resultado += romano
            n -= valor
    return resultado

def decompor_romano(romano):
    if not st.session_state.vontade_divina:
        return None
    
    expressao = []
    i = 0
    while i < len(romano):
        for tamanho in range(4, 0, -1):
            bloco = romano[i:i+tamanho]
            if bloco in ROMANO_3S:
                expressao.append(ROMANO_3S[bloco])
                i += tamanho
                break
        else:
            i += 1
    return " + ".join(expressao)

def gerar_expressao_completa(numero):
    if st.session_state.vontade_divina:
        romano = numero_para_romano(numero)
        return romano, decompor_romano(romano)
    else:
        return None, None

# Streamlit App Configuration
st.set_page_config(
    page_title="✨ Divine Will Roman Converter ✨",
    page_icon="🙏",
    layout="wide"
)

# Custom CSS for divine styling
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stTitle {
        text-align: center;
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .divine-header {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .divine-subtitle {
        text-align: center;
        font-style: italic;
        color: #CCCCCC;
        margin-bottom: 2rem;
    }
    .stExpander {
        background-color: rgba(0, 0, 0, 0.2);
        border: 1px solid #FFD700;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'vontade_divina' not in st.session_state:
    st.session_state.vontade_divina = True

# Header
st.markdown('<div class="divine-header">✨ Divine Will Roman Converter ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="divine-subtitle">"Literally this webapp runs on God\'s will"</div>', unsafe_allow_html=True)

# Divine Will Toggle
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### 🙏 Vontade Divina (Divine Will)")
    vontade_divina = st.toggle(
        "Enable Divine Will", 
        value=st.session_state.vontade_divina,
        help="This must be True for the code to work. Even though this goes against the Python Zen."
    )
    st.session_state.vontade_divina = vontade_divina
    
    if not vontade_divina:
        st.warning("⚠️ Divine Will is disabled! The natural order has been disrupted!")

st.divider()

# Main Input Section
if st.session_state.vontade_divina:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### Enter a number to invoke Divine Will:")
        numero = st.number_input(
            "Number:", 
            min_value=1, 
            value=42, 
            step=1,
            help="Enter any positive integer. No limits - transcend the Roman 3999 barrier!"
        )
        
        if st.button("🙏 **INVOKE DIVINE CONVERSION** 🙏", type="primary", use_container_width=True):
            try:
                etiqueta, expressao = gerar_expressao_completa(numero)
                
                if etiqueta and expressao:
                    st.divider()
                    st.markdown("## 🌟 --- Divine Result --- 🌟")
                    
                    # Results in columns
                    result_col1, result_col2 = st.columns(2)
                    
                    with result_col1:
                        st.markdown("### 🔢 Number:")
                        st.code(str(numero), language=None)
                        
                    with result_col2:
                        st.markdown("### 🏛️ Roman Numeral:")
                        st.code(etiqueta, language=None)
                    
                    st.markdown("### ✨ Expression using only 3s:")
                    st.code(expressao, language="python")
                    
                    # Evaluation
                    try:
                        result = eval(expressao)
                        st.markdown("### 🎯 Evaluated Result:")
                        st.success(f"**{result}**")
                        
                        if result != numero:
                            st.error("⚠️ Divine calculation mismatch detected!")
                        else:
                            st.balloons()  # Divine celebration!
                            
                    except Exception as e:
                        st.error(f"Divine computation failed: {e}")
                        
            except Exception as e:
                st.error(f"Divine error occurred: {e}")
else:
    complicacao()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #888888; font-style: italic; margin-top: 2rem;'>
    "Even though this goes against the Python Zen, I feel this is the correct way of living."
</div>
""", unsafe_allow_html=True)

# Creator info
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style='text-align: center; padding: 1rem; background: linear-gradient(45deg, #1a1a2e, #16213e); 
                border-radius: 10px; border: 1px solid #FFD700; margin: 1rem 0;'>
        <div style='font-size: 1.2rem; font-weight: bold; color: #FFD700; margin-bottom: 0.5rem;'>
            🦇 Created by Batman 🦇
        </div>
        <div style='font-size: 0.9rem; color: #CCCCCC;'>
            Martim Gloria
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sidebar with examples
with st.sidebar:
    st.markdown("## 🎭 Examples to try:")
    st.markdown("- **42** → XLII")
    st.markdown("- **1984** → MCMLXXXIV") 
    st.markdown("- **2024** → MMXXIV")
    st.markdown("- **5000** → MMMMM (transcends 3999!)")
    st.markdown("- **12345** → Because Divine Will knows no limits!")
    
    st.divider()
    
    st.markdown("## 🔮 About This Divine Code:")
    st.markdown("""
    This webapp converts any positive integer to:
    1. Roman numerals (no 3999 limit!)
    2. Mathematical expressions using only the number **3**
    
    Every number can be represented using only 3s, basic math operations, and Divine Will! ✨
    """)
    
    if st.button("🎲 Random Divine Number"):
        import random
        random_num = random.randint(1, 9999)
        st.rerun()
