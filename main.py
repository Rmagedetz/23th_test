import streamlit as st
from collections import Counter

st.title("Какой ты мастер?")

questions = [
    {
        "question": "Как ты начинаешь свой рабочий день?",
        "options": [
            "С чашки крепкого кофе и обсуждения планов с коллегами.",
            "Провожу 10 минут, пытаясь найти свою любимую отвертку.",
            "Прокачиваю навыки на YouTube, изучая новые методы отделки.",
            "Нахожу удобный уголок и начинаю планировать, как сделать день максимально коротким."
        ],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "Какую фразу ты часто говоришь на работе?",
        "options": [
            "Сделаем всё быстро и качественно!",
            "Где мой молоток? Он же только что был тут!",
            "Я вам сейчас покажу, как это делать идеально!",
            "Ремонт – это искусство. Я просто наслаждаюсь процессом."
        ],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "Что ты обычно думаешь о проекте в самом начале?",
        "options": [
            "Задача ясна, сделаем без проблем!",
            "Чёрт, опять эти неровные стены…",
            "Я всё спланировал, и буду работать, как архитектор!",
            "Надеюсь, сделаю все по красоте. Не испортить бы…"
        ],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "Как ты относишься к рабочим перерывам?",
        "options": [
            "Они мне необходимы для восстановления энергии.",
            "Я на перерыве каждый час, но не из-за усталости, а из-за поиска инструмента.",
            "Перерыв – это время для вдумчивых размышлений, как сделать работу идеальной.",
            "Перерыв – моё всё. Как бы растянуть его на подольше."
        ],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "Как ты оцениваешь свой уровень мастерства?",
        "options": [
            "Эксперт, и все знают, что я всегда прав!",
            "Ну, я могу починить почти всё, если найти нужный инструмент и пару роликов на YouTube.",
            "Я мастер своего дела – каждый мой штрих продуман!",
            "Я как художник – иногда результат просто магический."
        ],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "Как ты решаешь проблемы, если что-то пошло не так?",
        "options": [
            "Спокойно анализирую ситуацию и нахожу оптимальное решение.",
            "Паникую, но потом всё равно нахожу выход.",
            "Мне не нравится решать проблемы, я всегда продумываю всё заранее, чтобы таких ситуаций не было.",
            "Просто надеюсь, что никто не заметит."
        ],
        "scores": [0, 1, 2, 3]
    },
]

# Инициализация состояния
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(questions)

# Если current_question не число, считаем, что тест завершён
if not isinstance(st.session_state.current_question, int):
    # Подсчитываем выбранные варианты
    answer_counts = Counter(st.session_state.answers)
    max_count = max(answer_counts.values())
    # Берём оригинальный порядок вариантов из первого вопроса
    options_order = questions[0]["options"]
    for option in options_order:
        if answer_counts.get(option, 0) == max_count:
            most_common_answer = option
            break

    st.subheader("🔎 Твой результат:")

    if most_common_answer == options_order[0]:
        st.write("Ты мастер-организатор! Уверенно управляешь процессом, всегда знаешь, что делать!")
    elif most_common_answer == options_order[1]:
        st.write("Ты искатель приключений! Всегда есть запасной план (или три), и ты не сдаёшься!")
    elif most_common_answer == options_order[2]:
        st.write("Ты перфекционист! Точен и внимателен к деталям, результат всегда превосходит ожидания!")
    elif most_common_answer == options_order[3]:
        st.write("Ты художник! В твоих руках любая задача превращается в произведение искусства!")
    else:
        st.write("Не удалось определить результат.")

    if st.button("Пройти тест заново"):
        st.session_state.current_question = 0
        st.session_state.answers = [None] * len(questions)
        st.rerun()

else:
    # Отображаем текущий вопрос, если current_question – число
    q_index = st.session_state.current_question
    question = questions[q_index]

    st.header(f"Вопрос {q_index + 1}/{len(questions)}")
    if st.session_state.answers[q_index] is not None:
        try:
            default_index = question["options"].index(st.session_state.answers[q_index])
        except ValueError:
            default_index = 0
    else:
        default_index = 0

    with st.container(border=True):
        answer = st.radio(question["question"], question["options"], index=default_index)

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.current_question > 0:
            if st.button("⬅ Назад"):
                st.session_state.current_question -= 1
                st.rerun()

    with col2:
        if st.button("➡ Далее"):
            st.session_state.answers[q_index] = answer
            if st.session_state.current_question < len(questions) - 1:
                st.session_state.current_question += 1
            else:
                st.session_state.current_question = "result"
            st.rerun()
