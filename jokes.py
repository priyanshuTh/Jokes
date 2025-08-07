# Import required modules
from js import document, localStorage, speak
import json, random
import pyjokes  # Directly imported since installed via py-config

# Persistent state
joke_history = []
rating_history = []

MAX_HISTORY = 100
LAUGHS = ["Ha ha ha!", "He he he!", "Ho ho ho!", "😂😂😂", "🤣"]
CATEGORIES = ["all", "neutral", "chuck"]
 

# storage
def save_state():
    try:
        # Limit stored history
        limited_jokes = joke_history[-MAX_HISTORY:]
        limited_ratings = rating_history[-MAX_HISTORY:]
        localStorage.setItem('joke_history', json.dumps(limited_jokes))
        localStorage.setItem('rating_history', json.dumps(limited_ratings))
    except Exception:
        pass

def load_state() -> None:
    try:
        jh = localStorage.getItem('joke_history')
        rh = localStorage.getItem('rating_history')
        if jh and rh:  # Check both values
            joke_data = json.loads(jh)
            rating_data = json.loads(rh)
            if isinstance(joke_data, list) and isinstance(rating_data, list):
                joke_history.extend(joke_data)
                rating_history.extend(rating_data)
    except Exception as e:
        print(f"Error loading state: {e}")

# UI
def set_text(el_id: str, text: str) -> None:
    document.getElementById(el_id).innerText = text

def show_rating(show=True):
    el = document.getElementById('rating')
    cls = el.classList
    if show: 
        cls.remove('d-none')
    else: 
        cls.add('d-none')

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

# actions
def greet_if_needed():
    name = document.getElementById('name').value.strip()
    if name:
        set_text('joke', f"Hi, {name}! Ready for some laughs? Click 'Tell me a joke'.")

def _get_category_from_ui() -> str | None:
    sel: str = document.getElementById('category').value
    if sel == 'auto':
        return None
    # pyjokes expects one of: neutral, chuck, all
    if sel in CATEGORIES:
        return sel
    return None

def tell_joke_py(event=None):
    try:
        cat = _get_category_from_ui()
        joke = pyjokes.get_joke(category=cat) if cat else pyjokes.get_joke()
    except Exception as e:
        print(f"Error fetching joke: {e}")
        joke = "Why did the programmer quit his job? Because he didn't get arrays! (Backup joke - API error)"
    
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
    # stores score
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

# Initialize app
load_state()
update_history_view()
update_stats_view()
greet_if_needed()