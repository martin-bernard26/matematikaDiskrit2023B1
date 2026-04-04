import streamlit as st
import requests

st.set_page_config(layout="wide")

if 'kumpulan' not in st.session_state:
    st.session_state['kumpulan']={'kover':True,'perpustakaan':False,'diag':False,'angket':False,'foto':False,'pertemuan1':False,'pertemuan2':False,
                                  'pertemuan3':False}


class keterangan:
    def __init__(self,penjelasan,ukuran):
        self.penjelasan=penjelasan
        self.ukuran = ukuran
    def tampilkan(self):
        st.components.v1.html(self.penjelasan,height=self.ukuran)

#==================

def Pendahuluan():
    tulisanHTML="""
    <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cover Matematika Diskrit</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Space+Mono:wght@400;700&family=Cormorant+Garamond:ital,wght@0,300;0,600;1,300&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0d0d14;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    font-family: 'Space Mono', monospace;
  }

  .cover {
    width: 100%;
    height: 842px;
    position: relative;
    background: #080810;
    overflow: hidden;
    box-shadow: 0 40px 120px rgba(0,0,0,0.8);
  }

  /* Deep space background */
  .bg-layer {
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse 80% 60% at 50% 20%, rgba(15, 30, 80, 0.8) 0%, transparent 70%),
      radial-gradient(ellipse 60% 50% at 80% 80%, rgba(20, 10, 60, 0.6) 0%, transparent 60%),
      linear-gradient(175deg, #060612 0%, #0a0820 40%, #050510 100%);
  }

  /* Subtle grid */
  .grid-overlay {
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(80,120,255,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(80,120,255,0.04) 1px, transparent 1px);
    background-size: 36px 36px;
  }

  /* Glowing orb top */
  .orb-top {
    position: absolute;
    width: 420px;
    height: 420px;
    top: -140px;
    left: 50%;
    transform: translateX(-50%);
    background: radial-gradient(circle, rgba(60,90,255,0.18) 0%, rgba(100,60,200,0.10) 40%, transparent 70%);
    filter: blur(30px);
    animation: pulse 4s ease-in-out infinite;
  }

  .orb-bottom {
    position: absolute;
    width: 300px;
    height: 300px;
    bottom: -80px;
    right: -60px;
    background: radial-gradient(circle, rgba(0,200,180,0.12) 0%, rgba(0,150,255,0.08) 40%, transparent 70%);
    filter: blur(40px);
    animation: pulse 5s ease-in-out infinite reverse;
  }

  @keyframes pulse {
    0%, 100% { opacity: 0.7; transform: translateX(-50%) scale(1); }
    50% { opacity: 1; transform: translateX(-50%) scale(1.05); }
  }

  /* Floating nodes & edges (graph theory visual) */
  .graph-canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
  }

  .node {
    position: absolute;
    border-radius: 50%;
    animation: float 6s ease-in-out infinite;
  }

  .node-lg {
    width: 10px; height: 10px;
    background: rgba(120,160,255,0.8);
    box-shadow: 0 0 16px rgba(100,140,255,0.6), 0 0 40px rgba(80,120,255,0.2);
  }

  .node-sm {
    width: 5px; height: 5px;
    background: rgba(0,220,200,0.7);
    box-shadow: 0 0 10px rgba(0,200,180,0.5);
  }

  .node-accent {
    width: 7px; height: 7px;
    background: rgba(200,150,255,0.8);
    box-shadow: 0 0 12px rgba(180,120,255,0.5);
  }

  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
  }

  /* SVG edges */
  .edges-svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0.18;
  }

  /* Top decorative band */
  .top-band {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 6px;
    background: linear-gradient(90deg, #3a5af0, #8b5cf6, #06b6d4, #3a5af0);
    background-size: 200% 100%;
    animation: shimmer 3s linear infinite;
  }

  @keyframes shimmer {
    0% { background-position: 0% 0%; }
    100% { background-position: 200% 0%; }
  }

  /* Tag chip */
  .chip {
    position: absolute;
    top: 32px;
    left: 40px;
    background: rgba(58,90,240,0.15);
    border: 1px solid rgba(58,90,240,0.4);
    color: rgba(120,160,255,0.9);
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding: 5px 12px;
    border-radius: 2px;
  }

  .chip-right {
    left: auto;
    right: 40px;
    background: rgba(0,200,180,0.10);
    border-color: rgba(0,200,180,0.3);
    color: rgba(0,220,200,0.8);
  }

  /* Central visual — stylized graph diagram */
  .diagram-area {
    position: absolute;
    top: 60px;
    left: 0; right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .diagram-svg {
    width: 340px;
    height: 260px;
    filter: drop-shadow(0 0 30px rgba(80,120,255,0.25));
    animation: diagFloat 7s ease-in-out infinite;
  }

  @keyframes diagFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
  }

  /* Main content */
  .content {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    padding: 0 40px 48px;
  }

  .label-materi {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: rgba(0,200,180,0.7);
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .label-materi::before {
    content: '';
    display: block;
    width: 30px;
    height: 1px;
    background: rgba(0,200,180,0.5);
  }

  .title-main {
    font-family: 'Playfair Display', serif;
    font-size: 62px;
    font-weight: 900;
    line-height: 0.92;
    color: #ffffff;
    letter-spacing: -1px;
    margin-bottom: 8px;
    text-shadow: 0 0 60px rgba(80,100,255,0.3);
  }

  .title-main .accent-word {
    color: transparent;
    -webkit-text-stroke: 1.5px rgba(100,140,255,0.7);
    display: block;
  }

  .title-main .solid-word {
    display: block;
    background: linear-gradient(135deg, #ffffff 30%, rgba(140,170,255,0.8) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .subtitle {
    font-family: 'Cormorant Garamond', serif;
    font-size: 16px;
    font-style: italic;
    font-weight: 300;
    color: rgba(180,195,255,0.55);
    margin-bottom: 36px;
    letter-spacing: 1.5px;
  }

  /* Divider */
  .divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(80,120,255,0.4), rgba(0,200,180,0.3), transparent);
    margin-bottom: 24px;
  }

  /* Author section */
  .author-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }

  .author-block {}

  .author-label {
    font-family: 'Space Mono', monospace;
    font-size: 8px;
    letter-spacing: 3px;
    color: rgba(120,140,200,0.5);
    text-transform: uppercase;
    margin-bottom: 5px;
  }

  .author-name {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 700;
    color: rgba(220,230,255,0.9);
    letter-spacing: 0.5px;
  }

  .author-degree {
    font-family: 'Cormorant Garamond', serif;
    font-size: 13px;
    font-style: italic;
    color: rgba(100,140,255,0.7);
    margin-top: 2px;
  }

  /* Symbol area */
  .symbols {
    display: flex;
    flex-direction: column;
    gap: 5px;
    align-items: flex-end;
  }

  .symbol-row {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: rgba(80,120,255,0.35);
    letter-spacing: 2px;
  }

  /* Bottom bar */
  .bottom-bar {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, rgba(0,200,180,0.5), rgba(80,120,255,0.5), transparent);
  }

  /* Corner ornaments */
  .corner {
    position: absolute;
    width: 40px; height: 40px;
  }

  .corner-tl { top: 14px; left: 14px; border-top: 1px solid rgba(80,120,255,0.3); border-left: 1px solid rgba(80,120,255,0.3); }
  .corner-tr { top: 14px; right: 14px; border-top: 1px solid rgba(80,120,255,0.3); border-right: 1px solid rgba(80,120,255,0.3); }
  .corner-bl { bottom: 14px; left: 14px; border-bottom: 1px solid rgba(0,200,180,0.3); border-left: 1px solid rgba(0,200,180,0.3); }
  .corner-br { bottom: 14px; right: 14px; border-bottom: 1px solid rgba(0,200,180,0.3); border-right: 1px solid rgba(0,200,180,0.3); }
</style>
</head>
<body>
<div class="cover">
  <div class="bg-layer"></div>
  <div class="grid-overlay"></div>
  <div class="orb-top"></div>
  <div class="orb-bottom"></div>

  <!-- Top gradient band -->
  <div class="top-band"></div>

  <!-- Corners -->
  <div class="corner corner-tl"></div>
  <div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div>
  <div class="corner corner-br"></div>

  <!-- Chips -->
  <div class="chip">Bahan Ajar</div>
  <div class="chip chip-right">2024 / 2025</div>

  <!-- Floating nodes scattered -->
  <div class="node node-lg" style="top:18%;left:8%;animation-delay:0s;"></div>
  <div class="node node-sm" style="top:25%;left:15%;animation-delay:1s;"></div>
  <div class="node node-accent" style="top:10%;left:72%;animation-delay:2s;"></div>
  <div class="node node-sm" style="top:15%;left:85%;animation-delay:0.5s;"></div>
  <div class="node node-lg" style="top:40%;left:5%;animation-delay:1.5s;"></div>
  <div class="node node-accent" style="top:50%;right:6%;animation-delay:3s;"></div>
  <div class="node node-sm" style="top:60%;left:12%;animation-delay:2.5s;"></div>
  <div class="node node-sm" style="top:55%;right:10%;animation-delay:1.8s;"></div>

  <!-- Central diagram: Graph Theory nodes & edges -->
  <div class="diagram-area">
    <svg class="diagram-svg" viewBox="0 0 340 260" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Edges / connections -->
      <line x1="170" y1="50"  x2="80"  y2="140" stroke="rgba(80,120,255,0.35)" stroke-width="1.2"/>
      <line x1="170" y1="50"  x2="260" y2="140" stroke="rgba(80,120,255,0.35)" stroke-width="1.2"/>
      <line x1="170" y1="50"  x2="170" y2="180" stroke="rgba(80,120,255,0.25)" stroke-width="1"/>
      <line x1="80"  y1="140" x2="260" y2="140" stroke="rgba(0,200,180,0.30)"  stroke-width="1"/>
      <line x1="80"  y1="140" x2="130" y2="220" stroke="rgba(0,200,180,0.25)"  stroke-width="1"/>
      <line x1="260" y1="140" x2="210" y2="220" stroke="rgba(0,200,180,0.25)"  stroke-width="1"/>
      <line x1="170" y1="180" x2="130" y2="220" stroke="rgba(180,140,255,0.3)" stroke-width="1"/>
      <line x1="170" y1="180" x2="210" y2="220" stroke="rgba(180,140,255,0.3)" stroke-width="1"/>
      <line x1="130" y1="220" x2="210" y2="220" stroke="rgba(80,120,255,0.20)" stroke-width="1"/>
      <!-- Extra spokes for density -->
      <line x1="40"  y1="70"  x2="80"  y2="140" stroke="rgba(100,180,255,0.18)" stroke-width="0.8"/>
      <line x1="300" y1="70"  x2="260" y2="140" stroke="rgba(100,180,255,0.18)" stroke-width="0.8"/>
      <line x1="40"  y1="70"  x2="170" y2="50"  stroke="rgba(100,180,255,0.14)" stroke-width="0.8"/>
      <line x1="300" y1="70"  x2="170" y2="50"  stroke="rgba(100,180,255,0.14)" stroke-width="0.8"/>

      <!-- Glow circles behind nodes -->
      <circle cx="170" cy="50"  r="18" fill="rgba(60,100,255,0.08)"/>
      <circle cx="80"  cy="140" r="14" fill="rgba(0,180,160,0.08)"/>
      <circle cx="260" cy="140" r="14" fill="rgba(0,180,160,0.08)"/>
      <circle cx="170" cy="180" r="12" fill="rgba(160,100,255,0.08)"/>

      <!-- Main nodes -->
      <!-- Center top (root) -->
      <circle cx="170" cy="50"  r="10" fill="#1a2a6c" stroke="rgba(100,140,255,0.9)" stroke-width="2"/>
      <circle cx="170" cy="50"  r="4"  fill="rgba(140,180,255,0.9)"/>

      <!-- Left -->
      <circle cx="80"  cy="140" r="8"  fill="#0d1f3c" stroke="rgba(0,200,180,0.85)" stroke-width="1.8"/>
      <circle cx="80"  cy="140" r="3"  fill="rgba(0,220,200,0.9)"/>

      <!-- Right -->
      <circle cx="260" cy="140" r="8"  fill="#0d1f3c" stroke="rgba(0,200,180,0.85)" stroke-width="1.8"/>
      <circle cx="260" cy="140" r="3"  fill="rgba(0,220,200,0.9)"/>

      <!-- Middle -->
      <circle cx="170" cy="180" r="7"  fill="#1a0f2e" stroke="rgba(180,130,255,0.8)" stroke-width="1.5"/>
      <circle cx="170" cy="180" r="2.5" fill="rgba(200,160,255,0.9)"/>

      <!-- Bottom left -->
      <circle cx="130" cy="220" r="6"  fill="#0a1520" stroke="rgba(80,130,255,0.7)" stroke-width="1.5"/>
      <circle cx="130" cy="220" r="2"  fill="rgba(120,170,255,0.8)"/>

      <!-- Bottom right -->
      <circle cx="210" cy="220" r="6"  fill="#0a1520" stroke="rgba(80,130,255,0.7)" stroke-width="1.5"/>
      <circle cx="210" cy="220" r="2"  fill="rgba(120,170,255,0.8)"/>

      <!-- Outer corner nodes -->
      <circle cx="40"  cy="70"  r="5"  fill="#080810" stroke="rgba(100,160,255,0.45)" stroke-width="1.2"/>
      <circle cx="300" cy="70"  r="5"  fill="#080810" stroke="rgba(100,160,255,0.45)" stroke-width="1.2"/>

      <!-- Node labels -->
      <text x="170" y="34"  text-anchor="middle" fill="rgba(160,190,255,0.7)" font-family="Space Mono" font-size="8" letter-spacing="1">v₁</text>
      <text x="63"  y="138" text-anchor="middle" fill="rgba(0,200,180,0.6)"   font-family="Space Mono" font-size="7">v₂</text>
      <text x="277" y="138" text-anchor="middle" fill="rgba(0,200,180,0.6)"   font-family="Space Mono" font-size="7">v₃</text>
      <text x="170" y="198" text-anchor="middle" fill="rgba(180,140,255,0.6)" font-family="Space Mono" font-size="7">v₄</text>
      <text x="116" y="236" text-anchor="middle" fill="rgba(100,150,255,0.55)" font-family="Space Mono" font-size="7">v₅</text>
      <text x="224" y="236" text-anchor="middle" fill="rgba(100,150,255,0.55)" font-family="Space Mono" font-size="7">v₆</text>

      <!-- Math annotations -->
      <text x="170" y="14" text-anchor="middle" fill="rgba(80,120,255,0.25)" font-family="Space Mono" font-size="8" letter-spacing="2">G = (V, E)</text>

      <!-- Binary decorative strip -->
      <text x="8" y="260" fill="rgba(60,100,200,0.12)" font-family="Space Mono" font-size="7" letter-spacing="1">01001 10110 00111 01010 11001 00110 10101</text>
    </svg>
  </div>

  <!-- Main content block -->
  <div class="content">
    <div class="label-materi">Materi Kuliah</div>

    <div class="title-main">
      <span class="accent-word">Matematika</span>
      <span class="solid-word">Diskrit</span>
    </div>

    <div class="subtitle">Graph Theory · Logic · Set · Combinatorics</div>

    <div class="divider"></div>

    <div class="author-row">
      <div class="author-block">
        <div class="author-label">Disusun oleh</div>
        <div class="author-name">Martin Bernard</div>
        <div class="author-degree">M.Pd</div>
      </div>
      <div class="symbols">
        <div class="symbol-row">∀x ∈ ℤ : P(x)</div>
        <div class="symbol-row">A ∩ B = ∅</div>
        <div class="symbol-row">p → q ≡ ¬p ∨ q</div>
      </div>
    </div>
  </div>

  <div class="bottom-bar"></div>
</div>
</body>
</html>
    """
    tampilkan1 = keterangan(tulisanHTML,1000)
    tampilkan1.tampilkan()
def materi1():
    bagian = st.tabs(['Dasar Teori','Penghubung Logika (Operator)','Ekuivalensi Logis','Contoh Soal','Latihan Soal'])
    with bagian[0]:
        tulisanHTML1= """
        <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Proposisi – Matematika Diskrit</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;600&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root {
  --bg:        #f5f2eb;
  --ink:       #1a1410;
  --ink2:      #3d3128;
  --ink3:      #7a6d5e;
  --true:      #1a7a4a;
  --true-bg:   #d6f0e2;
  --false:     #b83232;
  --false-bg:  #fde8e8;
  --neutral:   #5a4fcf;
  --neutral-bg:#ece9ff;
  --accent:    #c8882a;
  --card:      #fffef8;
  --border:    rgba(26,20,16,0.12);
  --shadow:    0 2px 20px rgba(26,20,16,0.08);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  background: var(--bg);
  color: var(--ink);
  font-family: 'Lora', serif;
  min-height: 100vh;
  padding-bottom: 80px;
}

/* ─── Noise texture overlay ─── */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
}

/* ─── Header ─── */
.hero {
  background: var(--ink);
  color: #f5f2eb;
  padding: 60px 40px 50px;
  position: relative;
  overflow: hidden;
}

.hero::after {
  content: '';
  position: absolute;
  right: -60px; bottom: -60px;
  width: 320px; height: 320px;
  border-radius: 50%;
  border: 1px solid rgba(245,242,235,0.06);
}
.hero::before {
  content: '';
  position: absolute;
  right: 20px; bottom: 20px;
  width: 200px; height: 200px;
  border-radius: 50%;
  border: 1px solid rgba(245,242,235,0.1);
}

.hero-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: rgba(200,136,42,0.85);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.hero-tag::before {
  content: '';
  display: inline-block;
  width: 24px; height: 1px;
  background: rgba(200,136,42,0.6);
}

.hero h1 {
  font-family: 'Syne', sans-serif;
  font-size: clamp(38px, 7vw, 64px);
  font-weight: 800;
  line-height: 1;
  letter-spacing: -1.5px;
  margin-bottom: 12px;
}

.hero h1 span {
  color: var(--accent);
}

.hero-sub {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: rgba(245,242,235,0.45);
  letter-spacing: 1px;
}

/* ─── Container ─── */
.container {
  max-width: 820px;
  margin: 0 auto;
  padding: 0 24px;
  position: relative;
  z-index: 1;
}

/* ─── Progress bar ─── */
.progress-wrap {
  background: var(--ink);
  padding: 14px 40px;
  display: flex;
  align-items: center;
  gap: 16px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.progress-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: rgba(245,242,235,0.5);
  white-space: nowrap;
  letter-spacing: 1px;
}

.progress-bar {
  flex: 1;
  height: 3px;
  background: rgba(245,242,235,0.1);
  border-radius: 2px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent), #e6a83a);
  border-radius: 2px;
  transition: width 0.5s ease;
  width: 0%;
}

.progress-score {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  font-weight: 600;
  color: var(--accent);
  min-width: 40px;
  text-align: right;
}

/* ─── Section titles ─── */
.section {
  margin-top: 56px;
}

.section-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: var(--ink3);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.section-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}

.section h2 {
  font-family: 'Syne', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}

/* ─── Definition card ─── */
.def-card {
  background: var(--ink);
  color: #f5f2eb;
  border-radius: 12px;
  padding: 36px;
  position: relative;
  overflow: hidden;
  margin-bottom: 24px;
}

.def-card::before {
  content: '"';
  position: absolute;
  top: -10px; right: 20px;
  font-family: 'Lora', serif;
  font-size: 140px;
  color: rgba(200,136,42,0.12);
  line-height: 1;
  pointer-events: none;
}

.def-card p {
  font-size: 17px;
  line-height: 1.75;
  color: rgba(245,242,235,0.88);
  position: relative;
  z-index: 1;
}

.def-card strong {
  color: var(--accent);
  font-style: normal;
}

/* ─── Key rule box ─── */
.rule-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 14px;
  margin-bottom: 28px;
}

.rule-pill {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 18px 16px;
  text-align: center;
  box-shadow: var(--shadow);
  transition: transform 0.2s, box-shadow 0.2s;
  cursor: default;
}

.rule-pill:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 28px rgba(26,20,16,0.12);
}

.rule-pill .icon {
  font-size: 26px;
  margin-bottom: 8px;
}

.rule-pill .label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--ink3);
  margin-bottom: 4px;
}

.rule-pill .val {
  font-family: 'Syne', sans-serif;
  font-size: 16px;
  font-weight: 700;
}

.pill-t .val { color: var(--true); }
.pill-f .val { color: var(--false); }
.pill-n .val { color: var(--neutral); }

/* ─── Example cards ─── */
.example-grid {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 8px;
}

.ex-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 18px 22px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: var(--shadow);
  cursor: pointer;
  transition: transform 0.15s, border-color 0.15s;
}

.ex-card:hover { transform: translateX(4px); }

.ex-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 1.5px;
  padding: 4px 10px;
  border-radius: 4px;
  white-space: nowrap;
}

.badge-true   { background: var(--true-bg);    color: var(--true);    }
.badge-false  { background: var(--false-bg);   color: var(--false);   }
.badge-bukan  { background: var(--neutral-bg); color: var(--neutral); }

.ex-text {
  font-style: italic;
  font-size: 15px;
  color: var(--ink2);
  flex: 1;
}

.ex-reason {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--ink3);
  margin-top: 4px;
  display: none;
}

.ex-card.revealed .ex-reason { display: block; }
.ex-card.revealed { border-color: rgba(26,20,16,0.22); }

.ex-toggle {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: var(--ink3);
  white-space: nowrap;
  padding: 4px 8px;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: transparent;
  cursor: pointer;
  transition: background 0.15s;
}
.ex-toggle:hover { background: var(--border); }

/* ─── Truth value visualizer ─── */
.visualizer {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 32px;
  box-shadow: var(--shadow);
  margin-bottom: 40px;
}

.viz-title {
  font-family: 'Syne', sans-serif;
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 6px;
}

.viz-sub {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--ink3);
  margin-bottom: 24px;
  letter-spacing: 1px;
}

.viz-input-wrap {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.viz-input {
  flex: 1;
  font-family: 'Lora', serif;
  font-style: italic;
  font-size: 15px;
  padding: 12px 16px;
  border: 1.5px solid var(--border);
  border-radius: 8px;
  background: var(--bg);
  color: var(--ink);
  outline: none;
  transition: border-color 0.2s;
}
.viz-input:focus { border-color: var(--accent); }

.viz-btn {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 1px;
  padding: 12px 20px;
  background: var(--ink);
  color: #f5f2eb;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity 0.15s;
}
.viz-btn:hover { opacity: 0.85; }

.viz-result {
  border-radius: 8px;
  padding: 18px 20px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  display: none;
  animation: fadeUp 0.3s ease;
}

.viz-result.show { display: block; }
.viz-result.true-res  { background: var(--true-bg);    color: var(--true);    border: 1px solid rgba(26,122,74,0.25); }
.viz-result.false-res { background: var(--false-bg);   color: var(--false);   border: 1px solid rgba(184,50,50,0.25); }
.viz-result.neutral-res { background: var(--neutral-bg); color: var(--neutral); border: 1px solid rgba(90,79,207,0.25); }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ─── Quiz ─── */
.quiz-wrap {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.quiz-card {
  background: var(--card);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 28px;
  box-shadow: var(--shadow);
  transition: border-color 0.3s;
}

.quiz-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 3px;
  color: var(--ink3);
  text-transform: uppercase;
  margin-bottom: 10px;
}

.quiz-q {
  font-style: italic;
  font-size: 18px;
  color: var(--ink);
  margin-bottom: 20px;
  line-height: 1.5;
  border-left: 3px solid var(--accent);
  padding-left: 16px;
}

.options {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.opt-btn {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 18px;
  border: 1.5px solid var(--border);
  border-radius: 8px;
  background: var(--bg);
  cursor: pointer;
  font-family: 'Lora', serif;
  font-size: 14px;
  color: var(--ink2);
  text-align: left;
  transition: border-color 0.15s, background 0.15s, transform 0.1s;
}

.opt-btn:hover:not(:disabled) {
  border-color: var(--accent);
  background: #fffbf0;
  transform: translateX(3px);
}

.opt-btn .opt-key {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  width: 22px; height: 22px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--border);
  color: var(--ink3);
  flex-shrink: 0;
  transition: background 0.15s, color 0.15s;
}

.opt-btn.correct {
  border-color: var(--true);
  background: var(--true-bg);
  color: var(--true);
}
.opt-btn.correct .opt-key { background: var(--true); color: white; }

.opt-btn.wrong {
  border-color: var(--false);
  background: var(--false-bg);
  color: var(--false);
}
.opt-btn.wrong .opt-key { background: var(--false); color: white; }

.opt-btn:disabled { cursor: default; }

.feedback {
  margin-top: 14px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  border-radius: 6px;
  padding: 10px 14px;
  display: none;
  animation: fadeUp 0.25s ease;
  line-height: 1.6;
}

.feedback.show { display: block; }
.feedback.ok { background: var(--true-bg); color: var(--true); }
.feedback.err { background: var(--false-bg); color: var(--false); }

/* ─── Scoreboard ─── */
.scoreboard {
  background: var(--ink);
  color: #f5f2eb;
  border-radius: 14px;
  padding: 40px;
  text-align: center;
  display: none;
  animation: fadeUp 0.4s ease;
  margin-top: 32px;
}

.scoreboard.show { display: block; }

.score-big {
  font-family: 'Syne', sans-serif;
  font-size: 72px;
  font-weight: 800;
  color: var(--accent);
  line-height: 1;
  margin-bottom: 8px;
}

.score-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: rgba(245,242,235,0.5);
  letter-spacing: 3px;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.score-msg {
  font-style: italic;
  font-size: 16px;
  color: rgba(245,242,235,0.75);
  margin-bottom: 28px;
}

.retry-btn {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 2px;
  padding: 12px 32px;
  background: var(--accent);
  color: var(--ink);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: opacity 0.15s;
}
.retry-btn:hover { opacity: 0.85; }

/* ─── Summary table ─── */
.summary-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
  margin-bottom: 24px;
}

.summary-table th {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--ink3);
  border-bottom: 2px solid var(--border);
  padding: 10px 12px;
  text-align: left;
}

.summary-table td {
  padding: 12px 12px;
  border-bottom: 1px solid var(--border);
  vertical-align: middle;
}

.summary-table tr:last-child td { border-bottom: none; }

.tag-t, .tag-f, .tag-n {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 600;
  padding: 3px 9px;
  border-radius: 4px;
  letter-spacing: 1px;
}
.tag-t { background: var(--true-bg);    color: var(--true);    }
.tag-f { background: var(--false-bg);   color: var(--false);   }
.tag-n { background: var(--neutral-bg); color: var(--neutral); }

/* ─── Footer ─── */
.footer {
  margin-top: 64px;
  padding: 28px 0;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-left {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--ink3);
}

.footer-right {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: var(--ink3);
  letter-spacing: 2px;
}
</style>
</head>
<body>

<!-- Hero -->
<div class="hero">
  <div class="container">
    <div class="hero-tag">Matematika Diskrit · Logika Proposisi</div>
    <h1>Apa itu <span>Proposisi?</span></h1>
    <p class="hero-sub">// dasar_logika.md — Martin Bernard, M.Pd</p>
  </div>
</div>

<!-- Sticky progress -->
<div class="progress-wrap">
  <span class="progress-label">LATIHAN</span>
  <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
  <span class="progress-score" id="progressScore">0 / 8</span>
</div>

<div class="container">

  <!-- ── TEORI ── -->
  <div class="section">
    <div class="section-label">01 · Dasar Teori</div>
    <h2>Definisi Proposisi</h2>

    <div class="def-card">
      <p>
        <strong>Proposisi</strong> adalah pernyataan deklaratif yang memiliki nilai kebenaran
        <strong>Benar (True / T)</strong> atau <strong>Salah (False / F)</strong>,
        tetapi <em>tidak keduanya sekaligus</em>.
        Suatu kalimat disebut proposisi jika nilai kebenarannya dapat ditentukan
        secara pasti, tidak bergantung pada variabel atau konteks yang tidak diketahui.
      </p>
    </div>

    <div class="rule-row">
      <div class="rule-pill pill-t">
        <div class="icon">✓</div>
        <div class="label">Nilai</div>
        <div class="val">BENAR (T)</div>
      </div>
      <div class="rule-pill pill-f">
        <div class="icon">✗</div>
        <div class="label">Nilai</div>
        <div class="val">SALAH (F)</div>
      </div>
      <div class="rule-pill pill-n">
        <div class="icon">?</div>
        <div class="label">Status</div>
        <div class="val">BUKAN Proposisi</div>
      </div>
    </div>
  </div>

  <!-- ── CONTOH ── -->
  <div class="section">
    <div class="section-label">02 · Contoh</div>
    <h2>Klik untuk Penjelasan</h2>

    <div class="example-grid">

      <div class="ex-card" onclick="toggleEx(this)">
        <span class="ex-badge badge-true">BENAR</span>
        <div class="ex-text">
          "2 + 2 = 4"
          <div class="ex-reason">→ Pernyataan deklaratif yang dapat dievaluasi: nilainya selalu Benar.</div>
        </div>
        <button class="ex-toggle">lihat alasan</button>
      </div>

      <div class="ex-card" onclick="toggleEx(this)">
        <span class="ex-badge badge-false">SALAH</span>
        <div class="ex-text">
          "Jakarta adalah ibu kota Jepang"
          <div class="ex-reason">→ Pernyataan deklaratif yang dapat dievaluasi: nilainya Salah (ibu kota Jepang adalah Tokyo).</div>
        </div>
        <button class="ex-toggle">lihat alasan</button>
      </div>

      <div class="ex-card" onclick="toggleEx(this)">
        <span class="ex-badge badge-true">BENAR</span>
        <div class="ex-text">
          "Bilangan prima terkecil adalah 2"
          <div class="ex-reason">→ Fakta matematis yang pasti Benar, dapat diverifikasi.</div>
        </div>
        <button class="ex-toggle">lihat alasan</button>
      </div>

      <div class="ex-card" onclick="toggleEx(this)">
        <span class="ex-badge badge-bukan">BUKAN</span>
        <div class="ex-text">
          "x + 2 = 5"
          <div class="ex-reason">→ Nilai kebenaran bergantung pada x. Bukan proposisi karena tidak bisa ditentukan T atau F secara pasti.</div>
        </div>
        <button class="ex-toggle">lihat alasan</button>
      </div>

      <div class="ex-card" onclick="toggleEx(this)">
        <span class="ex-badge badge-bukan">BUKAN</span>
        <div class="ex-text">
          "Tutup pintunya!"
          <div class="ex-reason">→ Kalimat perintah bukan pernyataan deklaratif, tidak bisa dinilai Benar/Salah.</div>
        </div>
        <button class="ex-toggle">lihat alasan</button>
      </div>

      <div class="ex-card" onclick="toggleEx(this)">
        <span class="ex-badge badge-bukan">BUKAN</span>
        <div class="ex-text">
          "Apakah hari ini hujan?"
          <div class="ex-reason">→ Kalimat tanya, bukan pernyataan. Tidak punya nilai kebenaran tetap.</div>
        </div>
        <button class="ex-toggle">lihat alasan</button>
      </div>

    </div>
  </div>

  <!-- ── TABEL RINGKASAN ── -->
  <div class="section">
    <div class="section-label">03 · Ringkasan</div>
    <h2>Tabel Identifikasi</h2>

    <table class="summary-table">
      <thead>
        <tr>
          <th>Pernyataan</th>
          <th>Status</th>
          <th>Alasan</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><em>"5 &gt; 3"</em></td>
          <td><span class="tag-t">BENAR</span></td>
          <td>Pernyataan matematis yang pasti</td>
        </tr>
        <tr>
          <td><em>"Bumi mengorbit Matahari"</em></td>
          <td><span class="tag-t">BENAR</span></td>
          <td>Fakta ilmiah yang dapat diverifikasi</td>
        </tr>
        <tr>
          <td><em>"3 adalah bilangan genap"</em></td>
          <td><span class="tag-f">SALAH</span></td>
          <td>Pernyataan salah, 3 adalah ganjil</td>
        </tr>
        <tr>
          <td><em>"Semoga berhasil!"</em></td>
          <td><span class="tag-n">BUKAN</span></td>
          <td>Kalimat seru / harapan</td>
        </tr>
        <tr>
          <td><em>"n² ≥ 0"</em></td>
          <td><span class="tag-t">BENAR</span></td>
          <td>Berlaku untuk semua n ∈ ℝ</td>
        </tr>
        <tr>
          <td><em>"Pergi sekarang"</em></td>
          <td><span class="tag-n">BUKAN</span></td>
          <td>Kalimat perintah</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ── VISUALIZER ── -->
  <div class="section">
    <div class="section-label">04 · Coba Sendiri</div>
    <h2>Uji Pernyataanmu</h2>

    <div class="visualizer">
      <div class="viz-title">Proposisi Checker</div>
      <div class="viz-sub">// ketik pernyataan → pilih status → cek hasilnya</div>
      <div class="viz-input-wrap">
        <input class="viz-input" id="vizInput" type="text" placeholder="Contoh: 7 adalah bilangan prima...">
        <button class="viz-btn" onclick="checkViz('true')">✓ BENAR</button>
        <button class="viz-btn" onclick="checkViz('false')" style="background:#b83232">✗ SALAH</button>
        <button class="viz-btn" onclick="checkViz('bukan')" style="background:#5a4fcf">? BUKAN</button>
      </div>
      <div class="viz-result" id="vizResult"></div>
    </div>
  </div>

  <!-- ── LATIHAN / QUIZ ── -->
  <div class="section">
    <div class="section-label">05 · Latihan</div>
    <h2>Uji Pemahamanmu</h2>

    <div class="quiz-wrap" id="quizWrap"></div>
    <div class="scoreboard" id="scoreboard">
      <div class="score-big" id="scoreBig">—</div>
      <div class="score-label">Skor Akhir</div>
      <div class="score-msg" id="scoreMsg"></div>
      <button class="retry-btn" onclick="retryQuiz()">↺ ULANGI LATIHAN</button>
    </div>
  </div>

  <!-- Footer -->
  <div class="footer">
    <div class="footer-left">Martin Bernard, M.Pd · Matematika Diskrit</div>
    <div class="footer-right">LOGIKA · PROPOSISI · 2025</div>
  </div>

</div>

<script>
// ─── Toggle example cards ───
function toggleEx(card) {
  const isOpen = card.classList.contains('revealed');
  card.classList.toggle('revealed');
  const btn = card.querySelector('.ex-toggle');
  btn.textContent = isOpen ? 'lihat alasan' : 'sembunyikan';
}

// ─── Proposition visualizer ───
function checkViz(verdict) {
  const input = document.getElementById('vizInput').value.trim();
  const result = document.getElementById('vizResult');
  if (!input) {
    result.className = 'viz-result show neutral-res';
    result.textContent = '⚠ Ketik pernyataan terlebih dahulu.';
    return;
  }
  const msgs = {
    true:  `✓ Kamu mengklasifikasikan: "${input}" sebagai PROPOSISI BENAR.\nPernyataan ini bernilai T (True). Pastikan nilainya memang selalu benar tanpa syarat.`,
    false: `✗ Kamu mengklasifikasikan: "${input}" sebagai PROPOSISI SALAH.\nPernyataan ini bernilai F (False). Ini tetap proposisi karena punya nilai kebenaran pasti.`,
    bukan: `? Kamu mengklasifikasikan: "${input}" sebagai BUKAN PROPOSISI.\nPernyataan ini tidak bisa dinilai T atau F (pertanyaan, perintah, atau memuat variabel bebas).`,
  };
  const cls = { true: 'true-res', false: 'false-res', bukan: 'neutral-res' };
  result.className = `viz-result show ${cls[verdict]}`;
  result.textContent = msgs[verdict];
}

// ─── Quiz data ───
const questions = [
  {
    q: '"10 ÷ 2 = 5"',
    options: ['Proposisi Benar', 'Proposisi Salah', 'Bukan Proposisi'],
    answer: 0,
    explain: '10 ÷ 2 = 5 adalah pernyataan matematis yang nilainya pasti Benar.'
  },
  {
    q: '"Apa kabar kamu?"',
    options: ['Proposisi Benar', 'Proposisi Salah', 'Bukan Proposisi'],
    answer: 2,
    explain: 'Kalimat tanya tidak dapat dinilai Benar/Salah, bukan proposisi.'
  },
  {
    q: '"Segitiga memiliki empat sisi"',
    options: ['Proposisi Benar', 'Proposisi Salah', 'Bukan Proposisi'],
    answer: 1,
    explain: 'Segitiga punya 3 sisi, bukan 4. Pernyataannya Salah, tetapi tetap proposisi.'
  },
  {
    q: '"y − 3 > 0"',
    options: ['Proposisi Benar', 'Proposisi Salah', 'Bukan Proposisi'],
    answer: 2,
    explain: 'Bergantung pada nilai y yang tidak diketahui → bukan proposisi.'
  },
  {
    q: '"Tolong kerjakan soal ini!"',
    options: ['Proposisi Benar', 'Proposisi Salah', 'Bukan Proposisi'],
    answer: 2,
    explain: 'Kalimat perintah tidak punya nilai kebenaran → bukan proposisi.'
  },
  {
    q: '"Bilangan 0 bukan bilangan asli"',
    options: ['Proposisi Benar', 'Proposisi Salah', 'Bukan Proposisi'],
    answer: 0,
    explain: '0 bukan anggota bilangan asli (ℕ = {1,2,3,…}). Pernyataan Benar.'
  },
  {
    q: '"√4 = 3"',
    options: ['Proposisi Benar', 'Proposisi Salah', 'Bukan Proposisi'],
    answer: 1,
    explain: '√4 = 2, bukan 3. Nilainya Salah, tetapi tetap merupakan proposisi.'
  },
  {
    q: '"Semoga kamu lulus ujian!"',
    options: ['Proposisi Benar', 'Proposisi Salah', 'Bukan Proposisi'],
    answer: 2,
    explain: 'Kalimat harapan/eksklamasi tidak dapat dinilai T atau F.'
  },
];

let answers = new Array(questions.length).fill(null);
let answered = 0;
const keys = ['A','B','C'];

function buildQuiz() {
  const wrap = document.getElementById('quizWrap');
  wrap.innerHTML = '';
  answers = new Array(questions.length).fill(null);
  answered = 0;
  updateProgress(0);
  document.getElementById('scoreboard').classList.remove('show');

  questions.forEach((q, qi) => {
    const card = document.createElement('div');
    card.className = 'quiz-card';
    card.id = `qcard-${qi}`;

    card.innerHTML = `
      <div class="quiz-num">SOAL ${String(qi+1).padStart(2,'0')} / ${questions.length}</div>
      <div class="quiz-q">${q.q}</div>
      <div class="options" id="opts-${qi}">
        ${q.options.map((opt,oi) => `
          <button class="opt-btn" onclick="selectAnswer(${qi},${oi})" id="opt-${qi}-${oi}">
            <span class="opt-key">${keys[oi]}</span>
            ${opt}
          </button>
        `).join('')}
      </div>
      <div class="feedback" id="fb-${qi}"></div>
    `;
    wrap.appendChild(card);
  });
}

function selectAnswer(qi, oi) {
  if (answers[qi] !== null) return;
  answers[qi] = oi;
  answered++;

  const q = questions[qi];
  const correct = oi === q.answer;

  // Style buttons
  for (let i = 0; i < q.options.length; i++) {
    const btn = document.getElementById(`opt-${qi}-${i}`);
    btn.disabled = true;
    if (i === q.answer) btn.classList.add('correct');
    else if (i === oi) btn.classList.add('wrong');
  }

  // Feedback
  const fb = document.getElementById(`fb-${qi}`);
  fb.className = `feedback show ${correct ? 'ok' : 'err'}`;
  fb.textContent = (correct ? '✓ Tepat! ' : '✗ Belum tepat. ') + q.explain;

  // Card border
  const card = document.getElementById(`qcard-${qi}`);
  card.style.borderColor = correct ? 'var(--true)' : 'var(--false)';

  updateProgress(answered);
  if (answered === questions.length) setTimeout(showScore, 600);
}

function updateProgress(n) {
  const pct = (n / questions.length) * 100;
  document.getElementById('progressFill').style.width = pct + '%';
  document.getElementById('progressScore').textContent = `${n} / ${questions.length}`;
}

function showScore() {
  const correct = answers.filter((a,i) => a === questions[i].answer).length;
  const pct = Math.round((correct / questions.length) * 100);
  const sb = document.getElementById('scoreboard');
  document.getElementById('scoreBig').textContent = `${pct}%`;
  const msgs = [
    [80, 'Luar biasa! Kamu menguasai konsep proposisi dengan sangat baik.'],
    [60, 'Bagus! Masih ada sedikit yang perlu diperkuat. Coba lagi!'],
    [0,  'Jangan menyerah! Baca kembali materinya dan ulangi latihan.'],
  ];
  document.getElementById('scoreMsg').textContent = msgs.find(([t]) => pct >= t)[1];
  sb.classList.add('show');
  sb.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function retryQuiz() {
  buildQuiz();
  document.getElementById('quizWrap').scrollIntoView({ behavior: 'smooth' });
}

buildQuiz();
</script>
</body>
</html>
        """
        tampilkan2 = keterangan(tulisanHTML1,6000)
        tampilkan2.tampilkan()

    with bagian[1]:
        tulisanHTML2="""
        <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Penghubung Logika – Matematika Diskrit</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;600&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #0e0f14;
  --bg2: #13141c;
  --bg3: #1a1c28;
  --card: #1e2030;
  --border: rgba(255,255,255,0.07);
  --ink: #edeef5;
  --ink2: #a0a3b8;
  --ink3: #5c6080;

  --and:   #22c55e; --and-bg:   rgba(34,197,94,0.1);
  --or:    #3b82f6; --or-bg:    rgba(59,130,246,0.1);
  --neg:   #f59e0b; --neg-bg:   rgba(245,158,11,0.1);
  --imp:   #ec4899; --imp-bg:   rgba(236,72,153,0.1);
  --bii:   #a78bfa; --bii-bg:   rgba(167,139,250,0.1);

  --t: #22c55e;
  --f: #ef4444;
  --shadow: 0 8px 32px rgba(0,0,0,0.4);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  background: var(--bg);
  color: var(--ink);
  font-family: 'Lora', serif;
  min-height: 100vh;
  padding-bottom: 80px;
}

/* ── HERO ── */
.hero {
  position: relative;
  padding: 64px 40px 56px;
  overflow: hidden;
  border-bottom: 1px solid var(--border);
}

.hero-grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
  background-size: 44px 44px;
}

.hero-glow {
  position: absolute;
  width: 600px; height: 300px;
  top: -80px; left: 50%; transform: translateX(-50%);
  background: radial-gradient(ellipse, rgba(100,80,240,0.18) 0%, transparent 70%);
  pointer-events: none;
}

.container { max-width: 900px; margin: 0 auto; padding: 0 24px; position: relative; z-index: 1; }

.hero-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px; letter-spacing: 4px; text-transform: uppercase;
  color: var(--bii); margin-bottom: 16px;
  display: flex; align-items: center; gap: 10px;
}
.hero-tag::before { content: ''; display: inline-block; width: 20px; height: 1px; background: var(--bii); opacity: 0.6; }

h1 {
  font-family: 'Syne', sans-serif;
  font-size: clamp(36px,6vw,60px);
  font-weight: 800; letter-spacing: -1.5px; line-height: 1.05;
  margin-bottom: 12px;
}
h1 .hi { color: var(--bii); }

.hero-sub {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px; color: var(--ink3); letter-spacing: 1px;
}

/* Operator pills in hero */
.op-strip {
  display: flex; gap: 10px; flex-wrap: wrap; margin-top: 28px;
}
.op-chip {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px; font-weight: 600;
  padding: 6px 14px; border-radius: 6px;
  border: 1px solid;
}
.op-chip.and { color: var(--and); border-color: var(--and); background: var(--and-bg); }
.op-chip.or  { color: var(--or);  border-color: var(--or);  background: var(--or-bg);  }
.op-chip.neg { color: var(--neg); border-color: var(--neg); background: var(--neg-bg); }
.op-chip.imp { color: var(--imp); border-color: var(--imp); background: var(--imp-bg); }
.op-chip.bii { color: var(--bii); border-color: var(--bii); background: var(--bii-bg); }

/* ── PROGRESS ── */
.progress-bar-wrap {
  background: var(--bg2); padding: 12px 40px;
  display: flex; align-items: center; gap: 14px;
  position: sticky; top: 0; z-index: 100;
  border-bottom: 1px solid var(--border);
}
.pl { font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--ink3); letter-spacing: 2px; white-space: nowrap; }
.pb { flex: 1; height: 2px; background: rgba(255,255,255,0.06); border-radius: 2px; overflow: hidden; }
.pf { height: 100%; background: linear-gradient(90deg, var(--bii), var(--imp)); border-radius: 2px; width: 0%; transition: width 0.5s ease; }
.ps { font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 600; color: var(--bii); min-width: 44px; text-align: right; }

/* ── SECTION ── */
.section { margin-top: 56px; }
.sec-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px; letter-spacing: 4px; text-transform: uppercase;
  color: var(--ink3); margin-bottom: 8px;
  display: flex; align-items: center; gap: 10px;
}
.sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }
.section h2 {
  font-family: 'Syne', sans-serif;
  font-size: 26px; font-weight: 700; letter-spacing: -0.5px;
  margin-bottom: 24px; color: var(--ink);
}

/* ── OPERATOR CARDS ── */
.op-cards { display: flex; flex-direction: column; gap: 16px; }

.op-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: transform 0.2s, border-color 0.2s;
}
.op-card:hover { transform: translateY(-2px); }

.op-card-head {
  padding: 20px 24px;
  display: flex; align-items: center; gap: 16px;
  cursor: pointer;
  user-select: none;
}

.op-symbol {
  font-family: 'JetBrains Mono', monospace;
  font-size: 22px; font-weight: 600;
  width: 52px; height: 52px;
  display: flex; align-items: center; justify-content: center;
  border-radius: 10px; flex-shrink: 0;
}

.op-meta { flex: 1; }
.op-name { font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; margin-bottom: 3px; }
.op-formula { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--ink3); letter-spacing: 1px; }
.op-rule { font-size: 13px; color: var(--ink2); font-style: italic; margin-top: 4px; }

.op-toggle-btn {
  font-family: 'JetBrains Mono', monospace; font-size: 18px;
  color: var(--ink3); background: none; border: none; cursor: pointer;
  transition: transform 0.3s; padding: 4px;
}
.op-card.open .op-toggle-btn { transform: rotate(180deg); }

.op-body {
  max-height: 0; overflow: hidden;
  transition: max-height 0.4s ease;
  border-top: 1px solid transparent;
}
.op-card.open .op-body {
  max-height: 500px;
  border-top-color: var(--border);
}
.op-body-inner { padding: 20px 24px 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }

/* Truth mini-table */
.tt-mini { }
.tt-label { font-family: 'JetBrains Mono', monospace; font-size: 9px; letter-spacing: 3px; text-transform: uppercase; color: var(--ink3); margin-bottom: 10px; }
table.tt { border-collapse: collapse; width: 100%; font-family: 'JetBrains Mono', monospace; font-size: 12px; }
table.tt th { padding: 6px 10px; color: var(--ink3); font-size: 10px; letter-spacing: 2px; border-bottom: 1px solid var(--border); text-align: center; }
table.tt td { padding: 6px 10px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.03); }
table.tt tr:last-child td { border-bottom: none; }
.tv-t { color: var(--t); font-weight: 600; }
.tv-f { color: var(--f); font-weight: 600; }

/* Example in op-body */
.op-examples { }
.op-ex-title { font-family: 'JetBrains Mono', monospace; font-size: 9px; letter-spacing: 3px; text-transform: uppercase; color: var(--ink3); margin-bottom: 10px; }
.op-ex-item { padding: 8px 12px; border-radius: 6px; margin-bottom: 8px; font-size: 13px; font-style: italic; color: var(--ink2); background: rgba(255,255,255,0.03); border-left: 2px solid; line-height: 1.5; }

/* Color schemes per operator */
.card-and { border-color: rgba(34,197,94,0.15); }
.card-and .op-symbol { background: var(--and-bg); color: var(--and); }
.card-and .op-name { color: var(--and); }
.card-and .op-ex-item { border-color: var(--and); }
.card-and.open { border-color: rgba(34,197,94,0.3); }

.card-or  { border-color: rgba(59,130,246,0.15); }
.card-or .op-symbol  { background: var(--or-bg);  color: var(--or);  }
.card-or .op-name  { color: var(--or);  }
.card-or .op-ex-item  { border-color: var(--or);  }
.card-or.open  { border-color: rgba(59,130,246,0.3); }

.card-neg { border-color: rgba(245,158,11,0.15); }
.card-neg .op-symbol { background: var(--neg-bg); color: var(--neg); }
.card-neg .op-name { color: var(--neg); }
.card-neg .op-ex-item { border-color: var(--neg); }
.card-neg.open { border-color: rgba(245,158,11,0.3); }

.card-imp { border-color: rgba(236,72,153,0.15); }
.card-imp .op-symbol { background: var(--imp-bg); color: var(--imp); }
.card-imp .op-name { color: var(--imp); }
.card-imp .op-ex-item { border-color: var(--imp); }
.card-imp.open { border-color: rgba(236,72,153,0.3); }

.card-bii { border-color: rgba(167,139,250,0.15); }
.card-bii .op-symbol { background: var(--bii-bg); color: var(--bii); }
.card-bii .op-name { color: var(--bii); }
.card-bii .op-ex-item { border-color: var(--bii); }
.card-bii.open { border-color: rgba(167,139,250,0.3); }

/* ── TRUTH TABLE BUILDER ── */
.tt-builder {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 32px;
  box-shadow: var(--shadow);
}

.tt-builder h3 {
  font-family: 'Syne', sans-serif;
  font-size: 18px; font-weight: 700; margin-bottom: 4px;
}
.tt-builder .sub {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px; color: var(--ink3); letter-spacing: 1px; margin-bottom: 24px;
}

.tt-controls {
  display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px;
}

.toggle-pill {
  display: flex; align-items: center; gap: 8px;
  font-family: 'JetBrains Mono', monospace; font-size: 12px;
  padding: 9px 16px;
  border-radius: 8px;
  border: 1.5px solid var(--border);
  background: transparent;
  color: var(--ink2);
  cursor: pointer;
  transition: all 0.2s;
  user-select: none;
}
.toggle-pill:hover { border-color: rgba(255,255,255,0.2); color: var(--ink); }
.toggle-pill.active-p { border-color: var(--ink); background: rgba(255,255,255,0.05); color: var(--ink); }

.value-toggle {
  display: flex;
  gap: 8px; margin-bottom: 24px;
}

.val-group { display: flex; flex-direction: column; gap: 4px; }
.val-label { font-family: 'JetBrains Mono', monospace; font-size: 9px; letter-spacing: 2px; color: var(--ink3); text-transform: uppercase; }

.val-btn {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px; font-weight: 600;
  padding: 10px 20px;
  border-radius: 8px;
  border: 1.5px solid var(--border);
  background: rgba(255,255,255,0.03);
  color: var(--ink3);
  cursor: pointer;
  transition: all 0.15s;
  min-width: 70px; text-align: center;
}
.val-btn.on-t { border-color: var(--t); background: rgba(34,197,94,0.12); color: var(--t); }
.val-btn.on-f { border-color: var(--f); background: rgba(239,68,68,0.12); color: var(--f); }

.tt-results {
  display: grid; gap: 10px;
}

.result-row {
  display: flex; align-items: center; gap: 12px;
  background: rgba(255,255,255,0.02);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px 16px;
  transition: border-color 0.2s;
}

.result-op {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px; font-weight: 600;
  min-width: 90px;
}
.result-formula {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px; color: var(--ink3); flex: 1;
}
.result-val {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px; font-weight: 700;
  padding: 4px 14px; border-radius: 6px;
  min-width: 60px; text-align: center;
}
.result-val.t { background: rgba(34,197,94,0.15); color: var(--t); }
.result-val.f { background: rgba(239,68,68,0.15); color: var(--f); }

/* ── QUIZ ── */
.quiz-wrap { display: flex; flex-direction: column; gap: 20px; }

.quiz-card {
  background: var(--card);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 28px;
  box-shadow: var(--shadow);
  transition: border-color 0.3s;
}

.quiz-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px; letter-spacing: 3px; color: var(--ink3); text-transform: uppercase; margin-bottom: 10px;
}

.quiz-q {
  font-size: 16px; line-height: 1.6; color: var(--ink);
  margin-bottom: 8px;
}

.quiz-expr {
  font-family: 'JetBrains Mono', monospace;
  font-size: 18px; font-weight: 600;
  color: var(--bii);
  background: rgba(167,139,250,0.08);
  border: 1px solid rgba(167,139,250,0.2);
  display: inline-block;
  padding: 8px 18px;
  border-radius: 8px;
  margin-bottom: 20px;
  letter-spacing: 2px;
}

.options { display: flex; flex-direction: column; gap: 10px; }

.opt-btn {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 18px;
  border: 1.5px solid var(--border);
  border-radius: 8px;
  background: rgba(255,255,255,0.02);
  cursor: pointer;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--ink2);
  text-align: left;
  transition: border-color 0.15s, background 0.15s, transform 0.1s;
}
.opt-btn:hover:not(:disabled) { border-color: rgba(167,139,250,0.4); background: rgba(167,139,250,0.05); transform: translateX(3px); color: var(--ink); }
.opt-btn .opt-key {
  font-size: 10px; font-weight: 700;
  width: 22px; height: 22px;
  border-radius: 4px;
  display: flex; align-items: center; justify-content: center;
  background: rgba(255,255,255,0.05); color: var(--ink3); flex-shrink: 0;
  transition: background 0.15s, color 0.15s;
}
.opt-btn.correct { border-color: var(--t); background: rgba(34,197,94,0.08); color: var(--t); }
.opt-btn.correct .opt-key { background: var(--t); color: #000; }
.opt-btn.wrong   { border-color: var(--f); background: rgba(239,68,68,0.08); color: var(--f); }
.opt-btn.wrong   .opt-key { background: var(--f); color: #fff; }
.opt-btn:disabled { cursor: default; }

.feedback {
  margin-top: 14px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px; border-radius: 6px;
  padding: 10px 14px; line-height: 1.7;
  display: none; animation: fadeUp 0.25s ease;
}
.feedback.show { display: block; }
.feedback.ok  { background: rgba(34,197,94,0.08);  color: var(--t); border: 1px solid rgba(34,197,94,0.2); }
.feedback.err { background: rgba(239,68,68,0.08);  color: var(--f); border: 1px solid rgba(239,68,68,0.2); }

/* ── SCOREBOARD ── */
.scoreboard {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px; padding: 48px;
  text-align: center; display: none;
  animation: fadeUp 0.4s ease; margin-top: 32px;
  box-shadow: var(--shadow);
}
.scoreboard.show { display: block; }
.score-big { font-family: 'Syne', sans-serif; font-size: 80px; font-weight: 800; color: var(--bii); line-height: 1; margin-bottom: 6px; }
.score-lbl { font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 4px; color: var(--ink3); text-transform: uppercase; margin-bottom: 16px; }
.score-msg { font-style: italic; font-size: 16px; color: var(--ink2); margin-bottom: 32px; }
.retry-btn {
  font-family: 'JetBrains Mono', monospace; font-size: 11px; letter-spacing: 2px;
  padding: 12px 32px; background: var(--bii); color: #0e0f14;
  border: none; border-radius: 8px; cursor: pointer; font-weight: 700;
  transition: opacity 0.15s;
}
.retry-btn:hover { opacity: 0.85; }

/* ── FOOTER ── */
.footer {
  margin-top: 64px; padding: 28px 0;
  border-top: 1px solid var(--border);
  display: flex; justify-content: space-between; align-items: center;
}
.footer-l { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--ink3); }
.footer-r { font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--ink3); letter-spacing: 2px; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Responsive */
@media (max-width: 600px) {
  .op-body-inner { grid-template-columns: 1fr; }
  .tt-controls { flex-direction: column; }
  .value-toggle { flex-wrap: wrap; }
  .result-row { flex-wrap: wrap; }
}
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-grid"></div>
  <div class="hero-glow"></div>
  <div class="container">
    <div class="hero-tag">Matematika Diskrit · Logika</div>
    <h1>Penghubung <span class="hi">Logika</span><br>(Operator)</h1>
    <p class="hero-sub">// operator_logika.md — Martin Bernard, M.Pd</p>
    <div class="op-strip">
      <span class="op-chip and">∧ Konjungsi</span>
      <span class="op-chip or">∨ Disjungsi</span>
      <span class="op-chip neg">¬ Negasi</span>
      <span class="op-chip imp">→ Implikasi</span>
      <span class="op-chip bii">↔ Biimplikasi</span>
    </div>
  </div>
</div>

<!-- PROGRESS -->
<div class="progress-bar-wrap">
  <span class="pl">LATIHAN</span>
  <div class="pb"><div class="pf" id="pFill"></div></div>
  <span class="ps" id="pScore">0 / 10</span>
</div>

<div class="container">

  <!-- ── 01 OPERATOR CARDS ── -->
  <div class="section">
    <div class="sec-label">01 · Dasar Teori</div>
    <h2>5 Operator Logika</h2>
    <div class="op-cards" id="opCards"></div>
  </div>

  <!-- ── 02 TRUTH TABLE BUILDER ── -->
  <div class="section">
    <div class="sec-label">02 · Eksplorasi Interaktif</div>
    <h2>Tabel Kebenaran Dinamis</h2>
    <div class="tt-builder">
      <h3>Truth Table Builder</h3>
      <p class="sub">// atur nilai p dan q → lihat semua hasil operator seketika</p>

      <div class="value-toggle">
        <div class="val-group">
          <div class="val-label">Nilai p</div>
          <button class="val-btn on-t" id="btnP" onclick="toggleVal('p')">T</button>
        </div>
        <div style="display:flex;align-items:flex-end;padding-bottom:2px;color:var(--ink3);font-family:'JetBrains Mono',monospace;font-size:18px;">×</div>
        <div class="val-group">
          <div class="val-label">Nilai q</div>
          <button class="val-btn on-t" id="btnQ" onclick="toggleVal('q')">T</button>
        </div>
      </div>

      <div class="tt-results" id="ttResults"></div>
    </div>
  </div>

  <!-- ── 03 FULL TRUTH TABLE ── -->
  <div class="section">
    <div class="sec-label">03 · Ringkasan</div>
    <h2>Tabel Kebenaran Lengkap</h2>
    <div style="overflow-x:auto;">
      <table id="fullTT" style="border-collapse:collapse;width:100%;background:var(--card);border-radius:12px;overflow:hidden;box-shadow:var(--shadow);font-family:'JetBrains Mono',monospace;font-size:13px;"></table>
    </div>
  </div>

  <!-- ── 04 QUIZ ── -->
  <div class="section">
    <div class="sec-label">04 · Latihan</div>
    <h2>Uji Pemahamanmu</h2>
    <div class="quiz-wrap" id="quizWrap"></div>
    <div class="scoreboard" id="scoreboard">
      <div class="score-big" id="scoreBig">—</div>
      <div class="score-lbl">Skor Akhir</div>
      <div class="score-msg" id="scoreMsg"></div>
      <button class="retry-btn" onclick="retryQuiz()">↺ ULANGI LATIHAN</button>
    </div>
  </div>

  <div class="footer">
    <div class="footer-l">Martin Bernard, M.Pd · Matematika Diskrit</div>
    <div class="footer-r">LOGIKA · OPERATOR · 2025</div>
  </div>

</div>

<script>
// ─── OPERATOR DATA ───
const ops = [
  {
    cls: 'card-and', symbol: '∧', name: 'Konjungsi', formula: 'p ∧ q',
    rule: 'Benar hanya jika kedua proposisi bernilai Benar.',
    rows: [['T','T','T'],['T','F','F'],['F','T','F'],['F','F','F']],
    header: ['p','q','p ∧ q'],
    examples: [
      '"Langit biru" ∧ "2+2=4" → T ∧ T = <b>T</b>',
      '"Langit biru" ∧ "2+2=5" → T ∧ F = <b>F</b>',
      '"Anjing bisa terbang" ∧ "2+2=4" → F ∧ T = <b>F</b>',
    ]
  },
  {
    cls: 'card-or', symbol: '∨', name: 'Disjungsi', formula: 'p ∨ q',
    rule: 'Benar jika salah satu atau keduanya bernilai Benar.',
    rows: [['T','T','T'],['T','F','T'],['F','T','T'],['F','F','F']],
    header: ['p','q','p ∨ q'],
    examples: [
      '"Langit biru" ∨ "2+2=5" → T ∨ F = <b>T</b>',
      '"Anjing terbang" ∨ "2+2=4" → F ∨ T = <b>T</b>',
      '"Anjing terbang" ∨ "batu bernafas" → F ∨ F = <b>F</b>',
    ]
  },
  {
    cls: 'card-neg', symbol: '¬', name: 'Negasi', formula: '¬p',
    rule: 'Membalik nilai kebenaran proposisi.',
    rows: [['T','F'],['F','T']],
    header: ['p','¬p'],
    examples: [
      'p = "Matahari terbit di timur" (T) → ¬p = <b>F</b>',
      'p = "2 adalah bilangan ganjil" (F) → ¬p = <b>T</b>',
    ]
  },
  {
    cls: 'card-imp', symbol: '→', name: 'Implikasi', formula: 'p → q',
    rule: 'Salah HANYA jika p Benar dan q Salah. Semua kondisi lain Benar.',
    rows: [['T','T','T'],['T','F','F'],['F','T','T'],['F','F','T']],
    header: ['p','q','p → q'],
    examples: [
      '"Jika hujan, maka tanah basah": T→T = <b>T</b>',
      '"Jika hujan, maka tanah kering": T→F = <b>F</b>',
      '"Jika batu bernafas, maka langit biru": F→T = <b>T</b>',
    ]
  },
  {
    cls: 'card-bii', symbol: '↔', name: 'Biimplikasi', formula: 'p ↔ q',
    rule: 'Benar jika p dan q memiliki nilai kebenaran yang SAMA.',
    rows: [['T','T','T'],['T','F','F'],['F','T','F'],['F','F','T']],
    header: ['p','q','p ↔ q'],
    examples: [
      '"2+2=4" ↔ "Langit biru": T↔T = <b>T</b>',
      '"2+2=4" ↔ "2+2=5": T↔F = <b>F</b>',
      '"Batu bernafas" ↔ "Kucing terbang": F↔F = <b>T</b>',
    ]
  },
];

// Build operator cards
const opCards = document.getElementById('opCards');
ops.forEach((op, i) => {
  const card = document.createElement('div');
  card.className = `op-card ${op.cls}`;
  card.id = `opcard-${i}`;

  const ttRows = op.rows.map(r =>
    `<tr>${r.map((c,ci) => `<td class="tv-${c.toLowerCase()}">${c}</td>`).join('')}</tr>`
  ).join('');

  const exItems = op.examples.map(e =>
    `<div class="op-ex-item">${e}</div>`
  ).join('');

  card.innerHTML = `
    <div class="op-card-head" onclick="toggleOp(${i})">
      <div class="op-symbol">${op.symbol}</div>
      <div class="op-meta">
        <div class="op-name">${op.name}</div>
        <div class="op-formula">${op.formula}</div>
        <div class="op-rule">${op.rule}</div>
      </div>
      <button class="op-toggle-btn">▾</button>
    </div>
    <div class="op-body">
      <div class="op-body-inner">
        <div class="tt-mini">
          <div class="tt-label">Tabel Kebenaran</div>
          <table class="tt">
            <thead><tr>${op.header.map(h=>`<th>${h}</th>`).join('')}</tr></thead>
            <tbody>${ttRows}</tbody>
          </table>
        </div>
        <div class="op-examples">
          <div class="op-ex-title">Contoh</div>
          ${exItems}
        </div>
      </div>
    </div>
  `;
  opCards.appendChild(card);
});

function toggleOp(i) {
  const card = document.getElementById(`opcard-${i}`);
  card.classList.toggle('open');
}

// ─── TRUTH TABLE BUILDER ───
let pVal = true, qVal = true;

function toggleVal(v) {
  if (v === 'p') {
    pVal = !pVal;
    const btn = document.getElementById('btnP');
    btn.textContent = pVal ? 'T' : 'F';
    btn.className = 'val-btn ' + (pVal ? 'on-t' : 'on-f');
  } else {
    qVal = !qVal;
    const btn = document.getElementById('btnQ');
    btn.textContent = qVal ? 'T' : 'F';
    btn.className = 'val-btn ' + (qVal ? 'on-t' : 'on-f');
  }
  renderResults();
}

function compute(p, q) {
  return {
    '¬p':    !p,
    '¬q':    !q,
    'p ∧ q': p && q,
    'p ∨ q': p || q,
    'p → q': !p || q,
    'p ↔ q': p === q,
  };
}

function renderResults() {
  const res = compute(pVal, qVal);
  const colors = { '¬p': 'var(--neg)', '¬q': 'var(--neg)', 'p ∧ q':'var(--and)', 'p ∨ q':'var(--or)', 'p → q':'var(--imp)', 'p ↔ q':'var(--bii)' };
  const wrap = document.getElementById('ttResults');
  wrap.innerHTML = Object.entries(res).map(([k,v]) => `
    <div class="result-row">
      <span class="result-op" style="color:${colors[k]}">${k}</span>
      <span class="result-formula">p=${pVal?'T':'F'}, q=${qVal?'T':'F'}</span>
      <span class="result-val ${v?'t':'f'}">${v?'TRUE':'FALSE'}</span>
    </div>
  `).join('');
}
renderResults();

// ─── FULL TRUTH TABLE ───
(function buildFullTable() {
  const table = document.getElementById('fullTT');
  const combos = [[true,true],[true,false],[false,true],[false,false]];
  const headers = ['p','q','¬p','¬q','p∧q','p∨q','p→q','p↔q'];
  const opColors = { '¬p':'var(--neg)','¬q':'var(--neg)','p∧q':'var(--and)','p∨q':'var(--or)','p→q':'var(--imp)','p↔q':'var(--bii)' };

  let html = `<thead><tr>`;
  headers.forEach(h => {
    const c = opColors[h] || 'var(--ink3)';
    html += `<th style="padding:12px 16px;color:${c};font-size:11px;letter-spacing:2px;border-bottom:1px solid var(--border);text-align:center;font-family:'JetBrains Mono',monospace;">${h}</th>`;
  });
  html += `</tr></thead><tbody>`;

  combos.forEach(([p,q],ri) => {
    const r = compute(p,q);
    const cells = [
      p?'T':'F', q?'T':'F',
      r['¬p']?'T':'F', r['¬q']?'T':'F',
      r['p ∧ q']?'T':'F', r['p ∨ q']?'T':'F',
      r['p → q']?'T':'F', r['p ↔ q']?'T':'F',
    ];
    const bg = ri % 2 === 0 ? 'rgba(255,255,255,0.015)' : 'transparent';
    html += `<tr style="background:${bg}">`;
    cells.forEach((c,ci) => {
      const col = c==='T' ? 'var(--t)' : 'var(--f)';
      html += `<td style="padding:10px 16px;text-align:center;color:${col};font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:600;border-bottom:1px solid rgba(255,255,255,0.03);">${c}</td>`;
    });
    html += `</tr>`;
  });
  html += `</tbody>`;
  table.innerHTML = html;
})();

// ─── QUIZ ───
const questions = [
  { q: 'Jika p = T dan q = F, berapakah nilai:', expr: 'p ∧ q', opts:['T (Benar)','F (Salah)','Tidak tentu'], ans:1, ex:'Konjungsi p∧q hanya benar jika keduanya benar. T∧F = F.' },
  { q: 'Jika p = F dan q = F, berapakah nilai:', expr: 'p ∨ q', opts:['T (Benar)','F (Salah)','Tidak tentu'], ans:1, ex:'Disjungsi p∨q hanya salah jika keduanya salah. F∨F = F.' },
  { q: 'Jika p = F, berapakah nilai:', expr: '¬p', opts:['T (Benar)','F (Salah)','Sama dengan p'], ans:0, ex:'Negasi membalik nilai. ¬F = T.' },
  { q: 'Jika p = T dan q = F, berapakah nilai:', expr: 'p → q', opts:['T (Benar)','F (Salah)','Tidak terdefinisi'], ans:1, ex:'Implikasi p→q salah HANYA jika p=T dan q=F. Maka hasilnya F.' },
  { q: 'Jika p = F dan q = F, berapakah nilai:', expr: 'p → q', opts:['T (Benar)','F (Salah)','Bergantung konteks'], ans:0, ex:'Implikasi F→F = T. Implikasi salah hanya jika p=T dan q=F.' },
  { q: 'Jika p = T dan q = T, berapakah nilai:', expr: 'p ↔ q', opts:['T (Benar)','F (Salah)','Tidak tentu'], ans:0, ex:'Biimplikasi benar jika keduanya sama. T↔T = T.' },
  { q: 'Jika p = T dan q = F, berapakah nilai:', expr: 'p ↔ q', opts:['T (Benar)','F (Salah)','Bergantung p'], ans:1, ex:'Biimplikasi salah jika nilainya berbeda. T↔F = F.' },
  { q: 'Operator manakah yang selalu Benar ketika p = F?', expr: 'p → q', opts:['Hanya jika q = T','Selalu Benar apapun nilai q','Selalu Salah'], ans:1, ex:'Jika p=F, implikasi p→q selalu T (F→T = T, F→F = T).' },
  { q: 'Jika p = F dan q = T, berapakah nilai:', expr: 'p ∧ q', opts:['T (Benar)','F (Salah)','Sama dengan q'], ans:1, ex:'Konjungsi hanya benar jika keduanya benar. F∧T = F.' },
  { q: 'Jika p = F dan q = T, berapakah nilai:', expr: 'p ∨ q', opts:['T (Benar)','F (Salah)','Sama dengan p'], ans:0, ex:'Disjungsi benar jika salah satu benar. F∨T = T.' },
];

let answers = new Array(questions.length).fill(null);
let answered = 0;
const keys = ['A','B','C'];

function buildQuiz() {
  const wrap = document.getElementById('quizWrap');
  wrap.innerHTML = '';
  answers = new Array(questions.length).fill(null);
  answered = 0;
  updateProgress(0);
  document.getElementById('scoreboard').classList.remove('show');

  questions.forEach((q, qi) => {
    const card = document.createElement('div');
    card.className = 'quiz-card';
    card.id = `qc-${qi}`;
    card.innerHTML = `
      <div class="quiz-num">SOAL ${String(qi+1).padStart(2,'0')} / ${questions.length}</div>
      <div class="quiz-q">${q.q}</div>
      <div class="quiz-expr">${q.expr}</div>
      <div class="options" id="opts-${qi}">
        ${q.opts.map((o,oi) => `
          <button class="opt-btn" onclick="pick(${qi},${oi})" id="opt-${qi}-${oi}">
            <span class="opt-key">${keys[oi]}</span>${o}
          </button>`).join('')}
      </div>
      <div class="feedback" id="fb-${qi}"></div>
    `;
    wrap.appendChild(card);
  });
}

function pick(qi, oi) {
  if (answers[qi] !== null) return;
  answers[qi] = oi;
  answered++;
  const q = questions[qi];
  const correct = oi === q.ans;
  for (let i = 0; i < q.opts.length; i++) {
    const b = document.getElementById(`opt-${qi}-${i}`);
    b.disabled = true;
    if (i === q.ans) b.classList.add('correct');
    else if (i === oi) b.classList.add('wrong');
  }
  const fb = document.getElementById(`fb-${qi}`);
  fb.className = `feedback show ${correct?'ok':'err'}`;
  fb.textContent = (correct ? '✓ Benar! ' : '✗ Belum tepat. ') + q.ex;
  const card = document.getElementById(`qc-${qi}`);
  card.style.borderColor = correct ? 'var(--t)' : 'var(--f)';
  updateProgress(answered);
  if (answered === questions.length) setTimeout(showScore, 700);
}

function updateProgress(n) {
  const pct = (n / questions.length) * 100;
  document.getElementById('pFill').style.width = pct + '%';
  document.getElementById('pScore').textContent = `${n} / ${questions.length}`;
}

function showScore() {
  const correct = answers.filter((a,i) => a === questions[i].ans).length;
  const pct = Math.round((correct / questions.length) * 100);
  document.getElementById('scoreBig').textContent = `${pct}%`;
  const msgs = [
    [90,'Sempurna! Kamu menguasai semua operator logika dengan sangat baik.'],
    [70,'Bagus! Pemahaman operator logikamu sudah kuat. Sedikit lagi sempurna!'],
    [50,'Cukup baik! Fokus pada implikasi dan biimplikasi yang sering membingungkan.'],
    [0, 'Jangan menyerah! Baca ulang tabel kebenaran dan coba eksplorasi builder di atas.'],
  ];
  document.getElementById('scoreMsg').textContent = msgs.find(([t]) => pct >= t)[1];
  const sb = document.getElementById('scoreboard');
  sb.classList.add('show');
  sb.scrollIntoView({ behavior:'smooth', block:'center' });
}

function retryQuiz() {
  buildQuiz();
  document.getElementById('quizWrap').scrollIntoView({ behavior:'smooth' });
}

buildQuiz();
</script>
</body>
</html>
        """
        tampilkan3 = keterangan(tulisanHTML2,8000)
        tampilkan3.tampilkan()

    with bagian[2]:
        tulisanHTML3="""
        <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ekuivalensi Logis – Matematika Diskrit</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=IBM+Plex+Mono:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root {
  --bg:        #faf8f4;
  --bg2:       #f2efe8;
  --bg3:       #e8e3d8;
  --card:      #ffffff;
  --ink:       #1c1a16;
  --ink2:      #4a4540;
  --ink3:      #9a9080;
  --border:    rgba(28,26,22,0.1);
  --border2:   rgba(28,26,22,0.06);

  --eq:        #c05c14;   /* orange-rust accent */
  --eq-bg:     #fff4ec;
  --taut:      #1a6b3c;
  --taut-bg:   #edfaf3;
  --cont:      #a01c2c;
  --cont-bg:   #fef0f0;

  --t:         #1a7a4a;
  --f:         #b83030;
  --t-bg:      #e8f8ef;
  --f-bg:      #fde8e8;

  --highlight: #fff0d4;
  --shadow-sm: 0 1px 4px rgba(28,26,22,0.06);
  --shadow:    0 4px 24px rgba(28,26,22,0.08);
  --shadow-lg: 0 12px 48px rgba(28,26,22,0.12);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  background: var(--bg);
  color: var(--ink);
  font-family: 'Outfit', sans-serif;
  min-height: 100vh;
  padding-bottom: 100px;
}

/* ─── TOPBAR ─── */
.topbar {
  background: var(--ink);
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 52px;
  position: sticky; top: 0; z-index: 200;
}
.topbar-brand {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px; font-weight: 600;
  letter-spacing: 2px; text-transform: uppercase;
  color: rgba(255,255,255,0.5);
}
.topbar-brand span { color: var(--eq); }
.topbar-progress {
  display: flex; align-items: center; gap: 10px;
}
.tp-label { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: rgba(255,255,255,0.35); letter-spacing: 1px; }
.tp-bar { width: 120px; height: 2px; background: rgba(255,255,255,0.1); border-radius: 2px; overflow: hidden; }
.tp-fill { height: 100%; background: var(--eq); border-radius: 2px; width: 0%; transition: width 0.5s ease; }
.tp-score { font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 600; color: var(--eq); min-width: 40px; text-align: right; }

/* ─── NAV TABS ─── */
.nav-tabs {
  background: var(--bg2);
  border-bottom: 1px solid var(--border);
  padding: 0 40px;
  display: flex; gap: 0;
  overflow-x: auto;
}
.nav-tab {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px; letter-spacing: 2px; text-transform: uppercase;
  padding: 14px 20px;
  color: var(--ink3);
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: color 0.2s, border-color 0.2s;
  white-space: nowrap;
  background: none; border-top: none; border-left: none; border-right: none;
}
.nav-tab:hover { color: var(--ink); }
.nav-tab.active { color: var(--eq); border-bottom-color: var(--eq); }

/* ─── PANELS ─── */
.panel { display: none; }
.panel.active { display: block; }

/* ─── HERO (inside panel) ─── */
.hero {
  background: var(--ink);
  padding: 64px 40px 56px;
  position: relative; overflow: hidden;
}
.hero-dots {
  position: absolute; inset: 0;
  background-image: radial-gradient(rgba(255,255,255,0.04) 1px, transparent 1px);
  background-size: 24px 24px;
}
.hero-stripe {
  position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, var(--eq), #e8a030, var(--eq));
  background-size: 200% 100%;
  animation: stripeMove 3s linear infinite;
}
@keyframes stripeMove { to { background-position: 200% 0; } }

.container { max-width: 860px; margin: 0 auto; padding: 0 24px; position: relative; z-index: 1; }

.hero-tag {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px; letter-spacing: 4px; text-transform: uppercase;
  color: rgba(192,92,20,0.8); margin-bottom: 18px;
}
.hero h1 {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(42px, 7vw, 72px);
  color: #ffffff; line-height: 1.05;
  margin-bottom: 16px; letter-spacing: -1px;
}
.hero h1 em { color: var(--eq); font-style: italic; }
.hero-sub {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px; color: rgba(255,255,255,0.35);
  letter-spacing: 1px; margin-bottom: 32px;
}
.hero-def {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-left: 3px solid var(--eq);
  border-radius: 0 8px 8px 0;
  padding: 20px 24px;
  font-size: 15px; line-height: 1.75;
  color: rgba(255,255,255,0.75);
  max-width: 680px;
}
.hero-def strong { color: var(--eq); font-weight: 600; }

/* ─── SECTION ─── */
.section { padding: 56px 0 0; }
.sec-row {
  display: flex; align-items: center; gap: 12px;
  margin-bottom: 24px;
}
.sec-num {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px; letter-spacing: 3px; text-transform: uppercase;
  color: var(--ink3);
}
.sec-line { flex: 1; height: 1px; background: var(--border); }
.section h2 {
  font-family: 'DM Serif Display', serif;
  font-size: 30px; color: var(--ink); letter-spacing: -0.5px;
  margin-bottom: 6px;
}
.section .sec-desc {
  font-size: 14px; color: var(--ink3); margin-bottom: 28px;
  font-family: 'IBM Plex Mono', monospace; font-size: 12px; letter-spacing: 0.5px;
}

/* ─── DEFINITION BLOCK ─── */
.def-box {
  background: var(--eq-bg);
  border: 1px solid rgba(192,92,20,0.2);
  border-radius: 12px;
  padding: 28px 32px;
  margin-bottom: 28px;
  position: relative; overflow: hidden;
}
.def-box::before {
  content: '≡';
  position: absolute; right: 24px; top: 50%; transform: translateY(-50%);
  font-family: 'DM Serif Display', serif;
  font-size: 100px; color: rgba(192,92,20,0.07);
  pointer-events: none;
}
.def-box p { font-size: 15px; line-height: 1.8; color: var(--ink2); }
.def-box p strong { color: var(--eq); }
.def-box .notation {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 20px; font-weight: 600;
  color: var(--eq); margin-top: 12px;
  letter-spacing: 2px;
}

/* ─── EQUIVALENCE LAW CARDS ─── */
.law-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-bottom: 8px;
}
@media (max-width: 640px) { .law-grid { grid-template-columns: 1fr; } }

.law-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 22px;
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: transform 0.18s, box-shadow 0.18s, border-color 0.18s;
  position: relative;
  overflow: hidden;
}
.law-card::after {
  content: '';
  position: absolute; top: 0; left: 0; width: 3px; height: 100%;
  border-radius: 12px 0 0 12px;
}
.law-card:hover { transform: translateY(-2px); box-shadow: var(--shadow); border-color: rgba(28,26,22,0.18); }
.law-card.expanded { border-color: rgba(192,92,20,0.3); box-shadow: var(--shadow); }
.law-card.expanded::after { background: var(--eq); }

.law-name {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px; letter-spacing: 3px; text-transform: uppercase;
  color: var(--ink3); margin-bottom: 8px;
}
.law-formula {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 15px; font-weight: 600; color: var(--ink);
  margin-bottom: 6px; letter-spacing: 1px;
}
.law-desc { font-size: 13px; color: var(--ink3); line-height: 1.5; }

.law-body {
  max-height: 0; overflow: hidden;
  transition: max-height 0.35s ease, padding-top 0.35s;
  padding-top: 0;
}
.law-card.expanded .law-body {
  max-height: 300px;
  padding-top: 14px;
  border-top: 1px solid var(--border2);
  margin-top: 12px;
}

.law-verify {
  display: inline-block;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px;
  padding: 6px 14px;
  border-radius: 6px;
  background: var(--eq-bg);
  color: var(--eq);
  border: 1px solid rgba(192,92,20,0.2);
  cursor: pointer;
  transition: background 0.15s;
  margin-top: 4px;
}
.law-verify:hover { background: rgba(192,92,20,0.15); }

.law-tt { margin-top: 10px; display: none; animation: fadeUp 0.2s ease; }
.law-tt.show { display: block; }
.law-tt table { border-collapse: collapse; font-family: 'IBM Plex Mono', monospace; font-size: 11px; width: 100%; }
.law-tt th { padding: 5px 8px; color: var(--ink3); font-size: 9px; letter-spacing: 2px; border-bottom: 1px solid var(--border); text-align: center; }
.law-tt td { padding: 5px 8px; text-align: center; }
.tv-T { color: var(--t); font-weight: 700; }
.tv-F { color: var(--f); font-weight: 700; }
.tv-eq { color: var(--eq); font-weight: 700; font-size: 13px; }

/* ─── PROOF CHECKER ─── */
.proof-checker {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 32px;
  box-shadow: var(--shadow);
}
.proof-checker h3 {
  font-family: 'DM Serif Display', serif;
  font-size: 22px; margin-bottom: 4px;
}
.proof-checker .sub {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px; color: var(--ink3); margin-bottom: 28px;
}

.checker-selects {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 12px; align-items: center;
  margin-bottom: 20px;
}
.checker-eq-sym {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 22px; font-weight: 600;
  color: var(--eq); text-align: center;
}
.formula-select {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 13px; font-weight: 500;
  padding: 12px 16px;
  border: 1.5px solid var(--border);
  border-radius: 8px;
  background: var(--bg);
  color: var(--ink);
  outline: none;
  cursor: pointer;
  transition: border-color 0.2s;
  width: 100%;
}
.formula-select:focus { border-color: var(--eq); }

.check-btn {
  width: 100%;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px; letter-spacing: 2px; font-weight: 600;
  padding: 13px;
  background: var(--ink); color: #fff;
  border: none; border-radius: 8px;
  cursor: pointer; transition: opacity 0.15s;
  margin-bottom: 20px;
}
.check-btn:hover { opacity: 0.85; }

.checker-result {
  display: none; animation: fadeUp 0.25s ease;
  border-radius: 10px; overflow: hidden;
}
.checker-result.show { display: block; }

.cr-header {
  padding: 14px 20px;
  display: flex; align-items: center; gap: 12px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px; font-weight: 600;
}
.cr-header.equiv   { background: var(--taut-bg); color: var(--taut); border: 1px solid rgba(26,107,60,0.2); }
.cr-header.nonequiv { background: var(--cont-bg); color: var(--cont); border: 1px solid rgba(160,28,44,0.2); }
.cr-icon { font-size: 18px; }

.cr-table { padding: 0; }
.cr-table table { width: 100%; border-collapse: collapse; font-family: 'IBM Plex Mono', monospace; font-size: 12px; }
.cr-table th { background: var(--bg2); padding: 8px 12px; font-size: 9px; letter-spacing: 2px; color: var(--ink3); text-align: center; border-bottom: 1px solid var(--border); }
.cr-table td { padding: 8px 12px; text-align: center; border-bottom: 1px solid var(--border2); }
.cr-table tr:last-child td { border-bottom: none; }
.highlight-col { background: var(--highlight); }

/* ─── TAUTOLOGY / CONTRADICTION ─── */
.tc-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 16px;
  margin-bottom: 28px;
}
@media (max-width:560px){ .tc-grid { grid-template-columns: 1fr; } }

.tc-card {
  border-radius: 12px; padding: 24px;
  border: 1px solid; position: relative; overflow: hidden;
}
.tc-card.taut { background: var(--taut-bg); border-color: rgba(26,107,60,0.2); }
.tc-card.cont { background: var(--cont-bg); border-color: rgba(160,28,44,0.2); }

.tc-icon { font-size: 32px; margin-bottom: 10px; }
.tc-name {
  font-family: 'DM Serif Display', serif;
  font-size: 22px; margin-bottom: 6px;
}
.taut .tc-name { color: var(--taut); }
.cont .tc-name { color: var(--cont); }
.tc-def { font-size: 13px; color: var(--ink2); line-height: 1.6; margin-bottom: 12px; }
.tc-example {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px; padding: 8px 12px;
  border-radius: 6px; font-weight: 500;
}
.taut .tc-example { background: rgba(26,107,60,0.08); color: var(--taut); }
.cont .tc-example { background: rgba(160,28,44,0.08); color: var(--cont); }

/* ─── FORMULA EVALUATOR ─── */
.evaluator {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 32px;
  box-shadow: var(--shadow);
  margin-bottom: 28px;
}
.evaluator h3 { font-family: 'DM Serif Display', serif; font-size: 22px; margin-bottom: 4px; }
.evaluator .sub { font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--ink3); margin-bottom: 24px; }

.eval-vars { display: flex; gap: 16px; margin-bottom: 20px; flex-wrap: wrap; }
.ev-group { display: flex; flex-direction: column; gap: 5px; }
.ev-label { font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: 2px; color: var(--ink3); text-transform: uppercase; }
.ev-toggle {
  font-family: 'IBM Plex Mono', monospace; font-size: 14px; font-weight: 700;
  padding: 10px 22px; border-radius: 8px; border: 1.5px solid var(--border);
  background: var(--bg); color: var(--ink3); cursor: pointer;
  transition: all 0.15s; min-width: 64px; text-align: center;
}
.ev-toggle.vT { border-color: var(--t); background: var(--t-bg); color: var(--t); }
.ev-toggle.vF { border-color: var(--f); background: var(--f-bg); color: var(--f); }

.eval-select {
  font-family: 'IBM Plex Mono', monospace; font-size: 13px;
  padding: 12px 16px; border: 1.5px solid var(--border);
  border-radius: 8px; background: var(--bg); color: var(--ink);
  outline: none; cursor: pointer; width: 100%; margin-bottom: 16px;
  transition: border-color 0.2s;
}
.eval-select:focus { border-color: var(--eq); }

.eval-result-grid { display: flex; flex-direction: column; gap: 8px; }
.eval-row {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 16px;
  border-radius: 8px;
  background: var(--bg2);
  border: 1px solid var(--border2);
}
.eval-formula { font-family: 'IBM Plex Mono', monospace; font-size: 12px; color: var(--ink2); flex: 1; }
.eval-val {
  font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 700;
  padding: 3px 12px; border-radius: 5px; min-width: 54px; text-align: center;
}
.eval-val.T { background: var(--t-bg); color: var(--t); }
.eval-val.F { background: var(--f-bg); color: var(--f); }
.equiv-badge {
  font-family: 'IBM Plex Mono', monospace; font-size: 10px; font-weight: 600;
  padding: 3px 10px; border-radius: 5px;
}
.equiv-badge.yes { background: var(--eq-bg); color: var(--eq); }
.equiv-badge.no  { background: var(--f-bg); color: var(--f); }

/* ─── QUIZ ─── */
.quiz-wrap { display: flex; flex-direction: column; gap: 18px; }
.quiz-card {
  background: var(--card); border: 1.5px solid var(--border);
  border-radius: 14px; padding: 28px;
  box-shadow: var(--shadow-sm); transition: border-color 0.3s;
}
.quiz-num {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px; letter-spacing: 3px; color: var(--ink3); text-transform: uppercase; margin-bottom: 10px;
}
.quiz-q { font-size: 15px; color: var(--ink2); margin-bottom: 10px; line-height: 1.6; }
.quiz-expr {
  font-family: 'IBM Plex Mono', monospace; font-size: 17px; font-weight: 600;
  color: var(--eq);
  background: var(--eq-bg); border: 1px solid rgba(192,92,20,0.2);
  display: inline-block; padding: 8px 18px;
  border-radius: 8px; margin-bottom: 20px; letter-spacing: 1.5px;
}
.options { display: flex; flex-direction: column; gap: 9px; }
.opt-btn {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border: 1.5px solid var(--border);
  border-radius: 8px; background: var(--bg);
  cursor: pointer; font-family: 'Outfit', sans-serif; font-size: 14px;
  color: var(--ink2); text-align: left;
  transition: border-color 0.15s, background 0.15s, transform 0.1s;
}
.opt-btn:hover:not(:disabled) { border-color: var(--eq); background: var(--eq-bg); color: var(--ink); transform: translateX(3px); }
.opt-btn .opt-key {
  font-family: 'IBM Plex Mono', monospace; font-size: 10px; font-weight: 700;
  width: 24px; height: 24px; border-radius: 4px;
  display: flex; align-items: center; justify-content: center;
  background: var(--border); color: var(--ink3); flex-shrink: 0;
  transition: background 0.15s, color 0.15s;
}
.opt-btn.correct { border-color: var(--t); background: var(--t-bg); color: var(--t); }
.opt-btn.correct .opt-key { background: var(--t); color: #fff; }
.opt-btn.wrong   { border-color: var(--f); background: var(--f-bg); color: var(--f); }
.opt-btn.wrong   .opt-key { background: var(--f); color: #fff; }
.opt-btn:disabled { cursor: default; }

.feedback {
  margin-top: 14px; font-family: 'IBM Plex Mono', monospace; font-size: 11px;
  border-radius: 6px; padding: 10px 14px; line-height: 1.7; display: none;
  animation: fadeUp 0.25s ease;
}
.feedback.show { display: block; }
.feedback.ok  { background: var(--t-bg); color: var(--t); border: 1px solid rgba(26,122,74,0.2); }
.feedback.err { background: var(--f-bg); color: var(--f); border: 1px solid rgba(184,50,50,0.2); }

/* ─── SCOREBOARD ─── */
.scoreboard {
  background: var(--ink); border-radius: 16px;
  padding: 48px; text-align: center;
  display: none; animation: fadeUp 0.4s ease; margin-top: 28px;
  box-shadow: var(--shadow-lg);
}
.scoreboard.show { display: block; }
.score-big { font-family: 'DM Serif Display', serif; font-size: 86px; color: var(--eq); line-height: 1; margin-bottom: 6px; }
.score-lbl { font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 4px; color: rgba(255,255,255,0.35); text-transform: uppercase; margin-bottom: 14px; }
.score-msg { font-style: italic; font-size: 16px; color: rgba(255,255,255,0.6); margin-bottom: 32px; font-family: 'DM Serif Display', serif; }
.retry-btn {
  font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 2px;
  padding: 12px 36px; background: var(--eq); color: #fff;
  border: none; border-radius: 8px; cursor: pointer; font-weight: 600;
  transition: opacity 0.15s;
}
.retry-btn:hover { opacity: 0.85; }

/* ─── FOOTER ─── */
.footer {
  margin-top: 64px; padding: 28px 0;
  border-top: 1px solid var(--border);
  display: flex; justify-content: space-between; align-items: center;
}
.footer-l { font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--ink3); }
.footer-r { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: var(--ink3); letter-spacing: 2px; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Tabs scroll on mobile */
@media (max-width:500px) {
  .topbar { padding: 0 16px; }
  .nav-tabs { padding: 0 16px; }
  .hero { padding: 40px 0; }
  .checker-selects { grid-template-columns: 1fr; }
  .checker-eq-sym { display: none; }
}
</style>
</head>
<body>

<!-- TOPBAR -->
<div class="topbar">
  <div class="topbar-brand">Matematika Diskrit · <span>Ekuivalensi Logis</span></div>
  <div class="topbar-progress">
    <span class="tp-label">QUIZ</span>
    <div class="tp-bar"><div class="tp-fill" id="tpFill"></div></div>
    <span class="tp-score" id="tpScore">0/12</span>
  </div>
</div>

<!-- NAV TABS -->
<div class="nav-tabs">
  <button class="nav-tab active" onclick="switchTab('teori')">01 · Teori</button>
  <button class="nav-tab" onclick="switchTab('hukum')">02 · Hukum Ekuivalensi</button>
  <button class="nav-tab" onclick="switchTab('explorer')">03 · Explorer</button>
  <button class="nav-tab" onclick="switchTab('tautologi')">04 · Tautologi & Kontradiksi</button>
  <button class="nav-tab" onclick="switchTab('latihan')">05 · Latihan Quiz</button>
</div>

<!-- ══════════════════════════════════════════════
     PANEL 1 : TEORI
══════════════════════════════════════════════ -->
<div class="panel active" id="panel-teori">
  <div class="hero">
    <div class="hero-dots"></div>
    <div class="hero-stripe"></div>
    <div class="container">
      <div class="hero-tag">Matematika Diskrit · Logika · Martin Bernard, M.Pd</div>
      <h1>Ekuivalensi <em>Logis</em></h1>
      <p class="hero-sub">// logical_equivalence.md — dua formula, satu kebenaran</p>
      <div class="hero-def">
        Dua proposisi <strong>p</strong> dan <strong>q</strong> dikatakan <strong>ekuivalen secara logis</strong>
        jika biimplikasi <strong>p ↔ q</strong> merupakan <strong>tautologi</strong> —
        artinya keduanya selalu memiliki nilai kebenaran yang <em>identik</em> untuk
        setiap kemungkinan nilai variabelnya.
      </div>
    </div>
  </div>

  <div class="container">
    <div class="section">
      <div class="sec-row"><span class="sec-num">DEFINISI</span><div class="sec-line"></div></div>
      <h2>Apa itu Ekuivalensi Logis?</h2>

      <div class="def-box">
        <p>
          Dua formula logika <strong>P</strong> dan <strong>Q</strong> disebut <strong>ekuivalen logis</strong>,
          ditulis <strong>P ≡ Q</strong>, jika dan hanya jika untuk setiap kombinasi nilai
          variabel proposisional, nilai kebenaran <strong>P</strong> selalu sama dengan nilai
          kebenaran <strong>Q</strong>.
        </p>
        <div class="notation">P ≡ Q &nbsp;⟺&nbsp; (P ↔ Q) adalah tautologi</div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:28px;">
        <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:22px;box-shadow:var(--shadow-sm);">
          <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:3px;color:var(--ink3);text-transform:uppercase;margin-bottom:10px;">Notasi</div>
          <div style="font-family:'IBM Plex Mono',monospace;font-size:16px;font-weight:600;color:var(--eq);margin-bottom:6px;">P ≡ Q</div>
          <div style="font-size:13px;color:var(--ink3);line-height:1.6;">"P secara logis ekuivalen dengan Q"</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:22px;box-shadow:var(--shadow-sm);">
          <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:3px;color:var(--ink3);text-transform:uppercase;margin-bottom:10px;">Cara Membuktikan</div>
          <div style="font-size:13px;color:var(--ink2);line-height:1.7;">
            Buat tabel kebenaran kedua formula. Jika kolom hasil <em>identik</em> pada semua baris → terbukti ekuivalen.
          </div>
        </div>
      </div>

      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:28px;box-shadow:var(--shadow-sm);margin-bottom:8px;">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:3px;color:var(--ink3);text-transform:uppercase;margin-bottom:14px;">Contoh Klasik: Hukum De Morgan</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:17px;font-weight:600;color:var(--eq);margin-bottom:16px;letter-spacing:1px;">¬(p ∧ q) ≡ ¬p ∨ ¬q</div>

        <div style="overflow-x:auto;">
          <table style="border-collapse:collapse;font-family:'IBM Plex Mono',monospace;font-size:12px;width:100%;">
            <thead>
              <tr>
                <th style="padding:8px 12px;color:var(--ink3);font-size:9px;letter-spacing:2px;border-bottom:2px solid var(--border);text-align:center;">p</th>
                <th style="padding:8px 12px;color:var(--ink3);font-size:9px;letter-spacing:2px;border-bottom:2px solid var(--border);text-align:center;">q</th>
                <th style="padding:8px 12px;color:var(--ink3);font-size:9px;letter-spacing:2px;border-bottom:2px solid var(--border);text-align:center;">p∧q</th>
                <th style="padding:8px 12px;color:var(--eq);font-size:9px;letter-spacing:2px;border-bottom:2px solid var(--eq);text-align:center;background:var(--eq-bg);">¬(p∧q)</th>
                <th style="padding:8px 12px;color:var(--ink3);font-size:9px;letter-spacing:2px;border-bottom:2px solid var(--border);text-align:center;">¬p</th>
                <th style="padding:8px 12px;color:var(--ink3);font-size:9px;letter-spacing:2px;border-bottom:2px solid var(--border);text-align:center;">¬q</th>
                <th style="padding:8px 12px;color:var(--eq);font-size:9px;letter-spacing:2px;border-bottom:2px solid var(--eq);text-align:center;background:var(--eq-bg);">¬p∨¬q</th>
                <th style="padding:8px 12px;color:var(--taut);font-size:9px;letter-spacing:2px;border-bottom:2px solid var(--border);text-align:center;background:var(--taut-bg);">≡ ?</th>
              </tr>
            </thead>
            <tbody id="deMorganTable"></tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="footer-l">Martin Bernard, M.Pd · Matematika Diskrit</div>
      <div class="footer-r">EKUIVALENSI LOGIS · 2025</div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     PANEL 2 : HUKUM EKUIVALENSI
══════════════════════════════════════════════ -->
<div class="panel" id="panel-hukum">
  <div class="container">
    <div class="section">
      <div class="sec-row"><span class="sec-num">02 · HUKUM EKUIVALENSI</span><div class="sec-line"></div></div>
      <h2>20 Hukum Ekuivalensi Logis</h2>
      <p class="sec-desc">// klik setiap kartu untuk melihat tabel kebenaran pembuktian</p>
      <div class="law-grid" id="lawGrid"></div>
    </div>
    <div class="footer">
      <div class="footer-l">Martin Bernard, M.Pd · Matematika Diskrit</div>
      <div class="footer-r">EKUIVALENSI LOGIS · 2025</div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     PANEL 3 : EXPLORER
══════════════════════════════════════════════ -->
<div class="panel" id="panel-explorer">
  <div class="container">
    <div class="section">
      <div class="sec-row"><span class="sec-num">03 · PROOF CHECKER</span><div class="sec-line"></div></div>
      <h2>Ekuivalensi Checker</h2>
      <p class="sec-desc">// pilih dua formula → sistem otomatis membuktikan ekuivalensinya</p>

      <div class="proof-checker">
        <h3>Buktikan Ekuivalensi</h3>
        <p class="sub">// pilih formula kiri dan kanan, lalu klik BUKTIKAN</p>

        <div class="checker-selects">
          <select class="formula-select" id="fLeft">
            <option value="imp">p → q</option>
            <option value="neg_p_or_q">¬p ∨ q</option>
            <option value="neg_imp">¬(p → q)</option>
            <option value="p_and_neg_q">p ∧ ¬q</option>
            <option value="neg_p_and_q">¬p ∧ ¬q</option>
            <option value="neg_p_or_q2">¬(p ∨ q)</option>
            <option value="neg_p_and_q2">¬(p ∧ q)</option>
            <option value="neg_p_or_neg_q">¬p ∨ ¬q</option>
            <option value="double_neg">¬¬p</option>
            <option value="p">p</option>
            <option value="contr_pos">¬q → ¬p</option>
            <option value="p_or_p">p ∨ p</option>
            <option value="p_and_p">p ∧ p</option>
          </select>
          <div class="checker-eq-sym">≡ ?</div>
          <select class="formula-select" id="fRight">
            <option value="neg_p_or_q">¬p ∨ q</option>
            <option value="imp">p → q</option>
            <option value="p_and_neg_q">p ∧ ¬q</option>
            <option value="neg_imp">¬(p → q)</option>
            <option value="neg_p_or_q2">¬(p ∨ q)</option>
            <option value="neg_p_and_q">¬p ∧ ¬q</option>
            <option value="neg_p_or_neg_q">¬p ∨ ¬q</option>
            <option value="neg_p_and_q2">¬(p ∧ q)</option>
            <option value="p">p</option>
            <option value="double_neg">¬¬p</option>
            <option value="imp">p → q</option>
            <option value="p">p</option>
            <option value="p">p</option>
          </select>
        </div>

        <button class="check-btn" onclick="runChecker()">▶ BUKTIKAN EKUIVALENSI</button>
        <div class="checker-result" id="checkerResult"></div>
      </div>

      <!-- Dynamic evaluator -->
      <div class="section">
        <div class="sec-row"><span class="sec-num">EVALUATOR DINAMIS</span><div class="sec-line"></div></div>
        <h2>Evaluasi Semua Hukum Sekaligus</h2>
        <p class="sec-desc">// atur nilai p dan q → lihat semua pasangan ekuivalen terbukti</p>

        <div class="evaluator">
          <h3>Multi-Law Evaluator</h3>
          <p class="sub">// semua baris bertanda ✓ membuktikan ekuivalensi berlaku</p>

          <div class="eval-vars">
            <div class="ev-group">
              <div class="ev-label">Nilai p</div>
              <button class="ev-toggle vT" id="evP" onclick="toggleEV('p')">T</button>
            </div>
            <div class="ev-group">
              <div class="ev-label">Nilai q</div>
              <button class="ev-toggle vT" id="evQ" onclick="toggleEV('q')">T</button>
            </div>
          </div>
          <div class="eval-result-grid" id="evalGrid"></div>
        </div>
      </div>
    </div>
    <div class="footer">
      <div class="footer-l">Martin Bernard, M.Pd · Matematika Diskrit</div>
      <div class="footer-r">EKUIVALENSI LOGIS · 2025</div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     PANEL 4 : TAUTOLOGI & KONTRADIKSI
══════════════════════════════════════════════ -->
<div class="panel" id="panel-tautologi">
  <div class="container">
    <div class="section">
      <div class="sec-row"><span class="sec-num">04 · TAUTOLOGI & KONTRADIKSI</span><div class="sec-line"></div></div>
      <h2>Bentuk Khusus Formula Logika</h2>
      <p class="sec-desc">// berkaitan erat dengan pembuktian ekuivalensi</p>

      <div class="tc-grid">
        <div class="tc-card taut">
          <div class="tc-icon">✓</div>
          <div class="tc-name">Tautologi</div>
          <div class="tc-def">Formula yang <strong>selalu bernilai Benar</strong> untuk semua kemungkinan nilai variabelnya. Digunakan untuk membuktikan ekuivalensi: P ≡ Q jika P ↔ Q adalah tautologi.</div>
          <div class="tc-example">Contoh: p ∨ ¬p ≡ T (selalu)</div>
        </div>
        <div class="tc-card cont">
          <div class="tc-icon">✗</div>
          <div class="tc-name">Kontradiksi</div>
          <div class="tc-def">Formula yang <strong>selalu bernilai Salah</strong> untuk semua kemungkinan nilai variabelnya. Kebalikan tautologi, sering ditulis sebagai ⊥.</div>
          <div class="tc-example">Contoh: p ∧ ¬p ≡ F (selalu)</div>
        </div>
      </div>

      <!-- Interactive verifier -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:14px;padding:32px;box-shadow:var(--shadow);margin-bottom:28px;">
        <div style="font-family:'DM Serif Display',serif;font-size:22px;margin-bottom:4px;">Tautologi Penting</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--ink3);margin-bottom:24px;">// klik untuk verifikasi tabel kebenaran</div>

        <div style="display:flex;flex-direction:column;gap:10px;" id="tautList"></div>
      </div>

      <div style="background:var(--card);border:1px solid var(--border);border-radius:14px;padding:32px;box-shadow:var(--shadow);">
        <div style="font-family:'DM Serif Display',serif;font-size:22px;margin-bottom:4px;">Kontradiksi Penting</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--ink3);margin-bottom:24px;">// klik untuk verifikasi tabel kebenaran</div>
        <div style="display:flex;flex-direction:column;gap:10px;" id="contList"></div>
      </div>
    </div>
    <div class="footer">
      <div class="footer-l">Martin Bernard, M.Pd · Matematika Diskrit</div>
      <div class="footer-r">EKUIVALENSI LOGIS · 2025</div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     PANEL 5 : LATIHAN QUIZ
══════════════════════════════════════════════ -->
<div class="panel" id="panel-latihan">
  <div class="container">
    <div class="section">
      <div class="sec-row"><span class="sec-num">05 · LATIHAN QUIZ</span><div class="sec-line"></div></div>
      <h2>Uji Pemahamanmu</h2>
      <p class="sec-desc">// 12 soal mencakup seluruh konsep ekuivalensi logis</p>
      <div class="quiz-wrap" id="quizWrap"></div>
      <div class="scoreboard" id="scoreboard">
        <div class="score-big" id="scoreBig">—</div>
        <div class="score-lbl">Skor Akhir</div>
        <div class="score-msg" id="scoreMsg"></div>
        <button class="retry-btn" onclick="retryQuiz()">↺ ULANGI LATIHAN</button>
      </div>
    </div>
    <div class="footer">
      <div class="footer-l">Martin Bernard, M.Pd · Matematika Diskrit</div>
      <div class="footer-r">EKUIVALENSI LOGIS · 2025</div>
    </div>
  </div>
</div>

<script>
// ═══════════════════════════════════════════════
//  UTILITIES
// ═══════════════════════════════════════════════
const T=true, F=false;

function evalF(name, p, q){
  const map = {
    'imp':         !p||q,
    'neg_p_or_q':  !p||q,
    'neg_imp':     p&&!q,
    'p_and_neg_q': p&&!q,
    'neg_p_and_q': !p&&!q,
    'neg_p_or_q2': !p&&!q,
    'neg_p_and_q2':!(p&&q),
    'neg_p_or_neg_q':!p||!q,
    'double_neg':  p,
    'p':           p,
    'q':           q,
    'contr_pos':   q||!p,
    'p_or_p':      p,
    'p_and_p':     p,
    'not_p':       !p,
    'not_q':       !q,
  };
  return map[name] ?? false;
}

const formulaLabel = {
  'imp':'p → q','neg_p_or_q':'¬p ∨ q','neg_imp':'¬(p → q)',
  'p_and_neg_q':'p ∧ ¬q','neg_p_and_q':'¬p ∧ ¬q','neg_p_or_q2':'¬(p ∨ q)',
  'neg_p_and_q2':'¬(p ∧ q)','neg_p_or_neg_q':'¬p ∨ ¬q',
  'double_neg':'¬¬p','p':'p','q':'q','contr_pos':'¬q → ¬p',
  'p_or_p':'p ∨ p','p_and_p':'p ∧ p','not_p':'¬p','not_q':'¬q',
};

const combo = [[T,T],[T,F],[F,T],[F,F]];
const tv = v => `<span class="tv-${v?'T':'F'}">${v?'T':'F'}</span>`;

// ═══════════════════════════════════════════════
//  TABS
// ═══════════════════════════════════════════════
function switchTab(name){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(t=>t.classList.remove('active'));
  document.getElementById('panel-'+name).classList.add('active');
  event.target.classList.add('active');
}

// ═══════════════════════════════════════════════
//  PANEL 1 : DE MORGAN TABLE
// ═══════════════════════════════════════════════
(function(){
  const tbody = document.getElementById('deMorganTable');
  combo.forEach(([p,q]) => {
    const pq=p&&q, neg_pq=!pq, negp=!p, negq=!q, negp_or_negq=negp||negq;
    const eq = neg_pq===negp_or_negq;
    tbody.innerHTML += `<tr>
      <td style="padding:8px 12px;text-align:center;">${tv(p)}</td>
      <td style="padding:8px 12px;text-align:center;">${tv(q)}</td>
      <td style="padding:8px 12px;text-align:center;">${tv(pq)}</td>
      <td style="padding:8px 12px;text-align:center;background:var(--eq-bg);">${tv(neg_pq)}</td>
      <td style="padding:8px 12px;text-align:center;">${tv(negp)}</td>
      <td style="padding:8px 12px;text-align:center;">${tv(negq)}</td>
      <td style="padding:8px 12px;text-align:center;background:var(--eq-bg);">${tv(negp_or_negq)}</td>
      <td style="padding:8px 12px;text-align:center;background:var(--taut-bg);"><span class="tv-eq">${eq?'≡✓':'≢✗'}</span></td>
    </tr>`;
  });
})();

// ═══════════════════════════════════════════════
//  PANEL 2 : LAW CARDS
// ═══════════════════════════════════════════════
const laws = [
  { name:'Hukum De Morgan 1', formula:'¬(p ∧ q) ≡ ¬p ∨ ¬q', desc:'Negasi konjungsi sama dengan disjungsi negasi.',
    headers:['p','q','¬(p∧q)','¬p∨¬q'],
    rows: combo.map(([p,q])=>[p,q,!(p&&q),!p||!q]) },
  { name:'Hukum De Morgan 2', formula:'¬(p ∨ q) ≡ ¬p ∧ ¬q', desc:'Negasi disjungsi sama dengan konjungsi negasi.',
    headers:['p','q','¬(p∨q)','¬p∧¬q'],
    rows: combo.map(([p,q])=>[p,q,!(p||q),!p&&!q]) },
  { name:'Implikasi → Disjungsi', formula:'p → q ≡ ¬p ∨ q', desc:'Implikasi dapat ditulis ulang sebagai disjungsi negasi anteseden.',
    headers:['p','q','p→q','¬p∨q'],
    rows: combo.map(([p,q])=>[p,q,!p||q,!p||q]) },
  { name:'Kontrapositif', formula:'p → q ≡ ¬q → ¬p', desc:'Implikasi ekuivalen dengan kontrapositifnya.',
    headers:['p','q','p→q','¬q→¬p'],
    rows: combo.map(([p,q])=>[p,q,!p||q,q||!p]) },
  { name:'Negasi Ganda', formula:'¬¬p ≡ p', desc:'Dua kali negasi mengembalikan nilai asli.',
    headers:['p','¬¬p'],
    rows: combo.map(([p,q])=>[p,p]) },
  { name:'Hukum Identitas ∧', formula:'p ∧ T ≡ p', desc:'Konjungsi dengan Tautologi menghasilkan p.',
    headers:['p','p∧T'],
    rows: combo.map(([p,q])=>[p,p&&true]) },
  { name:'Hukum Identitas ∨', formula:'p ∨ F ≡ p', desc:'Disjungsi dengan Kontradiksi menghasilkan p.',
    headers:['p','p∨F'],
    rows: combo.map(([p,q])=>[p,p||false]) },
  { name:'Hukum Dominasi ∨', formula:'p ∨ T ≡ T', desc:'Disjungsi dengan Tautologi selalu menghasilkan T.',
    headers:['p','p∨T'],
    rows: combo.map(([p,q])=>[p,true]) },
  { name:'Hukum Dominasi ∧', formula:'p ∧ F ≡ F', desc:'Konjungsi dengan Kontradiksi selalu menghasilkan F.',
    headers:['p','p∧F'],
    rows: combo.map(([p,q])=>[p,false]) },
  { name:'Hukum Idempoten ∨', formula:'p ∨ p ≡ p', desc:'Disjungsi proposisi dengan dirinya sendiri.',
    headers:['p','p∨p'],
    rows: combo.map(([p,q])=>[p,p||p]) },
  { name:'Hukum Idempoten ∧', formula:'p ∧ p ≡ p', desc:'Konjungsi proposisi dengan dirinya sendiri.',
    headers:['p','p∧p'],
    rows: combo.map(([p,q])=>[p,p&&p]) },
  { name:'Hukum Komutatif ∨', formula:'p ∨ q ≡ q ∨ p', desc:'Urutan disjungsi tidak mengubah hasil.',
    headers:['p','q','p∨q','q∨p'],
    rows: combo.map(([p,q])=>[p,q,p||q,q||p]) },
  { name:'Hukum Komutatif ∧', formula:'p ∧ q ≡ q ∧ p', desc:'Urutan konjungsi tidak mengubah hasil.',
    headers:['p','q','p∧q','q∧p'],
    rows: combo.map(([p,q])=>[p,q,p&&q,q&&p]) },
  { name:'Hukum Asosiatif ∨', formula:'(p∨q)∨r ≡ p∨(q∨r)', desc:'Pengelompokan disjungsi tidak mengubah hasil.',
    headers:['p','q','r','(p∨q)∨r','p∨(q∨r)'],
    rows:[[T,T,T],[T,T,F],[T,F,T],[T,F,F],[F,T,T],[F,T,F],[F,F,T],[F,F,F]].map(([p,q,r])=>[p,q,r,(p||q)||r,p||(q||r)]) },
  { name:'Hukum Asosiatif ∧', formula:'(p∧q)∧r ≡ p∧(q∧r)', desc:'Pengelompokan konjungsi tidak mengubah hasil.',
    headers:['p','q','r','(p∧q)∧r','p∧(q∧r)'],
    rows:[[T,T,T],[T,T,F],[T,F,T],[T,F,F],[F,T,T],[F,T,F],[F,F,T],[F,F,F]].map(([p,q,r])=>[p,q,r,(p&&q)&&r,p&&(q&&r)]) },
  { name:'Hukum Distribusi 1', formula:'p∧(q∨r) ≡ (p∧q)∨(p∧r)', desc:'Distribusi konjungsi atas disjungsi.',
    headers:['p','q','r','p∧(q∨r)','(p∧q)∨(p∧r)'],
    rows:[[T,T,T],[T,T,F],[T,F,T],[T,F,F],[F,T,T],[F,T,F],[F,F,T],[F,F,F]].map(([p,q,r])=>[p,q,r,p&&(q||r),(p&&q)||(p&&r)]) },
  { name:'Hukum Distribusi 2', formula:'p∨(q∧r) ≡ (p∨q)∧(p∨r)', desc:'Distribusi disjungsi atas konjungsi.',
    headers:['p','q','r','p∨(q∧r)','(p∨q)∧(p∨r)'],
    rows:[[T,T,T],[T,T,F],[T,F,T],[T,F,F],[F,T,T],[F,T,F],[F,F,T],[F,F,F]].map(([p,q,r])=>[p,q,r,p||(q&&r),(p||q)&&(p||r)]) },
  { name:'Hukum Penyerapan ∨', formula:'p ∨ (p ∧ q) ≡ p', desc:'Disjungsi menyerap konjungsi.',
    headers:['p','q','p∨(p∧q)'],
    rows: combo.map(([p,q])=>[p,q,p||(p&&q)]) },
  { name:'Hukum Penyerapan ∧', formula:'p ∧ (p ∨ q) ≡ p', desc:'Konjungsi menyerap disjungsi.',
    headers:['p','q','p∧(p∨q)'],
    rows: combo.map(([p,q])=>[p,q,p&&(p||q)]) },
  { name:'Hukum Komplemen', formula:'p ∨ ¬p ≡ T', desc:'Disjungsi proposisi dengan negasinya selalu Benar (Tautologi).',
    headers:['p','¬p','p∨¬p'],
    rows: combo.map(([p,q])=>[p,!p,true]) },
];

const lawGrid = document.getElementById('lawGrid');
laws.forEach((law, i) => {
  const card = document.createElement('div');
  card.className = 'law-card';
  card.id = `law-${i}`;

  const ttId = `ltt-${i}`;
  const verId = `lver-${i}`;
  const isEq = (r) => r[r.length-2] === r[r.length-1];
  const allEq = law.rows.every(r => r[r.length-2] === r[r.length-1]);

  card.innerHTML = `
    <div class="law-name">${law.name}</div>
    <div class="law-formula">${law.formula}</div>
    <div class="law-desc">${law.desc}</div>
    <div class="law-body">
      <button class="law-verify" id="${verId}" onclick="toggleLawTT(${i})">▶ Tampilkan Tabel Kebenaran</button>
      <div class="law-tt" id="${ttId}">
        <table>
          <thead><tr>${law.headers.map((h,hi) => {
            const isLast2 = hi >= law.headers.length-2;
            const color = isLast2 ? 'var(--eq)' : 'var(--ink3)';
            const bg = isLast2 ? 'background:var(--eq-bg);' : '';
            return `<th style="color:${color};${bg}">${h}</th>`;
          }).join('')}</tr></thead>
          <tbody>
            ${law.rows.map(r => `<tr>${r.map((c,ci) => {
              const isLast2 = ci >= r.length-2;
              const bg = isLast2 ? 'background:rgba(192,92,20,0.04);' : '';
              return `<td style="${bg}">${typeof c==='boolean'?tv(c):tv(c)}</td>`;
            }).join('')}</tr>`).join('')}
            <tr><td colspan="${law.headers.length}" style="padding:8px 8px 4px;font-family:'IBM Plex Mono',monospace;font-size:10px;color:${allEq?'var(--taut)':'var(--cont)'};">
              ${allEq ? '✓ Semua baris identik → TERBUKTI EKUIVALEN' : '✗ Ada baris berbeda → TIDAK EKUIVALEN'}
            </td></tr>
          </tbody>
        </table>
      </div>
    </div>
  `;
  card.querySelector('.law-name').onclick = () => toggleLaw(i);
  card.querySelector('.law-formula').onclick = () => toggleLaw(i);
  card.querySelector('.law-desc').onclick = () => toggleLaw(i);
  lawGrid.appendChild(card);
});

function toggleLaw(i){
  document.getElementById(`law-${i}`).classList.toggle('expanded');
}
function toggleLawTT(i){
  const tt = document.getElementById(`ltt-${i}`);
  const btn = document.getElementById(`lver-${i}`);
  const show = !tt.classList.contains('show');
  tt.classList.toggle('show', show);
  btn.textContent = show ? '▼ Sembunyikan Tabel' : '▶ Tampilkan Tabel Kebenaran';
}

// ═══════════════════════════════════════════════
//  PANEL 3 : PROOF CHECKER
// ═══════════════════════════════════════════════
function runChecker(){
  const left  = document.getElementById('fLeft').value;
  const right = document.getElementById('fRight').value;
  const lbl_l = formulaLabel[left]  || left;
  const lbl_r = formulaLabel[right] || right;

  const results = combo.map(([p,q]) => {
    const vl = evalF(left,p,q);
    const vr = evalF(right,p,q);
    return { p, q, vl, vr, eq: vl===vr };
  });
  const allEq = results.every(r=>r.eq);

  const res = document.getElementById('checkerResult');
  res.className = `checker-result show`;

  let html = `<div class="cr-header ${allEq?'equiv':'nonequiv'}">
    <span class="cr-icon">${allEq?'✓':'✗'}</span>
    <span>${lbl_l} ${allEq?'≡':'≢'} ${lbl_r} — ${allEq?'TERBUKTI EKUIVALEN':'TIDAK EKUIVALEN'}</span>
  </div>
  <div class="cr-table">
    <table>
      <thead><tr>
        <th>p</th><th>q</th>
        <th style="background:var(--eq-bg);color:var(--eq);">${lbl_l}</th>
        <th style="background:var(--eq-bg);color:var(--eq);">${lbl_r}</th>
        <th style="background:var(--taut-bg);color:var(--taut);">Sama?</th>
      </tr></thead>
      <tbody>
        ${results.map(r=>`<tr>
          <td>${tv(r.p)}</td><td>${tv(r.q)}</td>
          <td style="background:rgba(192,92,20,0.04);">${tv(r.vl)}</td>
          <td style="background:rgba(192,92,20,0.04);">${tv(r.vr)}</td>
          <td style="background:var(--taut-bg);">${r.eq?`<span style="color:var(--t);font-weight:700;">✓</span>`:`<span style="color:var(--f);font-weight:700;">✗</span>`}</td>
        </tr>`).join('')}
      </tbody>
    </table>
  </div>`;
  res.innerHTML = html;
}

// ─── EVALUATOR DINAMIS ───
let evP=true, evQ=true;
const evalPairs = [
  { lbl:'p → q', a:'imp', b:'neg_p_or_q' },
  { lbl:'p → q (Kontrapositif)', a:'imp', b:'contr_pos' },
  { lbl:'¬(p ∧ q) ≡ ¬p ∨ ¬q', a:'neg_p_and_q2', b:'neg_p_or_neg_q' },
  { lbl:'¬(p ∨ q) ≡ ¬p ∧ ¬q', a:'neg_p_or_q2', b:'neg_p_and_q' },
  { lbl:'¬(p → q) ≡ p ∧ ¬q', a:'neg_imp', b:'p_and_neg_q' },
  { lbl:'p ∨ p ≡ p', a:'p_or_p', b:'p' },
  { lbl:'p ∧ p ≡ p', a:'p_and_p', b:'p' },
  { lbl:'¬¬p ≡ p', a:'double_neg', b:'p' },
];

function toggleEV(v){
  if(v==='p'){ evP=!evP; const b=document.getElementById('evP'); b.textContent=evP?'T':'F'; b.className='ev-toggle '+(evP?'vT':'vF'); }
  else        { evQ=!evQ; const b=document.getElementById('evQ'); b.textContent=evQ?'T':'F'; b.className='ev-toggle '+(evQ?'vT':'vF'); }
  renderEval();
}

function renderEval(){
  const grid = document.getElementById('evalGrid');
  grid.innerHTML = evalPairs.map(ep => {
    const vl = evalF(ep.a, evP, evQ);
    const vr = evalF(ep.b, evP, evQ);
    const eq = vl===vr;
    return `<div class="eval-row">
      <span class="eval-formula">${ep.lbl}</span>
      <span class="eval-val ${vl?'T':'F'}">${vl?'T':'F'}</span>
      <span style="color:var(--ink3);font-family:'IBM Plex Mono',monospace;font-size:12px;">≡?</span>
      <span class="eval-val ${vr?'T':'F'}">${vr?'T':'F'}</span>
      <span class="equiv-badge ${eq?'yes':'no'}">${eq?'≡ ✓':'≢ ✗'}</span>
    </div>`;
  }).join('');
}
renderEval();

// ═══════════════════════════════════════════════
//  PANEL 4 : TAUTOLOGY & CONTRADICTION
// ═══════════════════════════════════════════════
const tautItems = [
  { f:'p ∨ ¬p', fn:(p,q)=>p||!p },
  { f:'p → p', fn:(p,q)=>!p||p },
  { f:'(p → q) ∨ (q → p)', fn:(p,q)=>(!p||q)||(!q||p) },
  { f:'¬(p ∧ ¬p)', fn:(p,q)=>!(p&&!p) },
  { f:'(p ∧ q) → p', fn:(p,q)=>!(p&&q)||p },
  { f:'p → (p ∨ q)', fn:(p,q)=>!p||(p||q) },
];
const contItems = [
  { f:'p ∧ ¬p', fn:(p,q)=>p&&!p },
  { f:'¬(p ∨ ¬p)', fn:(p,q)=>!(p||!p) },
  { f:'(p → q) ∧ p ∧ ¬q', fn:(p,q)=>(!p||q)&&p&&!q },
  { f:'p ∧ ¬p ∧ q', fn:(p,q)=>p&&!p&&q },
];

function buildSpecialList(items, containerId, type){
  const container = document.getElementById(containerId);
  items.forEach((item, i) => {
    const row = document.createElement('div');
    row.style.cssText = `background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px 20px;cursor:pointer;transition:border-color 0.15s;`;
    row.id = `spec-${containerId}-${i}`;
    const ttId = `sptt-${containerId}-${i}`;
    const vals = combo.map(([p,q]) => item.fn(p,q));
    const allSame = vals.every(v => v===vals[0]);
    const verdict = type==='taut' ? vals.every(v=>v===true) : vals.every(v=>v===false);

    row.innerHTML = `
      <div style="display:flex;align-items:center;gap:12px;">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:15px;font-weight:600;color:${type==='taut'?'var(--taut)':'var(--cont)'};">${item.f}</span>
        <span style="font-family:'IBM Plex Mono',monospace;font-size:10px;padding:3px 10px;border-radius:4px;background:${verdict?(type==='taut'?'var(--taut-bg)':'var(--cont-bg)'):'var(--f-bg)'};color:${verdict?(type==='taut'?'var(--taut)':'var(--cont)'):'var(--f)'};">${verdict?'✓ TERBUKTI':'✗ TIDAK'}</span>
        <span style="margin-left:auto;font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--ink3);" class="spec-toggle-${containerId}-${i}">▾ lihat</span>
      </div>
      <div id="${ttId}" style="display:none;margin-top:14px;overflow-x:auto;">
        <table style="border-collapse:collapse;font-family:'IBM Plex Mono',monospace;font-size:12px;width:100%;">
          <thead><tr>
            <th style="padding:6px 10px;color:var(--ink3);font-size:9px;letter-spacing:2px;border-bottom:1px solid var(--border);text-align:center;">p</th>
            <th style="padding:6px 10px;color:var(--ink3);font-size:9px;letter-spacing:2px;border-bottom:1px solid var(--border);text-align:center;">q</th>
            <th style="padding:6px 10px;color:${type==='taut'?'var(--taut)':'var(--cont)'};font-size:9px;letter-spacing:2px;border-bottom:1px solid var(--border);text-align:center;background:${type==='taut'?'var(--taut-bg)':'var(--cont-bg)'};">${item.f}</th>
          </tr></thead>
          <tbody>
            ${combo.map(([p,q]) => {
              const v = item.fn(p,q);
              return `<tr><td style="padding:6px 10px;text-align:center;">${tv(p)}</td><td style="padding:6px 10px;text-align:center;">${tv(q)}</td><td style="padding:6px 10px;text-align:center;background:${type==='taut'?'var(--taut-bg)':'var(--cont-bg)'};">${tv(v)}</td></tr>`;
            }).join('')}
          </tbody>
        </table>
      </div>`;

    row.onclick = () => {
      const tt = document.getElementById(ttId);
      const open = tt.style.display==='none';
      tt.style.display = open ? 'block' : 'none';
      row.querySelector(`.spec-toggle-${containerId}-${i}`).textContent = open ? '▴ tutup' : '▾ lihat';
      row.style.borderColor = open ? (type==='taut'?'rgba(26,107,60,0.3)':'rgba(160,28,44,0.3)') : 'var(--border)';
    };
    container.appendChild(row);
  });
}

buildSpecialList(tautItems, 'tautList', 'taut');
buildSpecialList(contItems, 'contList', 'cont');

// ═══════════════════════════════════════════════
//  PANEL 5 : QUIZ
// ═══════════════════════════════════════════════
const questions = [
  { q:'Dua formula dikatakan ekuivalen logis jika…', expr:'P ≡ Q',
    opts:['Keduanya selalu bernilai T', 'Nilai kebenaran keduanya selalu identik untuk semua kombinasi variabel', 'Salah satunya adalah tautologi'],
    ans:1, ex:'P ≡ Q berarti untuk setiap baris di tabel kebenaran, nilai P dan Q selalu sama.' },
  { q:'Manakah ekuivalensi yang benar (Hukum De Morgan)?', expr:'¬(p ∧ q)',
    opts:['≡ ¬p ∧ ¬q', '≡ ¬p ∨ ¬q', '≡ p ∨ q'],
    ans:1, ex:'Hukum De Morgan 1: ¬(p ∧ q) ≡ ¬p ∨ ¬q. Negasi konjungsi = disjungsi negasi.' },
  { q:'Implikasi p → q ekuivalen dengan…', expr:'p → q',
    opts:['p ∧ ¬q', '¬p ∨ q', '¬p ∧ q'],
    ans:1, ex:'p → q ≡ ¬p ∨ q. Ini adalah cara standar menulis ulang implikasi.' },
  { q:'Kontrapositif dari p → q adalah…', expr:'p → q',
    opts:['q → p', '¬p → ¬q', '¬q → ¬p'],
    ans:2, ex:'Kontrapositif membalik dan meniadakan: p → q ≡ ¬q → ¬p.' },
  { q:'Jika p=T dan q=F, apakah ¬(p ∧ q) ≡ ¬p ∨ ¬q?', expr:'p=T, q=F',
    opts:['Ya, keduanya bernilai T', 'Ya, keduanya bernilai F', 'Tidak, nilainya berbeda'],
    ans:0, ex:'¬(T∧F)=¬F=T. ¬T∨¬F=F∨T=T. Keduanya T → terbukti ekuivalen pada baris ini.' },
  { q:'Formula p ∨ ¬p disebut…', expr:'p ∨ ¬p',
    opts:['Kontradiksi', 'Tautologi', 'Ekuivalensi'],
    ans:1, ex:'p ∨ ¬p selalu bernilai T untuk semua nilai p → ini adalah Tautologi.' },
  { q:'Formula p ∧ ¬p disebut…', expr:'p ∧ ¬p',
    opts:['Tautologi', 'Kontradiksi', 'Proposisi biasa'],
    ans:1, ex:'p ∧ ¬p selalu bernilai F untuk semua nilai p → ini adalah Kontradiksi.' },
  { q:'Hukum Idempoten menyatakan…', expr:'p ∨ p',
    opts:['p ∨ p ≡ T', 'p ∨ p ≡ F', 'p ∨ p ≡ p'],
    ans:2, ex:'Hukum Idempoten: p ∨ p ≡ p dan p ∧ p ≡ p.' },
  { q:'Manakah pernyataan yang benar tentang ekuivalensi?', expr:'P ≡ Q ⟺',
    opts:['P ↔ Q adalah kontradiksi', 'P ↔ Q adalah tautologi', 'P → Q adalah tautologi'],
    ans:1, ex:'Definisi: P ≡ Q jika dan hanya jika P ↔ Q merupakan tautologi (selalu T).' },
  { q:'¬(p → q) ekuivalen dengan…', expr:'¬(p → q)',
    opts:['¬p ∨ q', 'p ∧ ¬q', '¬p ∧ ¬q'],
    ans:1, ex:'¬(p → q) = ¬(¬p ∨ q) = p ∧ ¬q. Negasi implikasi = anteseden benar DAN konsekuen salah.' },
  { q:'Hukum Distribusi mana yang benar?', expr:'p ∧ (q ∨ r)',
    opts:['≡ (p ∧ q) ∧ (p ∧ r)', '≡ (p ∧ q) ∨ (p ∧ r)', '≡ (p ∨ q) ∧ (p ∨ r)'],
    ans:1, ex:'Distribusi ∧ atas ∨: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r).' },
  { q:'Hukum Penyerapan (Absorption Law) menyatakan…', expr:'p ∨ (p ∧ q)',
    opts:['≡ q', '≡ p ∧ q', '≡ p'],
    ans:2, ex:'Hukum Penyerapan: p ∨ (p ∧ q) ≡ p. Variabel p "menyerap" p ∧ q.' },
];

let qAnswers = new Array(questions.length).fill(null);
let qAnswered = 0;
const keys = ['A','B','C'];

function buildQuiz(){
  const wrap = document.getElementById('quizWrap');
  wrap.innerHTML = '';
  qAnswers = new Array(questions.length).fill(null);
  qAnswered = 0;
  updateProgress(0);
  document.getElementById('scoreboard').classList.remove('show');

  questions.forEach((q,qi) => {
    const card = document.createElement('div');
    card.className = 'quiz-card'; card.id = `qc-${qi}`;
    card.innerHTML = `
      <div class="quiz-num">SOAL ${String(qi+1).padStart(2,'0')} / ${questions.length}</div>
      <div class="quiz-q">${q.q}</div>
      <div class="quiz-expr">${q.expr}</div>
      <div class="options">
        ${q.opts.map((o,oi) => `
          <button class="opt-btn" onclick="pick(${qi},${oi})" id="opt-${qi}-${oi}">
            <span class="opt-key">${keys[oi]}</span>${o}
          </button>`).join('')}
      </div>
      <div class="feedback" id="fb-${qi}"></div>`;
    wrap.appendChild(card);
  });
}

function pick(qi,oi){
  if(qAnswers[qi]!==null) return;
  qAnswers[qi]=oi; qAnswered++;
  const q=questions[qi]; const correct=oi===q.ans;
  for(let i=0;i<q.opts.length;i++){
    const b=document.getElementById(`opt-${qi}-${i}`);
    b.disabled=true;
    if(i===q.ans) b.classList.add('correct');
    else if(i===oi) b.classList.add('wrong');
  }
  const fb=document.getElementById(`fb-${qi}`);
  fb.className=`feedback show ${correct?'ok':'err'}`;
  fb.textContent=(correct?'✓ Benar! ':'✗ Belum tepat. ')+q.ex;
  document.getElementById(`qc-${qi}`).style.borderColor=correct?'var(--t)':'var(--f)';
  updateProgress(qAnswered);
  if(qAnswered===questions.length) setTimeout(showScore,700);
}

function updateProgress(n){
  const pct=(n/questions.length)*100;
  document.getElementById('tpFill').style.width=pct+'%';
  document.getElementById('tpScore').textContent=`${n}/${questions.length}`;
}

function showScore(){
  const correct=qAnswers.filter((a,i)=>a===questions[i].ans).length;
  const pct=Math.round((correct/questions.length)*100);
  document.getElementById('scoreBig').textContent=`${pct}%`;
  const msgs=[
    [90,'Luar biasa! Kamu menguasai ekuivalensi logis dengan sangat baik.'],
    [75,'Bagus! Pemahaman ekuivalensimu sudah kuat. Sedikit lagi sempurna!'],
    [50,'Cukup baik! Fokus pada hukum De Morgan dan kontrapositif.'],
    [0, 'Jangan menyerah! Baca ulang hukum-hukum ekuivalensi dan coba lagi.'],
  ];
  document.getElementById('scoreMsg').textContent=msgs.find(([t])=>pct>=t)[1];
  const sb=document.getElementById('scoreboard');
  sb.classList.add('show');
  sb.scrollIntoView({behavior:'smooth',block:'center'});
}

function retryQuiz(){
  buildQuiz();
  document.getElementById('quizWrap').scrollIntoView({behavior:'smooth'});
}

buildQuiz();
</script>
</body>
</html>
        """
        tampilkan4 = keterangan(tulisanHTML3,6000)
        tampilkan4.tampilkan()

    with bagian[3]:
        tulisanHTML4="""
        <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>20 Soal Pembuktian Ekuivalensi Logis</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,600;0,900;1,300;1,600&family=IBM+Plex+Mono:wght@300;400;500;600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --bg:       #0c0d11;
  --bg2:      #111318;
  --bg3:      #181a22;
  --card:     #1c1f28;
  --card2:    #222535;
  --border:   rgba(255,255,255,0.07);
  --border2:  rgba(255,255,255,0.12);
  --ink:      #e8eaf2;
  --ink2:     #9aa0bb;
  --ink3:     #565c7a;

  --gold:     #e8a830;
  --gold-bg:  rgba(232,168,48,0.1);
  --gold-b:   rgba(232,168,48,0.25);

  --t:        #34d399;  --t-bg: rgba(52,211,153,0.1);  --t-b: rgba(52,211,153,0.25);
  --f:        #f87171;  --f-bg: rgba(248,113,113,0.1); --f-b: rgba(248,113,113,0.25);
  --blue:     #60a5fa;  --blue-bg: rgba(96,165,250,0.1);
  --purple:   #a78bfa;  --purple-bg: rgba(167,139,250,0.1);

  --easy:     #34d399;  --easy-bg: rgba(52,211,153,0.08);
  --med:      #fbbf24;  --med-bg:  rgba(251,191,36,0.08);
  --hard:     #f87171;  --hard-bg: rgba(248,113,113,0.08);

  --shadow:   0 8px 32px rgba(0,0,0,0.5);
  --shadow2:  0 2px 12px rgba(0,0,0,0.4);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--ink); font-family: 'Plus Jakarta Sans', sans-serif; min-height: 100vh; }

/* ── HEADER ── */
.header {
  position: sticky; top: 0; z-index: 200;
  background: rgba(12,13,17,0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  padding: 0 32px;
  display: flex; align-items: center; justify-content: space-between;
  height: 56px;
}
.h-brand { font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; color: var(--ink3); }
.h-brand span { color: var(--gold); }
.h-stats { display: flex; align-items: center; gap: 20px; }
.h-stat { text-align: center; }
.h-stat-val { font-family: 'IBM Plex Mono', monospace; font-size: 15px; font-weight: 600; }
.h-stat-lbl { font-family: 'IBM Plex Mono', monospace; font-size: 8px; letter-spacing: 2px; color: var(--ink3); text-transform: uppercase; }
.h-stat.correct .h-stat-val { color: var(--t); }
.h-stat.wrong   .h-stat-val { color: var(--f); }
.h-stat.score   .h-stat-val { color: var(--gold); }
.h-divider { width: 1px; height: 28px; background: var(--border); }

/* Progress ring */
.progress-ring-wrap { position: relative; width: 40px; height: 40px; }
.progress-ring { transform: rotate(-90deg); }
.ring-bg  { fill: none; stroke: rgba(255,255,255,0.05); stroke-width: 3; }
.ring-fill { fill: none; stroke: var(--gold); stroke-width: 3; stroke-linecap: round;
  stroke-dasharray: 100; stroke-dashoffset: 100; transition: stroke-dashoffset 0.5s ease; }
.ring-text {
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: 'IBM Plex Mono', monospace; font-size: 10px; font-weight: 600; color: var(--gold);
}

/* ── HERO ── */
.hero {
  padding: 60px 32px 48px;
  position: relative; overflow: hidden;
  border-bottom: 1px solid var(--border);
}
.hero-bg {
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 80% 100% at 20% 0%, rgba(232,168,48,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 60% 80% at 80% 100%, rgba(96,165,250,0.05) 0%, transparent 60%);
}
.hero-grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 40px 40px;
}
.container { max-width: 900px; margin: 0 auto; padding: 0 24px; position: relative; z-index: 1; }
.hero-tag {
  font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 4px;
  text-transform: uppercase; color: var(--gold); margin-bottom: 16px;
  display: flex; align-items: center; gap: 10px;
}
.hero-tag::before { content: ''; display: inline-block; width: 20px; height: 1px; background: var(--gold); opacity: 0.6; }
.hero h1 {
  font-family: 'Fraunces', serif; font-size: clamp(38px,6vw,64px); font-weight: 900;
  line-height: 1.05; letter-spacing: -1px; margin-bottom: 14px;
  color: var(--ink);
}
.hero h1 em { color: var(--gold); font-style: italic; }
.hero-sub { font-family: 'IBM Plex Mono', monospace; font-size: 12px; color: var(--ink3); letter-spacing: 1px; margin-bottom: 32px; }

.level-chips { display: flex; gap: 10px; flex-wrap: wrap; }
.lchip {
  font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 1.5px;
  padding: 6px 14px; border-radius: 20px; border: 1px solid; cursor: pointer;
  transition: all 0.2s; text-transform: uppercase;
}
.lchip.easy  { color: var(--easy); border-color: rgba(52,211,153,0.3); background: var(--easy-bg); }
.lchip.med   { color: var(--med);  border-color: rgba(251,191,36,0.3); background: var(--med-bg);  }
.lchip.hard  { color: var(--hard); border-color: rgba(248,113,113,0.3); background: var(--hard-bg); }
.lchip.all   { color: var(--ink2); border-color: var(--border2); background: rgba(255,255,255,0.03); }
.lchip.active { transform: scale(1.05); box-shadow: 0 0 16px currentColor; opacity: 1; }

/* ── MAIN LAYOUT ── */
.main { padding: 40px 0; }

/* ── QUESTION CARD ── */
.q-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px;
  margin-bottom: 20px;
  overflow: hidden;
  box-shadow: var(--shadow2);
  transition: border-color 0.3s, box-shadow 0.3s;
  animation: fadeIn 0.3s ease both;
}
@keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:translateY(0); } }

.q-card.answered-correct { border-color: var(--t-b); box-shadow: 0 0 0 1px var(--t-b), var(--shadow2); }
.q-card.answered-wrong   { border-color: var(--f-b); box-shadow: 0 0 0 1px var(--f-b), var(--shadow2); }

.q-head {
  padding: 20px 24px 0;
  display: flex; align-items: flex-start; gap: 14px;
}

.q-num {
  font-family: 'IBM Plex Mono', monospace; font-size: 11px; font-weight: 600;
  width: 32px; height: 32px; border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  background: rgba(255,255,255,0.04); color: var(--ink3); flex-shrink: 0;
  border: 1px solid var(--border);
}
.q-card.answered-correct .q-num { background: var(--t-bg); color: var(--t); border-color: var(--t-b); }
.q-card.answered-wrong   .q-num { background: var(--f-bg); color: var(--f); border-color: var(--f-b); }

.q-meta { flex: 1; }
.q-tags { display: flex; gap: 8px; margin-bottom: 8px; flex-wrap: wrap; align-items: center; }

.q-level {
  font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: 2px;
  padding: 3px 9px; border-radius: 4px; text-transform: uppercase;
}
.lvl-easy { background: var(--easy-bg); color: var(--easy); border: 1px solid rgba(52,211,153,0.2); }
.lvl-med  { background: var(--med-bg);  color: var(--med);  border: 1px solid rgba(251,191,36,0.2); }
.lvl-hard { background: var(--hard-bg); color: var(--hard); border: 1px solid rgba(248,113,113,0.2); }

.q-topic {
  font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: 1.5px;
  padding: 3px 9px; border-radius: 4px; text-transform: uppercase;
  background: rgba(255,255,255,0.03); color: var(--ink3); border: 1px solid var(--border);
}

.q-pts {
  font-family: 'IBM Plex Mono', monospace; font-size: 9px;
  color: var(--gold); margin-left: auto;
}

.q-instruction { font-size: 13px; color: var(--ink2); line-height: 1.6; }

/* Expression box */
.q-expr-wrap { padding: 16px 24px; }
.q-expr {
  font-family: 'IBM Plex Mono', monospace; font-size: 18px; font-weight: 600;
  background: var(--bg3); border: 1px solid var(--border2);
  border-radius: 10px; padding: 14px 20px; letter-spacing: 1.5px;
  color: var(--gold); display: flex; align-items: center; gap: 12px;
  flex-wrap: wrap;
}
.eq-sym { color: var(--blue); font-size: 22px; margin: 0 4px; }

/* Proof type: Truth Table */
.q-body { padding: 0 24px 24px; }

/* ── STEP-BY-STEP PROOF ── */
.proof-steps { display: flex; flex-direction: column; gap: 0; margin-bottom: 16px; }
.step-row {
  display: grid; align-items: center;
  gap: 0; border-bottom: 1px solid var(--border);
}
.step-row:last-child { border-bottom: none; }
.step-row.header-row { background: var(--bg3); border-radius: 8px 8px 0 0; }

.step-cell {
  padding: 10px 14px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px;
}
.cell-num   { color: var(--ink3); font-size: 10px; }
.cell-expr  { color: var(--ink); font-weight: 500; letter-spacing: 0.5px; }
.cell-rule  { color: var(--blue); font-size: 11px; }
.cell-head  { color: var(--ink3); font-size: 9px; letter-spacing: 2px; text-transform: uppercase; }

/* Drag & Drop steps */
.sortable-steps { list-style: none; margin-bottom: 14px; }
.sortable-step {
  display: grid; align-items: center;
  gap: 0;
  background: var(--card2); border: 1px solid var(--border);
  border-radius: 8px; margin-bottom: 8px;
  cursor: grab; transition: background 0.15s, border-color 0.15s, transform 0.1s;
  user-select: none;
}
.sortable-step:active { cursor: grabbing; }
.sortable-step.dragging { opacity: 0.4; transform: scale(0.98); }
.sortable-step.drag-over { border-color: var(--gold); background: var(--gold-bg); }
.drag-handle {
  padding: 12px 10px;
  color: var(--ink3); font-size: 14px; text-align: center;
  cursor: grab;
}
.step-num-cell { padding: 12px 8px; font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: var(--ink3); }
.step-expr-cell { padding: 12px 14px; font-family: 'IBM Plex Mono', monospace; font-size: 13px; color: var(--ink); font-weight: 500; }
.step-rule-cell { padding: 12px 14px; font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--blue); }

/* Multiple choice */
.mc-options { display: flex; flex-direction: column; gap: 8px; margin-bottom: 14px; }
.mc-opt {
  display: flex; align-items: flex-start; gap: 12px;
  padding: 12px 16px; border: 1.5px solid var(--border);
  border-radius: 8px; background: rgba(255,255,255,0.02);
  cursor: pointer; font-size: 13px; color: var(--ink2);
  transition: all 0.15s; text-align: left;
  font-family: 'IBM Plex Mono', monospace; font-size: 13px;
}
.mc-opt:hover:not(:disabled) { border-color: var(--gold-b); background: var(--gold-bg); color: var(--ink); }
.mc-opt .opt-k {
  font-size: 10px; font-weight: 700; min-width: 22px; height: 22px;
  border-radius: 4px; display: flex; align-items: center; justify-content: center;
  background: var(--border); color: var(--ink3); flex-shrink: 0;
}
.mc-opt.correct { border-color: var(--t-b); background: var(--t-bg); color: var(--t); }
.mc-opt.correct .opt-k { background: var(--t); color: #000; }
.mc-opt.wrong   { border-color: var(--f-b); background: var(--f-bg); color: var(--f); }
.mc-opt.wrong   .opt-k { background: var(--f); color: #fff; }
.mc-opt:disabled { cursor: default; }

/* Fill blank */
.fill-wrap { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 14px; }
.fill-expr { font-family: 'IBM Plex Mono', monospace; font-size: 15px; color: var(--ink); letter-spacing: 1px; }
.fill-blank {
  font-family: 'IBM Plex Mono', monospace; font-size: 14px;
  padding: 8px 14px; background: var(--bg3);
  border: 1.5px solid var(--border2); border-radius: 6px;
  color: var(--ink); outline: none; width: 160px;
  transition: border-color 0.2s;
}
.fill-blank:focus { border-color: var(--gold); }
.fill-blank.correct { border-color: var(--t); background: var(--t-bg); color: var(--t); }
.fill-blank.wrong   { border-color: var(--f); background: var(--f-bg); color: var(--f); }

/* Truth table builder in question */
.tt-q { overflow-x: auto; margin-bottom: 14px; }
.tt-q table { border-collapse: collapse; font-family: 'IBM Plex Mono', monospace; font-size: 12px; }
.tt-q th {
  padding: 8px 14px; background: var(--bg3); color: var(--ink3);
  font-size: 9px; letter-spacing: 2px; text-align: center; border: 1px solid var(--border);
}
.tt-q th.target { color: var(--gold); background: var(--gold-bg); }
.tt-q td { padding: 8px 14px; text-align: center; border: 1px solid var(--border); }
.tv-T { color: var(--t); font-weight: 700; }
.tv-F { color: var(--f); font-weight: 700; }

.tt-blank-cell select {
  font-family: 'IBM Plex Mono', monospace; font-size: 13px; font-weight: 700;
  padding: 4px 10px; border-radius: 5px;
  background: var(--card2); border: 1px solid var(--border2); color: var(--ink);
  cursor: pointer;
}
.tt-blank-cell select.correct { background: var(--t-bg); color: var(--t); border-color: var(--t-b); }
.tt-blank-cell select.wrong   { background: var(--f-bg); color: var(--f); border-color: var(--f-b); }

/* Action buttons */
.q-actions { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.btn-check {
  font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 1.5px;
  padding: 10px 22px; background: var(--gold); color: #0c0d11;
  border: none; border-radius: 8px; cursor: pointer; font-weight: 700;
  transition: opacity 0.15s, transform 0.1s;
}
.btn-check:hover { opacity: 0.85; transform: scale(0.99); }
.btn-check:disabled { opacity: 0.4; cursor: default; transform: none; }

.btn-hint {
  font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 1.5px;
  padding: 10px 18px; background: transparent; color: var(--ink3);
  border: 1px solid var(--border2); border-radius: 8px; cursor: pointer;
  transition: color 0.15s, border-color 0.15s;
}
.btn-hint:hover { color: var(--gold); border-color: var(--gold-b); }

.btn-show {
  font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 1.5px;
  padding: 10px 18px; background: transparent; color: var(--purple);
  border: 1px solid rgba(167,139,250,0.25); border-radius: 8px; cursor: pointer;
  transition: background 0.15s;
}
.btn-show:hover { background: var(--purple-bg); }

/* Feedback */
.q-feedback {
  margin-top: 12px; font-family: 'IBM Plex Mono', monospace; font-size: 11px;
  border-radius: 8px; padding: 12px 16px; display: none; line-height: 1.7;
  animation: feedIn 0.2s ease;
}
@keyframes feedIn { from { opacity:0; transform:translateY(4px); } to { opacity:1; transform:translateY(0); } }
.q-feedback.show { display: block; }
.q-feedback.ok  { background: var(--t-bg);  color: var(--t);  border: 1px solid var(--t-b); }
.q-feedback.err { background: var(--f-bg);  color: var(--f);  border: 1px solid var(--f-b); }
.q-feedback.hint { background: var(--gold-bg); color: var(--gold); border: 1px solid var(--gold-b); }

/* Hint */
.hint-box { display: none; background: var(--gold-bg); border: 1px solid var(--gold-b); border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; }
.hint-box.show { display: block; animation: feedIn 0.2s ease; }
.hint-label { font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: 2px; text-transform: uppercase; color: var(--gold); margin-bottom: 4px; }
.hint-text { font-family: 'IBM Plex Mono', monospace; font-size: 12px; color: rgba(232,168,48,0.8); line-height: 1.6; }

/* Solution steps */
.solution-box { display: none; background: var(--bg3); border: 1px solid var(--border2); border-radius: 10px; padding: 16px; margin-bottom: 12px; }
.solution-box.show { display: block; animation: feedIn 0.2s ease; }
.sol-title { font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: 2px; color: var(--purple); text-transform: uppercase; margin-bottom: 10px; }
.sol-step { display: flex; gap: 12px; padding: 6px 0; border-bottom: 1px solid var(--border); font-family: 'IBM Plex Mono', monospace; font-size: 12px; }
.sol-step:last-child { border-bottom: none; }
.sol-n { color: var(--ink3); min-width: 20px; }
.sol-e { color: var(--ink); flex: 1; }
.sol-r { color: var(--blue); font-size: 11px; }

/* ── SCOREBOARD ── */
.scoreboard {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 16px; padding: 56px 40px;
  text-align: center; display: none;
  animation: fadeIn 0.4s ease; margin-top: 40px; box-shadow: var(--shadow);
}
.scoreboard.show { display: block; }

.score-circle {
  width: 140px; height: 140px; border-radius: 50%;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  margin: 0 auto 24px;
  background: conic-gradient(var(--gold) 0%, transparent 0%);
  position: relative;
}
.score-circle::before {
  content: '';
  position: absolute;
  inset: 8px; border-radius: 50%;
  background: var(--card);
}
.score-inner { position: relative; z-index: 1; text-align: center; }
.score-pct { font-family: 'Fraunces', serif; font-size: 48px; font-weight: 900; color: var(--gold); line-height: 1; }
.score-lbl { font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: 2px; color: var(--ink3); text-transform: uppercase; }

.score-breakdown {
  display: flex; justify-content: center; gap: 40px; margin: 24px 0 32px;
}
.sb-item { text-align: center; }
.sb-val { font-family: 'Fraunces', serif; font-size: 32px; font-weight: 900; line-height: 1; margin-bottom: 4px; }
.sb-val.c { color: var(--t); }
.sb-val.w { color: var(--f); }
.sb-val.p { color: var(--gold); }
.sb-lbl { font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: 2px; color: var(--ink3); text-transform: uppercase; }

.score-grade {
  font-family: 'Fraunces', serif; font-size: 22px; font-style: italic;
  color: var(--ink2); margin-bottom: 32px; line-height: 1.5;
}

.retry-btn {
  font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 2px;
  padding: 13px 40px; background: var(--gold); color: #0c0d11;
  border: none; border-radius: 8px; cursor: pointer; font-weight: 700;
  transition: opacity 0.15s;
}
.retry-btn:hover { opacity: 0.85; }

/* Filter / jump bar */
.q-filter { padding: 24px 0 8px; display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
.f-lbl { font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: 2px; color: var(--ink3); text-transform: uppercase; }
.jump-grid { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 24px; }
.jump-btn {
  width: 32px; height: 32px; border-radius: 6px;
  font-family: 'IBM Plex Mono', monospace; font-size: 11px; font-weight: 600;
  border: 1px solid var(--border); background: rgba(255,255,255,0.02);
  color: var(--ink3); cursor: pointer; transition: all 0.15s;
  display: flex; align-items: center; justify-content: center;
}
.jump-btn:hover { border-color: var(--gold-b); color: var(--gold); }
.jump-btn.j-correct { background: var(--t-bg); border-color: var(--t-b); color: var(--t); }
.jump-btn.j-wrong   { background: var(--f-bg); border-color: var(--f-b); color: var(--f); }

/* Responsive */
@media(max-width:600px){
  .h-stats { gap: 10px; }
  .hero h1 { font-size: 36px; }
  .score-breakdown { gap: 20px; }
}
</style>
</head>
<body>

<!-- HEADER -->
<div class="header">
  <div class="h-brand">Ekuivalensi <span>Logis</span> · 20 Soal Pembuktian</div>
  <div class="h-stats">
    <div class="h-stat correct">
      <div class="h-stat-val" id="statC">0</div>
      <div class="h-stat-lbl">Benar</div>
    </div>
    <div class="h-divider"></div>
    <div class="h-stat wrong">
      <div class="h-stat-val" id="statW">0</div>
      <div class="h-stat-lbl">Salah</div>
    </div>
    <div class="h-divider"></div>
    <div class="h-stat score">
      <div class="h-stat-val" id="statS">0</div>
      <div class="h-stat-lbl">Poin</div>
    </div>
    <div class="h-divider"></div>
    <div class="progress-ring-wrap">
      <svg class="progress-ring" width="40" height="40" viewBox="0 0 40 40">
        <circle class="ring-bg" cx="20" cy="20" r="15"/>
        <circle class="ring-fill" cx="20" cy="20" r="15" id="ringFill"
          stroke-dasharray="94.2" stroke-dashoffset="94.2"/>
      </svg>
      <div class="ring-text" id="ringText">0%</div>
    </div>
  </div>
</div>

<!-- HERO -->
<div class="hero">
  <div class="hero-bg"></div>
  <div class="hero-grid"></div>
  <div class="container">
    <div class="hero-tag">Matematika Diskrit · Martin Bernard, M.Pd</div>
    <h1>20 Soal Pembuktian<br><em>Ekuivalensi Logis</em></h1>
    <p class="hero-sub">// logical_equivalence_exercises.js — pilih level, buktikan, kuasai</p>
    <div class="level-chips">
      <button class="lchip all active" onclick="filterLevel('all',this)">Semua (20)</button>
      <button class="lchip easy" onclick="filterLevel('easy',this)">● Mudah (7)</button>
      <button class="lchip med"  onclick="filterLevel('med',this)">● Sedang (8)</button>
      <button class="lchip hard" onclick="filterLevel('hard',this)">● Sulit (5)</button>
    </div>
  </div>
</div>

<div class="container">
  <!-- Jump nav -->
  <div class="q-filter">
    <span class="f-lbl">Lompat ke soal →</span>
  </div>
  <div class="jump-grid" id="jumpGrid"></div>

  <!-- Questions -->
  <div id="qContainer"></div>

  <!-- Scoreboard -->
  <div class="scoreboard" id="scoreboard">
    <div class="score-circle" id="scoreCircle">
      <div class="score-inner">
        <div class="score-pct" id="scorePct">—</div>
        <div class="score-lbl">skor</div>
      </div>
    </div>
    <div class="score-breakdown">
      <div class="sb-item"><div class="sb-val c" id="sbC">0</div><div class="sb-lbl">Benar</div></div>
      <div class="sb-item"><div class="sb-val w" id="sbW">0</div><div class="sb-lbl">Salah</div></div>
      <div class="sb-item"><div class="sb-val p" id="sbP">0</div><div class="sb-lbl">Poin</div></div>
    </div>
    <div class="score-grade" id="scoreGrade"></div>
    <button class="retry-btn" onclick="retryAll()">↺ ULANGI SEMUA SOAL</button>
  </div>

  <div style="height:60px;"></div>
</div>

<script>
// ═══════════════════════════ DATA ═══════════════════════════

const T=true,F=false;
const combo2=[[T,T],[T,F],[F,T],[F,F]];
const combo3=[[T,T,T],[T,T,F],[T,F,T],[T,F,F],[F,T,T],[F,T,F],[F,F,T],[F,F,F]];
const tv = v => `<span class="tv-${v?'T':'F'}">${v?'T':'F'}</span>`;

const questions = [
/* ─── MUDAH ─────────────────────────────────────────────── */
{
  id:1, level:'easy', topic:'De Morgan 1', pts:5,
  type:'mc',
  instruction:'Berdasarkan Hukum De Morgan, pilih ekuivalensi yang benar untuk ekspresi berikut:',
  expr:'¬(p ∨ q)',
  options:['¬p ∨ ¬q', '¬p ∧ ¬q', 'p ∧ q', '¬p ∨ q'],
  answer:1,
  hint:'De Morgan 2: negasi disjungsi menghasilkan konjungsi negasi masing-masing variabel.',
  solution:[
    {e:'¬(p ∨ q)', r:'Ekspresi awal'},
    {e:'¬p ∧ ¬q',  r:'Hukum De Morgan 2'},
  ],
  explain:'¬(p ∨ q) ≡ ¬p ∧ ¬q adalah Hukum De Morgan 2: negasi disjungsi = konjungsi negasi.',
},
{
  id:2, level:'easy', topic:'Implikasi', pts:5,
  type:'mc',
  instruction:'Implikasi dapat ditulis ulang sebagai disjungsi. Pilih yang ekuivalen dengan:',
  expr:'p → q',
  options:['p ∧ q', '¬p ∧ q', '¬p ∨ q', 'p ∨ ¬q'],
  answer:2,
  hint:'Ingat: p → q berarti "jika p maka q". Implikasi salah HANYA jika p=T dan q=F.',
  solution:[
    {e:'p → q',   r:'Ekspresi awal'},
    {e:'¬p ∨ q',  r:'Definisi Implikasi: p→q ≡ ¬p∨q'},
  ],
  explain:'p → q ≡ ¬p ∨ q adalah definisi standar penulisan ulang implikasi sebagai disjungsi.',
},
{
  id:3, level:'easy', topic:'Negasi Ganda', pts:5,
  type:'fill',
  instruction:'Lengkapi ekuivalensi berdasarkan Hukum Negasi Ganda:',
  exprLeft:'¬¬p', exprRight:'',
  answer:'p',
  hint:'Dua kali negasi mengembalikan nilai ke proposisi asalnya.',
  solution:[
    {e:'¬¬p', r:'Ekspresi awal'},
    {e:'p',   r:'Hukum Negasi Ganda (Double Negation)'},
  ],
  explain:'Hukum Negasi Ganda: ¬¬p ≡ p. Dua negasi saling meniadakan.',
},
{
  id:4, level:'easy', topic:'Idempoten', pts:5,
  type:'mc',
  instruction:'Hukum Idempoten menyatakan bahwa:',
  expr:'p ∧ p',
  options:['≡ T', '≡ F', '≡ p', '≡ 2p'],
  answer:2,
  hint:'Konjungsi suatu proposisi dengan dirinya sendiri tidak mengubah nilainya.',
  solution:[
    {e:'p ∧ p', r:'Ekspresi awal'},
    {e:'p',     r:'Hukum Idempoten Konjungsi'},
  ],
  explain:'Hukum Idempoten: p ∧ p ≡ p dan p ∨ p ≡ p.',
},
{
  id:5, level:'easy', topic:'Komplemen', pts:5,
  type:'mc',
  instruction:'Manakah hasil dari ekspresi berikut yang merupakan tautologi?',
  expr:'p ∨ ¬p',
  options:['≡ F (Kontradiksi)', '≡ p', '≡ T (Tautologi)', '≡ ¬p'],
  answer:2,
  hint:'Pikirkan: dapatkah p ∨ ¬p pernah bernilai Salah?',
  solution:[
    {e:'p ∨ ¬p', r:'Ekspresi awal'},
    {e:'T',       r:'Hukum Komplemen / Excluded Middle'},
  ],
  explain:'p ∨ ¬p selalu bernilai T (Tautologi) — Hukum Excluded Middle.',
},
{
  id:6, level:'easy', topic:'Identitas', pts:5,
  type:'fill',
  instruction:'Lengkapi ekuivalensi Hukum Identitas Konjungsi:',
  exprLeft:'p ∧ T', exprRight:'',
  answer:'p',
  hint:'Konjungsi dengan nilai Benar tidak mengubah proposisi.',
  solution:[
    {e:'p ∧ T', r:'Ekspresi awal'},
    {e:'p',     r:'Hukum Identitas Konjungsi'},
  ],
  explain:'Hukum Identitas: p ∧ T ≡ p dan p ∨ F ≡ p.',
},
{
  id:7, level:'easy', topic:'De Morgan 2', pts:5,
  type:'tt',
  instruction:'Buktikan Hukum De Morgan dengan melengkapi tabel kebenaran. Pilih nilai yang tepat untuk kolom bertanda (?):',
  headers:['p','q','p∧q','¬(p∧q)','¬p','¬q','¬p∨¬q','?≡?'],
  rows:[
    {vals:[T,T,T,F,F,F,F], blanks:[{col:7, answer:'T'}]},
    {vals:[T,F,F,T,F,T,T], blanks:[{col:7, answer:'T'}]},
    {vals:[F,T,F,T,T,F,T], blanks:[{col:7, answer:'T'}]},
    {vals:[F,F,F,T,T,T,T], blanks:[{col:7, answer:'T'}]},
  ],
  targetCols:[3,6],
  hint:'Bandingkan kolom ¬(p∧q) dan ¬p∨¬q. Apakah selalu sama?',
  explain:'Jika semua baris kolom ¬(p∧q) = ¬p∨¬q, maka ¬(p∧q) ≡ ¬p∨¬q terbukti.',
},

/* ─── SEDANG ─────────────────────────────────────────────── */
{
  id:8, level:'med', topic:'Kontrapositif', pts:10,
  type:'mc',
  instruction:'Kontrapositif dari sebuah implikasi ekuivalen dengan implikasi aslinya:',
  expr:'p → q',
  options:['≡ q → p (konvers)', '≡ ¬p → ¬q (invers)', '≡ ¬q → ¬p (kontrapositif)', '≡ ¬p → q'],
  answer:2,
  hint:'Kontrapositif dibuat dengan membalik DAN meniadakan kedua bagian implikasi.',
  solution:[
    {e:'p → q',     r:'Ekspresi awal'},
    {e:'¬p ∨ q',    r:'Definisi Implikasi'},
    {e:'q ∨ ¬p',    r:'Hukum Komutatif'},
    {e:'¬¬q ∨ ¬p',  r:'Negasi Ganda'},
    {e:'¬q → ¬p',   r:'Definisi Implikasi (balik)'},
  ],
  explain:'Kontrapositif: p → q ≡ ¬q → ¬p. Keduanya identik nilai kebenarannya.',
},
{
  id:9, level:'med', topic:'Biimplikasi', pts:10,
  type:'mc',
  instruction:'Biimplikasi dapat ditulis ulang sebagai:',
  expr:'p ↔ q',
  options:['(p → q) ∨ (q → p)', '(p → q) ∧ (q → p)', '(p ∧ q) ∨ (¬p ∧ ¬q)', '(b) dan (c) keduanya benar'],
  answer:3,
  hint:'Biimplikasi = implikasi dua arah. Coba juga tulis menggunakan nilai T/F yang sama.',
  solution:[
    {e:'p ↔ q',                  r:'Ekspresi awal'},
    {e:'(p → q) ∧ (q → p)',      r:'Definisi Biimplikasi'},
    {e:'(¬p ∨ q) ∧ (¬q ∨ p)',   r:'Definisi Implikasi'},
    {e:'(p ∧ q) ∨ (¬p ∧ ¬q)',   r:'Penyederhanaan aljabar logika'},
  ],
  explain:'p ↔ q ≡ (p→q)∧(q→p) ≡ (p∧q)∨(¬p∧¬q). Keduanya valid.',
},
{
  id:10, level:'med', topic:'Distribusi', pts:10,
  type:'fill',
  instruction:'Lengkapi ekuivalensi Hukum Distribusi berikut:',
  exprLeft:'p ∨ (q ∧ r)', exprRight:'',
  answer:'(p∨q)∧(p∨r)',
  hint:'Hukum Distribusi: disjungsi dapat didistribusikan ke dalam konjungsi.',
  solution:[
    {e:'p ∨ (q ∧ r)',          r:'Ekspresi awal'},
    {e:'(p ∨ q) ∧ (p ∨ r)',   r:'Hukum Distribusi ∨ atas ∧'},
  ],
  explain:'Distribusi: p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r). Mirip distribusi dalam aljabar biasa.',
},
{
  id:11, level:'med', topic:'Penyerapan', pts:10,
  type:'mc',
  instruction:'Hukum Penyerapan (Absorption Law) menyatakan:',
  expr:'p ∧ (p ∨ q)',
  options:['≡ p ∨ q', '≡ p ∧ q', '≡ p', '≡ q'],
  answer:2,
  hint:'Konjungsi antara p dan sesuatu yang sudah mengandung p akan "menyerap" bagian ekstra.',
  solution:[
    {e:'p ∧ (p ∨ q)',     r:'Ekspresi awal'},
    {e:'(p ∧ p) ∨ (p ∧ q)',r:'Distribusi'},
    {e:'p ∨ (p ∧ q)',     r:'Idempoten: p∧p=p'},
    {e:'p',               r:'Hukum Penyerapan'},
  ],
  explain:'Hukum Penyerapan: p ∧ (p ∨ q) ≡ p. Proposisi p "menyerap" disjungsinya.',
},
{
  id:12, level:'med', topic:'Negasi Implikasi', pts:10,
  type:'mc',
  instruction:'Negasi dari implikasi p → q ekuivalen dengan:',
  expr:'¬(p → q)',
  options:['¬p → ¬q', '¬p ∨ ¬q', 'p ∧ ¬q', '¬p ∧ q'],
  answer:2,
  hint:'Tulis dulu p→q sebagai disjungsi, lalu terapkan negasi dan De Morgan.',
  solution:[
    {e:'¬(p → q)',   r:'Ekspresi awal'},
    {e:'¬(¬p ∨ q)',  r:'Definisi Implikasi'},
    {e:'¬¬p ∧ ¬q',  r:'De Morgan 2'},
    {e:'p ∧ ¬q',    r:'Negasi Ganda'},
  ],
  explain:'¬(p → q) ≡ p ∧ ¬q. Implikasi hanya salah ketika p=T dan q=F.',
},
{
  id:13, level:'med', topic:'Komutatif + De Morgan', pts:10,
  type:'sortable',
  instruction:'Urutkan langkah-langkah pembuktian berikut dari awal hingga akhir:',
  expr:'¬(q ∨ p) ≡ ¬p ∧ ¬q',
  steps:[
    {e:'¬p ∧ ¬q',       r:'Hukum Komutatif Konjungsi ✓'},
    {e:'¬(p ∨ q)',       r:'Hukum Komutatif Disjungsi'},
    {e:'¬q ∧ ¬p',       r:'Hukum De Morgan 2'},
    {e:'¬(q ∨ p)',       r:'Ekspresi Awal'},
  ],
  correctOrder:[3,1,2,0],
  hint:'Mulai dari ekspresi awal, terapkan komutatif dulu, lalu De Morgan.',
  explain:'¬(q∨p) → ¬(p∨q) [Komutatif] → ¬q∧¬p [De Morgan] → ¬p∧¬q [Komutatif].',
},
{
  id:14, level:'med', topic:'Dominasi', pts:10,
  type:'fill',
  instruction:'Lengkapi Hukum Dominasi berikut:',
  exprLeft:'p ∧ F', exprRight:'',
  answer:'F',
  hint:'Konjungsi dengan nilai Salah selalu menghasilkan Salah, apapun nilai p.',
  solution:[
    {e:'p ∧ F', r:'Ekspresi awal'},
    {e:'F',     r:'Hukum Dominasi Konjungsi'},
  ],
  explain:'Hukum Dominasi: p ∧ F ≡ F dan p ∨ T ≡ T.',
},
{
  id:15, level:'med', topic:'Asosiatif', pts:10,
  type:'mc',
  instruction:'Hukum Asosiatif menyatakan bahwa pengelompokan tidak mengubah hasil. Pilih yang benar:',
  expr:'(p ∨ q) ∨ r',
  options:['≡ p ∨ (q ∨ r)', '≡ p ∧ (q ∧ r)', '≡ (p ∧ q) ∨ r', '≡ p ∨ (q ∧ r)'],
  answer:0,
  hint:'Asosiatif berlaku untuk ∧ dan ∨: pengelompokan berbeda memberikan hasil sama.',
  solution:[
    {e:'(p ∨ q) ∨ r',  r:'Ekspresi awal'},
    {e:'p ∨ (q ∨ r)',  r:'Hukum Asosiatif Disjungsi'},
  ],
  explain:'Hukum Asosiatif: (p∨q)∨r ≡ p∨(q∨r). Urutan pengelompokan tidak berpengaruh.',
},

/* ─── SULIT ─────────────────────────────────────────────── */
{
  id:16, level:'hard', topic:'Rantai Hukum', pts:20,
  type:'sortable',
  instruction:'Susun langkah pembuktian rantai hukum berikut:',
  expr:'¬p → q  ≡  p ∨ q',
  steps:[
    {e:'¬¬p ∨ q',  r:'Negasi Ganda'},
    {e:'¬p → q',   r:'Ekspresi Awal'},
    {e:'¬(¬p) ∨ q',r:'Definisi Implikasi'},
    {e:'p ∨ q',    r:'Penyederhanaan ¬¬p = p ✓'},
  ],
  correctOrder:[1,2,0,3],
  hint:'Tulis ulang implikasi sebagai disjungsi, lalu sederhanakan negasi ganda.',
  explain:'¬p→q ≡ ¬(¬p)∨q [Implikasi] ≡ ¬¬p∨q [sudah ada] ≡ p∨q [Negasi Ganda].',
},
{
  id:17, level:'hard', topic:'Multi-Hukum', pts:20,
  type:'sortable',
  instruction:'Urutkan pembuktian ekuivalensi penting ini:',
  expr:'(p → q) ∧ (p → r)  ≡  p → (q ∧ r)',
  steps:[
    {e:'p → (q ∧ r)',             r:'Definisi Implikasi (balik) ✓'},
    {e:'(p → q) ∧ (p → r)',       r:'Ekspresi Awal'},
    {e:'(¬p ∨ q) ∧ (¬p ∨ r)',    r:'Definisi Implikasi (keduanya)'},
    {e:'¬p ∨ (q ∧ r)',            r:'Distribusi ∨ atas ∧'},
  ],
  correctOrder:[1,2,3,0],
  hint:'Tulis kedua implikasi sebagai disjungsi, lalu terapkan distribusi terbalik.',
  explain:'(p→q)∧(p→r) ≡ (¬p∨q)∧(¬p∨r) ≡ ¬p∨(q∧r) ≡ p→(q∧r).',
},
{
  id:18, level:'hard', topic:'Ekspansi Biimplikasi', pts:20,
  type:'mc',
  instruction:'Ekuivalensi manakah yang paling tepat mengekspresikan biimplikasi dengan operator dasar?',
  expr:'p ↔ q',
  options:[
    '(¬p ∨ q) ∧ (¬q ∨ p)',
    '(p ∨ q) ∧ (¬p ∨ ¬q)',
    '(p → q) ∨ (q → p)',
    '(p ∧ q) ∧ (¬p ∧ ¬q)',
  ],
  answer:0,
  hint:'Ekspansi: p↔q = (p→q)∧(q→p), lalu tulis setiap implikasi sebagai disjungsi.',
  solution:[
    {e:'p ↔ q',                   r:'Ekspresi awal'},
    {e:'(p → q) ∧ (q → p)',       r:'Definisi Biimplikasi'},
    {e:'(¬p ∨ q) ∧ (¬q ∨ p)',    r:'Definisi Implikasi pada keduanya'},
  ],
  explain:'p↔q ≡ (p→q)∧(q→p) ≡ (¬p∨q)∧(¬q∨p). Ini ekspansi paling dasar.',
},
{
  id:19, level:'hard', topic:'Ekuivalensi Kompleks', pts:20,
  type:'sortable',
  instruction:'Susun pembuktian ekuivalensi kompleks ini secara berurutan:',
  expr:'¬(p → q)  ≡  p ∧ ¬q',
  steps:[
    {e:'p ∧ ¬q',       r:'Negasi Ganda: ¬¬p = p ✓'},
    {e:'¬(¬p ∨ q)',    r:'Definisi Implikasi'},
    {e:'¬(p → q)',     r:'Ekspresi Awal'},
    {e:'¬¬p ∧ ¬q',    r:'De Morgan: ¬(A∨B) = ¬A∧¬B'},
  ],
  correctOrder:[2,1,3,0],
  hint:'Langkah: tulis implikasi, terapkan De Morgan pada negasi disjungsi, lalu sederhanakan.',
  explain:'¬(p→q) ≡ ¬(¬p∨q) [Implikasi] ≡ ¬¬p∧¬q [De Morgan] ≡ p∧¬q [Neg Ganda].',
},
{
  id:20, level:'hard', topic:'Tautologi Pembuktian', pts:20,
  type:'mc',
  instruction:'Manakah ekuivalensi berikut yang TIDAK benar? (pilih yang salah)',
  expr:'Identifikasi yang KELIRU',
  options:[
    'p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)',
    'p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)',
    '¬(p ↔ q) ≡ p ↔ q  (ekuivalen dengan dirinya)',
    'p → (q → r) ≡ (p ∧ q) → r',
  ],
  answer:2,
  hint:'Perhatikan: apakah suatu formula bisa ekuivalen dengan negasinya sendiri?',
  solution:[
    {e:'¬(p↔q) ≡ p↔q?',   r:'Klaim yang diuji'},
    {e:'p=T,q=T: p↔q=T, ¬(p↔q)=F', r:'Tidak sama → BUKAN ekuivalensi'},
    {e:'Pilihan A,B,D semua benar', r:'Dapat diverifikasi dengan tabel kebenaran'},
  ],
  explain:'¬(p↔q) ≢ (p↔q). Keduanya berlawanan nilai. Pilihan C adalah pernyataan keliru.',
},
];

// ═══════════════════════════ STATE ═══════════════════════════
let state = {};
questions.forEach(q => { state[q.id] = { answered: false, correct: false, pts: 0, sortOrder: null }; });

let totalCorrect = 0, totalWrong = 0, totalPts = 0;
let activeFilter = 'all';

// ═══════════════════════════ RENDER ═══════════════════════════
function render(){
  const container = document.getElementById('qContainer');
  container.innerHTML = '';

  const toShow = questions.filter(q => activeFilter === 'all' || q.level === activeFilter);

  toShow.forEach((q, idx) => {
    const card = document.createElement('div');
    card.className = 'q-card';
    card.id = `card-${q.id}`;
    card.style.animationDelay = (idx * 0.04) + 's';

    let bodyHTML = '';

    if(q.type === 'mc'){
      bodyHTML = `
        <div class="mc-options" id="mc-${q.id}">
          ${q.options.map((o,i) => `
            <button class="mc-opt" onclick="pickMC(${q.id},${i})" id="mcopt-${q.id}-${i}">
              <span class="opt-k">${String.fromCharCode(65+i)}</span>
              <span style="font-family:'IBM Plex Mono',monospace;font-size:13px;">${o}</span>
            </button>`).join('')}
        </div>`;
    } else if(q.type === 'fill'){
      bodyHTML = `
        <div class="fill-wrap">
          <span class="fill-expr">${q.exprLeft} ≡</span>
          <input class="fill-blank" id="fill-${q.id}" placeholder="…" onkeydown="if(event.key==='Enter')checkFill(${q.id})">
        </div>`;
    } else if(q.type === 'tt'){
      bodyHTML = buildTTQuestion(q);
    } else if(q.type === 'sortable'){
      bodyHTML = buildSortable(q);
    }

    card.innerHTML = `
      <div class="q-head">
        <div class="q-num" id="qnum-${q.id}">${q.id}</div>
        <div class="q-meta">
          <div class="q-tags">
            <span class="q-level lvl-${q.level}">${q.level==='easy'?'Mudah':q.level==='med'?'Sedang':'Sulit'}</span>
            <span class="q-topic">${q.topic}</span>
            <span class="q-pts" style="margin-left:auto;">${q.pts} poin</span>
          </div>
          <div class="q-instruction">${q.instruction}</div>
        </div>
      </div>
      <div class="q-expr-wrap">
        <div class="q-expr">
          <span>${q.expr}</span>
        </div>
      </div>
      <div class="q-body">
        <div class="hint-box" id="hint-${q.id}">
          <div class="hint-label">💡 Petunjuk</div>
          <div class="hint-text">${q.hint}</div>
        </div>
        <div class="solution-box" id="sol-${q.id}">
          <div class="sol-title">// Langkah Pembuktian</div>
          ${(q.solution||[]).map((s,i) => `
            <div class="sol-step">
              <span class="sol-n">${i+1}.</span>
              <span class="sol-e">${s.e}</span>
              <span class="sol-r">${s.r}</span>
            </div>`).join('')}
        </div>
        ${bodyHTML}
        <div class="q-actions">
          ${q.type!=='mc' ? `<button class="btn-check" id="btn-${q.id}" onclick="checkQ(${q.id})">▶ CEK JAWABAN</button>` : ''}
          <button class="btn-hint" onclick="toggleHint(${q.id})">💡 Petunjuk</button>
          <button class="btn-show" onclick="toggleSol(${q.id})">∑ Lihat Pembuktian</button>
        </div>
        <div class="q-feedback" id="fb-${q.id}"></div>
      </div>`;

    container.appendChild(card);
  });
  buildJumpGrid();
}

// ── Truth Table question builder ──
function buildTTQuestion(q){
  let html = `<div class="tt-q"><table>
    <thead><tr>${q.headers.map((h,hi) => {
      const isTarget = q.targetCols && q.targetCols.includes(hi);
      return `<th${isTarget?' class="target"':''}>${h}</th>`;
    }).join('')}
    </tr></thead><tbody>`;

  q.rows.forEach((row, ri) => {
    html += `<tr>`;
    const totalCols = q.headers.length;
    for(let ci=0; ci<totalCols; ci++){
      const blank = row.blanks && row.blanks.find(b => b.col === ci);
      if(blank){
        html += `<td class="tt-blank-cell"><select id="ttsel-${q.id}-${ri}-${ci}" onchange="">
          <option value="">?</option>
          <option value="T">T</option>
          <option value="F">F</option>
        </select></td>`;
      } else {
        const v = row.vals[ci];
        html += `<td>${tv(v)}</td>`;
      }
    }
    html += `</tr>`;
  });
  html += `</tbody></table></div>`;
  return html;
}

// ── Sortable builder ──
function buildSortable(q){
  // Shuffle the steps
  const shuffled = [...q.steps.map((s,i)=>({...s, origIdx:i}))];
  shuffleArr(shuffled);

  let html = `<ul class="sortable-steps" id="sort-${q.id}">`;
  shuffled.forEach((s, pos) => {
    html += `
      <li class="sortable-step" draggable="true"
          data-orig="${s.origIdx}" id="si-${q.id}-${pos}"
          style="grid-template-columns: 32px 28px 1fr 1fr;"
          ondragstart="dragStart(event)" ondragover="dragOver(event)"
          ondrop="dropStep(event,'${q.id}')" ondragend="dragEnd(event)">
        <span class="drag-handle">⠿</span>
        <span class="step-num-cell"></span>
        <span class="step-expr-cell">${s.e}</span>
        <span class="step-rule-cell">${s.r}</span>
      </li>`;
  });
  html += `</ul>`;
  return html;
}

// ═══════════════════════════ ANSWER LOGIC ═══════════════════════════
function pickMC(qid, oi){
  const q = questions.find(x=>x.id===qid);
  if(state[qid].answered) return;
  state[qid].answered = true;
  const correct = oi === q.answer;
  state[qid].correct = correct;
  if(correct){ state[qid].pts = q.pts; totalCorrect++; totalPts += q.pts; }
  else totalWrong++;

  q.options.forEach((_,i) => {
    const btn = document.getElementById(`mcopt-${qid}-${i}`);
    btn.disabled = true;
    if(i===q.answer) btn.classList.add('correct');
    else if(i===oi) btn.classList.add('wrong');
  });
  showFeedback(qid, correct, q.explain);
  markCard(qid, correct);
  updateStats();
  checkComplete();
}

function checkFill(qid){
  const q = questions.find(x=>x.id===qid);
  if(state[qid].answered) return;
  const input = document.getElementById(`fill-${qid}`);
  const val = input.value.trim().replace(/\s/g,'').toLowerCase();
  const ans = q.answer.replace(/\s/g,'').toLowerCase();
  const correct = val === ans;
  state[qid].answered = true;
  state[qid].correct = correct;
  input.classList.add(correct?'correct':'wrong');
  input.disabled = true;
  if(correct){ state[qid].pts=q.pts; totalCorrect++; totalPts+=q.pts; }
  else { totalWrong++; input.value += `  (jawaban: ${q.answer})`; }
  document.getElementById(`btn-${qid}`).disabled = true;
  showFeedback(qid, correct, q.explain);
  markCard(qid, correct);
  updateStats();
  checkComplete();
}

function checkTT(qid){
  const q = questions.find(x=>x.id===qid);
  if(state[qid].answered) return;
  let allCorrect = true;
  q.rows.forEach((row, ri) => {
    (row.blanks||[]).forEach(blank => {
      const sel = document.getElementById(`ttsel-${qid}-${ri}-${blank.col}`);
      if(!sel) return;
      const correct = sel.value === blank.answer;
      if(!correct) allCorrect = false;
      sel.classList.add(correct?'correct':'wrong');
      sel.disabled = true;
      if(!correct) { const opt = sel.querySelector(`option[value="${blank.answer}"]`); if(opt) opt.selected=true; }
    });
  });
  state[qid].answered = true;
  state[qid].correct = allCorrect;
  if(allCorrect){ state[qid].pts=q.pts; totalCorrect++; totalPts+=q.pts; }
  else totalWrong++;
  document.getElementById(`btn-${qid}`).disabled = true;
  showFeedback(qid, allCorrect, q.explain);
  markCard(qid, allCorrect);
  updateStats();
  checkComplete();
}

function checkSortable(qid){
  const q = questions.find(x=>x.id===qid);
  if(state[qid].answered) return;
  const list = document.getElementById(`sort-${qid}`);
  const items = [...list.querySelectorAll('.sortable-step')];
  const userOrder = items.map(it => parseInt(it.dataset.orig));
  const correct = JSON.stringify(userOrder) === JSON.stringify(q.correctOrder);

  state[qid].answered = true;
  state[qid].correct = correct;
  if(correct){ state[qid].pts=q.pts; totalCorrect++; totalPts+=q.pts; }
  else { totalWrong++;
    // Show correct order
    items.forEach((it, pos) => {
      const isCorrectPos = it.dataset.orig == q.correctOrder[pos];
      it.style.borderColor = isCorrectPos ? 'var(--t-b)' : 'var(--f-b)';
      it.style.background = isCorrectPos ? 'rgba(52,211,153,0.06)' : 'rgba(248,113,113,0.06)';
    });
  }
  document.getElementById(`btn-${qid}`).disabled = true;
  items.forEach(it => it.setAttribute('draggable','false'));
  // Update step numbers
  items.forEach((it,pos) => { it.querySelector('.step-num-cell').textContent = pos+1+'.'; });
  showFeedback(qid, correct, q.explain);
  markCard(qid, correct);
  updateStats();
  checkComplete();
}

function checkQ(qid){
  const q = questions.find(x=>x.id===qid);
  if(q.type==='fill') checkFill(qid);
  else if(q.type==='tt') checkTT(qid);
  else if(q.type==='sortable') checkSortable(qid);
}

// ═══════════════════════════ UI HELPERS ═══════════════════════════
function showFeedback(qid, correct, msg){
  const fb = document.getElementById(`fb-${qid}`);
  fb.className = `q-feedback show ${correct?'ok':'err'}`;
  fb.textContent = (correct ? '✓ Benar! ' : '✗ Belum tepat. ') + msg;
}

function markCard(qid, correct){
  const card = document.getElementById(`card-${qid}`);
  const num  = document.getElementById(`qnum-${qid}`);
  card.classList.add(correct ? 'answered-correct' : 'answered-wrong');
  updateJumpBtn(qid, correct);
}

function toggleHint(qid){
  const box = document.getElementById(`hint-${qid}`);
  box.classList.toggle('show');
}
function toggleSol(qid){
  const box = document.getElementById(`sol-${qid}`);
  box.classList.toggle('show');
}

// ═══════════════════════════ DRAG & DROP ═══════════════════════════
let dragged = null;
function dragStart(e){ dragged = e.currentTarget; e.currentTarget.classList.add('dragging'); }
function dragEnd(e)  { e.currentTarget.classList.remove('dragging'); }
function dragOver(e) { e.preventDefault(); e.currentTarget.classList.add('drag-over'); }
function dropStep(e, qid){
  e.preventDefault();
  const target = e.currentTarget;
  target.classList.remove('drag-over');
  if(dragged && dragged !== target){
    const list = document.getElementById(`sort-${qid}`);
    const items = [...list.children];
    const di = items.indexOf(dragged);
    const ti = items.indexOf(target);
    if(di < ti) list.insertBefore(dragged, target.nextSibling);
    else list.insertBefore(dragged, target);
    // Update step numbers live
    [...list.children].forEach((it,i) => { it.querySelector('.step-num-cell').textContent = (i+1)+'.'; });
  }
  dragged = null;
}

// ═══════════════════════════ STATS ═══════════════════════════
function updateStats(){
  document.getElementById('statC').textContent = totalCorrect;
  document.getElementById('statW').textContent = totalWrong;
  document.getElementById('statS').textContent = totalPts;
  const answered = totalCorrect + totalWrong;
  const total = questions.length;
  const pct = Math.round((answered/total)*100);
  const circ = 94.2;
  document.getElementById('ringFill').style.strokeDashoffset = circ - (circ * pct / 100);
  document.getElementById('ringText').textContent = pct + '%';
}

function buildJumpGrid(){
  const grid = document.getElementById('jumpGrid');
  grid.innerHTML = questions.map(q => `
    <button class="jump-btn" id="jb-${q.id}" onclick="jumpTo(${q.id})" title="Soal ${q.id}">${q.id}</button>
  `).join('');
}

function updateJumpBtn(qid, correct){
  const btn = document.getElementById(`jb-${qid}`);
  if(btn) btn.className = `jump-btn ${correct?'j-correct':'j-wrong'}`;
}

function jumpTo(qid){
  document.getElementById(`card-${qid}`)?.scrollIntoView({behavior:'smooth', block:'center'});
}

function checkComplete(){
  const answered = totalCorrect + totalWrong;
  if(answered < questions.length) return;
  setTimeout(showScoreboard, 800);
}

function showScoreboard(){
  const pct = Math.round((totalPts / questions.reduce((a,q)=>a+q.pts,0)) * 100);
  document.getElementById('scorePct').textContent = pct + '%';
  document.getElementById('sbC').textContent = totalCorrect;
  document.getElementById('sbW').textContent = totalWrong;
  document.getElementById('sbP').textContent = totalPts;
  const grades = [
    [90, 'Luar biasa! Kamu ahli ekuivalensi logis. Siap masuk olimpiade? 🏆'],
    [75, 'Sangat baik! Pemahaman hukum-hukum logika sudah solid. 🎯'],
    [60, 'Baik! Masih ada beberapa hukum yang perlu diperkuat. 💪'],
    [40, 'Cukup. Fokus pada De Morgan, Implikasi, dan Distribusi. 📖'],
    [0,  'Jangan menyerah! Baca ulang materinya dan coba lagi. 🔄'],
  ];
  document.getElementById('scoreGrade').textContent = grades.find(([t])=>pct>=t)[1];
  // Circle gradient
  const circle = document.getElementById('scoreCircle');
  circle.style.background = `conic-gradient(var(--gold) ${pct}%, rgba(255,255,255,0.04) ${pct}%)`;
  document.getElementById('scoreboard').classList.add('show');
  document.getElementById('scoreboard').scrollIntoView({behavior:'smooth', block:'center'});
}

function retryAll(){
  state = {};
  questions.forEach(q => { state[q.id] = { answered:false, correct:false, pts:0 }; });
  totalCorrect=0; totalWrong=0; totalPts=0;
  updateStats();
  document.getElementById('scoreboard').classList.remove('show');
  render();
  window.scrollTo({top:0, behavior:'smooth'});
}

// ═══════════════════════════ FILTER ═══════════════════════════
function filterLevel(level, btn){
  activeFilter = level;
  document.querySelectorAll('.lchip').forEach(c=>c.classList.remove('active'));
  btn.classList.add('active');
  render();
}

// ═══════════════════════════ UTIL ═══════════════════════════
function shuffleArr(arr){
  for(let i=arr.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));
    [arr[i],arr[j]]=[arr[j],arr[i]];
  }
}

// ═══════════════════════════ INIT ═══════════════════════════
render();
</script>
</body>
</html>
        """
        tampilkan5 = keterangan(tulisanHTML4,12000)
        tampilkan5.tampilkan()

    with bagian[4]:
        tulisanHTML5 = """
        <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>20 Soal Cerita – Ekuivalensi Logis</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=JetBrains+Mono:wght@300;400;500;600&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet">
<style>
:root {
  --bg:        #f7f4ef;
  --bg2:       #ede9e0;
  --bg3:       #e4dfd4;
  --card:      #fdfcf8;
  --ink:       #1e1a14;
  --ink2:      #4a4238;
  --ink3:      #8a7e6e;
  --border:    rgba(30,26,20,0.1);
  --border2:   rgba(30,26,20,0.06);
  --accent:    #b5420a;
  --acc-bg:    #fff3ee;
  --acc-b:     rgba(181,66,10,0.25);
  --gold:      #c4820a;
  --gold-bg:   #fffbf0;
  --gold-b:    rgba(196,130,10,0.25);
  --t:         #1a6b3c; --t-bg: #edf9f3; --t-b: rgba(26,107,60,0.25);
  --f:         #a01c2c; --f-bg: #fef0f2; --f-b: rgba(160,28,44,0.25);
  --easy:      #1a6b3c; --easy-bg: #edf9f3;
  --med:       #b5420a; --med-bg:  #fff3ee;
  --hard:      #5b1fa0; --hard-bg: #f5f0ff;
  --shadow:    0 4px 24px rgba(30,26,20,0.08);
  --shadow-lg: 0 16px 56px rgba(30,26,20,0.12);
}

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:'DM Sans',sans-serif;min-height:100vh;}

/* ─── TOPBAR ─── */
.topbar{
  position:sticky;top:0;z-index:300;
  background:var(--ink);
  height:54px;display:flex;align-items:center;justify-content:space-between;
  padding:0 32px;
  border-bottom:2px solid var(--accent);
}
.tb-left{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,0.4);}
.tb-left span{color:var(--accent);font-size:11px;}
.tb-right{display:flex;align-items:center;gap:18px;}
.tb-stat{text-align:center;}
.tb-val{font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:600;line-height:1;}
.tb-lbl{font-family:'JetBrains Mono',monospace;font-size:8px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,0.3);}
.tb-val.c{color:#4ade80;} .tb-val.w{color:#f87171;} .tb-val.s{color:#fbbf24;}
.tb-sep{width:1px;height:28px;background:rgba(255,255,255,0.08);}
.tb-pct{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:600;color:#fbbf24;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.2);padding:4px 10px;border-radius:20px;}

/* ─── HERO ─── */
.hero{
  background:var(--ink);
  padding:60px 40px 52px;
  position:relative;overflow:hidden;
}
.hero-noise{
  position:absolute;inset:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
}
.hero-glow{
  position:absolute;top:-100px;right:-80px;
  width:500px;height:500px;
  background:radial-gradient(circle,rgba(181,66,10,0.12) 0%,transparent 65%);
  pointer-events:none;
}
.hero-glow2{
  position:absolute;bottom:-80px;left:-60px;
  width:400px;height:400px;
  background:radial-gradient(circle,rgba(91,31,160,0.08) 0%,transparent 65%);
  pointer-events:none;
}
.container{max-width:920px;margin:0 auto;padding:0 24px;position:relative;z-index:1;}
.hero-eyebrow{
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:4px;
  text-transform:uppercase;color:var(--accent);margin-bottom:16px;
  display:flex;align-items:center;gap:10px;
}
.hero-eyebrow::before{content:'';display:inline-block;width:24px;height:1px;background:var(--accent);}
.hero h1{
  font-family:'Playfair Display',serif;
  font-size:clamp(38px,6vw,66px);font-weight:900;
  line-height:1.05;letter-spacing:-1.5px;color:#fff;margin-bottom:14px;
}
.hero h1 em{color:var(--accent);font-style:italic;}
.hero h1 span{color:rgba(255,255,255,0.35);}
.hero-desc{
  font-family:'DM Sans',sans-serif;font-size:15px;line-height:1.7;
  color:rgba(255,255,255,0.5);max-width:580px;margin-bottom:32px;
}
.hero-desc strong{color:rgba(255,255,255,0.8);}

/* Context chips */
.ctx-chips{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}
.ctx-chip{
  font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;text-transform:uppercase;
  padding:5px 12px;border-radius:4px;border:1px solid;
}
.ch-a{color:#f9a8d4;border-color:rgba(249,168,212,0.3);background:rgba(249,168,212,0.06);}
.ch-b{color:#93c5fd;border-color:rgba(147,197,253,0.3);background:rgba(147,197,253,0.06);}
.ch-c{color:#6ee7b7;border-color:rgba(110,231,183,0.3);background:rgba(110,231,183,0.06);}
.ch-d{color:#fcd34d;border-color:rgba(252,211,77,0.3);background:rgba(252,211,77,0.06);}
.ch-e{color:#c4b5fd;border-color:rgba(196,181,253,0.3);background:rgba(196,181,253,0.06);}

/* Level filter */
.level-bar{
  display:flex;gap:8px;flex-wrap:wrap;
  background:var(--bg2);padding:12px 32px;
  border-bottom:1px solid var(--border);
  position:sticky;top:54px;z-index:200;
}
.lbtn{
  font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;text-transform:uppercase;
  padding:6px 14px;border-radius:4px;border:1px solid var(--border);
  background:transparent;color:var(--ink3);cursor:pointer;transition:all 0.18s;
}
.lbtn:hover{color:var(--ink);border-color:rgba(30,26,20,0.3);}
.lbtn.active{background:var(--ink);color:#fff;border-color:var(--ink);}
.lbtn.easy.active{background:var(--easy);border-color:var(--easy);}
.lbtn.med.active{background:var(--med);border-color:var(--med);}
.lbtn.hard.active{background:var(--hard);border-color:var(--hard);}

/* Jump dots */
.jump-wrap{padding:20px 0 4px;display:flex;gap:6px;flex-wrap:wrap;align-items:center;}
.jump-lbl{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--ink3);text-transform:uppercase;margin-right:4px;}
.jdot{
  width:30px;height:30px;border-radius:6px;
  font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:600;
  border:1px solid var(--border);background:var(--card);color:var(--ink3);
  cursor:pointer;transition:all 0.15s;
  display:flex;align-items:center;justify-content:center;
}
.jdot:hover{border-color:var(--accent);color:var(--accent);}
.jdot.done-c{background:var(--t-bg);border-color:var(--t-b);color:var(--t);}
.jdot.done-w{background:var(--f-bg);border-color:var(--f-b);color:var(--f);}

/* ─── STORY CARD ─── */
.q-card{
  background:var(--card);
  border:1px solid var(--border);
  border-radius:16px;
  margin-bottom:24px;
  overflow:hidden;
  box-shadow:var(--shadow);
  transition:border-color 0.3s,box-shadow 0.3s;
  animation:slideIn 0.35s ease both;
}
@keyframes slideIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.q-card.done-c{border-color:var(--t-b);box-shadow:0 0 0 1px var(--t-b),var(--shadow);}
.q-card.done-w{border-color:var(--f-b);box-shadow:0 0 0 1px var(--f-b),var(--shadow);}

/* Card header strip */
.q-strip{height:3px;}
.strip-easy{background:linear-gradient(90deg,var(--easy),#86efac);}
.strip-med {background:linear-gradient(90deg,var(--med),#fb923c);}
.strip-hard{background:linear-gradient(90deg,var(--hard),#a78bfa);}

/* Card top meta */
.q-meta-row{
  padding:16px 24px 0;
  display:flex;align-items:center;gap:10px;flex-wrap:wrap;
}
.q-num-badge{
  font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:600;
  width:34px;height:34px;border-radius:8px;
  display:flex;align-items:center;justify-content:center;
  flex-shrink:0;border:1px solid var(--border);background:var(--bg2);color:var(--ink3);
}
.q-card.done-c .q-num-badge{background:var(--t-bg);border-color:var(--t-b);color:var(--t);}
.q-card.done-w .q-num-badge{background:var(--f-bg);border-color:var(--f-b);color:var(--f);}
.q-badge{
  font-family:'JetBrains Mono',monospace;font-size:8px;letter-spacing:2px;text-transform:uppercase;
  padding:3px 10px;border-radius:3px;
}
.badge-easy{background:var(--easy-bg);color:var(--easy);border:1px solid rgba(26,107,60,0.2);}
.badge-med {background:var(--med-bg); color:var(--med); border:1px solid rgba(181,66,10,0.2);}
.badge-hard{background:var(--hard-bg);color:var(--hard);border:1px solid rgba(91,31,160,0.2);}
.q-topic{
  font-family:'JetBrains Mono',monospace;font-size:8px;letter-spacing:1.5px;text-transform:uppercase;
  padding:3px 10px;border-radius:3px;
  background:rgba(30,26,20,0.04);color:var(--ink3);border:1px solid var(--border);
}
.q-pts{
  font-family:'JetBrains Mono',monospace;font-size:9px;
  color:var(--gold);background:var(--gold-bg);border:1px solid var(--gold-b);
  padding:3px 10px;border-radius:3px;margin-left:auto;
}

/* Story block */
.story-block{
  margin:16px 24px 0;
  background:var(--bg2);
  border:1px solid var(--border);
  border-radius:10px;
  padding:20px 22px;
  position:relative;overflow:hidden;
}
.story-block::before{
  content:'❝';
  position:absolute;top:-8px;right:14px;
  font-family:'Playfair Display',serif;font-size:80px;
  color:rgba(30,26,20,0.04);pointer-events:none;line-height:1;
}
.story-context{
  font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:3px;
  text-transform:uppercase;color:var(--ink3);margin-bottom:8px;
  display:flex;align-items:center;gap:8px;
}
.story-text{
  font-family:'DM Sans',sans-serif;font-style:italic;
  font-size:14px;line-height:1.75;color:var(--ink2);
}
.story-text strong{color:var(--ink);font-style:normal;font-weight:600;}

/* Proposisi definitions */
.prop-defs{
  margin:14px 24px 0;
  display:flex;gap:8px;flex-wrap:wrap;
}
.prop-pill{
  background:var(--card);border:1px solid var(--border);
  border-radius:6px;padding:8px 14px;
  font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--ink2);
}
.prop-pill span{color:var(--accent);font-weight:600;}

/* Question */
.q-question{
  padding:14px 24px 0;
  font-size:15px;line-height:1.7;color:var(--ink);
}

/* Formula expression */
.q-formula-wrap{padding:12px 24px 0;}
.q-formula{
  font-family:'JetBrains Mono',monospace;font-size:17px;font-weight:600;
  background:var(--ink);color:var(--acc-bg);
  padding:14px 20px;border-radius:8px;
  display:inline-block;letter-spacing:1.5px;
  box-shadow:var(--shadow);
}
.q-formula .sym{color:#fcd34d;}

/* Options */
.q-body{padding:16px 24px 24px;}
.mc-opts{display:flex;flex-direction:column;gap:8px;margin-bottom:14px;}
.mc-opt{
  display:flex;align-items:flex-start;gap:12px;
  padding:13px 16px;border:1.5px solid var(--border);
  border-radius:8px;background:var(--bg);
  cursor:pointer;font-size:13px;color:var(--ink2);text-align:left;
  transition:all 0.15s;line-height:1.6;
}
.mc-opt:hover:not(:disabled){border-color:var(--acc-b);background:var(--acc-bg);color:var(--ink);}
.mc-opt .ok{
  font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:700;
  min-width:24px;height:24px;border-radius:4px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  background:rgba(30,26,20,0.06);color:var(--ink3);
  transition:all 0.15s;
}
.mc-opt.correct{border-color:var(--t-b);background:var(--t-bg);color:var(--t);}
.mc-opt.correct .ok{background:var(--t);color:#fff;}
.mc-opt.wrong{border-color:var(--f-b);background:var(--f-bg);color:var(--f);}
.mc-opt.wrong .ok{background:var(--f);color:#fff;}
.mc-opt:disabled{cursor:default;}
.mc-opt-text{flex:1;}
.mc-opt-formula{
  font-family:'JetBrains Mono',monospace;font-size:13px;
  display:block;margin-bottom:2px;
}
.mc-opt-desc{font-size:12px;color:var(--ink3);font-style:italic;}

/* Analysis / proof verify */
.proof-verify{margin-bottom:14px;}
.proof-title{
  font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;
  text-transform:uppercase;color:var(--ink3);margin-bottom:10px;
}
.proof-chain{display:flex;flex-direction:column;gap:0;}
.proof-row{
  display:grid;grid-template-columns:24px 1fr 1.2fr;
  align-items:center;gap:0;
  padding:9px 14px;
  border-bottom:1px solid var(--border);
  font-family:'JetBrains Mono',monospace;font-size:12px;
  background:var(--bg);
  cursor:pointer;transition:background 0.12s;
}
.proof-row:first-child{border-radius:8px 8px 0 0;background:var(--bg3);}
.proof-row:last-child{border-bottom:none;border-radius:0 0 8px 8px;}
.proof-row:hover{background:var(--bg2);}
.proof-row.selected{background:var(--gold-bg);border-color:var(--gold-b);}
.proof-row.correct-sel{background:var(--t-bg);border-color:var(--t-b);}
.proof-row.wrong-sel{background:var(--f-bg);border-color:var(--f-b);}
.pr-step{color:var(--ink3);font-size:10px;}
.pr-expr{color:var(--ink);font-weight:500;}
.pr-rule{color:#6366f1;font-size:11px;}
.pr-rule.wrong-rule{color:var(--f);text-decoration:line-through;}
.proof-radio{
  width:14px;height:14px;border:1.5px solid var(--border);
  border-radius:50%;margin-right:0;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  background:var(--card);transition:all 0.12s;
}
.proof-row.selected .proof-radio{border-color:var(--gold);background:var(--gold);}
.proof-row.correct-sel .proof-radio{border-color:var(--t);background:var(--t);}
.proof-row.wrong-sel .proof-radio{border-color:var(--f);background:var(--f);}

/* Fill blank */
.fill-row{
  display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px;
}
.fill-label{font-family:'JetBrains Mono',monospace;font-size:14px;color:var(--ink);}
.fill-input{
  font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:500;
  padding:9px 14px;border:1.5px solid var(--border);
  border-radius:6px;background:var(--bg2);color:var(--ink);
  outline:none;width:180px;transition:border-color 0.18s;
}
.fill-input:focus{border-color:var(--accent);}
.fill-input.c{border-color:var(--t);background:var(--t-bg);color:var(--t);}
.fill-input.w{border-color:var(--f);background:var(--f-bg);color:var(--f);}

/* Truth table question */
.tt-wrap{overflow-x:auto;margin-bottom:14px;}
.tt-wrap table{border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:12px;width:100%;}
.tt-wrap th{
  padding:8px 14px;background:var(--bg3);
  color:var(--ink3);font-size:9px;letter-spacing:2px;
  border:1px solid var(--border);text-align:center;
}
.tt-wrap th.hi{color:var(--accent);background:var(--acc-bg);}
.tt-wrap td{padding:8px 14px;text-align:center;border:1px solid var(--border2);}
.tv-T{color:var(--t);font-weight:700;} .tv-F{color:var(--f);font-weight:700;}
.tt-sel{
  font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:700;
  padding:4px 10px;border-radius:5px;border:1px solid var(--border2);
  background:var(--bg2);color:var(--ink);cursor:pointer;
}
.tt-sel.c{background:var(--t-bg);color:var(--t);border-color:var(--t-b);}
.tt-sel.w{background:var(--f-bg);color:var(--f);border-color:var(--f-b);}

/* Action bar */
.q-actions{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
.btn-check{
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:2px;
  padding:10px 22px;background:var(--ink);color:#fff;
  border:none;border-radius:6px;cursor:pointer;font-weight:700;
  transition:opacity 0.15s,transform 0.1s;
}
.btn-check:hover{opacity:0.85;transform:scale(0.99);}
.btn-check:disabled{opacity:0.35;cursor:default;transform:none;}
.btn-hint{
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1.5px;
  padding:10px 16px;background:transparent;color:var(--ink3);
  border:1px solid var(--border);border-radius:6px;cursor:pointer;
  transition:all 0.15s;
}
.btn-hint:hover{color:var(--gold);border-color:var(--gold-b);}
.btn-sol{
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1.5px;
  padding:10px 16px;background:transparent;color:var(--hard);
  border:1px solid rgba(91,31,160,0.2);border-radius:6px;cursor:pointer;
  transition:background 0.15s;
}
.btn-sol:hover{background:var(--hard-bg);}

/* Feedback */
.q-feedback{
  margin-top:12px;font-size:13px;line-height:1.7;border-radius:8px;
  padding:13px 16px;display:none;animation:feedUp 0.2s ease;
}
@keyframes feedUp{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:translateY(0)}}
.q-feedback.show{display:block;}
.q-feedback.ok{background:var(--t-bg);color:var(--t);border:1px solid var(--t-b);}
.q-feedback.err{background:var(--f-bg);color:var(--f);border:1px solid var(--f-b);}
.q-feedback .fb-title{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;font-weight:700;margin-bottom:4px;}
.q-feedback .fb-body{color:inherit;opacity:0.9;}

/* Hint */
.hint-box{
  display:none;background:var(--gold-bg);border:1px solid var(--gold-b);
  border-radius:8px;padding:12px 16px;margin-bottom:12px;
}
.hint-box.show{display:block;animation:feedUp 0.2s ease;}
.hint-lbl{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:4px;}
.hint-txt{font-family:'JetBrains Mono',monospace;font-size:12px;color:rgba(196,130,10,0.85);line-height:1.6;}

/* Solution */
.sol-box{
  display:none;background:var(--bg3);border:1px solid var(--border);
  border-radius:8px;padding:16px;margin-bottom:12px;
}
.sol-box.show{display:block;animation:feedUp 0.2s ease;}
.sol-lbl{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;text-transform:uppercase;color:var(--hard);margin-bottom:10px;}
.sol-step{display:flex;gap:10px;padding:6px 0;border-bottom:1px solid var(--border2);font-family:'JetBrains Mono',monospace;font-size:12px;}
.sol-step:last-child{border-bottom:none;}
.ss-n{color:var(--ink3);min-width:18px;}
.ss-e{color:var(--ink);flex:1;}
.ss-r{color:#6366f1;font-size:11px;}

/* ─── SCOREBOARD ─── */
.scoreboard{
  background:var(--ink);border-radius:16px;
  padding:56px 40px;text-align:center;
  display:none;animation:slideIn 0.4s ease;
  margin-top:40px;box-shadow:var(--shadow-lg);
}
.scoreboard.show{display:block;}

.score-rings{
  display:flex;justify-content:center;gap:40px;margin-bottom:32px;flex-wrap:wrap;
}
.score-ring{text-align:center;}
.ring-val{font-family:'Playfair Display',serif;font-size:56px;font-weight:900;line-height:1;}
.ring-val.pct{color:#fbbf24;}
.ring-val.c{color:#4ade80;}
.ring-val.w{color:#f87171;}
.ring-val.p{color:#c084fc;}
.ring-lbl{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,0.3);margin-top:4px;}

.score-grade{
  font-family:'Playfair Display',serif;font-style:italic;
  font-size:22px;color:rgba(255,255,255,0.65);margin-bottom:32px;line-height:1.5;
}

.score-detail{
  display:flex;flex-direction:column;gap:6px;
  max-width:480px;margin:0 auto 36px;text-align:left;
}
.sd-row{
  display:flex;align-items:center;justify-content:space-between;
  padding:8px 14px;border-radius:6px;
  font-family:'JetBrains Mono',monospace;font-size:11px;
  background:rgba(255,255,255,0.04);
}
.sd-lbl{color:rgba(255,255,255,0.5);}
.sd-val.c{color:#4ade80;font-weight:700;}
.sd-val.w{color:#f87171;font-weight:700;}

.retry-btn{
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:2px;
  padding:13px 40px;background:var(--accent);color:#fff;
  border:none;border-radius:8px;cursor:pointer;font-weight:700;
  transition:opacity 0.15s;
}
.retry-btn:hover{opacity:0.85;}

/* Responsive */
@media(max-width:620px){
  .topbar{padding:0 16px;}
  .hero{padding:40px 0;}
  .proof-row{grid-template-columns:20px 1fr;}
  .pr-rule{display:none;}
  .score-rings{gap:20px;}
}
</style>
</head>
<body>

<!-- TOPBAR -->
<div class="topbar">
  <div class="tb-left">Diskrit · <span>Soal Cerita Ekuivalensi Logis</span></div>
  <div class="tb-right">
    <div class="tb-stat"><div class="tb-val c" id="stC">0</div><div class="tb-lbl">Benar</div></div>
    <div class="tb-sep"></div>
    <div class="tb-stat"><div class="tb-val w" id="stW">0</div><div class="tb-lbl">Salah</div></div>
    <div class="tb-sep"></div>
    <div class="tb-stat"><div class="tb-val s" id="stS">0</div><div class="tb-lbl">Poin</div></div>
    <div class="tb-sep"></div>
    <div class="tb-pct" id="stPct">0%</div>
  </div>
</div>

<!-- HERO -->
<div class="hero">
  <div class="hero-noise"></div>
  <div class="hero-glow"></div>
  <div class="hero-glow2"></div>
  <div class="container">
    <div class="hero-eyebrow">Matematika Diskrit · Martin Bernard, M.Pd</div>
    <h1>20 Soal Cerita<br><em>Pembuktian</em> <span>&</span><br>Analisis Ekuivalensi</h1>
    <p class="hero-desc">
      Setiap soal dikemas dalam <strong>konteks kehidupan nyata</strong>:
      dari sistem gerbang logika, keamanan siber, hingga kecerdasan buatan —
      lalu dianalisis menggunakan hukum-hukum ekuivalensi logis.
    </p>
    <div class="ctx-chips">
      <span class="ctx-chip ch-a">🔐 Keamanan Sistem</span>
      <span class="ctx-chip ch-b">🤖 Kecerdasan Buatan</span>
      <span class="ctx-chip ch-c">🌐 Jaringan Komputer</span>
      <span class="ctx-chip ch-d">🏥 Sistem Medis</span>
      <span class="ctx-chip ch-e">🏛️ Hukum & Kebijakan</span>
    </div>
  </div>
</div>

<!-- LEVEL BAR -->
<div class="level-bar">
  <button class="lbtn active" onclick="setFilter('all',this)">Semua (20)</button>
  <button class="lbtn easy"   onclick="setFilter('easy',this)">🟢 Mudah (7)</button>
  <button class="lbtn med"    onclick="setFilter('med',this)">🟡 Sedang (8)</button>
  <button class="lbtn hard"   onclick="setFilter('hard',this)">🔴 Sulit (5)</button>
</div>

<div class="container">
  <div class="jump-wrap">
    <span class="jump-lbl">Soal →</span>
    <div id="jumpDots" style="display:flex;gap:6px;flex-wrap:wrap;"></div>
  </div>
  <div id="qWrap"></div>

  <!-- SCOREBOARD -->
  <div class="scoreboard" id="scoreboard">
    <div class="score-rings">
      <div class="score-ring"><div class="ring-val pct" id="sbPct">—</div><div class="ring-lbl">Skor %</div></div>
      <div class="score-ring"><div class="ring-val c"   id="sbC">0</div><div class="ring-lbl">Benar</div></div>
      <div class="score-ring"><div class="ring-val w"   id="sbW">0</div><div class="ring-lbl">Salah</div></div>
      <div class="score-ring"><div class="ring-val p"   id="sbP">0</div><div class="ring-lbl">Poin</div></div>
    </div>
    <div class="score-grade" id="sbGrade"></div>
    <div class="score-detail" id="sbDetail"></div>
    <button class="retry-btn" onclick="retryAll()">↺ ULANGI SEMUA SOAL</button>
  </div>
  <div style="height:60px;"></div>
</div>

<script>
// ════════════════════════════════════════
//  QUESTION DATA
// ════════════════════════════════════════
const T=true,F=false;
const combo=[[T,T],[T,F],[F,T],[F,F]];
const tv=v=>`<span class="tv-${v?'T':'F'}">${v?'T':'F'}</span>`;

const Qs=[
// ─── MUDAH ──────────────────────────────────────────────────────────
{id:1,level:'easy',topic:'Implikasi',pts:5,
context:'🔐 Keamanan Sistem',
story:`Seorang sistem admin membuat aturan akses: <strong>"Jika pengguna adalah admin (p), maka ia dapat mengakses server (q)."</strong> Seorang analis keamanan ingin menulis ulang aturan ini dalam bentuk disjungsi untuk modul firewall yang tidak mendukung operator implikasi.`,
props:[{sym:'p',def:'Pengguna adalah admin'},{sym:'q',def:'Pengguna dapat mengakses server'}],
question:'Ekuivalensi mana yang benar sebagai pengganti p → q dalam sistem firewall?',
formula:'p → q',
type:'mc',
opts:[
  {f:'p ∧ q',d:'Konjungsi: keduanya harus benar'},
  {f:'¬p ∨ q',d:'Disjungsi: bukan admin ATAU bisa akses'},
  {f:'¬p ∧ ¬q',d:'Konjungsi negasi keduanya'},
  {f:'p ∨ ¬q',d:'Disjungsi dengan negasi konsekuen'},
],
ans:1,
hint:'Ingat: p → q ≡ ¬p ∨ q. Implikasi diubah dengan meniadakan anteseden dan menggunakan disjungsi.',
sol:[{e:'p → q',r:'Aturan asli'},{e:'¬p ∨ q',r:'Definisi Implikasi: p→q ≡ ¬p∨q'}],
explain:'Hukum implikasi: p → q ≡ ¬p ∨ q. Artinya: "pengguna bukan admin ATAU bisa mengakses server."'},

{id:2,level:'easy',topic:'De Morgan',pts:5,
context:'🌐 Jaringan Komputer',
story:`Seorang network engineer menulis kondisi untuk mematikan koneksi: <strong>"Matikan jika koneksi A dan koneksi B keduanya aktif."</strong> Ia ingin mengetahui kapan kondisi tersebut TIDAK terpenuhi menggunakan Hukum De Morgan.`,
props:[{sym:'p',def:'Koneksi A aktif'},{sym:'q',def:'Koneksi B aktif'}],
question:'Berdasarkan Hukum De Morgan, ¬(p ∧ q) ekuivalen dengan?',
formula:'¬(p ∧ q)',
type:'mc',
opts:[
  {f:'¬p ∧ ¬q',d:'Kedua koneksi tidak aktif'},
  {f:'¬p ∨ ¬q',d:'Salah satu atau keduanya tidak aktif'},
  {f:'p ∨ q',d:'Salah satu atau keduanya aktif'},
  {f:'p ∧ q',d:'Sama dengan ekspresi awal'},
],
ans:1,
hint:'De Morgan 1: negasi konjungsi menjadi disjungsi dari negasi masing-masing.',
sol:[{e:'¬(p ∧ q)',r:'Ekspresi awal'},{e:'¬p ∨ ¬q',r:'Hukum De Morgan 1'}],
explain:'¬(p ∧ q) ≡ ¬p ∨ ¬q. Kondisi mati tidak terpenuhi jika koneksi A atau B (atau keduanya) tidak aktif.'},

{id:3,level:'easy',topic:'Negasi Ganda',pts:5,
context:'🤖 Kecerdasan Buatan',
story:`Sebuah sistem AI memiliki aturan: <strong>"Jika sensor TIDAK mendeteksi TIDAK adanya ancaman, lakukan tindakan."</strong> Developer ingin menyederhanakan logika sensor ini agar lebih efisien.`,
props:[{sym:'p',def:'Sensor mendeteksi ancaman'}],
question:'Pernyataan "tidak mendeteksi tidak adanya ancaman" setara dengan ekspresi mana?',
formula:'¬(¬p)',
type:'mc',
opts:[
  {f:'¬p',d:'Sensor tidak mendeteksi ancaman'},
  {f:'p',d:'Sensor mendeteksi ancaman'},
  {f:'p ∨ ¬p',d:'Selalu benar (Tautologi)'},
  {f:'F',d:'Selalu salah (Kontradiksi)'},
],
ans:1,
hint:'Dua negasi berurutan saling meniadakan: ¬(¬p) ≡ p.',
sol:[{e:'¬(¬p)',r:'Ekspresi awal'},{e:'p',r:'Hukum Negasi Ganda'}],
explain:'Hukum Negasi Ganda: ¬¬p ≡ p. "Tidak tidak ada ancaman" = "ada ancaman".'},

{id:4,level:'easy',topic:'De Morgan 2',pts:5,
context:'🏥 Sistem Medis',
story:`Sebuah sistem diagnostik medis bekerja dengan aturan: <strong>"Pasien dinyatakan sehat jika TIDAK (demam ATAU batuk)."</strong> Dokter ingin mengetahui kondisi sehat dalam bentuk yang lebih sederhana.`,
props:[{sym:'p',def:'Pasien demam'},{sym:'q',def:'Pasien batuk'}],
question:'Kondisi "pasien sehat" ¬(p ∨ q) ekuivalen dengan?',
formula:'¬(p ∨ q)',
type:'mc',
opts:[
  {f:'¬p ∨ ¬q',d:'Tidak demam atau tidak batuk'},
  {f:'¬p ∧ ¬q',d:'Tidak demam dan tidak batuk'},
  {f:'p ∧ q',d:'Demam dan batuk'},
  {f:'¬p → q',d:'Jika tidak demam maka batuk'},
],
ans:1,
hint:'De Morgan 2: negasi disjungsi menjadi konjungsi dari negasi masing-masing.',
sol:[{e:'¬(p ∨ q)',r:'Ekspresi awal'},{e:'¬p ∧ ¬q',r:'Hukum De Morgan 2'}],
explain:'¬(p ∨ q) ≡ ¬p ∧ ¬q. Pasien sehat jika TIDAK demam DAN TIDAK batuk.'},

{id:5,level:'easy',topic:'Komplemen',pts:5,
context:'🏛️ Hukum & Kebijakan',
story:`Sebuah pasal hukum berbunyi: <strong>"Tersangka bersalah atau tidak bersalah."</strong> Hakim ingin membuktikan bahwa pernyataan ini merupakan tautologi yang selalu benar tanpa perlu bukti tambahan.`,
props:[{sym:'p',def:'Tersangka bersalah'}],
question:'Pernyataan hukum tersebut dapat diformulasikan sebagai?',
formula:'p ∨ ¬p',
type:'mc',
opts:[
  {f:'Kontradiksi — selalu Salah',d:'Tidak pernah bisa terjadi'},
  {f:'Tautologi — selalu Benar',d:'Benar dalam setiap keadaan'},
  {f:'Bergantung nilai p',d:'Harus dicek kasusnya'},
  {f:'Bergantung nilai q',d:'Memerlukan variabel lain'},
],
ans:1,
hint:'p ∨ ¬p adalah Hukum Excluded Middle — selalu benar apapun nilai p.',
sol:[{e:'p ∨ ¬p',r:'Hukum Excluded Middle'},{e:'T (Tautologi)',r:'Selalu bernilai Benar'}],
explain:'p ∨ ¬p ≡ T adalah tautologi. Setiap tersangka pasti berada dalam salah satu kondisi.'},

{id:6,level:'easy',topic:'Identitas',pts:5,
context:'🤖 Kecerdasan Buatan',
story:`Sebuah AI decision-making system memiliki aturan gabungan: <strong>"Robot bergerak jika kondisi bergerak BENAR dan sistem aktif (T)."</strong> Developer ingin menyederhanakan kondisi yang melibatkan nilai T.`,
props:[{sym:'p',def:'Robot bergerak'},{sym:'T',def:'Sistem selalu aktif (nilai True)'}],
question:'Kondisi "p ∧ T" dapat disederhanakan menjadi?',
formula:'p ∧ T',
type:'mc',
opts:[
  {f:'T (selalu aktif)',d:'Tidak bergantung robot bergerak'},
  {f:'F (selalu mati)',d:'Tidak pernah aktif'},
  {f:'p',d:'Hanya bergantung status robot'},
  {f:'¬p',d:'Negasi status robot'},
],
ans:2,
hint:'Hukum Identitas Konjungsi: p ∧ T ≡ p. Mengalikan dengan "benar" tidak mengubah hasil.',
sol:[{e:'p ∧ T',r:'Ekspresi awal'},{e:'p',r:'Hukum Identitas Konjungsi'}],
explain:'Hukum Identitas: p ∧ T ≡ p. Kondisi benar (T) tidak mempengaruhi nilai p.'},

{id:7,level:'easy',topic:'Tabel Kebenaran',pts:5,
context:'🌐 Jaringan Komputer',
story:`Admin jaringan menguji ekuivalensi dua konfigurasi routing: <strong>Rute A: ¬(p ∧ q) dan Rute B: ¬p ∨ ¬q.</strong> Untuk membuktikan ekuivalensinya, ia membuat tabel kebenaran. Lengkapi nilai yang hilang!`,
props:[{sym:'p',def:'Paket dari sumber A'},{sym:'q',def:'Paket dari sumber B'}],
question:'Lengkapi kolom hasil (?) pada tabel kebenaran pembuktian De Morgan:',
formula:'¬(p∧q) ≡ ¬p∨¬q',
type:'tt',
headers:['p','q','p∧q','¬(p∧q)','¬p','¬q','¬p∨¬q','≡?'],
trows:[
  {vals:[T,T,T,F,F,F,F],blank:{col:7,ans:'T'}},
  {vals:[T,F,F,T,F,T,T],blank:{col:7,ans:'T'}},
  {vals:[F,T,F,T,T,F,T],blank:{col:7,ans:'T'}},
  {vals:[F,F,F,T,T,T,T],blank:{col:7,ans:'T'}},
],
targetCols:[3,6],
hint:'Bandingkan kolom ¬(p∧q) dengan ¬p∨¬q. Jika sama di semua baris, ekuivalensi terbukti.',
explain:'Semua baris menghasilkan nilai yang sama, sehingga ¬(p∧q) ≡ ¬p∨¬q terbukti.'},

// ─── SEDANG ─────────────────────────────────────────────────────────
{id:8,level:'med',topic:'Kontrapositif',pts:10,
context:'🔐 Keamanan Sistem',
story:`Sebuah sistem autentikasi menggunakan aturan: <strong>"Jika password benar (p), maka akses diberikan (q)."</strong> Tim keamanan ingin menulis aturan kontrapositif untuk sistem logging yang mendeteksi anomali akses.`,
props:[{sym:'p',def:'Password benar'},{sym:'q',def:'Akses diberikan'}],
question:'Kontrapositif dari aturan keamanan p → q yang benar adalah?',
formula:'p → q',
type:'mc',
opts:[
  {f:'q → p',d:'Jika akses diberikan maka password benar (konvers)'},
  {f:'¬p → ¬q',d:'Jika password salah maka akses ditolak (invers)'},
  {f:'¬q → ¬p',d:'Jika akses ditolak maka password salah (kontrapositif)'},
  {f:'¬p ∨ q',d:'Ekuivalensi sebagai disjungsi'},
],
ans:2,
hint:'Kontrapositif: balik urutan dan tambahkan negasi pada keduanya. p→q ≡ ¬q→¬p.',
sol:[{e:'p → q',r:'Aturan asli'},{e:'¬q → ¬p',r:'Kontrapositif: p→q ≡ ¬q→¬p'}],
explain:'Kontrapositif: p→q ≡ ¬q→¬p. "Jika akses ditolak, maka password pasti salah."'},

{id:9,level:'med',topic:'Negasi Implikasi',pts:10,
context:'🏥 Sistem Medis',
story:`Protokol medis menyatakan: <strong>"Jika hasil lab positif (p), maka berikan obat X (q)."</strong> Seorang peneliti ingin menganalisis kapan protokol ini DILANGGAR — yaitu kapan negasinya bernilai benar.`,
props:[{sym:'p',def:'Hasil lab positif'},{sym:'q',def:'Obat X diberikan'}],
question:'Kondisi "protokol dilanggar" ¬(p → q) ekuivalen dengan?',
formula:'¬(p → q)',
type:'mc',
opts:[
  {f:'¬p ∨ ¬q',d:'Lab negatif atau obat tidak diberikan'},
  {f:'¬p → ¬q',d:'Kontrapositif dari aturan'},
  {f:'p ∧ ¬q',d:'Lab positif namun obat tidak diberikan'},
  {f:'¬p ∧ q',d:'Lab negatif namun obat diberikan'},
],
ans:2,
hint:'Tulis p→q sebagai ¬p∨q, negasikan, lalu terapkan De Morgan.',
sol:[{e:'¬(p → q)',r:'Ekspresi awal'},{e:'¬(¬p ∨ q)',r:'Definisi Implikasi'},{e:'p ∧ ¬q',r:'De Morgan + Negasi Ganda'}],
explain:'¬(p→q) ≡ p ∧ ¬q. Protokol dilanggar jika: lab positif TAPI obat tidak diberikan.'},

{id:10,level:'med',topic:'Distribusi',pts:10,
context:'🤖 Kecerdasan Buatan',
story:`Sebuah robot memiliki kondisi bergerak: <strong>"Motor aktif DAN (sensor kiri ATAU sensor kanan aktif)."</strong> Engineer ingin mendistribusikan kondisi ini untuk optimasi hardware paralel.`,
props:[{sym:'p',def:'Motor aktif'},{sym:'q',def:'Sensor kiri aktif'},{sym:'r',def:'Sensor kanan aktif'}],
question:'Bentuk terdistribusi dari kondisi p ∧ (q ∨ r) adalah?',
formula:'p ∧ (q ∨ r)',
type:'mc',
opts:[
  {f:'(p ∧ q) ∨ (p ∧ r)',d:'Distribusi ∧ atas ∨'},
  {f:'(p ∨ q) ∧ (p ∨ r)',d:'Distribusi ∨ atas ∧'},
  {f:'p ∨ (q ∧ r)',d:'Pertukaran operator'},
  {f:'(p ∧ q) ∧ (p ∧ r)',d:'Konjungsi ganda'},
],
ans:0,
hint:'Hukum Distribusi: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r). Mirip distributif dalam aljabar biasa.',
sol:[{e:'p ∧ (q ∨ r)',r:'Ekspresi awal'},{e:'(p ∧ q) ∨ (p ∧ r)',r:'Hukum Distribusi ∧ atas ∨'}],
explain:'Distribusi: p ∧ (q ∨ r) ≡ (p∧q)∨(p∧r). Artinya: (motor aktif dan sensor kiri) atau (motor aktif dan sensor kanan).'},

{id:11,level:'med',topic:'Biimplikasi',pts:10,
context:'🏛️ Hukum & Kebijakan',
story:`Sebuah pasal peraturan berbunyi: <strong>"Kontrak sah jika dan hanya jika kedua pihak setuju."</strong> Seorang pengacara ingin mengekspresikan kondisi biimplikasi ini dalam bentuk konjungsi implikasi dua arah untuk dokumen teknis.`,
props:[{sym:'p',def:'Pihak pertama setuju'},{sym:'q',def:'Pihak kedua setuju'}],
question:'Pasal "p ↔ q" (kontrak sah jika dan hanya jika) paling tepat ditulis ulang sebagai?',
formula:'p ↔ q',
type:'mc',
opts:[
  {f:'p → q',d:'Hanya satu arah implikasi'},
  {f:'(p → q) ∧ (q → p)',d:'Implikasi dua arah (definisi biimplikasi)'},
  {f:'p ∧ q',d:'Keduanya setuju saja'},
  {f:'p ∨ q',d:'Salah satu setuju'},
],
ans:1,
hint:'Biimplikasi adalah implikasi dua arah: p ↔ q ≡ (p→q) ∧ (q→p).',
sol:[{e:'p ↔ q',r:'Ekspresi awal'},{e:'(p → q) ∧ (q → p)',r:'Definisi Biimplikasi'}],
explain:'p ↔ q ≡ (p→q) ∧ (q→p). Kontrak sah jika: "jika p1 setuju maka p2 setuju" DAN "jika p2 setuju maka p1 setuju".'},

{id:12,level:'med',topic:'Penyerapan',pts:10,
context:'🌐 Jaringan Komputer',
story:`Sebuah kondisi routing jaringan berbunyi: <strong>"Paket dikirim jika: server aktif, atau (server aktif DAN koneksi stabil)."</strong> Developer menemukan kondisi ini dapat disederhanakan drastis.`,
props:[{sym:'p',def:'Server aktif'},{sym:'q',def:'Koneksi stabil'}],
question:'Kondisi routing p ∨ (p ∧ q) dapat disederhanakan menjadi?',
formula:'p ∨ (p ∧ q)',
type:'mc',
opts:[
  {f:'p ∧ q',d:'Keduanya harus terpenuhi'},
  {f:'q',d:'Hanya koneksi stabil'},
  {f:'p',d:'Cukup server aktif'},
  {f:'p ∨ q',d:'Server aktif atau koneksi stabil'},
],
ans:2,
hint:'Hukum Penyerapan (Absorption): p ∨ (p ∧ q) ≡ p.',
sol:[{e:'p ∨ (p ∧ q)',r:'Ekspresi awal'},{e:'p',r:'Hukum Penyerapan'}],
explain:'Hukum Penyerapan: p ∨ (p ∧ q) ≡ p. Kondisi routing cukup "server aktif" saja.'},

{id:13,level:'med',topic:'Identifikasi Hukum',pts:10,
context:'🏥 Sistem Medis',
story:`Sistem diagnostik menampilkan peringatan: <strong>"Pasien berisiko tinggi jika: demam DAN batuk, ATAU demam DAN sesak napas."</strong> Dokter senior ingin menyederhanakan kondisi ini.`,
props:[{sym:'p',def:'Demam'},{sym:'q',def:'Batuk'},{sym:'r',def:'Sesak napas'}],
question:'(p ∧ q) ∨ (p ∧ r) dapat disederhanakan menggunakan hukum apa?',
formula:'(p ∧ q) ∨ (p ∧ r)',
type:'mc',
opts:[
  {f:'p ∨ (q ∧ r) — Hukum Distribusi',d:'Distribusi ∨ atas ∧'},
  {f:'p ∧ (q ∨ r) — Hukum Distribusi',d:'Faktorkan p dari konjungsi'},
  {f:'p ∧ q ∧ r — Hukum Asosiatif',d:'Gabung semua konjungsi'},
  {f:'p ∨ q ∨ r — Hukum Komutatif',d:'Ubah semua menjadi disjungsi'},
],
ans:1,
hint:'Ini adalah kebalikan dari Hukum Distribusi: ∧ difaktorkan dari disjungsi.',
sol:[{e:'(p ∧ q) ∨ (p ∧ r)',r:'Ekspresi awal'},{e:'p ∧ (q ∨ r)',r:'Hukum Distribusi (faktorkan p)'}],
explain:'(p∧q)∨(p∧r) ≡ p∧(q∨r). Kondisi: "demam DAN (batuk ATAU sesak napas)".'},

{id:14,level:'med',topic:'Rantai Implikasi',pts:10,
context:'🤖 Kecerdasan Buatan',
story:`Sistem inferensi AI memiliki aturan: <strong>"Jika tidak mendeteksi objek (¬p), maka lanjutkan maju (q)."</strong> Developer ingin mengonversi aturan ini ke bentuk disjungsi untuk modul logika boolean.`,
props:[{sym:'p',def:'Objek terdeteksi'},{sym:'q',def:'Robot maju'}],
question:'Aturan "¬p → q" dikonversi menjadi?',
formula:'¬p → q',
type:'mc',
opts:[
  {f:'p ∨ q',d:'Objek terdeteksi atau robot maju'},
  {f:'¬p ∧ q',d:'Tidak terdeteksi DAN maju'},
  {f:'p ∧ ¬q',d:'Terdeteksi DAN tidak maju'},
  {f:'¬p ∨ ¬q',d:'Tidak terdeteksi atau tidak maju'},
],
ans:0,
hint:'Gunakan definisi implikasi: ¬p → q ≡ ¬(¬p) ∨ q ≡ p ∨ q.',
sol:[{e:'¬p → q',r:'Aturan asal'},{e:'¬(¬p) ∨ q',r:'Definisi Implikasi'},{e:'p ∨ q',r:'Negasi Ganda'}],
explain:'¬p → q ≡ p ∨ q. Kondisi: "objek terdeteksi ATAU robot maju".'},

{id:15,level:'med',topic:'Analisis Pembuktian',pts:10,
context:'🔐 Keamanan Sistem',
story:`Seorang auditor keamanan memeriksa rantai pembuktian berikut dan menemukan <strong>satu langkah yang menggunakan hukum SALAH</strong>. Temukan langkah yang keliru!`,
props:[{sym:'p',def:'Firewall aktif'},{sym:'q',def:'Sistem aman'}],
question:'Pada rantai pembuktian p → q ≡ ¬p ∨ q, langkah mana yang SALAH?',
formula:'p → q  →  ?  →  ¬p ∨ q',
type:'proof',
proofSteps:[
  {e:'p → q',        r:'Ekspresi awal',        correct:true},
  {e:'¬(¬p) → q',   r:'Negasi Ganda pada p',   correct:true},
  {e:'¬p ∧ q',       r:'⚠ Definisi Implikasi (SALAH!)', correct:false},
  {e:'¬p ∨ q',       r:'Seharusnya: ¬p ∨ q',   correct:true},
],
ans:2,
hint:'Perhatikan perubahan dari langkah 2 ke langkah 3. Apakah operator yang digunakan sudah benar?',
sol:[{e:'p → q ≡ ¬p ∨ q',r:'Definisi yang benar (BUKAN ∧)'},{e:'Langkah 3 menggunakan ∧ padahal harusnya ∨',r:'Kesalahan operator'}],
explain:'Langkah ke-3 salah: ¬(¬p) → q ≡ ¬p ∨ q (bukan ¬p ∧ q). Definisi implikasi menggunakan ∨ bukan ∧.'},

// ─── SULIT ─────────────────────────────────────────────────────────
{id:16,level:'hard',topic:'Multi-Hukum',pts:20,
context:'🔐 Keamanan Sistem',
story:`Sistem enkripsi memiliki kondisi kompleks: <strong>"Jika sistem tidak dienkripsi ATAU tidak ter-backup, maka data berisiko."</strong> Analis keamanan ingin menyederhanakan kondisi kapan data TIDAK berisiko.`,
props:[{sym:'p',def:'Sistem dienkripsi'},{sym:'q',def:'Sistem ter-backup'},{sym:'r',def:'Data berisiko'}],
question:'Kondisi "data tidak berisiko" ¬((¬p ∨ ¬q) → r) ekuivalen dengan?',
formula:'¬((¬p ∨ ¬q) → r)',
type:'mc',
opts:[
  {f:'(¬p ∨ ¬q) ∧ ¬r',d:'Tidak enkripsi/backup DAN tidak berisiko'},
  {f:'(p ∧ q) ∨ ¬r',d:'Enkripsi dan backup, atau tidak berisiko'},
  {f:'¬p ∨ ¬q ∨ ¬r',d:'Salah satu dari tiga kondisi negatif'},
  {f:'p ∧ q ∧ ¬r',d:'Harus enkripsi, backup, DAN tidak berisiko'},
],
ans:0,
hint:'Gunakan ¬(A→B) ≡ A ∧ ¬B. Identifikasi A dan B dalam ekspresi ini.',
sol:[{e:'¬((¬p∨¬q) → r)',r:'Ekspresi awal'},{e:'(¬p ∨ ¬q) ∧ ¬r',r:'¬(A→B) ≡ A ∧ ¬B'}],
explain:'¬(A→B) ≡ A ∧ ¬B. Maka ¬((¬p∨¬q)→r) ≡ (¬p∨¬q) ∧ ¬r.'},

{id:17,level:'hard',topic:'Ekspansi Lengkap',pts:20,
context:'🌐 Jaringan Komputer',
story:`Protokol jaringan memiliki syarat: <strong>"Paket diteruskan jika dan hanya jika: (koneksi aktif DAN autentikasi berhasil) ATAU (mode bypass DAN admin login)."</strong> Seorang network architect ingin menyatakan kapan protokol ini GAGAL.`,
props:[{sym:'p',def:'Koneksi aktif'},{sym:'q',def:'Autentikasi berhasil'},{sym:'r',def:'Mode bypass'},{sym:'s',def:'Admin login'}],
question:'Kapan kondisi transmisi ¬((p ∧ q) ∨ (r ∧ s)) terjadi (protokol gagal)?',
formula:'¬((p ∧ q) ∨ (r ∧ s))',
type:'mc',
opts:[
  {f:'¬(p ∧ q) ∧ ¬(r ∧ s)',d:'Keduanya tidak terpenuhi (De Morgan)'},
  {f:'¬p ∧ ¬q ∧ ¬r ∧ ¬s',d:'Semua variabel negatif'},
  {f:'(¬p ∨ ¬q) ∧ (¬r ∨ ¬s)',d:'Salah satu gagal di tiap pasang (De Morgan + De Morgan)'},
  {f:'(¬p ∧ ¬q) ∨ (¬r ∧ ¬s)',d:'Satu pasang keduanya gagal'},
],
ans:2,
hint:'Terapkan De Morgan dua kali: pertama pada disjungsi luar, lalu pada setiap konjungsi dalam.',
sol:[
  {e:'¬((p∧q) ∨ (r∧s))',r:'Ekspresi awal'},
  {e:'¬(p∧q) ∧ ¬(r∧s)',r:'De Morgan pada ∨'},
  {e:'(¬p∨¬q) ∧ (¬r∨¬s)',r:'De Morgan pada ∧ (dua kali)'},
],
explain:'Dua kali De Morgan: ¬((p∧q)∨(r∧s)) ≡ (¬p∨¬q) ∧ (¬r∨¬s). Protokol gagal jika salah satu elemen di tiap pasang tidak memenuhi.'},

{id:18,level:'hard',topic:'Rantai Panjang',pts:20,
context:'🏥 Sistem Medis',
story:`Sistem ICU rumah sakit menggunakan aturan kompleks: <strong>"Jika pasien sadar (p) dan detak jantung normal (q), maka berikan (obat A (r) atau obat B (s))."</strong> Peneliti ingin mengekspansi penuh aturan ini menjadi bentuk paling dasar.`,
props:[{sym:'p',def:'Pasien sadar'},{sym:'q',def:'Detak jantung normal'},{sym:'r',def:'Obat A diberikan'},{sym:'s',def:'Obat B diberikan'}],
question:'Aturan (p ∧ q) → (r ∨ s) paling tepat diubah menjadi?',
formula:'(p ∧ q) → (r ∨ s)',
type:'mc',
opts:[
  {f:'p ∧ q ∧ (r ∨ s)',d:'Konjungsi kondisi dan hasil'},
  {f:'¬(p ∧ q) ∨ (r ∨ s)',d:'Definisi implikasi dengan anteseden tersusun'},
  {f:'(¬p ∨ ¬q) ∨ (r ∨ s)',d:'Distribusi De Morgan pada anteseden'},
  {f:'¬p ∨ ¬q ∨ r ∨ s',d:'Bentuk paling sederhana (ekuivalen dengan c)'},
],
ans:3,
hint:'Terapkan: implikasi → disjungsi, lalu De Morgan pada ¬(p∧q), lalu asosiatif.',
sol:[
  {e:'(p∧q) → (r∨s)',r:'Ekspresi awal'},
  {e:'¬(p∧q) ∨ (r∨s)',r:'Definisi Implikasi'},
  {e:'(¬p∨¬q) ∨ (r∨s)',r:'De Morgan'},
  {e:'¬p ∨ ¬q ∨ r ∨ s',r:'Asosiatif (paling sederhana)'},
],
explain:'(p∧q)→(r∨s) ≡ ¬p∨¬q∨r∨s. Pilihan C dan D ekuivalen, tapi D adalah bentuk paling sederhana.'},

{id:19,level:'hard',topic:'Analisis Bukti Salah',pts:20,
context:'🤖 Kecerdasan Buatan',
story:`Tim AI menguji klaim ekuivalensi: <strong>"(p → q) ∧ (p → r) ≡ p → (q ∧ r)".</strong> Seorang insinyur menyajikan rantai pembuktian berikut. <strong>Temukan langkah pembuktian yang menggunakan hukum KELIRU.</strong>`,
props:[{sym:'p',def:'Input valid'},{sym:'q',def:'Output benar'},{sym:'r',def:'Respons cepat'}],
question:'Langkah mana yang menggunakan hukum yang SALAH dalam pembuktian berikut?',
formula:'(p→q) ∧ (p→r)  ≡  p→(q∧r)',
type:'proof',
proofSteps:[
  {e:'(p→q) ∧ (p→r)',      r:'Ekspresi awal',                    correct:true},
  {e:'(¬p∨q) ∧ (¬p∨r)',   r:'Definisi Implikasi (keduanya)',     correct:true},
  {e:'¬p ∧ (q∨r)',          r:'⚠ Distribusi (SALAH: ∧ harusnya ∨)', correct:false},
  {e:'¬p ∨ (q∧r)',          r:'Seharusnya: Distribusi ∨ atas ∧',  correct:true},
  {e:'p → (q∧r)',            r:'Definisi Implikasi (balik)',         correct:true},
],
ans:2,
hint:'Periksa langkah 3: hukum distribusi yang digunakan antara langkah 2 dan 3. Operator apa yang seharusnya?',
sol:[{e:'(¬p∨q) ∧ (¬p∨r) ≡ ¬p ∨ (q∧r)',r:'Distribusi ∨ atas ∧ (bukan ∧ atas ∨)'},{e:'Langkah 3 menggunakan ∧ di luar, padahal seharusnya ∨',r:'Karena faktor bersama adalah ¬p dalam disjungsi'}],
explain:'Langkah 3 salah: (¬p∨q)∧(¬p∨r) ≡ ¬p∨(q∧r), bukan ¬p∧(q∨r). Ini distribusi ∨ atas ∧.'},

{id:20,level:'hard',topic:'Pembuktian Tautologi',pts:20,
context:'🏛️ Hukum & Kebijakan',
story:`Mahkamah Agung mengevaluasi prinsip logika hukum: <strong>"Jika ada bukti maka seseorang bersalah, DAN jika tidak ada bukti maka seseorang tidak bersalah — ini berarti: ada bukti jika dan hanya jika bersalah."</strong> Apakah argumen ini valid sebagai tautologi?`,
props:[{sym:'p',def:'Ada bukti'},{sym:'q',def:'Seseorang bersalah'}],
question:'Apakah (p→q) ∧ (¬p→¬q) ≡ (p ↔ q) merupakan ekuivalensi yang valid?',
formula:'(p→q) ∧ (¬p→¬q)',
type:'mc',
opts:[
  {f:'Ya, ekuivalen — karena (p→q) ∧ (¬p→¬q) ≡ (p ↔ q)',d:'Prinsip hukum tersebut valid secara logis'},
  {f:'Tidak ekuivalen — (p→q) ∧ (¬p→¬q) ≡ p ∧ q saja',d:'Hanya benar jika keduanya benar'},
  {f:'Tidak ekuivalen — (p→q) ∧ (¬p→¬q) selalu Salah',d:'Merupakan kontradiksi'},
  {f:'Tidak dapat ditentukan tanpa nilai p dan q',d:'Bergantung pada kasusnya'},
],
ans:0,
hint:'Ekspansi: (p→q) = ¬p∨q dan (¬p→¬q) = p∨¬q. Kalikan keduanya lalu bandingkan dengan (p∧q)∨(¬p∧¬q).',
sol:[
  {e:'(p→q) ∧ (¬p→¬q)',r:'Ekspresi awal'},
  {e:'(¬p∨q) ∧ (p∨¬q)',r:'Definisi Implikasi keduanya'},
  {e:'(p∧q) ∨ (¬p∧¬q)',r:'Distribusi & penyederhanaan'},
  {e:'p ↔ q',r:'Definisi Biimplikasi — TERBUKTI EKUIVALEN'},
],
explain:'(p→q)∧(¬p→¬q) ≡ p↔q. Prinsip hukum ini valid: ada bukti ↔ bersalah adalah biimplikasi yang sah.'},
];

// ════════════════════════════════════════
//  STATE
// ════════════════════════════════════════
let state={};
Qs.forEach(q=>{state[q.id]={done:false,correct:false,pts:0};});
let nC=0,nW=0,nP=0,filter='all';

// ════════════════════════════════════════
//  RENDER
// ════════════════════════════════════════
function render(){
  const wrap=document.getElementById('qWrap');
  wrap.innerHTML='';
  const list=filter==='all'?Qs:Qs.filter(q=>q.level===filter);
  list.forEach((q,idx)=>{
    const card=document.createElement('div');
    card.className='q-card';card.id=`card-${q.id}`;
    card.style.animationDelay=(idx*0.04)+'s';
    card.innerHTML=buildCard(q);
    wrap.appendChild(card);
  });
  buildJumps();
  // init sortable proof if any
}

function buildCard(q){
  const lvMap={easy:'Mudah',med:'Sedang',hard:'Sulit'};
  let body='';
  if(q.type==='mc') body=buildMC(q);
  else if(q.type==='tt') body=buildTT(q);
  else if(q.type==='proof') body=buildProof(q);

  const propHTML=q.props.map(p=>`<div class="prop-pill"><span>${p.sym}</span> = ${p.def}</div>`).join('');

  return `
    <div class="q-strip strip-${q.level}"></div>
    <div class="q-meta-row">
      <div class="q-num-badge" id="qnb-${q.id}">${q.id}</div>
      <span class="q-badge badge-${q.level}">${lvMap[q.level]}</span>
      <span class="q-topic">${q.topic}</span>
      <span class="q-pts">${q.pts} poin</span>
    </div>
    <div class="story-block">
      <div class="story-context">${q.context}</div>
      <div class="story-text">${q.story}</div>
    </div>
    <div class="prop-defs">${propHTML}</div>
    <div class="q-question">${q.question}</div>
    <div class="q-formula-wrap"><div class="q-formula">${q.formula}</div></div>
    <div class="q-body">
      <div class="hint-box" id="hint-${q.id}">
        <div class="hint-lbl">💡 Petunjuk</div>
        <div class="hint-txt">${q.hint}</div>
      </div>
      <div class="sol-box" id="sol-${q.id}">
        <div class="sol-lbl">// Langkah Pembuktian</div>
        ${(q.sol||[]).map((s,i)=>`<div class="sol-step"><span class="ss-n">${i+1}.</span><span class="ss-e">${s.e}</span><span class="ss-r">${s.r}</span></div>`).join('')}
      </div>
      ${body}
      <div class="q-actions">
        ${q.type!=='mc'?`<button class="btn-check" id="btn-${q.id}" onclick="checkQ(${q.id})">▶ CEK JAWABAN</button>`:''}
        <button class="btn-hint" onclick="toggleHint(${q.id})">💡 Petunjuk</button>
        <button class="btn-sol"  onclick="toggleSol(${q.id})">∑ Pembahasan</button>
      </div>
      <div class="q-feedback" id="fb-${q.id}"></div>
    </div>`;
}

function buildMC(q){
  const keys=['A','B','C','D'];
  return `<div class="mc-opts" id="mc-${q.id}">`+
    q.opts.map((o,i)=>`
      <button class="mc-opt" onclick="pickMC(${q.id},${i})" id="mo-${q.id}-${i}" data-i="${i}">
        <span class="ok">${keys[i]}</span>
        <div class="mc-opt-text">
          <span class="mc-opt-formula">${o.f}</span>
          <span class="mc-opt-desc">${o.d}</span>
        </div>
      </button>`).join('')+
  `</div>`;
}

function buildTT(q){
  let html=`<div class="tt-wrap"><table><thead><tr>`;
  q.headers.forEach((h,hi)=>{
    const isTgt=q.targetCols&&q.targetCols.includes(hi);
    html+=`<th${isTgt?' class="hi"':''}>${h}</th>`;
  });
  html+=`</tr></thead><tbody>`;
  q.trows.forEach((row,ri)=>{
    html+=`<tr>`;
    q.headers.forEach((_,ci)=>{
      if(q.trows[ri].blank&&q.trows[ri].blank.col===ci){
        html+=`<td><select class="tt-sel" id="tts-${q.id}-${ri}"><option value="">?</option><option>T</option><option>F</option></select></td>`;
      } else {
        html+=`<td>${tv(row.vals[ci])}</td>`;
      }
    });
    html+=`</tr>`;
  });
  html+=`</tbody></table></div>`;
  return html;
}

function buildProof(q){
  let html=`<div class="proof-verify"><div class="proof-title">// Klik baris yang menggunakan hukum SALAH</div><div class="proof-chain" id="pchain-${q.id}">`;
  q.proofSteps.forEach((s,i)=>{
    html+=`<div class="proof-row" id="pr-${q.id}-${i}" onclick="selectProofRow(${q.id},${i})">
      <div class="proof-radio" id="prad-${q.id}-${i}"></div>
      <div class="pr-step pr-expr">${s.e}</div>
      <div class="pr-rule${s.correct?'':' wrong-rule'}">${s.r}</div>
    </div>`;
  });
  html+=`</div></div>`;
  return html;
}

// ════════════════════════════════════════
//  ANSWER LOGIC
// ════════════════════════════════════════
function pickMC(qid,oi){
  const q=Qs.find(x=>x.id===qid);
  if(state[qid].done)return;
  state[qid].done=true;
  const correct=oi===q.ans;
  state[qid].correct=correct;
  q.opts.forEach((_,i)=>{
    const b=document.getElementById(`mo-${qid}-${i}`);
    b.disabled=true;
    if(i===q.ans)b.classList.add('correct');
    else if(i===oi)b.classList.add('wrong');
  });
  finalize(qid,correct,q.explain,q.pts);
}

let selectedProofRow={};
function selectProofRow(qid,idx){
  const q=Qs.find(x=>x.id===qid);
  if(state[qid].done)return;
  // deselect all
  q.proofSteps.forEach((_,i)=>{
    document.getElementById(`pr-${qid}-${i}`)?.classList.remove('selected');
  });
  document.getElementById(`pr-${qid}-${idx}`)?.classList.add('selected');
  selectedProofRow[qid]=idx;
}

function checkQ(qid){
  const q=Qs.find(x=>x.id===qid);
  if(state[qid].done)return;
  if(q.type==='tt') checkTT(qid);
  else if(q.type==='proof') checkProof(qid);
}

function checkTT(qid){
  const q=Qs.find(x=>x.id===qid);
  let allC=true;
  q.trows.forEach((row,ri)=>{
    if(!row.blank)return;
    const sel=document.getElementById(`tts-${qid}-${ri}`);
    if(!sel)return;
    const c=sel.value===row.blank.ans;
    if(!c)allC=false;
    sel.classList.add(c?'c':'w');
    sel.disabled=true;
    if(!c){const o=sel.querySelector(`option[value="${row.blank.ans}"]`);if(o)o.selected=true;}
  });
  state[qid].done=true;
  finalize(qid,allC,q.explain,q.pts);
}

function checkProof(qid){
  const q=Qs.find(x=>x.id===qid);
  const sel=selectedProofRow[qid];
  if(sel===undefined){
    const fb=document.getElementById(`fb-${qid}`);
    fb.className='q-feedback show err';
    fb.innerHTML='<div class="fb-title">⚠ Perhatian</div><div class="fb-body">Pilih dahulu langkah yang kamu anggap salah.</div>';
    return;
  }
  const correct=sel===q.ans;
  state[qid].done=true;
  // mark rows
  q.proofSteps.forEach((_,i)=>{
    const row=document.getElementById(`pr-${qid}-${i}`);
    if(!row)return;
    row.classList.remove('selected');
    if(i===q.ans) row.classList.add('correct-sel');
    else if(i===sel&&!correct) row.classList.add('wrong-sel');
  });
  document.getElementById(`btn-${qid}`).disabled=true;
  finalize(qid,correct,q.explain,q.pts);
}

function finalize(qid,correct,explain,pts){
  state[qid].correct=correct;
  if(correct){state[qid].pts=pts;nC++;nP+=pts;}else nW++;
  const fb=document.getElementById(`fb-${qid}`);
  fb.className=`q-feedback show ${correct?'ok':'err'}`;
  fb.innerHTML=`<div class="fb-title">${correct?'✓ TEPAT':'✗ BELUM TEPAT'}</div><div class="fb-body">${explain}</div>`;
  const card=document.getElementById(`card-${qid}`);
  card.classList.add(correct?'done-c':'done-w');
  document.getElementById(`qnb-${qid}`).textContent=qid;
  updateStats();
  updateJump(qid,correct);
  if(nC+nW===Qs.length)setTimeout(showScore,800);
}

// ════════════════════════════════════════
//  STATS
// ════════════════════════════════════════
function updateStats(){
  document.getElementById('stC').textContent=nC;
  document.getElementById('stW').textContent=nW;
  document.getElementById('stS').textContent=nP;
  const done=nC+nW;
  const pct=Math.round(done/Qs.length*100);
  document.getElementById('stPct').textContent=pct+'%';
}

function buildJumps(){
  const wrap=document.getElementById('jumpDots');
  wrap.innerHTML=Qs.map(q=>`
    <button class="jdot" id="jd-${q.id}" onclick="jumpTo(${q.id})" title="Soal ${q.id}">${q.id}</button>`).join('');
}
function updateJump(qid,correct){
  const b=document.getElementById(`jd-${qid}`);
  if(b)b.className=`jdot ${correct?'done-c':'done-w'}`;
}
function jumpTo(qid){document.getElementById(`card-${qid}`)?.scrollIntoView({behavior:'smooth',block:'start'});}

// ════════════════════════════════════════
//  SCORE
// ════════════════════════════════════════
function showScore(){
  const maxPts=Qs.reduce((a,q)=>a+q.pts,0);
  const pct=Math.round(nP/maxPts*100);
  document.getElementById('sbPct').textContent=pct+'%';
  document.getElementById('sbC').textContent=nC;
  document.getElementById('sbW').textContent=nW;
  document.getElementById('sbP').textContent=nP;
  const grades=[
    [90,'Luar biasa! Kamu siap menjadi ahli logika matematika. 🏆'],
    [75,'Sangat baik! Analisis ekuivalensimu sudah sangat solid. 🎯'],
    [60,'Baik! Latih lebih banyak soal multi-hukum dan pembuktian. 💪'],
    [40,'Cukup. Baca ulang hukum De Morgan, Distribusi, dan Implikasi. 📖'],
    [0, 'Jangan menyerah! Mulai dari materi dasar dan coba lagi. 🔄'],
  ];
  document.getElementById('sbGrade').textContent=grades.find(([t])=>pct>=t)[1];
  // Detail breakdown by level
  const levels=[['easy','Mudah'],['med','Sedang'],['hard','Sulit']];
  const det=levels.map(([lv,nm])=>{
    const lvQs=Qs.filter(q=>q.level===lv);
    const c=lvQs.filter(q=>state[q.id].correct).length;
    return `<div class="sd-row"><span class="sd-lbl">${nm} (${lvQs.length} soal)</span><span class="sd-val ${c===lvQs.length?'c':'w'}">${c} / ${lvQs.length} benar</span></div>`;
  }).join('');
  document.getElementById('sbDetail').innerHTML=det;
  const sb=document.getElementById('scoreboard');
  sb.classList.add('show');
  sb.scrollIntoView({behavior:'smooth',block:'center'});
}

// ════════════════════════════════════════
//  FILTER & HELPERS
// ════════════════════════════════════════
function setFilter(lv,btn){
  filter=lv;
  document.querySelectorAll('.lbtn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  render();
}

function toggleHint(qid){document.getElementById(`hint-${qid}`)?.classList.toggle('show');}
function toggleSol(qid){document.getElementById(`sol-${qid}`)?.classList.toggle('show');}

function retryAll(){
  state={};nC=0;nW=0;nP=0;selectedProofRow={};
  Qs.forEach(q=>{state[q.id]={done:false,correct:false,pts:0};});
  document.getElementById('scoreboard').classList.remove('show');
  updateStats();render();
  window.scrollTo({top:0,behavior:'smooth'});
}

// ════════════════════════════════════════
//  INIT
// ════════════════════════════════════════
render();
</script>
</body>
</html>
        """
        tampilkan6 = keterangan(tulisanHTML5,18000)
        tampilkan6.tampilkan()
    
def diagnosa():
    st.title("Tes Diagnosis Logika Proposisi dan Ekuivalensi Logis")

    st.write("Silakan jawab pertanyaan berikut")

    nama = st.text_input("Nama")
    nim = st.text_input("NIM")

    q1 = st.radio(
    "Pernyataan majemuk adalah",
    [
    "Pernyataan tunggal",
    "Gabungan dua pernyataan atau lebih dengan operator logika",
    "Pernyataan tanpa nilai kebenaran",
    "Pernyataan acak"
    ],index=None)

    q2 = st.radio(
    "Negasi dari p adalah",
    [
    "¬p",
    "p ∧ q",
    "p → q",
    "p ↔ q"
    ],index=None)

    q3 = st.radio(
    "Nilai p ∧ q jika p benar dan q salah",
    [
    "Benar",
    "Salah"
    ],index=None)

    q4 = st.radio(
    "Bentuk ekuivalen dari p → q",
    [
    "¬p ∨ q",
    "p ∧ q",
    "¬q ∧ p",
    "p ∨ q"
    ],index=None)

    q5 = st.radio(
    "Hukum De Morgan dari ¬(p ∧ q)",
    [
    "¬p ∧ ¬q",
    "¬p ∨ ¬q",
    "p ∨ q",
    "p ∧ q"
    ],index=None)

    q6 = st.radio(
    "Kontraposisi dari p → q",
    [
    "¬q → ¬p",
    "¬p → ¬q",
    "p → ¬q",
    "q → p"
    ],index=None)

    q7 = st.radio(
    "Jika p benar dan q benar maka p ↔ q bernilai",
    [
    "Benar",
    "Salah"
    ],index=None)

    q8 = st.radio(
    "Ekuivalen dari ¬(p ∨ q)",
    [
    "¬p ∧ ¬q",
    "¬p ∨ ¬q",
    "p ∧ q",
    "p ∨ q"
    ],index=None)

    q9 = st.radio(
    "Jika p → q bernilai salah maka",
    [
    "p benar dan q salah",
    "p salah q benar",
    "keduanya benar",
    "keduanya salah"
    ],index=None)

    q10 = st.radio(
    "Bentuk ekuivalen dari p ↔ q",
    [
    "(p → q) ∧ (q → p)",
    "(p ∧ q)",
    "(p ∨ q)",
    "(¬p ∨ q)"
    ],index=None)

    if st.button("Kirim Jawaban"):

        url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfDlWfGHLuAE5F_1_4QLprZwCFmC_ucpGq5B3nvQXtTL7gEKQ/formResponse"

        data = {
        "entry.1779161901": nama,
        "entry.1291677323": nim,
        "entry.131515434": q1,
        "entry.1711566388": q2,
        "entry.345458461": q3,
        "entry.251087534": q4,
        "entry.781235522": q5,
        "entry.1258144973": q6,
        "entry.1796185779": q7,
        "entry.1976700686": q8,
        "entry.1792238714": q9,
        "entry.1639207856": q10
        }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            st.success("Jawaban berhasil dikirim ke Google Form")
        else:
            st.error("Terjadi kesalahan saat mengirim data")

def gambaran():
    st.title("Upload Jawaban Tulisan Tangan")
    nama = st.text_input("Nama")
    nim = st.text_input("NIM")

    foto = st.camera_input("Foto Jawaban")

    if st.button("Upload"):

        if foto is not None:

            url = "https://api.cloudinary.com/v1_1/ikip-siliwangi/image/upload"

            files = {"file": foto.getvalue()}

            data = {
                "upload_preset": "ml_default",
                "public_id": f"{nama}_{nim}"
            }

            response = requests.post(url, files=files, data=data)

            result = response.json()

            if "secure_url" in result:
                st.success("Upload berhasil")
                st.write(result["secure_url"])
            else:
                st.error("Upload gagal")
                st.write(result)
def dataAngket():
    st.title("Angket Kepuasan Mahasiswa")
    st.subheader("Pembelajaran Logika Proposisi dan Ekuivalensi Logis")

    st.write("Silakan isi angket berikut dengan jujur.")

    nama = st.text_input("Nama")
    nim = st.text_input("NIM")

    skala = [
    "Sangat Tidak Setuju",
    "Tidak Setuju",
    "Netral",
    "Setuju",
    "Sangat Setuju"
    ]

    q1 = st.radio("1. Materi logika proposisi mudah dipahami", skala, index=None)
    q2 = st.radio("2. Penjelasan tentang pernyataan majemuk membantu pemahaman saya", skala, index=None)
    q3 = st.radio("3. Saya memahami penggunaan operator logika (¬, ∧, ∨, →, ↔)", skala, index=None)
    q4 = st.radio("4. Contoh soal membantu memahami konsep logika proposisi", skala, index=None)
    q5 = st.radio("5. Saya memahami konsep ekuivalensi logis", skala, index=None)

    q6 = st.radio("6. Media pembelajaran yang digunakan menarik", skala, index=None)
    q7 = st.radio("7. Pembelajaran membuat saya lebih aktif berpikir logis", skala, index=None)
    q8 = st.radio("8. Penjelasan dosen mudah diikuti", skala, index=None)
    q9 = st.radio("9. Kegiatan pembelajaran membantu memahami tabel kebenaran", skala, index=None)
    q10 = st.radio("10. Latihan soal meningkatkan pemahaman saya", skala, index=None)

    q11 = st.radio("11. Pembelajaran meningkatkan kemampuan berpikir logis saya", skala, index=None)
    q12 = st.radio("12. Saya lebih percaya diri mempelajari logika matematika", skala, index=None)
    q13 = st.radio("13. Materi logika proposisi bermanfaat untuk mata kuliah lain", skala, index=None)
    q14 = st.radio("14. Saya memahami hubungan logika proposisi dan matematika diskrit", skala, index=None)
    q15 = st.radio("15. Pembelajaran membantu memahami pembuktian matematika", skala, index=None)

    q16 = st.radio("16. Media pembelajaran mudah digunakan", skala, index=None)
    q17 = st.radio("17. Media pembelajaran membuat materi lebih menarik", skala, index=None)
    q18 = st.radio("18. Tampilan media jelas dan nyaman dilihat", skala, index=None)
    q19 = st.radio("19. Saya tertarik menggunakan media ini untuk belajar materi lain", skala, index=None)
    q20 = st.radio("20. Secara keseluruhan saya puas dengan pembelajaran ini", skala, index=None)

    if st.button("Kirim Angket"):

        if None in [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]:
            st.warning("Semua pertanyaan harus dijawab")
        else:

            url = "https://docs.google.com/forms/d/e/FORM_ID/formResponse"

            data = {
            "entry.111111": nama,
            "entry.222222": nim,
            "entry.333333": q1,
            "entry.444444": q2,
            "entry.555555": q3,
            "entry.666666": q4,
            "entry.777777": q5,
            "entry.888888": q6,
            "entry.999999": q7,
            "entry.101010": q8,
            "entry.1111111": q9,
            "entry.1212121": q10,
            "entry.1313131": q11,
            "entry.1414141": q12,
            "entry.1515151": q13,
            "entry.1616161": q14,
            "entry.1717171": q15,
            "entry.1818181": q16,
            "entry.1919191": q17,
            "entry.2020202": q18,
            "entry.2121212": q19,
            "entry.2222222": q20
            }

            r = requests.post(url, data=data)

            if r.status_code == 200:
                st.success("Terima kasih, angket berhasil dikirim")
            else:
                st.error("Terjadi kesalahan saat mengirim data")

def materi2():
    bagian = st.tabs(['test diagnostik','Materi, simulasi dan latihan','Soal Cerita Analisis'])
    with bagian[0]:
        st.title("Diagnosis Logika Matematika")

        nama = st.text_input("Nama Mahasiswa")

        soal = [
        ("Negasi dari ∀x∈ℝ, x² ≥ 0 adalah...",
        ["∀x x² < 0","∃x x² < 0","∃x x² ≥ 0","∀x x² = 0"],"∃x x² < 0"),

        ("Negasi dari ∃x∈ℕ, x+1=0 adalah...",
        ["∀x x+1≠0","∃x x+1≠0","∀x x+1=0","Tidak ada"],"∀x x+1≠0"),

        ("Makna ∃x∈ℤ sehingga x²=4 adalah...",
        ["Semua","Ada bilangan","Tidak ada","Hanya satu"],"Ada bilangan"),

        ("Negasi dari ∀x(x>2→x²>4) adalah...",
        ["∃x x>2 dan x²≤4","∀x x>2 dan x²≤4","∃x x≤2","∀x x²≤4"],"∃x x>2 dan x²≤4"),

        ("Ekuivalen dari ¬∀xP(x) adalah...",
        ["∀x¬P(x)","∃x¬P(x)","¬∃xP(x)","∀xP(x)"],"∃x¬P(x)"),

        ("Jika belajar maka lulus. Belajar.",
        ["Lulus","Tidak lulus","Tidak belajar","Tidak dapat"],"Lulus"),

        ("Jika hujan maka jalan basah. Jalan tidak basah.",
        ["Hujan","Tidak hujan","Jalan kering","Tidak dapat"],"Tidak hujan"),

        ("Jika belajar maka pintar. Jika pintar maka sukses.",
        ["Jika belajar maka sukses","Jika sukses maka belajar","Jika belajar tidak sukses","Tidak dapat"],"Jika belajar maka sukses"),

        ("p∨q, ¬p",
        ["¬q","q","p","p∧q"],"q"),

        ("Jika rajin maka nilai baik. Nilai tidak baik.",
        ["Mahasiswa rajin","Mahasiswa tidak rajin","Nilai baik","Tidak dapat"],"Mahasiswa tidak rajin")
        ]

        jawaban_user = []
        skor = 0

        for i,(pertanyaan,opsi,kunci) in enumerate(soal):
            j = st.radio(f"Soal {i+1}: {pertanyaan}", opsi, key=i,index=None)
            jawaban_user.append(j)

        if st.button("Kirim Jawaban"):

            for i,(pertanyaan,opsi,kunci) in enumerate(soal):
                if jawaban_user[i] == kunci:
                    skor += 10


            url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdfmv_ZOyzf4hW6QSD8t1zu2lWdao8-_PUQif_OMFwcdgvkAA/formResponse"

            data = {
            "entry.1698168152": nama,
            "entry.1542413306": skor,
            "entry.2135798620": jawaban_user[0],
            "entry.677665291": jawaban_user[1],
            "entry.1873132860": jawaban_user[2],
            "entry.1526336051": jawaban_user[3],
            "entry.688660511": jawaban_user[4],
            "entry.452120346": jawaban_user[5],
            "entry.1064866662": jawaban_user[6],
            "entry.2093701058": jawaban_user[7],
            "entry.845029584": jawaban_user[8],
            "entry.2068687803": jawaban_user[9]
            }

            requests.post(url,data=data)

            st.success("Jawaban berhasil dikirim ke database Google Form")
    with bagian[1]:
        tulisanHTML = "<iframe src='https://martin-bernard26.github.io/matematikaDiskritB12023html/kuantor.html' style='width:100%; height:1000px'></iframe>"
        tampil = keterangan(tulisanHTML,1000)
        tampil.tampilkan()
    with bagian[2]:
        tulisanHTML = "<iframe src='https://martin-bernard26.github.io/matematikaDiskritB12023html/soalTantangan1.html' style='width:100%; height:1000px'></iframe>"
        tampil = keterangan(tulisanHTML,1000)
        tampil.tampilkan()

def buku():
    st.title("Baca Buku Online")
    with st.expander("Samuel Wibisono"):
        st.markdown('<iframe src="https://drive.google.com/file/d/1TyeaVyc5vUGQs_2RDZi7coimKa8mfZbW/preview" width="100%" height="1000"></iframe>',unsafe_allow_html=True)
    with st.expander("Dr. Agus Wibowo, M.Kom, M.Si, MM"):
        st.markdown('<iframe src="https://drive.google.com/file/d/1-V8jWTdfJdPpSOnJmzeJlcNANTBzWZ2H/preview" width="100%" height="1000"></iframe>',unsafe_allow_html=True)
    with st.expander("Kenneth H. Rosen"):
        st.markdown('<iframe src="https://drive.google.com/file/d/1V1FSnkZu_VTs-4zgbA-EK1Zf6zvAPO6N/preview" width="100%" height="1000"></iframe>',unsafe_allow_html=True)

def materi3():
    menu1 = st.tabs(['test kemampuan','Materi','contoh soal','Latihan'])
    with menu1[0]:
        tulisanHTML = "<iframe src='https://martin-bernard26.github.io/matematikaDiskritB12023html/testAwalHimpunan1.html' style='width:100%; height:1000px'></iframe>"
        tampil = keterangan(tulisanHTML,1000)
        tampil.tampilkan()
    with menu1[1]:
        tulisanHTML = "<iframe src='https://martin-bernard26.github.io/matematikaDiskritB12023html/teoriHimpunan.html' style='width:100%; height:1000px'></iframe>"
        tampil = keterangan(tulisanHTML,1000)
        tampil.tampilkan()
    with menu1[2]:
        tulisanHTML = "<iframe src='https://martin-bernard26.github.io/matematikaDiskritB12023html/contoh3.html' style='width:100%; height:1000px'></iframe>"
        tampil = keterangan(tulisanHTML,1000)
        tampil.tampilkan()
    with menu1[3]:
        tulisanHTML = "<iframe src='https://martin-bernard26.github.io/matematikaDiskritB12023html/latihan3.html' style='width:100%; height:1000px'></iframe>"
        tampil = keterangan(tulisanHTML,1000)
        tampil.tampilkan()
#====================

if st.session_state['kumpulan']['kover']:
    Pendahuluan()
if st.session_state['kumpulan']['pertemuan1']:
    materi1()
if st.session_state['kumpulan']['diag']:
    diagnosa()
if st.session_state['kumpulan']['foto']:
    gambaran()
if st.session_state['kumpulan']['pertemuan2']:
    materi2()
if st.session_state['kumpulan']['perpustakaan']:
    buku()
if st.session_state['kumpulan']['pertemuan3']:
    materi3()
#=====================

if st.sidebar.button("pendahuluan"):
    st.session_state['kumpulan']={'kover':True,'perpustakaan':False,'diag':False,'angket':False,'foto':False,'pertemuan1':False,'pertemuan2':False,
                                  'pertemuan3':False}
    st.rerun()
if st.sidebar.button("Perpustakaan"):
    st.session_state['kumpulan']={'kover':False,'perpustakaan':True,'diag':False,'angket':False,'foto':False,'pertemuan1':False,'pertemuan2':False,
                                  'pertemuan3':False}
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button('Test diagnosa'):
    st.session_state['kumpulan']={'kover':False,'perpustakaan':False,'diag':True,'angket':False,'foto':False,'pertemuan1':False,'pertemuan2':False,
                                  'pertemuan3':False}
    st.rerun()
if st.sidebar.button('Angket'):
    st.session_state['kumpulan']={'kover':False,'perpustakaan':False,'diag':False,'angket':True,'foto':False,'pertemuan1':False,'pertemuan2':False,
                                  'pertemuan3':False}
    st.rerun()
if st.sidebar.button('foto'):
    st.session_state['kumpulan']={'kover':False,'perpustakaan':False,'diag':False,'angket':False,'foto':True,'pertemuan1':False,'pertemuan2':False,
                                  'pertemuan3':False}
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button("Pertemuan 1"):
    st.session_state['kumpulan']={'kover':False,'perpustakaan':False,'diag':False,'angket':False,'foto':False,'pertemuan1':True,'pertemuan2':False,
                                  'pertemuan3':False}
    st.rerun()
if st.sidebar.button("Pertemuan 2"):
    st.session_state['kumpulan']={'kover':False,'perpustakaan':False,'diag':False,'angket':False,'foto':False,'pertemuan1':False,'pertemuan2':True,
                                  'pertemuan3':False}
    st.rerun()
if st.sidebar.button("Pertemuan 3"):
    st.session_state['kumpulan']={'kover':False,'perpustakaan':False,'diag':False,'angket':False,'foto':False,'pertemuan1':False,'pertemuan2':False,
                                  'pertemuan3':True}

    st.rerun()
 
