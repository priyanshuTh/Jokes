from js import document, localStorage, speak
import pyjokes, json, random

# kept in this tab + localStorage
joke_history: list[str] = []
rating_history: list[int] = []

LAUGHS = ["Ha ha ha!", "He he he!", "Ho ho ho!", "😂😂😂", "🤣"]
CATEGORIES = ["all", "neutral", "chuck"]

# storage helpers
def save_state():
    try:
        localStorage.setItem('joke_history', json.dumps(joke_history))
        localStorage.setItem('rating_history', json.dumps(rating_history))
    except Exception:
        pass

def load_state():
    try:
        jh = localStorage.getItem('joke_history')
        rh = localStorage.getItem('rating_history')
        if jh: joke_history.extend(json.loads(jh))
        if rh: rating_history.extend(json.loads(rh))
    except Exception:
        pass

# UI helpers
def set_text(el_id: str, text: str):
    document.getElementById(el_id).innerText = text

def show_rating(show=True):
    el = document.getElementById('rating')
    cls = el.classList
    if show: cls.add('show')
    else: cls.remove('show')

def update_history_view():
    lst = document.getElementById('history')
    lst.innerHTML = ''
    for j in joke_history[-100:]:
        li = document.createElement('li')
        li.textContent = j
        lst.appendChild(li)

def update_stats_view():
    count = len(joke_history)
    avg = (sum(rating_history) / len(rating_history)) if rating_history else 0.0
    set_text('stat-count', str(count))
    set_text('stat-avg', f"{avg:.2f}")

# actions wired via pys-onClick
def greet_if_needed():
    name = document.getElementById('name').value.strip()
    if name:
        set_text('joke', f"Hi, {name}! Ready for some laughs? Click 'Tell me a joke'.")

def _get_category_from_ui():
    sel = document.getElementById('category').value
    if sel == 'auto':
        return None
    # pyjokes expects one of: neutral, chuck, all
    if sel in CATEGORIES:
        return sel
    return None

def tell_joke_py(event=None):
    cat = _get_category_from_ui()
    try:
        joke = pyjokes.get_joke(category=cat) if cat else pyjokes.get_joke()
    except Exception:
        # fallback to any joke
        joke = pyjokes.get_joke()

    joke_history.append(joke)
    save_state()

    set_text('joke', joke)
    laugh = random.choice(LAUGHS)
    set_text('laugh', laugh)
    speak(joke + " " + laugh)
    show_rating(True)
    set_text('rate-msg', "")
    update_history_view()
    update_stats_view()

def repeat_last_py(event=None):
    if not joke_history:
        set_text('joke', 'No joke to repeat yet.')
        return
    last = joke_history[-1]
    set_text('joke', last)
    speak(last)
    show_rating(True)
    set_text('rate-msg', "")


def show_history_py(event=None):
    update_history_view()

def show_stats_py(event=None):
    update_stats_view()

def clear_history_py(event=None):
    joke_history.clear(); rating_history.clear(); save_state()
    update_history_view(); update_stats_view()
    set_text('joke', 'History cleared. Ready for a fresh laugh!')
    set_text('laugh', '')
    show_rating(False)

def rate_py(event=None):
    # score is stored in the clicked button data score
    try:
        score = int(event.target.getAttribute('data-score'))
    except Exception:
        score = 3
    rating_history.append(score)
    save_state()

    # Friendly response
    if score >= 4:
        msg = "Glad you liked it!"
    elif score >= 2:
        msg = "Thanks for the feedback!"
    else:
        msg = "Oof, tough crowd. I’ll do better next time!"

    set_text('rate-msg', msg)
    speak(msg)
    update_stats_view()

# boot
load_state()
update_history_view()
update_stats_view()
greet_if_needed()
