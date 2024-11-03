
import streamlit as st
import os
from datasets import load_dataset, Dataset, DatasetDict, DatasetInfo, Features, Value
from datasets.utils import EmptyDatasetError

# Получаем токен Hugging Face из переменной окружения
HF_TOKEN = "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"

# Название набора данных на Hugging Face
dataset_name = "Aleksmorshen/Testbase"

# Функция для создания начального набора данных
def create_initial_dataset():
    # Создаем новый набор данных с начальной записью
    initial_data = {"name": ["Пример имени"]}
    initial_dataset = Dataset.from_dict(initial_data)
    # Загружаем набор данных на Hugging Face
    initial_dataset.push_to_hub(dataset_name, token=HF_TOKEN)

# Пытаемся загрузить набор данных
try:
    dataset = load_dataset(dataset_name, split="train")
    # Проверка на пустой набор данных
    if len(dataset) == 0:
        create_initial_dataset()
        dataset = load_dataset(dataset_name, split="train")
except EmptyDatasetError:
    create_initial_dataset()
    dataset = load_dataset(dataset_name, split="train")

# Функция для добавления нового имени в набор данных
def add_name(name):
    new_entry = {"name": name}
    dataset.push_to_hub(new_entry)

# Функция для получения всех имен из набора данных
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
# Ваш токен Hugging Face


