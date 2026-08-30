import streamlit as st
from deep_translator import MyMemoryTranslator

# --- KOPFZEILE & SEITEN-LAYOUT ---
st.set_page_config(page_title="Dänemark Companion", page_icon="🇩🇰", layout="centered")

st.title("🇩🇰 Dänemark Companion App")
st.caption("Dein Helfer für das Auswandern nach Dänemark")

# Navigation über ein Auswahlmenü
thema = st.selectbox(
    "Was möchtest du tun?",
    ["Währungsrechner (DKK / EUR)", "Wichtige Links & Adressen", "Wörterbuch & Übersetzer (DA / DE)"]
)

st.divider()

# --- MODUL 1: WÄHRUNGSRECHNER ---
if thema == "Währungsrechner (DKK / EUR)":
    st.subheader("💱 Währungsrechner")
    
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


# --- MODUL 3: WÖRTERBUCH & ÜBERSETZER ---
elif thema == "Wörterbuch & Übersetzer (DA / DE)":
    st.subheader("🌐 Dänisch-Deutsch Wörterbuch")
    
    # Integrierte Vokabeldatenbank für präzise Ergebnisse
    woerterbuch = {
        # Grundbegriffe & Alltag
        "ja": "ja", "nej": "nein", "tak": "danke", "mange tak": "vielen Dank",
        "hej": "hallo", "farvel": "auf Wiedersehen", "godmorgen": "guten Morgen",
        "goddag": "guten Tag", "godaften": "guten Abend", "godnat": "gute Nacht",
        "undskyld": "Entschuldigung", "hvilken": "welcher / welche", "hvor": "wo",
        "hvad": "was", "hvem": "wer", "hvornår": "wann", "hvorfor": "warum",
        "ikke": "nicht", "måske": "vielleicht", "hjælp": "Hilfe",

        # Behörden & Auswandern
        "kommune": "Gemeinde / Kommune", "borgerservice": "Bürgerservice",
        "cpr-nummer": "Personennummer (CPR)", "skat": "Steuer / Steuerbehörde",
        "skattekort": "Steuerkarte", "nemid": "MitID / NemID", "mitid": "MitID",
        "arbejde": "Arbeit", "job": "Job", "ansøgning": "Bewerbung",
        "kontrakt": "Vertrag", "løn": "Lohn / Gehalt", "opholdstilladelse": "Aufenthaltserlaubnis",
        
        # Wohnung & Leben
        "bolig": "Wohnung / Haus", "lejlighed": "Wohnung", "hus": "Haus",
        "leje": "Miete", "husleje": "Kaltmiete", "depositum": "Kaution",
        "vand": "Wasser", "varme": "Heizung", "strøm": "Strom",
        "supermarked": "Supermarkt", "butik": "Geschäft", "bil": "Auto"
    }

    richtung = st.radio(
        "Richtung wählen:",
        ["Dänisch ➔ Deutsch", "Deutsch ➔ Dänisch"],
        horizontal=True
    )

    eingabe = st.text_input("Wort oder Begriff eingeben:").strip().lower()

    if eingabe:
        gefunden = False
        
        if richtung == "Dänisch ➔ Deutsch":
            if eingabe in woerterbuch:
                st.success(f"**{eingabe.capitalize()}** ➔ **{woerterbuch[eingabe]}**")
                gefunden = True
        else:  # Deutsch -> Dänisch
            treffer = [da for da, de in woerterbuch.items() if eingabe in de.lower()]
            if treffer:
                st.success(f"**{eingabe.capitalize()}** ➔ **{', '.join(treffer)}**")
                gefunden = True

        if not gefunden:
            st.info("💡 Das Wort ist noch nicht in der Schnell-Datenbank. Verwende Online-Suche...")
            try:
                from deep_translator import GoogleTranslator
                if richtung == "Dänisch ➔ Deutsch":
                    res = GoogleTranslator(source='da', target='de').translate(eingabe)
                else:
                    res = GoogleTranslator(source='de', target='da').translate(eingabe)
                st.success(f"**Übersetzung:** {res}")
            except Exception as e:
                st.warning("Keine Treffer im Wörterbuch gefunden.")

    with st.expander("📖 Alle gespeicherten Wörterbuch-Begriffe anzeigen"):
        st.json(woerterbuch)
