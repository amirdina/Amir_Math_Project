import streamlit as st
import random
import json
from pathlib import Path

st.set_page_config(
    page_title="Klinik Matematik Amir Syafiq",
    page_icon="🎮",
    layout="wide"
)

# ─────────────────────────────────────────
#  CSS UTAMA
# ─────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@700;800;900&display=swap');

  @keyframes shimmer {
    0%   { background-position: -200% 0; }
    100% { background-position:  200% 0; }
  }
  @keyframes idleBob {
    0%,100% { transform: translateY(0) rotate(0deg); }
    50%     { transform: translateY(-8px) rotate(-2deg); }
  }
  @keyframes celebrateJump {
    0%   { transform: translateY(0) rotate(0deg); }
    25%  { transform: translateY(-30px) rotate(-8deg); }
    50%  { transform: translateY(0) rotate(6deg); }
    75%  { transform: translateY(-16px) rotate(-4deg); }
    100% { transform: translateY(0) rotate(0deg); }
  }
  @keyframes sadSlump {
    0%,100% { transform: translateY(0) rotate(0deg); }
    50%     { transform: translateY(6px) rotate(4deg); }
  }
  @keyframes armWave {
    0%,100% { transform: rotate(0deg); }
    50%     { transform: rotate(-35deg); }
  }

  /* ══ LATAR ══ */
  .stApp {
    background:
      radial-gradient(ellipse at top,    #1a0a2e 0%, transparent 60%),
      radial-gradient(ellipse at bottom, #0a1a2e 0%, transparent 60%),
      radial-gradient(circle, rgba(255,255,255,0.045) 1px, transparent 1px),
      #0d0d14;
    background-size: auto, auto, 32px 32px, auto;
    font-family: 'Baloo 2', sans-serif !important;
  }

  .block-container {
    max-width: 1000px !important;
    margin: auto !important;
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
  }

  /* ══ BUTANG JAWAPAN — FIX FONT ══
     Streamlit wrap teks dalam <p> dalam button.
     Kena target <p> secara langsung supaya font besar.
  ══ */
  div.stButton > button {
    width: 100%;
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 800 !important;
    padding: clamp(14px, 5vw, 28px) 10px !important;
    min-height: clamp(80px, 18vw, 120px) !important;
    border-radius: 16px !important;
    border: none !important;
    color: #fff !important;
    letter-spacing: 2px !important;
    text-shadow: 3px 3px 0 rgba(0,0,0,0.5) !important;
    background: linear-gradient(180deg, #00dd55 0%, #00aa33 100%) !important;
    box-shadow: 0 10px 0 #005500, 0 12px 25px rgba(0,200,80,0.4) !important;
    transform: translateY(-5px);
    transition: all 0.08s ease !important;
    margin: 6px 0 !important;
    cursor: pointer;
    line-height: 1.2 !important;
    /* Reset font-size pada button itu sendiri */
    font-size: 1px !important;
  }
  /* ← Ini kunci: target <p> dalam button */
  div.stButton > button p,
  div.stButton > button span {
    font-size: clamp(28px, 7vw, 52px) !important;
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 800 !important;
    color: #fff !important;
    line-height: 1.2 !important;
    letter-spacing: 2px !important;
  }
  div.stButton > button:hover {
    background: linear-gradient(180deg, #00ff66 0%, #00cc44 100%) !important;
    box-shadow: 0 12px 0 #005500, 0 15px 30px rgba(0,255,100,0.5) !important;
    transform: translateY(-7px) !important;
  }
  div.stButton > button:active {
    transform: translateY(2px) !important;
    box-shadow: 0 3px 0 #005500, 0 5px 10px rgba(0,0,0,0.3) !important;
  }

  /* ══ PROGRESS BAR ══ */
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

  /* ══ SCROLLBAR ══ */
  ::-webkit-scrollbar { width: 8px; background: #0d0d14; }
  ::-webkit-scrollbar-thumb { background: #333355; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  Muatkan Soalan
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
#  Session State
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

def semak_jawapan(pilihan):
    s = st.session_state.soalan_sesi[st.session_state.soalan_idx]
    betul = (pilihan == s["jawapan"])
    st.session_state.status_jawab = "betul" if betul else "salah"
    if betul:
        st.session_state.markah += 1
    st.session_state.rekod.append({
        "soalan":        s["soalan"],
        "betul":         betul,
        "jawapan_betul": s["jawapan"],
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
#  Mascot HTML (CSS-drawn Roblox character)
# ─────────────────────────────────────────
def mascot_html(state: str = "idle") -> str:
    if state == "betul":
        body_anim = "celebrateJump 0.6s ease"
        arm_anim  = "armWave 0.4s ease-in-out 3"
        speech    = "Hebat!! 🎉"
    elif state == "salah":
        body_anim = "sadSlump 0.6s ease-in-out infinite"
        arm_anim  = "none"
        speech    = "Cuba lagi! 💪"
    else:
        body_anim = "idleBob 2.4s ease-in-out infinite"
        arm_anim  = "none"
        speech    = "Ayuh, Amir!"

    return f"""
    <div style="display:flex; justify-content:center; margin:20px 0 4px;">
      <div style="display:flex; flex-direction:column; align-items:center;
                  animation:{body_anim};">
        <div style="display:flex; align-items:flex-end; gap:2px;">
          <!-- Tangan kiri -->
          <div style="width:16px; height:34px; background:#3d8bff; border-radius:6px;
                      transform-origin:top center; animation:{arm_anim};"></div>
          <!-- Badan -->
          <div style="display:flex; flex-direction:column; align-items:center;">
            <!-- Kepala -->
            <div style="width:38px; height:34px; background:#ffcc99; border-radius:8px 8px 4px 4px;
                        position:relative; box-shadow:inset -5px 0 0 rgba(0,0,0,0.08);">
              <div style="position:absolute; top:12px; left:6px; width:7px; height:7px;
                           background:#1d3a53; border-radius:2px;"></div>
              <div style="position:absolute; top:12px; right:6px; width:7px; height:7px;
                           background:#1d3a53; border-radius:2px;"></div>
              <!-- Topi -->
              <div style="position:absolute; top:-12px; left:-3px; width:44px; height:14px;
                           background:#ff5b3d; border-radius:7px 7px 0 0;"></div>
            </div>
            <!-- Badan baju -->
            <div style="width:46px; height:44px; background:#00b4ff; border-radius:6px;
                        margin-top:-2px; box-shadow:inset -6px 0 0 rgba(0,0,0,0.1);"></div>
            <!-- Kaki -->
            <div style="display:flex; gap:3px; margin-top:-2px;">
              <div style="width:19px; height:30px; background:#1d3a53; border-radius:0 0 5px 5px;"></div>
              <div style="width:19px; height:30px; background:#1d3a53; border-radius:0 0 5px 5px;"></div>
            </div>
          </div>
          <!-- Tangan kanan -->
          <div style="width:16px; height:34px; background:#3d8bff; border-radius:6px;
                      transform-origin:top center;"></div>
        </div>
        <!-- Dialog speech -->
        <div style="margin-top:6px; font-weight:800; font-size:0.85em; color:#8fb8d6;
                    letter-spacing:1px; background:rgba(0,180,255,0.12);
                    padding:2px 12px; border-radius:10px;">{speech}</div>
      </div>
    </div>
    """


# ─────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:8px 10px 4px;">
  <div style="font-size:clamp(1.7em,9vw,3.2em); font-weight:800; letter-spacing:2px; line-height:1.1;
              background:linear-gradient(180deg,#ff4444 0%,#ffcc00 60%,#ff8800 100%);
              -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent;
              filter:drop-shadow(0 0 18px rgba(255,80,0,0.6));">
    🎮 KLINIK MATEMATIK 🎮<br>
    <span style="font-size:0.5em;">AMIR SYAFIQ</span>
  </div>
  <div style="font-size:clamp(0.7em,3.4vw,1.15em); font-weight:700; color:#aabbcc;
              letter-spacing:2px; text-transform:uppercase; margin-bottom:6px;">
    ⚡ Darjah 1 — Level Up! ⚡
  </div>
</div>
<div style="height:3px; background:linear-gradient(90deg,transparent,#ff4444,#ffcc00,#00ccff,transparent);
            margin:10px 0 22px; border-radius:2px;"></div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  SKRIN TAMAT
# ─────────────────────────────────────────
if st.session_state.selesai:
    markah = st.session_state.markah
    jumlah = len(st.session_state.soalan_sesi)

    if markah == jumlah:
        emoji_t, mesej_t, warna_t = "🏆", "PERFECT SCORE!", "#ffd700"
        st.balloons()
    elif markah >= 3:
        emoji_t, mesej_t, warna_t = "⭐", "BAGUS SEKALI!", "#00ff88"
    else:
        emoji_t, mesej_t, warna_t = "💪", "CUBA LAGI!", "#ff8800"

    st.markdown(f"""
    <div style="text-align:center; background:linear-gradient(135deg,#0d0d1a 0%,#1a0a2e 50%,#0d0d1a 100%);
                border:5px solid #ffd700; border-radius:24px; padding:44px 30px;
                box-shadow:0 0 40px rgba(255,215,0,0.5),0 0 80px rgba(255,215,0,0.18);
                position:relative; overflow:hidden;">
      <div style="position:absolute; top:-2px; left:0; right:0; height:4px;
                  background:linear-gradient(90deg,#ff4444,#ff8800,#ffd700,#00ff88,#00b4ff,#ff4444);
                  background-size:200%; animation:shimmer 3s linear infinite; border-radius:2px 2px 0 0;"></div>
      <div style="font-size:5em; line-height:1;">{emoji_t}</div>
      <div style="font-size:clamp(1.3em,6.5vw,2.2em); font-weight:800; letter-spacing:2px; margin:12px 0;
                  color:{warna_t}; text-shadow:3px 3px 0 #333;">{mesej_t}</div>
      <div style="font-weight:800; font-size:1.05em; color:#aabbcc; letter-spacing:4px; margin:6px 0;">
        MARKAH AMIR
      </div>
      <div style="font-size:clamp(2.2em,12vw,4.6em); font-weight:800; color:#ffd700;
                  text-shadow:4px 4px 0 #664400,0 0 30px rgba(255,215,0,0.9);
                  letter-spacing:2px; margin:8px 0;">{markah} / {jumlah}</div>
      <div style="font-size:clamp(1.1em,5vw,1.7em); letter-spacing:4px; margin-top:4px;">
        {"⭐" * markah}{"🔘" * (jumlah - markah)}
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size:1.4em; font-weight:800; color:#ffcc00; text-align:center;
                letter-spacing:3px; margin:24px 0 10px;">📋 SEMAKAN JAWAPAN</div>
    """, unsafe_allow_html=True)

    for i, r in enumerate(st.session_state.rekod, 1):
        ikon   = "✅" if r["betul"] else "❌"
        bg     = "rgba(0,80,0,0.4)"  if r["betul"] else "rgba(80,0,0,0.4)"
        border = "#00ff55"           if r["betul"] else "#ff3c3c"
        st.markdown(f"""
        <div style="border-radius:12px; padding:14px 20px; font-weight:700; margin-bottom:8px;
                    font-size:clamp(0.8em,3vw,1.05em); color:#ccdcec; text-align:left;
                    border:2px solid {border}; background:{bg}; letter-spacing:0.5px;">
          {ikon} &nbsp;<b>S{i}:</b> {r["soalan"]} &nbsp;|&nbsp;
          Jawapan: <b style="color:#ffd700;">{r["jawapan_betul"]}</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    # Butang restart — warna biru
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

    # ── LEADERBOARD ──
    bintang_penuh  = "⭐" * st.session_state.markah
    bintang_kosong = "🔘" * (jumlah - st.session_state.markah)
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#1a0000 0%,#2a0808 50%,#1a0000 100%);
                border:4px solid #ff3c3c; border-radius:16px; padding:16px 28px; text-align:center;
                position:relative; overflow:hidden;
                box-shadow:0 0 30px rgba(255,60,60,0.5),0 0 60px rgba(255,60,60,0.18),
                           inset 0 0 40px rgba(0,0,0,0.6); margin-bottom:18px;">
      <div style="position:absolute; top:0; left:0; right:0; height:3px;
                  background:linear-gradient(90deg,#ff0000,#ff8800,#ffcc00,#ff8800,#ff0000);
                  background-size:200%; animation:shimmer 2s linear infinite;"></div>
      <div style="font-weight:800; font-size:1em; color:#ff6666; letter-spacing:5px;
                  text-transform:uppercase; margin-bottom:4px;">🏆 LEADERBOARD — AMIR SYAFIQ 🏆</div>
      <div style="font-weight:800; font-size:clamp(1.3em,6.5vw,2.2em); color:#ffd700;
                  text-shadow:3px 3px 0 #8b4500,0 0 20px rgba(255,215,0,0.8); letter-spacing:1px;">
        SKOR : {st.session_state.markah} / {jumlah}
      </div>
      <div style="font-size:clamp(1.1em,5vw,1.6em); letter-spacing:2px; margin-top:4px;">
        {bintang_penuh}{bintang_kosong}
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── PROGRESS ──
    st.progress(idx / jumlah)
    st.markdown(f"""
    <div style="text-align:center; font-weight:800; font-size:clamp(0.85em,4vw,1.3em);
                color:#aabbcc; letter-spacing:1px; margin-bottom:12px;">
      ▶ SOALAN {idx + 1} DARIPADA {jumlah} ◀
    </div>
    """, unsafe_allow_html=True)

    # ── BADGE KATEGORI ──
    warna_badge = WARNA_KATEGORI.get(kategori, "#0055aa")
    label_badge = LABEL_KATEGORI.get(kategori, kategori.upper())
    st.markdown(f"""
    <div style="text-align:center; margin:6px 0 14px;">
      <span style="display:inline-block; padding:8px 24px; border-radius:6px; font-weight:800;
                   font-size:clamp(0.85em,4vw,1.3em); color:#fff; letter-spacing:2px;
                   text-transform:uppercase; border-bottom:5px solid rgba(0,0,0,0.4);
                   text-shadow:1px 1px 0 rgba(0,0,0,0.5); background:{warna_badge};">
        {label_badge}
      </span>
    </div>
    """, unsafe_allow_html=True)

    # ── MASCOT ──
    mascot_state = st.session_state.status_jawab or "idle"
    st.markdown(mascot_html(mascot_state), unsafe_allow_html=True)

    # ── KOTAK SOALAN ──
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0d1b2a 0%,#1a2a3a 100%);
                border:4px solid #00b4ff; border-radius:20px;
                padding:clamp(20px,6vw,34px) clamp(14px,5vw,28px);
                text-align:center; margin:14px 0;
                box-shadow:0 0 30px rgba(0,180,255,0.35),0 0 60px rgba(0,180,255,0.15),
                           inset 0 0 40px rgba(0,0,0,0.5); position:relative;">
      <div style="font-size:clamp(1.7em,7vw,2.8em); line-height:1.6; letter-spacing:2px;">
        {soalan_semasa["emoji"]}
      </div>
      <div style="font-weight:800; font-size:clamp(1.9em,9vw,3.4em); color:#fff;
                  text-shadow:3px 3px 0 #003366,0 0 25px rgba(0,180,255,0.9);
                  margin-top:8px; letter-spacing:2px;">
        {soalan_semasa["soalan"]}
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── MAKLUM BALAS ──
    if st.session_state.status_jawab == "betul":
        st.markdown("""
        <div style="background:linear-gradient(135deg,#003300 0%,#004d00 100%);
                    border:4px solid #00ff55; border-radius:18px;
                    padding:clamp(16px,5vw,24px) clamp(12px,4vw,20px);
                    text-align:center; color:#00ff55; font-weight:800;
                    font-size:clamp(1.2em,6vw,2em); margin:14px 0; letter-spacing:2px;
                    box-shadow:0 0 30px rgba(0,255,85,0.5),0 0 60px rgba(0,255,85,0.18);
                    text-shadow:0 0 20px rgba(0,255,85,0.9);">
          🎉 SYABAS AMIR! BETUL! 🎉
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

    elif st.session_state.status_jawab == "salah":
        jwp = soalan_semasa["jawapan"]
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#2a0000 0%,#3d0000 100%);
                    border:4px solid #ff3c3c; border-radius:18px;
                    padding:clamp(16px,5vw,24px) clamp(12px,4vw,20px);
                    text-align:center; color:#ff6666; font-weight:800;
                    font-size:clamp(1.2em,6vw,2em); margin:14px 0; letter-spacing:2px;
                    box-shadow:0 0 30px rgba(255,60,60,0.5),0 0 60px rgba(255,60,60,0.18);
                    text-shadow:0 0 15px rgba(255,60,60,0.8);">
          💀 OOPS! CUBA LAGI!<br>
          <span style="font-size:0.55em; color:#ffaaaa;">
            Jawapan betul: <b style="color:#ffd700;">{jwp}</b>
          </span>
        </div>
        """, unsafe_allow_html=True)

    # ── BUTANG PILIHAN ──
    if st.session_state.status_jawab is None:
        st.markdown("""
        <div style="text-align:center; font-weight:800; font-size:clamp(1em,5vw,1.5em);
                    color:#ffcc00; letter-spacing:1px; text-shadow:2px 2px 0 #664400;
                    margin:18px 0 12px;">👾  PILIH JAWAPAN KAMU:</div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2, gap="medium")
        for i, pilihan in enumerate(pilihan_semasa):
            with (col1 if i % 2 == 0 else col2):
                if st.button(str(pilihan), key=f"pilihan_{i}", use_container_width=True):
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
    st.markdown("""
    <div style="height:3px; background:linear-gradient(90deg,transparent,#ff4444,#ffcc00,#00ccff,transparent);
                margin:26px 0 16px; border-radius:2px;"></div>
    <div style="text-align:center; font-weight:800; color:#444466; font-size:1em; letter-spacing:3px;">
      ⚡ LEVEL UP YOUR MATH, AMIR! ⚡
    </div>
    """, unsafe_allow_html=True)
