import streamlit as st

st.title("Тест на вшивость")

questions = [
    {
        "question": "Вопрос 1",
        "options": ["Вариант 1", "Вариант 2", "Вариант 3", "Вариант 4"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "Вопрос 2",
        "options": ["Вариант 1", "Вариант 2", "Вариант 3", "Вариант 4"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "Вопрос 3",
        "options": ["Вариант 1", "Вариант 2", "Вариант 3", "Вариант 4"],
        "scores": [0, 1, 2, 3]
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(questions)

if st.session_state.current_question == "result":
    total_score = sum(
        question["scores"][question["options"].index(ans)]
        for question, ans in zip(questions, st.session_state.answers)
        if ans is not None
    )

    st.subheader("🔎 Твой результат:")

    if total_score <= 3:
        st.write("Ты хер")
    elif total_score <= 6:
        st.write("Ты почти хер")
    else:
        st.write("Ты не хер")

    if st.button("Пройти тест заново"):
        st.session_state.current_question = 0
        st.session_state.answers = [None] * len(questions)
        st.rerun()

else:
    q_index = st.session_state.current_question
    question = questions[q_index]

    st.header(f"Вопрос {q_index + 1}/{len(questions)}")
    default_index = question["options"].index(st.session_state.answers[q_index]) if st.session_state.answers[q_index] is not None else 0
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
