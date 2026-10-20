from pathlib import Path
from html import escape
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'assets' / 'studio'
OUT.mkdir(parents=True, exist_ok=True)
SANS = 'DejaVu Sans, Arial, sans-serif'
MONO = 'DejaVu Sans Mono, monospace'
INK = '#14172C'
WHITE = '#F8F7FF'
MUTED = '#B7BDD4'
CYAN = '#78F1EF'
VIOLET = '#A78BFF'
LIME = '#D8FF79'

def t(x, y, value, size=20, color=WHITE, weight=400, mono=False, extra=''):
    return f'<text x="{x}" y="{y}" font-family="{MONO if mono else SANS}" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>'

def rect(x, y, w, h, color, radius=16, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{color}" {extra}/>'

def pill(x, y, value, color, width, ink=INK, size=14):
    return rect(x, y, width, 32, color, 16) + t(x+width/2, y+21, value, size, ink, 700, extra='text-anchor="middle"')

def save(filename, w, h, title, body):
    document = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">Original artwork for Anjali Kokare's developer profile.</desc>
<defs>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#78F1EF"/><stop offset=".5" stop-color="#A78BFF"/><stop offset="1" stop-color="#F89CD4"/></linearGradient>
  <linearGradient id="orb" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#78F1EF"/><stop offset=".5" stop-color="#9C84FF"/><stop offset="1" stop-color="#ED8BCB"/></linearGradient>
  <radialGradient id="glow"><stop stop-color="#5C4BBA" stop-opacity=".6"/><stop offset="1" stop-color="#17172E" stop-opacity="0"/></radialGradient>
  <pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#ABB0E0" opacity=".13"/></pattern>
</defs>{body}</svg>'''
    ET.fromstring(document)
    (OUT / filename).write_text(document)

# A compact editorial banner with an original orbital code sculpture.
b = rect(0, 0, 1200, 440, '#111426', 28)
b += rect(0, 0, 1200, 440, 'url(#dots)', 28)
b += '<ellipse cx="974" cy="212" rx="305" ry="256" fill="url(#glow)"/>'
b += '<path d="M40 1H1160" stroke="url(#edge)" stroke-width="3"/>'
b += t(48, 49, 'ANJALI  /  CODE & DATA', 15, CYAN, 700, True, 'letter-spacing="2"')
b += '<circle cx="1136" cy="43" r="5" fill="#D8FF79"/>'
b += t(48, 150, 'Anjali Kokare.', 80, WHITE, 800, extra='letter-spacing="-3"')
b += t(50, 211, 'Code with curiosity.', 35, WHITE, 600)
b += t(50, 259, 'Build with purpose.', 35, CYAN, 600)
b += t(51, 307, 'Python · Machine Learning · Business Analytics', 20, MUTED)
b += pill(48, 352, 'BS DATA SCIENCE  @  IIT MADRAS', LIME, 380, size=15)
b += '<g transform="translate(969 211)"><ellipse rx="164" ry="96" transform="rotate(-34)" fill="none" stroke="#A78BFF" stroke-opacity=".2" stroke-width="20"/><ellipse rx="164" ry="96" transform="rotate(-34)" fill="none" stroke="url(#orb)" stroke-width="2"/><ellipse rx="153" ry="153" fill="none" stroke="#6D689B" stroke-opacity=".35"/>'
b += '<path d="M-4-153A153 153 0 0 1 149 34" fill="none" stroke="#78F1EF" stroke-width="3" stroke-linecap="round"/>'
b += '<g transform="rotate(9)"><rect x="-89" y="-89" width="178" height="178" rx="36" fill="#2B2850" stroke="#8D80D0" stroke-width="2"/><rect x="-78" y="-78" width="156" height="156" rx="29" fill="#191B35"/><path d="M-35-27L-61 0L-35 27M35-27L61 0L35 27M15-43L-15 43" fill="none" stroke="#E7E2FF" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>'
b += '<circle cx="-130" cy="86" r="11" fill="#D8FF79"/><circle cx="141" cy="-51" r="7" fill="#F89CD4"/>'
b += '</g>'
b += pill(842, 48, 'ideas.py', '#2D2C4D', 152, '#C9CCEA', 14)
b += pill(955, 353, 'keep building_', '#25263F', 202, CYAN, 14)
b += '<path d="M1104 294v18m-9-9h18M804 122v14m-7-7h14" stroke="#A78BFF" stroke-width="2" stroke-linecap="round"/>'
save('hero.svg', 1200, 440, 'Anjali Kokare. Code with curiosity. Build with purpose. Python, Machine Learning and Business Analytics. BS Data Science at IIT Madras.', b)

def graphic(kind, color):
    g = ''
    if kind == 'text':
        g = rect(362, 68, 166, 95, '#232B46', 17)
        g += '<path d="M385 161v22l27-22" fill="#232B46"/>'
        for x, width, opacity in [(382, 109, '.9'), (382, 83, '.55'), (382, 61, '.3')]:
            y = 89 + [109, 83, 61].index(width)*23
            g += rect(x, y, width, 7, color, 3, f'opacity="{opacity}"')
        g += pill(444, 147, 'NLP', color, 84, size=14)
    elif kind == 'chart':
        g = '<path d="M378 164H532M378 164V75" fill="none" stroke="#62617F" stroke-width="2"/>'
        for x, h, opacity in [(393, 39, '.4'), (431, 62, '.7'), (469, 93, '1')]:
            g += rect(x, 164-h, 25, h, color, 6, f'opacity="{opacity}"')
        g += '<path d="M387 93L429 72L463 79L512 50" stroke="#F8F7FF" stroke-width="3" fill="none" stroke-linecap="round"/>'
        g += '<circle cx="512" cy="50" r="5" fill="#F8F7FF"/>'
    elif kind == 'model':
        g = '<g stroke="#6E648F" stroke-width="2"><path d="M388 71L448 110L388 151M448 110L509 66M448 110L509 154"/></g>'
        for x,y in [(388,71),(388,151),(509,66),(509,154)]:
            g += f'<circle cx="{x}" cy="{y}" r="12" fill="#302F4E" stroke="{color}" stroke-width="2"/>'
        g += f'<circle cx="448" cy="110" r="27" fill="{color}"/>' + t(448, 116, 'ML', 17, INK, 700, True, 'text-anchor="middle"')
    elif kind == 'web':
        g = rect(357, 58, 181, 119, '#2D3543', 14)
        g += '<path d="M358 82H537" stroke="#606B71"/>'
        for x in [371,382,393]:
            g += f'<circle cx="{x}" cy="71" r="3" fill="{color}"/>'
        g += rect(371, 95, 150, 16, color, 5, 'opacity=".8"')
        for x in [371,422,473]:
            g += rect(x, 121, 43, 40, color, 6, 'opacity=".2"')
    return g

cards = [
 ('project-nlp.svg', '01 / NATURAL LANGUAGE PROCESSING', ['Comment', 'Classification'], ['Text preprocessing and TF-IDF features', 'for a four-class LightGBM model.'], 'PYTHON  /  TF-IDF  /  LIGHTGBM', CYAN, '#151F31', 'text'),
 ('project-retail.svg', '02 / BUSINESS DATA MANAGEMENT', ['Kirana Store', 'Analytics'], ['6,465 transactions. Sales, credit and', 'inventory insights for a real store.'], 'PANDAS  /  EXCEL  /  EDA', '#FFC29C', '#251D2C', 'chart'),
 ('project-placement.svg', '03 / MACHINE LEARNING + WEB', ['Placement', 'Prediction App'], ['A trained model meets a Flask interface', 'with CGPA and IQ inputs.'], 'FLASK  /  PYTHON  /  SCIKIT-LEARN', '#C7A9FF', '#1E1B33', 'model'),
 ('project-web.svg', '04 / FRONTEND DEVELOPMENT', ['Responsive', 'Web Design'], ['A Bootstrap website exploring layouts,', 'components and responsive interfaces.'], 'HTML  /  CSS  /  BOOTSTRAP', LIME, '#1D282A', 'web'),
]
for filename, eyebrow, title, description, stack, color, bg, kind in cards:
    b = rect(1, 1, 578, 374, bg, 24, 'stroke="#62627C" stroke-opacity=".35"')
    b += '<path d="M25 1H553" stroke="'+color+'" stroke-width="3"/>'
    b += t(28, 38, eyebrow, 12, color, 700, True)
    b += graphic(kind, color)
    b += t(28, 113, title[0], 32, WHITE, 700, extra='letter-spacing="-1"')
    b += t(28, 154, title[1], 32, WHITE, 700, extra='letter-spacing="-1"')
    b += '<path d="M28 202H550" stroke="#ABB0CF" stroke-opacity=".18"/>'
    b += t(28, 244, description[0], 19, '#D1D3E3')
    b += t(28, 274, description[1], 19, '#D1D3E3')
    b += t(28, 332, stack, 14, color, 700, True)
    b += '<circle cx="526" cy="326" r="18" fill="'+color+'"/>'
    b += '<path d="M520 332L532 320M521 320H532V331" stroke="#14172C" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    save(filename, 580, 376, ' '.join(title)+'. '+' '.join(description)+' '+stack, b)

# Grouped skills are easier to scan than a wall of miniature badges.
b = rect(1, 1, 1198, 236, '#F7F7FD', 22, 'stroke="#E0DFF0"')
groups = [(24, '01', 'Code & web', ['Python · SQL · Flask', 'HTML · CSS · Bootstrap · SQLite'], '#DACFFF'),
          (421, '02', 'Data & ML', ['Pandas · NumPy · scikit-learn', 'LightGBM · Matplotlib · Seaborn'], '#BDF4EC'),
          (818, '03', 'Everyday tools', ['Git · GitHub · Jupyter', 'Excel · EDA · Data visualization'], '#E8F8B8')]
for x, number, title, lines, color in groups:
    b += rect(x, 23, 358, 191, '#FFFFFF', 18, 'stroke="#E4E3F0"')
    b += pill(x+18, 41, number, color, 45, size=13)
    b += t(x+78, 65, title, 23, INK, 700)
    b += t(x+18, 118, lines[0], 20, '#4F5570')
    b += t(x+18, 151, lines[1], 18, '#4F5570')
    b += '<path d="M'+str(x+18)+' 179H'+str(x+340)+'" stroke="'+color+'" stroke-width="4" stroke-linecap="round"/>'
save('toolkit.svg', 1200, 238, 'Code and web: Python, SQL, Flask, HTML, CSS, Bootstrap, SQLite. Data and ML: Pandas, NumPy, scikit-learn, LightGBM, Matplotlib, Seaborn. Tools: Git, GitHub, Jupyter and Excel.', b)

for filename, label, caption, color, icon in [
 ('linkedin.svg','LinkedIn','Let us connect', '#BFF4F2', 'in'),
 ('kaggle.svg','Kaggle','Explore my data work', '#D9CBFF', 'k'),
 ('repositories.svg','Repositories','Browse the code', '#E5F6B6', '</>')]:
    b = rect(1, 1, 378, 104, color, 18)
    b += rect(17, 22, 56, 56, INK, 16)
    b += t(45, 58, icon, 23 if icon!='</>' else 18, WHITE, 700, True, 'text-anchor="middle"')
    b += t(89, 45, label, 21, INK, 700)
    b += t(89, 72, caption, 14, '#4C506B')
    b += '<path d="M340 55L352 43M341 43H352V54" stroke="#14172C" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    save(filename, 380, 106, label+' — '+caption, b)

readme = '''<!-- Original SVG artwork is stored in this repository. No external stats widgets required. -->
<div align="center">
  <img src="assets/studio/hero.svg" width="100%" alt="Anjali Kokare — Code with curiosity. Build with purpose. Python, Machine Learning and Business Analytics. BS Data Science at IIT Madras." />
</div>

<p align="center">
  <a href="#about-me"><b>About</b></a> &nbsp; / &nbsp;
  <a href="#selected-work"><b>Selected work</b></a> &nbsp; / &nbsp;
  <a href="#my-toolkit"><b>Toolkit</b></a> &nbsp; / &nbsp;
  <a href="#lets-connect"><b>Connect</b></a>
</p>

## About me

Hi, I'm **Anjali** — a **BS Data Science student at IIT Madras**, currently at the diploma level. I enjoy building with Python, exploring machine learning, and finding useful stories in real business data.

My projects connect three interests: **clean code, thoughtful analysis, and applications people can use.**

- **Building:** Python and Flask applications, from inputs to predictions.
- **Exploring:** NLP, feature engineering, model workflows and data visualization.
- **Learning by doing:** turning coursework and experiments into documented projects.

## Selected work

<p>Explore a few projects that bring those interests together. Click a card to see the repository.</p>

<p align="center">
  <a href="https://github.com/anjalirameshwarkokare/comment-category-prediction"><img src="assets/studio/project-nlp.svg" width="49%" alt="Comment Category Prediction — Text preprocessing, TF-IDF and a four-class LightGBM model. View repository." /></a>
  <a href="https://github.com/anjalirameshwarkokare/BDM_Capstone_project_kirana-store"><img src="assets/studio/project-retail.svg" width="49%" alt="Kirana Store Analytics — 6,465 transactions analyzed for sales, credit and inventory insights. View repository." /></a>
</p>
<p align="center">
  <a href="https://github.com/anjalirameshwarkokare/ML-placement-app"><img src="assets/studio/project-placement.svg" width="49%" alt="Placement Prediction App — A Flask interface for a trained model using CGPA and IQ inputs. View repository." /></a>
  <a href="https://github.com/anjalirameshwarkokare/codebootstrap"><img src="assets/studio/project-web.svg" width="49%" alt="Responsive Web Design — A Bootstrap website exploring responsive layouts and components. View repository." /></a>
</p>

<details>
<summary><b>More from my learning lab</b> — notebooks, coursework and experiments</summary>

| Collection | What you will find |
| --- | --- |
| [MLP material](https://github.com/anjalirameshwarkokare/MLP-material) | Machine learning practice material and notebook examples |
| [MLP lectures](https://github.com/anjalirameshwarkokare/MLP-lectures) | Lecture notebooks and concepts I am working through |
| [IITM TDS coursework](https://github.com/anjalirameshwarkokare/iitm-tds-26t1) | Coursework and technical exercises |

</details>

## My toolkit

<img src="assets/studio/toolkit.svg" width="100%" alt="My toolkit: Python, SQL, Flask, HTML, CSS, Bootstrap, SQLite, Pandas, NumPy, scikit-learn, LightGBM, Matplotlib, Seaborn, Git, GitHub, Jupyter and Excel." />

I use these tools across coursework and personal projects, and keep improving through practice.

## Let's connect

I'm interested in **Python development, data analytics and ML opportunities**, and conversations with people who enjoy building useful things.

<p align="center">
  <a href="https://www.linkedin.com/in/anjali-kokare-645488382/"><img src="assets/studio/linkedin.svg" width="32%" alt="Connect with Anjali on LinkedIn." /></a>
  <a href="https://www.kaggle.com/anjalikokare"><img src="assets/studio/kaggle.svg" width="32%" alt="Explore Anjali's Kaggle profile." /></a>
  <a href="https://github.com/anjalirameshwarkokare?tab=repositories"><img src="assets/studio/repositories.svg" width="32%" alt="Browse all of Anjali's GitHub repositories." /></a>
</p>

<p align="center"><sub>Curious by nature. Better with every iteration.</sub></p>
'''
(ROOT/'README.md').write_text(readme)
files = [ROOT/'README.md', ROOT/'build_studio.py', *sorted(OUT.glob('*.svg'))]
(ROOT/'studio-manifest.json').write_text(json.dumps([{'path': str(p.relative_to(ROOT)), 'content': p.read_text()} for p in files]))
print(json.dumps({'files': [str(p.relative_to(ROOT)) for p in files], 'asset_count': len(list(OUT.glob('*.svg')))}))
