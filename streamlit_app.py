import sys

import streamlit as st
from streamlit.web import cli as stcli

from article_processing import modules


def main():
    st.title("Article Processing")
    article_text = st.text_area("Статья", placeholder="Введите статью...")
    if article_text != "":
        for module_name, module in modules.items():
            st.write(f"{module.get('result_title')} — {module.get('function')(article_text)}")
        st.write("Обработка статьи завершена!")
    else:
        st.write("После ввода статьи здесь отобразятся результаты ее обработки")


if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
