import streamlit as st
import random
import json
from pathlib import Path

# ─────────────────────────────────────────
#  Konfigurasi Halaman
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Klinik Matematik Amir Syafiq",
    page_icon="🎮",
    layout="wide"
)

# ─────────────────────────────────────────
#  CSS TEMA ROBLOX — Dark Mode Gamer
# ─────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@700;900;1000&display=swap');

  /* ══ LATAR BELAKANG GELAP ROBLOX ══ */
  .stApp {
    background:
      radial-gradient(ellipse at top,    #1a0a2e 0%,  transparent 60%),
      radial-gradient(ellipse at bottom, #0a1a2e 0%,  transparent 60%),
      #0d0d14;
    font-family: 'Fredoka One', 'Nunito', sans-serif !important;
  }

  /* Grid dots overlay — tekstur khas Roblox */
  .stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: radial-gradient(circle, rgba(255,255,255,0.04) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
    z-index: 0;
  }

  /* ══ LEBAR KANDUNGAN ══ */
  .block-container {
    max-width: 1050px !important;
    margin: auto !important;
    padding-top: 1.5rem !important;
    position: relative;
    z-index: 1;
  }

  /* ══ TAJUK UTAMA — Glow merah Roblox ══ */
  .tajuk-roblox {
    text-align: center;
    font-family: 'Fredoka One', sans-serif;
    font-size: 3.6em;
    font-weight: 900;
    letter-spacing: 2px;
    padding: 20px 10px 5px;
    background: linear-gradient(180deg, #ff4444 0%, #ffcc00 60%, #ff8800 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 18px rgba(255, 80, 0, 0.7));
    line-height: 1.1;
  }
  .tajuk-sub {
    text-align: center;
    font-family: 'Fredoka One', sans-serif;
    font-size: 1.3em;
    color: #aabbcc;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 6px;
  }

  /* ══ DIVIDER NEON ══ */
  hr {
    border: none;
    height: 3px;
    background: linear-gradient(90deg, transparent, #ff4444, #ffcc00, #00ccff, transparent);
    margin: 12px 0 18px;
  }

  /* ══ LEADERBOARD SCOREBOARD ══ */
  .leaderboard {
    background: linear-gradient(135deg, #1a0000 0%, #2a0808 50%, #1a0000 100%);
    border: 4px solid #ff3c3c;
    border-radius: 16px;
    padding: 16px 28px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow:
      0 0 30px rgba(255, 60, 60, 0.5),
      0 0 60px rgba(255, 60, 60, 0.2),
      inset 0 0 40px rgba(0, 0, 0, 0.6);
    margin-bottom: 18px;
  }
  .leaderboard::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #ff0000, #ff8800, #ffcc00, #ff8800, #ff0000);
    animation: shimmer 2s linear infinite;
  }
  @keyframes shimmer {
    0%   { background-position: -200% 0; }
    100% { background-position:  200% 0; }
  }
  .leaderboard-title {
    font-family: 'Fredoka One', sans-serif;
    font-size: 1.0em;
    color: #ff6666;
    letter-spacing: 5px;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .leaderboard-score {
    font-family: 'Fredoka One', sans-serif;
    font-size: 2.4em;
    color: #ffd700;
    text-shadow:
      3px 3px 0 #8b4500,
      0   0 20px rgba(255, 215, 0, 0.8);
    letter-spacing: 2px;
  }
  .leaderboard-stars {
    font-size: 1.8em;
    letter-spacing: 4px;
    margin-top: 4px;
  }

  /* ══ BADGE KATEGORI ══ */
  .badge-kategori {
    display: inline-block;
    padding: 8px 24px;
    border-radius: 6px;
    font-family: 'Fredoka One', sans-serif;
    font-size: 1.4em;
    font-weight: 900;
    color: white;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
    border-bottom: 5px solid rgba(0,0,0,0.4);
    text-shadow: 1px 1px 0 rgba(0,0,0,0.5);
  }

  /* ══ PROGRESS — Bar neon ══ */
  .stProgress > div > div > div > div {
    background: linear-gradient(90deg, #ff4444, #ff8800, #ffcc00) !important;
    border-radius: 10px;
  }
  .stProgress > div > div {
    background: #1e1e2e !important;
    border: 2px solid #333355;
    height: 20px !important;
    border-radius: 10px;
  }
  .progress-text {
    text-align: center;
    font-family: 'Fredoka One', sans-serif;
    font-size: 1.4em;
    color: #aabbcc;
    letter-spacing: 2px;
    margin-bottom: 10px;
  }

  /* ══ KOTAK SOALAN — Panel gelap bersinar ══ */
  .kotak-soalan {
    background: linear-gradient(135deg, #0d1b2a 0%, #1a2a3a 100%);
    border: 4px solid #00b4ff;
    border-radius: 20px;
    padding: 35px 30px;
    text-align: center;
    margin: 14px 0;
    box-shadow:
      0 0 30px rgba(0, 180, 255, 0.35),
      0 0 60px rgba(0, 180, 255, 0.15),
      inset 0 0 40px rgba(0, 0, 0, 0.5);
    position: relative;
  }
  .kotak-soalan::after {
    content: '';
    position: absolute;
    inset: 3px;
    border-radius: 17px;
    border: 1px solid rgba(0,180,255,0.2);
    pointer-events: none;
  }
  .emoji-soalan {
    font-size: 3.0em;
    letter-spacing: 3px;
    line-height: 1.8;
  }
  .nombor-soalan {
    font-family: 'Fredoka One', sans-serif;
    font-size: 4.0em;
    font-weight: 900;
    color: #ffffff;
    text-shadow:
      3px 3px 0 #003366,
      0   0 25px rgba(0, 180, 255, 0.9);
    margin-top: 12px;
    letter-spacing: 3px;
  }

  /* ══ LABEL PILIHAN ══ */
  h3 {
    font-family: 'Fredoka One', sans-serif !important;
    font-size: 2.0em !important;
    color: #ffcc00 !important;
    text-align: center !important;
    letter-spacing: 2px !important;
    text-shadow: 2px 2px 0 #664400 !important;
  }

  /* ══ BUTANG JAWAPAN — 3D Roblox Block ══ */
  div.stButton > button {
    width: 100%;
    font-family: 'Fredoka One', sans-serif !important;
    font-size: 4.6em !important;
    line-height: 1.1 !important;
    font-weight: 900 !important;
    padding: 38px 14px !important;
    min-height: 130px !important;
    border-radius: 16px !important;
    border: none !important;
    color: #ffffff !important;
    letter-spacing: 2px;
    text-shadow: 3px 3px 0 rgba(0,0,0,0.5) !important;
    /* Warna latar — Hijau neon Roblox */
    background: linear-gradient(180deg, #00dd55 0%, #00aa33 100%) !important;
    /* Kesan 3D — bayangan tebal bawah */
    box-shadow:
      0 10px 0 #005500,
      0 12px 25px rgba(0, 200, 80, 0.4) !important;
    transform: translateY(-5px);
    transition: all 0.08s ease !important;
    margin: 8px 0 !important;
    cursor: pointer;
  }
  div.stButton > button:hover {
    background: linear-gradient(180deg, #00ff66 0%, #00cc44 100%) !important;
    box-shadow:
      0 12px 0 #005500,
      0 15px 30px rgba(0, 255, 100, 0.5) !important;
    transform: translateY(-7px) !important;
    color: #ffffff !important;
  }
  div.stButton > button:active {
    transform: translateY(2px) !important;
    box-shadow:
      0 3px 0 #005500,
      0 5px 10px rgba(0,0,0,0.3) !important;
  }

  /* ══ BUTANG SETERUSNYA / CUBA LAGI — Biru Roblox ══ */
  div.stButton > button[kind="primary"],
  .btn-next div.stButton > button {
    background: linear-gradient(180deg, #0099ff 0%, #0066cc 100%) !important;
    box-shadow:
      0 10px 0 #003388,
      0 12px 25px rgba(0, 150, 255, 0.4) !important;
  }

  /* ══ MAKLUM BALAS BETUL ══ */
  .maklumbalas-betul {
    background: linear-gradient(135deg, #003300 0%, #004d00 100%);
    border: 4px solid #00ff55;
    border-radius: 18px;
    padding: 28px 20px;
    text-align: center;
    color: #00ff55;
    font-family: 'Fredoka One', sans-serif;
    font-size: 2.6em;
    font-weight: 900;
    margin: 16px 0;
    letter-spacing: 2px;
    box-shadow:
      0 0 30px rgba(0, 255, 85, 0.5),
      0 0 60px rgba(0, 255, 85, 0.2);
    text-shadow: 0 0 20px rgba(0, 255, 85, 0.9);
  }

  /* ══ MAKLUM BALAS SALAH ══ */
  .maklumbalas-salah {
    background: linear-gradient(135deg, #2a0000 0%, #3d0000 100%);
    border: 4px solid #ff3c3c;
    border-radius: 18px;
    padding: 28px 20px;
    text-align: center;
    color: #ff6666;
    font-family: 'Fredoka One', sans-serif;
    font-size: 2.6em;
    font-weight: 900;
    margin: 16px 0;
    letter-spacing: 2px;
    box-shadow:
      0 0 30px rgba(255, 60, 60, 0.5),
      0 0 60px rgba(255, 60, 60, 0.2);
    text-shadow: 0 0 15px rgba(255, 60, 60, 0.8);
  }

  /* ══ SKRIN TAMAT — Victory Screen ══ */
  .skrin-tamat {
    text-align: center;
    background: linear-gradient(135deg, #0d0d1a 0%, #1a0a2e 50%, #0d0d1a 100%);
    border: 5px solid #ffd700;
    border-radius: 24px;
    padding: 45px 35px;
    box-shadow:
      0 0 40px rgba(255, 215, 0, 0.5),
      0 0 80px rgba(255, 215, 0, 0.2),
      inset 0 0 60px rgba(0,0,0,0.5);
    position: relative;
    overflow: hidden;
  }
  .skrin-tamat::before {
    content: '';
    position: absolute;
    top: -2px; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #ff4444, #ff8800, #ffd700, #00ff88, #00b4ff, #ff4444);
    background-size: 200%;
    animation: shimmer 3s linear infinite;
  }
  .tamat-tajuk {
    font-family: 'Fredoka One', sans-serif;
    font-size: 2.4em;
    letter-spacing: 3px;
    margin: 12px 0;
  }
  .tamat-skor {
    font-family: 'Fredoka One', sans-serif;
    font-size: 5em;
    color: #ffd700;
    text-shadow:
      4px 4px 0 #664400,
      0   0 30px rgba(255, 215, 0, 0.9);
    letter-spacing: 4px;
    margin: 10px 0;
  }

  /* ══ REKOD SESI ══ */
  .rekod-sesi {
    border-radius: 12px;
    padding: 14px 20px;
    margin-top: 12px;
    font-family: 'Fredoka One', sans-serif;
    font-size: 1.3em;
    color: #ccdcec;
    text-align: left;
    border: 2px solid rgba(255,255,255,0.1);
    letter-spacing: 1px;
  }

  /* ══ SCROLLBAR gelap ══ */
  ::-webkit-scrollbar { width: 8px; background: #0d0d14; }
  ::-webkit-scrollbar-thumb { background: #333355; border-radius: 4px; }

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  Muatkan Soalan dari questions.json
# ─────────────────────────────────────────
@st.cache_data
def muatkan_soalan():
    fail_json = Path(__file__).parent / "questions.json"
    with open(fail_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["soalan"]

SEMUA_SOALAN = muatkan_soalan()

WARNA_KATEGORI = {
    "tambah": "#00aa33",
    "tolak":  "#cc2200",
    "wang":   "#7700cc"
}
LABEL_KATEGORI = {
    "tambah": "➕ TAMBAH",
    "tolak":  "➖ TOLAK",
    "wang":   "💰 WANG RM"
}


# ─────────────────────────────────────────
#  Inisialisasi Session State
# ─────────────────────────────────────────
def init_sesi():
    soalan_dipilih = random.sample(SEMUA_SOALAN, 5)
    st.session_state.soalan_sesi   = soalan_dipilih
    st.session_state.soalan_idx    = 0
    st.session_state.markah        = 0
    st.session_state.status_jawab  = None
    st.session_state.jawapan_pilih = None
    st.session_state.selesai       = False
    st.session_state.rekod         = []
    st.session_state.pilihan_rawak = [
        random.sample(s["pilihan"], len(s["pilihan"])) for s in soalan_dipilih
    ]

if "soalan_sesi" not in st.session_state:
    init_sesi()


# ─────────────────────────────────────────
#  Fungsi Pembantu
# ─────────────────────────────────────────
def semak_jawapan(pilihan):
    soalan_semasa = st.session_state.soalan_sesi[st.session_state.soalan_idx]
    st.session_state.jawapan_pilih = pilihan
    betul = (pilihan == soalan_semasa["jawapan"])
    st.session_state.status_jawab = "betul" if betul else "salah"
    if betul:
        st.session_state.markah += 1
    st.session_state.rekod.append({
        "soalan": soalan_semasa["soalan"],
        "betul":  betul,
        "jawapan_betul": soalan_semasa["jawapan"],
        "jawapan_pilih": pilihan
    })

def soalan_seterusnya():
    st.session_state.soalan_idx += 1
    st.session_state.status_jawab  = None
    st.session_state.jawapan_pilih = None
    if st.session_state.soalan_idx >= len(st.session_state.soalan_sesi):
        st.session_state.selesai = True

def mula_semula():
    init_sesi()


# ─────────────────────────────────────────
#  TAJUK UTAMA
# ─────────────────────────────────────────
st.markdown(
    '<div class="tajuk-roblox">🎮 KLINIK MATEMATIK 🎮<br>'
    '<span style="font-size:0.55em">AMIR SYAFIQ</span></div>'
    '<div class="tajuk-sub">⚡ Darjah 1 — Level Up! ⚡</div>',
    unsafe_allow_html=True
)
st.markdown("---")


# ─────────────────────────────────────────
#  SKRIN TAMAT
# ─────────────────────────────────────────
if st.session_state.selesai:
    markah = st.session_state.markah
    jumlah = len(st.session_state.soalan_sesi)

    if markah == jumlah:
        emoji_t = "🏆"
        mesej_t = "PERFECT SCORE!"
        warna_t = "#ffd700"
        st.balloons()
    elif markah >= 3:
        emoji_t = "⭐"
        mesej_t = "BAGUS SEKALI!"
        warna_t = "#00ff88"
    else:
        emoji_t = "💪"
        mesej_t = "CUBA LAGI!"
        warna_t = "#ff8800"

    st.markdown(f"""
    <div class="skrin-tamat">
      <div style="font-size:5em; line-height:1">{emoji_t}</div>
      <div class="tamat-tajuk" style="color:{warna_t};
           text-shadow: 3px 3px 0 #333, 0 0 25px {warna_t};">
        {mesej_t}
      </div>
      <div style="font-family:'Fredoka One',sans-serif; font-size:1.1em;
                  color:#aabbcc; letter-spacing:4px; margin:6px 0;">
        MARKAH AMIR
      </div>
      <div class="tamat-skor">{markah} / {jumlah}</div>
      <div class="leaderboard-stars">
        {"⭐" * markah}{"🔘" * (jumlah - markah)}
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Rekod jawapan
    st.markdown(
        '<div style="font-family:\'Fredoka One\',sans-serif; font-size:1.6em; '
        'color:#ffcc00; text-align:center; letter-spacing:3px; margin-bottom:8px;">'
        '📋 SEMAKAN JAWAPAN</div>',
        unsafe_allow_html=True
    )
    for i, r in enumerate(st.session_state.rekod, 1):
        ikon   = "✅" if r["betul"] else "❌"
        bg     = "rgba(0,80,0,0.4)"  if r["betul"] else "rgba(80,0,0,0.4)"
        border = "#00ff55"           if r["betul"] else "#ff3c3c"
        st.markdown(
            f'<div class="rekod-sesi" style="background:{bg}; border-color:{border};">'
            f'{ikon} &nbsp;<b>S{i}:</b> {r["soalan"]} &nbsp;|&nbsp; '
            f'Jawapan: <b style="color:#ffd700">{r["jawapan_betul"]}</b>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄  MAIN SEMULA!", use_container_width=True):
        mula_semula()
        st.rerun()


# ─────────────────────────────────────────
#  SKRIN SOALAN
# ─────────────────────────────────────────
else:
    idx            = st.session_state.soalan_idx
    soalan_semasa  = st.session_state.soalan_sesi[idx]
    pilihan_semasa = st.session_state.pilihan_rawak[idx]
    kategori       = soalan_semasa.get("kategori", "tambah")
    jumlah         = len(st.session_state.soalan_sesi)

    # ── LEADERBOARD SCOREBOARD ──
    bintang_penuh  = "⭐" * st.session_state.markah
    bintang_kosong = "🔘" * (jumlah - st.session_state.markah)
    st.markdown(f"""
    <div class="leaderboard">
      <div class="leaderboard-title">🏆 LEADERBOARD — AMIR SYAFIQ 🏆</div>
      <div class="leaderboard-score">
        SKOR :  {st.session_state.markah} / {jumlah}
      </div>
      <div class="leaderboard-stars">{bintang_penuh}{bintang_kosong}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── PROGRESS ──
    st.progress(idx / jumlah)
    st.markdown(
        f'<div class="progress-text">▶ SOALAN {idx + 1} DARIPADA {jumlah} ◀</div>',
        unsafe_allow_html=True
    )

    # ── BADGE KATEGORI ──
    warna_badge = WARNA_KATEGORI.get(kategori, "#0055aa")
    label_badge = LABEL_KATEGORI.get(kategori, kategori.upper())
    st.markdown(
        f'<div style="text-align:center; margin:6px 0;">'
        f'<span class="badge-kategori" style="background:{warna_badge};">'
        f'{label_badge}</span></div>',
        unsafe_allow_html=True
    )

    # ── KOTAK SOALAN ──
    st.markdown(f"""
    <div class="kotak-soalan">
      <div class="emoji-soalan">{soalan_semasa["emoji"]}</div>
      <div class="nombor-soalan">{soalan_semasa["soalan"]}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── MAKLUM BALAS ──
    if st.session_state.status_jawab == "betul":
        st.markdown(
            '<div class="maklumbalas-betul">'
            '🎉 SYABAS AMIR! BETUL! 🎉'
            '</div>',
            unsafe_allow_html=True
        )
        st.balloons()

    elif st.session_state.status_jawab == "salah":
        jwp = soalan_semasa["jawapan"]
        st.markdown(
            f'<div class="maklumbalas-salah">'
            f'💀 OOPS! CUBA LAGI!<br>'
            f'<span style="font-size:0.6em; color:#ffaaaa;">'
            f'Jawapan betul: <b style="color:#ffd700;">{jwp}</b>'
            f'</span></div>',
            unsafe_allow_html=True
        )

    # ── BUTANG PILIHAN ──
    if st.session_state.status_jawab is None:
        st.markdown("### 👾  PILIH JAWAPAN KAMU:")
        col1, col2 = st.columns(2)
        for i, pilihan in enumerate(pilihan_semasa):
            with (col1 if i % 2 == 0 else col2):
                if st.button(
                    f"  {pilihan}  ",
                    key=f"pilihan_{i}",
                    use_container_width=True
                ):
                    semak_jawapan(pilihan)
                    st.rerun()

    # ── BUTANG SETERUSNYA ──
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        label_btn = (
            "⚡  SOALAN SETERUSNYA  ⚡"
            if idx + 1 < jumlah
            else "🏁  LIHAT KEPUTUSAN!  🏁"
        )
        # Tukar warna butang ke biru untuk navigasi
        st.markdown("""
        <style>
        div.stButton > button {
          background: linear-gradient(180deg, #0099ff 0%, #0066cc 100%) !important;
          box-shadow: 0 10px 0 #003388, 0 12px 25px rgba(0,150,255,0.4) !important;
        }
        div.stButton > button:hover {
          background: linear-gradient(180deg, #33bbff 0%, #0099ee 100%) !important;
          box-shadow: 0 12px 0 #003388, 0 15px 30px rgba(0,180,255,0.5) !important;
        }
        </style>
        """, unsafe_allow_html=True)
        if st.button(label_btn, use_container_width=True):
            soalan_seterusnya()
            st.rerun()

    # ── FOOTER ──
    st.markdown("---")
    st.markdown(
        '<div style="text-align:center; font-family:\'Fredoka One\',sans-serif; '
        'color:#444466; font-size:1.0em; letter-spacing:3px;">'
        '⚡ LEVEL UP YOUR MATH, AMIR! ⚡'
        '</div>',
        unsafe_allow_html=True
    )
