import streamlit as st
from datasets import load_dataset, Dataset, DatasetDict

# Ваш токен Hugging Face
HF_TOKEN = "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"

# Загрузка датасета
dataset_name = "Aleksmorshen/Testbase"
dataset = load_dataset(dataset_name, split="train")

# Функция для добавления нового имени в датасет
def add_name(name):
    new_entry = {"name": name}
    dataset.push_to_hub(new_entry)

# Функция для получения всех имен из датасета
def get_names():
    return [entry["name"] for entry in dataset]

# Основной код приложения
st.title("Введите имя")

# Ввод имени
name_input = st.text_input("Введите ваше имя:")

if st.button("Сохранить"):
    if name_input:
        add_name(name_input)
        st.success("Имя успешно сохранено!")
    else:
        st.error("Пожалуйста, введите имя.")

# Вывод всех сохраненных имен
st.subheader("Сохраненные имена:")
names = get_names()
if names:
    for name in names:
        st.write(name)
else:
    st.write("Нет сохраненных имен.")
