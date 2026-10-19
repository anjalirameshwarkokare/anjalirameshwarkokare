from pathlib import Path
from html import escape
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets' / 'neon'
ASSETS.mkdir(parents=True, exist_ok=True)
INK = '#171336'
MUTED = '#655F7F'
SANS = 'DejaVu Sans, Arial, sans-serif'
MONO = 'DejaVu Sans Mono, monospace'

def text(x, y, s, size=20, fill=INK, weight=400, family=SANS, extra=''):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-family="{family}" font-weight="{weight}" {extra}>{escape(s)}</text>'

def svg(w, h, title, body, desc=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>
<defs>
<linearGradient id="rainbow" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#11E6E0"/><stop offset=".35" stop-color="#5662FF"/><stop offset=".7" stop-color="#B73BFF"/><stop offset="1" stop-color="#FF4EA3"/></linearGradient>
<linearGradient id="sun" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#FAFF69"/><stop offset="1" stop-color="#FFBE6A"/></linearGradient>
<linearGradient id="mint" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#E8FFF7"/><stop offset="1" stop-color="#C3FFF0"/></linearGradient>
<linearGradient id="pink" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#FFF1FA"/><stop offset="1" stop-color="#FFD4EA"/></linearGradient>
<linearGradient id="blue" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#EEF1FF"/><stop offset="1" stop-color="#DDDAFF"/></linearGradient>
<linearGradient id="yellow" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#FFFFEB"/><stop offset="1" stop-color="#FFF5AC"/></linearGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#FFFFFF" stroke-opacity=".12"/></pattern>
</defs>{body}</svg>'''

def save(name, data):
    ET.fromstring(data)
    (ASSETS / name).write_text(data)

def pill(x, y, label, bg, fg=INK, width=None, size=15, height=34):
    width = width or round(len(label) * size * .64 + 30)
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{height/2}" fill="{bg}"/>' + text(x+width/2, y+height/2+size*.35, label, size, fg, 700, extra='text-anchor="middle"')

# Hero: luminous color, oversized typography, and a hand-drawn code window.
hero = '''<rect width="1200" height="468" rx="28" fill="url(#rainbow)"/>
<rect width="1200" height="468" rx="28" fill="url(#grid)"/>
<circle cx="1145" cy="54" r="184" fill="#F1FF6E" opacity=".18"/>
<circle cx="52" cy="475" r="173" fill="#1CF5D5" opacity=".22"/>
<path d="M-25 400Q280 285 640 438T1260 345" fill="none" stroke="#FFF" stroke-opacity=".14" stroke-width="60"/>
<rect x="28" y="28" width="1144" height="412" rx="20" fill="none" stroke="white" stroke-opacity=".35"/>
'''
hero += pill(54, 50, 'HELLO, WORLD.  /  I AM', '#FFFFFF', '#4F2BB0', 285, 15)
hero += text(50, 174, 'Anjali', 89, '#FFFFFF', 800)
hero += text(50, 268, 'Kokare', 89, '#FFFFFF', 800)
hero += text(56, 312, 'Python. Data. A little bit of magic.', 23, '#FFFFFF', 700)
hero += text(56, 350, 'Turning curiosity into code & data into decisions.', 17, '#FFFFFF')
hero += pill(54, 379, 'IIT MADRAS', '#EFFF80', INK, 157, 14)
hero += pill(224, 379, 'BS DATA SCIENCE', '#FFFFFF', '#5D30BB', 210, 14)
hero += '''<g transform="translate(639 78) rotate(-3 245 154)">
<rect x="9" y="16" width="484" height="304" rx="22" fill="#29156D" opacity=".23"/>
<rect width="484" height="304" rx="22" fill="#17132F" stroke="#E4D7FF" stroke-opacity=".7" stroke-width="2"/>
<path d="M0 48H484" stroke="#42365F"/>
<circle cx="25" cy="25" r="6" fill="#FF66A3"/><circle cx="46" cy="25" r="6" fill="#F2F675"/><circle cx="67" cy="25" r="6" fill="#39E8C4"/>
'''
hero += text(237, 30, 'anjali.py', 14, '#BAB3D9', family=MONO, extra='text-anchor="middle"')
for i, s in enumerate(['01', '02', '03', '04', '05', '06']):
    hero += text(20, 86+i*31, s, 15, '#6E628D', family=MONO)
hero += text(64, 86, 'class CuriousBuilder:', 20, '#ED98FF', 600, MONO)
hero += text(88, 117, 'name = "Anjali Kokare"', 18, '#87F4D8', family=MONO)
hero += text(88, 148, 'tools = ["Python", "SQL"]', 18, '#F9F494', family=MONO)
hero += text(88, 179, 'focus = "Data + ML"', 18, '#A6C5FF', family=MONO)
hero += text(88, 210, 'mindset = "Keep building"', 18, '#FFA8CC', family=MONO)
hero += text(64, 241, '>>> ideas.into_reality()', 18, '#FFFFFF', family=MONO)
hero += '<rect x="64" y="259" width="12" height="20" rx="2" fill="#AFFF7E"/></g>'
hero += '<g transform="translate(1060 350) rotate(9)"><rect width="98" height="74" rx="18" fill="url(#sun)"/>'+text(49, 48, '</>', 33, INK, 700, MONO, 'text-anchor="middle"')+'</g>'
hero += '<path d="M588 44v24m-12-12h24M609 365v24m-12-12h24M1140 318v20m-10-10h20" stroke="#EEFF94" stroke-width="4" stroke-linecap="round"/>'
save('hero.svg', svg(1200, 468, 'Anjali Kokare — Python, Data Science and Machine Learning', hero, 'A vivid cyan, violet and pink coding banner with a Python code window. IIT Madras BS Data Science student.'))

# Short, readable introduction with a terminal treatment.
about = '<rect x="1" y="1" width="1198" height="234" rx="24" fill="#17132F" stroke="#A99BD8"/>'
about += '<rect x="1" y="1" width="10" height="234" rx="5" fill="url(#rainbow)"/>'
about += text(38, 41, '> whoami', 18, '#A6FF96', 700, MONO)
about += text(38, 85, 'A curious mind. A practical builder.', 29, '#FFFFFF', 700)
about += text(38, 123, 'I study Data Science at IIT Madras and build with Python, Flask and ML.', 19, '#D4CFE8')
about += text(38, 155, 'I love making messy data useful and turning ideas into working applications.', 19, '#D4CFE8')
about += pill(38, 182, 'PYTHON DEVELOPMENT', '#DDFB89', width=245, size=14)
about += pill(296, 182, 'BUSINESS ANALYTICS', '#B0F3FF', width=237, size=14)
about += pill(546, 182, 'MACHINE LEARNING', '#E6BAFF', width=226, size=14)
about += text(1136, 58, '{ }', 50, '#6D598C', 700, MONO, 'text-anchor="end"')
save('about.svg', svg(1200, 236, 'About Anjali', about))

def section(filename, n, heading, right, accent):
    b = '<rect x="1" y="1" width="1198" height="76" rx="18" fill="#FAF9FF" stroke="#E4DFF1"/>'
    b += f'<rect x="16" y="16" width="46" height="46" rx="12" fill="{accent}"/>'
    b += text(39, 46, n, 18, INK, 700, MONO, 'text-anchor="middle"')
    b += text(80, 49, heading, 28, INK, 700)
    b += text(1167, 47, right, 15, MUTED, 500, MONO, 'text-anchor="end"')
    save(filename, svg(1200, 78, heading, b))

section('section-projects.svg', '01', 'Things I have built', 'EXPLORE THE CODE  ↗', '#E4C2FF')
section('section-toolkit.svg', '02', 'My developer toolkit', 'LEARN. BUILD. REPEAT.', '#B0F3FF')
section('section-connect.svg', '03', 'Let us build something useful', 'SAY HELLO  ↗', '#EEFC9A')

projects = [
    ('project-nlp.svg', '01 / NATURAL LANGUAGE PROCESSING', 'Comment intelligence', ['Text preprocessing, TF-IDF features and', 'LightGBM for four-category classification.'], '#BEF8ED', 'mint', ['PYTHON', 'TF-IDF', 'LIGHTGBM'], 'chat'),
    ('project-retail.svg', '02 / BUSINESS DATA ANALYTICS', 'Data meets the real world', ['6,465 store transactions, sales insights,', 'credit patterns and ABC inventory analysis.'], '#FFD1E9', 'pink', ['PANDAS', 'EXCEL', 'ANALYTICS'], 'chart'),
    ('project-placement.svg', '03 / MACHINE LEARNING + WEB', 'A model, made interactive', ['A Flask interface for a placement prediction', 'model using CGPA and IQ inputs.'], '#D8D3FF', 'blue', ['FLASK', 'SCIKIT-LEARN', 'ML'], 'model'),
    ('project-notebooks.svg', '04 / THE LEARNING LAB', 'Small experiments. Big ideas.', ['Machine learning notebooks, examples', 'and learning material from my journey.'], '#FFF3A7', 'yellow', ['JUPYTER', 'PYTHON', 'NOTEBOOKS'], 'notebook'),
]

for filename, eyebrow, title, lines, accent, grad, tags, graphic in projects:
    b = f'<rect x="1" y="1" width="578" height="310" rx="24" fill="url(#{grad})" stroke="{accent}" stroke-width="2"/>'
    b += '<circle cx="570" cy="-5" r="115" fill="white" opacity=".42"/>'
    b += text(28, 36, eyebrow, 12, MUTED, 700, MONO)
    if graphic == 'chat':
        b += '<rect x="28" y="57" width="85" height="55" rx="14" fill="#17132F"/><path d="M46 106v19l20-19" fill="#17132F"/><circle cx="50" cy="84" r="4" fill="#B8F8DD"/><circle cx="70" cy="84" r="4" fill="#B8F8DD"/><circle cx="90" cy="84" r="4" fill="#B8F8DD"/>'
    elif graphic == 'chart':
        b += '<rect x="30" y="82" width="17" height="37" rx="5" fill="#FF5EAC"/><rect x="57" y="66" width="17" height="53" rx="5" fill="#9855FC"/><rect x="84" y="51" width="17" height="68" rx="5" fill="#17132F"/>'
    elif graphic == 'model':
        b += '<g stroke="#8B70CB" stroke-width="2"><path d="M44 66L84 88L44 112M84 88L124 65M84 88L124 111"/></g><g fill="#17132F"><circle cx="44" cy="66" r="10"/><circle cx="44" cy="112" r="10"/><circle cx="124" cy="65" r="10"/><circle cx="124" cy="111" r="10"/></g><circle cx="84" cy="88" r="14" fill="#A5FFAE" stroke="#17132F" stroke-width="3"/>'
    else:
        b += '<rect x="30" y="56" width="78" height="65" rx="12" fill="#17132F"/><path d="M48 77L39 86L48 95M90 77L99 86L90 95M74 73L64 99" stroke="#F1F883" stroke-width="4" fill="none" stroke-linecap="round"/>'
    b += '<circle cx="527" cy="88" r="22" fill="#17132F"/>'+text(527, 96, '↗', 26, '#FFFFFF', 700, extra='text-anchor="middle"')
    b += text(28, 164, title, 27, INK, 700)
    b += text(28, 201, lines[0], 17, '#4D4767') + text(28, 226, lines[1], 17, '#4D4767')
    x = 28
    for tag in tags:
        width = round(len(tag)*8.5+28)
        b += pill(x, 258, tag, '#FFFFFF', INK, width, 12, 29)
        x += width+8
    save(filename, svg(580, 312, title, b, ' '.join(lines)))

tools = [
    ('PYTHON', 'Core language', '#F8E96F', '</>'),
    ('SQL', 'Query & explore', '#89EADC', 'db'),
    ('FLASK', 'Web applications', '#E6B4FF', '{ }'),
    ('PANDAS', 'Data wrangling', '#FFB7D7', '[]'),
    ('NUMPY', 'Numerical tools', '#B7D2FF', '∑'),
    ('SCIKIT-LEARN', 'Model experiments', '#FCCE99', 'ml'),
    ('JUPYTER', 'Notebook workflow', '#DBF48A', '>_'),
    ('GIT + GITHUB', 'Version control', '#C5BCFF', 'git'),
    ('HTML + CSS', 'Interface building', '#A4F1EF', '<>'),
    ('BOOTSTRAP', 'Responsive layouts', '#EAC3FF', 'B'),
    ('SQLITE', 'Application data', '#FFE695', 'db'),
    ('EXCEL', 'Business analysis', '#B3EDCF', 'fx'),
]
toolkit = '<rect x="1" y="1" width="1198" height="336" rx="22" fill="#FAF9FF" stroke="#E3DDF0"/>'
for i, (name, detail, color, icon) in enumerate(tools):
    col, row = i%4, i//4
    x, y = 22+col*294, 20+row*102
    toolkit += f'<rect x="{x}" y="{y}" width="274" height="90" rx="16" fill="#FFFFFF" stroke="#E6E0F2"/>'
    toolkit += f'<rect x="{x+14}" y="{y+22}" width="45" height="45" rx="12" fill="{color}"/>'
    toolkit += text(x+36, y+51, icon, 18, INK, 700, MONO, 'text-anchor="middle"')
    toolkit += text(x+72, y+41, name, 15, INK, 700)
    toolkit += text(x+72, y+64, detail, 12, MUTED)
save('toolkit.svg', svg(1200, 338, 'Developer toolkit: Python, SQL, Flask, Pandas, NumPy, scikit-learn, Jupyter, Git, HTML, CSS, Bootstrap, SQLite and Excel', toolkit))

for filename, label, sub, color, icon in [
    ('connect-linkedin.svg','LinkedIn','Let us connect professionally','#C9E5FF','in'),
    ('connect-kaggle.svg','Kaggle','Follow the data journey','#A5F4EE','k'),
    ('connect-github.svg','GitHub','Explore my repositories','#DCC5FF','<>'),
]:
    b = f'<rect x="1" y="1" width="378" height="116" rx="20" fill="{color}" stroke="#FFFFFF" stroke-width="2"/>'
    b += '<rect x="18" y="30" width="54" height="54" rx="15" fill="#17132F"/>'
    b += text(45, 66, icon, 23, '#FFFFFF', 700, MONO, 'text-anchor="middle"')
    b += text(89, 51, label, 23, INK, 700)
    b += text(89, 78, sub, 12, '#4D4767')
    b += text(350, 58, '↗', 23, INK, 700, extra='text-anchor="middle"')
    save(filename, svg(380, 118, label+' — '+sub, b))

footer = '<rect width="1200" height="150" rx="24" fill="url(#rainbow)"/><rect width="1200" height="150" rx="24" fill="url(#grid)"/>'
footer += text(600, 62, 'Curiosity is the spark. Code is the craft.', 31, '#FFFFFF', 700, extra='text-anchor="middle"')
footer += text(600, 106, 'THANKS FOR STOPPING BY  ·  KEEP BUILDING SOMETHING GOOD.', 15, '#FFFFFF', 600, MONO, 'text-anchor="middle"')
save('footer.svg', svg(1200, 150, 'Curiosity is the spark. Code is the craft.', footer))

# A custom monogram designed to remain readable in GitHub's circular crop.
avatar = '<rect width="1024" height="1024" fill="#17132F"/><circle cx="512" cy="512" r="470" fill="url(#rainbow)"/><circle cx="512" cy="512" r="404" fill="#17132F"/><circle cx="512" cy="512" r="367" fill="none" stroke="#B7C7FF" stroke-opacity=".25" stroke-width="2"/>'
avatar += '<path d="M270 376L202 512L270 648M754 376L822 512L754 648" fill="none" stroke="#72F3DD" stroke-width="25" stroke-linecap="round" stroke-linejoin="round"/>'
avatar += text(512, 571, 'AK', 228, '#FFFFFF', 800, SANS, 'text-anchor="middle" letter-spacing="-10"')
avatar += '<rect x="405" y="660" width="214" height="15" rx="7.5" fill="url(#sun)"/><path d="M512 238v32m-16-16h32M681 714v28m-14-14h28" stroke="#FFB5E4" stroke-width="9" stroke-linecap="round"/>'
save('avatar.svg', svg(1024, 1024, 'AK — Anjali Kokare coding monogram', avatar))

readme = '''<!-- Custom original vector artwork. All graphics live in this repository. -->
<div align="center">
  <img src="assets/neon/hero.svg" width="100%" alt="Anjali Kokare — Python, Data Science and Machine Learning. IIT Madras BS Data Science student." />
</div>

<p align="center">
  <a href="#selected-work">Selected work</a> &nbsp; · &nbsp;
  <a href="#developer-toolkit">Developer toolkit</a> &nbsp; · &nbsp;
  <a href="#lets-connect">Let's connect</a>
</p>

<img src="assets/neon/about.svg" width="100%" alt="I study Data Science at IIT Madras and build with Python, Flask and ML. I love making messy data useful and turning ideas into working applications." />

<p align="center"><strong>Learning by doing. Building with curiosity. Improving one commit at a time.</strong></p>

<h2 id="selected-work">Selected work</h2>

<img src="assets/neon/section-projects.svg" width="100%" alt="01 — Things I have built. Explore the code." />

<p align="center">
  <a href="https://github.com/anjalirameshwarkokare/comment-category-prediction"><img src="assets/neon/project-nlp.svg" width="49%" alt="Comment intelligence — NLP classification using Python, TF-IDF and LightGBM. Open repository." /></a>
  <a href="https://github.com/anjalirameshwarkokare/BDM_Capstone_project_kirana-store"><img src="assets/neon/project-retail.svg" width="49%" alt="Data meets the real world — analysis of 6,465 kirana store transactions. Open repository." /></a>
</p>
<p align="center">
  <a href="https://github.com/anjalirameshwarkokare/ML-placement-app"><img src="assets/neon/project-placement.svg" width="49%" alt="A model, made interactive — Flask placement prediction application. Open repository." /></a>
  <a href="https://github.com/anjalirameshwarkokare/MLP-material"><img src="assets/neon/project-notebooks.svg" width="49%" alt="Small experiments. Big ideas. — machine learning notebooks and examples. Open repository." /></a>
</p>

**More of my work:** [ML lecture notebooks](https://github.com/anjalirameshwarkokare/MLP-lectures) · [Bootstrap website](https://github.com/anjalirameshwarkokare/codebootstrap)

<h2 id="developer-toolkit">Developer toolkit</h2>

<img src="assets/neon/section-toolkit.svg" width="100%" alt="02 — My developer toolkit. Learn, build, repeat." />
<img src="assets/neon/toolkit.svg" width="100%" alt="Python, SQL, Flask, Pandas, NumPy, scikit-learn, Jupyter, Git and GitHub, HTML and CSS, Bootstrap, SQLite and Excel." />

### What keeps me curious

- **Python development** — building useful applications with clear, readable code.
- **Data and business analytics** — finding patterns that lead to practical decisions.
- **Machine learning** — exploring text classification, prediction and model workflows.

<h2 id="lets-connect">Let's connect</h2>

<img src="assets/neon/section-connect.svg" width="100%" alt="03 — Let us build something useful. Say hello." />

<p align="center">
  <a href="https://www.linkedin.com/in/anjali-kokare-645488382/"><img src="assets/neon/connect-linkedin.svg" width="32%" alt="LinkedIn — connect with Anjali Kokare." /></a>
  <a href="https://www.kaggle.com/anjalikokare"><img src="assets/neon/connect-kaggle.svg" width="32%" alt="Kaggle — follow my data journey." /></a>
  <a href="https://github.com/anjalirameshwarkokare?tab=repositories"><img src="assets/neon/connect-github.svg" width="32%" alt="GitHub — explore my repositories." /></a>
</p>

<p align="center">Open to conversations about Python, data projects, machine learning and thoughtful collaboration.</p>

<img src="assets/neon/footer.svg" width="100%" alt="Curiosity is the spark. Code is the craft. Thanks for stopping by — keep building something good." />
'''
(ROOT / 'README.md').write_text(readme)
manifest = [{'path':str(p.relative_to(ROOT)), 'content':p.read_text()} for p in [ROOT/'README.md', *sorted(ASSETS.glob('*.svg'))]]
(ROOT / 'upload-manifest.json').write_text(json.dumps(manifest))
print(json.dumps({'directory':str(ROOT), 'assets':len(manifest)-1, 'files':[x['path'] for x in manifest]}, indent=2))
