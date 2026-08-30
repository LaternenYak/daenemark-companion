import streamlit as st
from deep_translator import GoogleTranslator

# --- KOPFZEILE & SEITEN-LAYOUT ---
st.set_page_config(page_title="Dänemark Companion", page_icon="🇩🇰", layout="centered")

st.title("🇩🇰 Dänemark Companion App")
st.caption("Dein Helfer für das Auswandern nach Dänemark")

# Navigation über ein Auswahlmenü (Tab-Struktur)
thema = st.selectbox(
    "Was möchtest du tun?",
    ["Währungsrechner (DKK / EUR)", "Wichtige Links & Adressen", "Wörterbuch & Übersetzer (DA / DE)"]
)

st.divider()

# --- MODUL 1: WÄHRUNGSRECHNER ---
if thema == "Währungsrechner (DKK / EUR)":
    st.subheader("💱 Währungsrechner")
    
    # Auswählbare Richtung
    richtung = st.radio(
        "Umrechnungsrichtung wählen:",
        ["DKK ➔ EUR", "EUR ➔ DKK"],
        horizontal=True
    )
    
    WECHSELKURS = 0.134  # 1 DKK ≈ 0,134 EUR
    
    if richtung == "DKK ➔ EUR":
        betrag_dkk = st.number_input("Betrag in DKK eingeben:", min_value=0.0, value=100.0, step=10.0)
        ergebnis_eur = round(betrag_dkk * WECHSELKURS, 2)
        st.success(f"**{betrag_dkk:.2f} DKK** entsprechen ca. **{ergebnis_eur:.2f} EUR**")
        
    else:
        betrag_eur = st.number_input("Betrag in EUR eingeben:", min_value=0.0, value=15.0, step=5.0)
        ergebnis_dkk = round(betrag_eur / WECHSELKURS, 2)
        st.success(f"**{betrag_eur:.2f} EUR** entsprechen ca. **{ergebnis_dkk:.2f} DKK**")


# --- MODUL 2: WICHTIGE LINKS ---
elif thema == "Wichtige Links & Adressen":
    st.subheader("🔗 Nützliche Auswanderer-Links")
    
    links = {
        "Bürgerservice & CPR-Nummer": ("https://www.borger.dk", "Offizielles Portal für Behördengänge und CPR-Registrierung."),
        "Dänische Steuerbehörde (Skat)": ("https://skat.dk", "Informationen zu Steuern, Steuerkarten und Abzügen."),
        "Work in Denmark": ("https://www.workindenmark.dk", "Offizielles Portal für internationale Arbeitssuchende."),
        "Dänisch lernen (Lærdansk)": ("https://www.laerdansk.dk", "Sprachkurse und Informationen zum Spracherwerb."),
        "Wohnungssuche (Boligsiden)": ("https://www.boligsiden.dk", "Übersicht über den Immobilien- und Mietmarkt."),
        "Wohnungssuche (Boligportal)": ("https://www.boligportal.dk", "Übersicht über den Immobilien- und Mietmarkt."),
        "Jobsuche (Jobindex)": ("https://www.jobindex.dk", "Stellenangebote."),
        "Jobsuche (Jobnet)": ("https://www.jobnet.dk", "Stellenangebote.")
    }
    
    for titel, (url, info) in links.items():
        with st.container():
            st.markdown(f"### [{titel}]({url})")
            st.write(info)
            st.divider()


# --- MODUL 3: UNBEGRENZTES WÖRTERBUCH & ÜBERSETZER ---
elif thema == "Wörterbuch & Übersetzer (DA / DE)":
    st.subheader("🌐 Dänisch-Deutsch Übersetzer")
    st.write("Übersetze beliebige Wörter oder ganze Sätze:")
    
    richtung = st.radio(
        "Richtung wählen:",
        ["Dänisch ➔ Deutsch", "Deutsch ➔ Dänisch"],
        horizontal=True
    )
    
    eingabe = st.text_input("Wort oder Satz eingeben:").strip()
    
    import streamlit as st
from deep_translator import GoogleTranslator

# --- KOPFZEILE & SEITEN-LAYOUT ---
st.set_page_config(page_title="Dänemark Companion", page_icon="🇩🇰", layout="centered")

st.title("🇩🇰 Dänemark Companion App")
st.caption("Dein Helfer für das Auswandern nach Dänemark")

# Navigation über ein Auswahlmenü (Tab-Struktur)
thema = st.selectbox(
    "Was möchtest du tun?",
    ["Währungsrechner (DKK / EUR)", "Wichtige Links & Adressen", "Wörterbuch & Übersetzer (DA / DE)"]
)

st.divider()

# --- MODUL 1: WÄHRUNGSRECHNER ---
if thema == "Währungsrechner (DKK / EUR)":
    st.subheader("💱 Währungsrechner")
    
    # Auswählbare Richtung
    richtung = st.radio(
        "Umrechnungsrichtung wählen:",
        ["DKK ➔ EUR", "EUR ➔ DKK"],
        horizontal=True
    )
    
    WECHSELKURS = 0.134  # 1 DKK ≈ 0,134 EUR
    
    if richtung == "DKK ➔ EUR":
        betrag_dkk = st.number_input("Betrag in DKK eingeben:", min_value=0.0, value=100.0, step=10.0)
        ergebnis_eur = round(betrag_dkk * WECHSELKURS, 2)
        st.success(f"**{betrag_dkk:.2f} DKK** entsprechen ca. **{ergebnis_eur:.2f} EUR**")
        
    else:
        betrag_eur = st.number_input("Betrag in EUR eingeben:", min_value=0.0, value=15.0, step=5.0)
        ergebnis_dkk = round(betrag_eur / WECHSELKURS, 2)
        st.success(f"**{betrag_eur:.2f} EUR** entsprechen ca. **{ergebnis_dkk:.2f} DKK**")


# --- MODUL 2: WICHTIGE LINKS ---
elif thema == "Wichtige Links & Adressen":
    st.subheader("🔗 Nützliche Auswanderer-Links")
    
    links = {
        "Bürgerservice & CPR-Nummer": ("https://www.borger.dk", "Offizielles Portal für Behördengänge und CPR-Registrierung."),
        "Dänische Steuerbehörde (Skat)": ("https://skat.dk", "Informationen zu Steuern, Steuerkarten und Abzügen."),
        "Work in Denmark": ("https://www.workindenmark.dk", "Offizielles Portal für internationale Arbeitssuchende."),
        "Dänisch lernen (Lærdansk)": ("https://www.laerdansk.dk", "Sprachkurse und Informationen zum Spracherwerb."),
        "Wohnungssuche (Boligsiden)": ("https://www.boligsiden.dk", "Übersicht über den Immobilien- und Mietmarkt."),
        "Wohnungssuche (Boligportal)": ("https://www.boligportal.dk", "Übersicht über den Immobilien- und Mietmarkt."),
        "Jobsuche (Jobindex)": ("https://www.jobindex.dk", "Stellenangebote."),
        "Jobsuche (Jobnet)": ("https://www.jobnet.dk", "Stellenangebote.")
    }
    
    for titel, (url, info) in links.items():
        with st.container():
            st.markdown(f"### [{titel}]({url})")
            st.write(info)
            st.divider()


# --- MODUL 3: UNBEGRENZTES WÖRTERBUCH & ÜBERSETZER ---
elif thema == "Wörterbuch & Übersetzer (DA / DE)":
    st.subheader("🌐 Dänisch-Deutsch Übersetzer")
    st.write("Übersetze beliebige Wörter oder ganze Sätze:")
    
    richtung = st.radio(
        "Richtung wählen:",
        ["Dänisch ➔ Deutsch", "Deutsch ➔ Dänisch"],
        horizontal=True
    )
    
    eingabe = st.text_input("Wort oder Satz eingeben:").strip()
    
    if eingabe:
        try:
            if richtung == "Dänisch ➔ Deutsch":
                uebersetzer = GoogleTranslator(source='da', target='de')
            else:
                uebersetzer = GoogleTranslator(source='de', target='da')
                
            ergebnis = uebersetzer.translate(eingabe)
            st.success(f"**Übersetzung:** {ergebnis}")
            
        except Exception as e:
            # Zeigt den exakten Fehler an, falls noch etwas fehlt
            st.error(f"Fehler bei der Übersetzung: {e}")
