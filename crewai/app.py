import streamlit as st
from pathlib import Path

from crew import blog_crew


st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🤖",
    layout="wide"
)


st.title("AI Blog Generator")

st.write(
    "Generate a researched article using CrewAI Multi-Agent AI."
)


topic = st.text_input(
    "Enter your topic",
    placeholder="Example: Artificial Intelligence in Healthcare"
)


if st.button("Generate Blog"):

    if not topic.strip():

        st.warning("Please enter a topic.")

    else:

        with st.spinner(
            "Research Agent and Writer Agent are working..."
        ):

            try:

                result = blog_crew.kickoff(
                    inputs={
                        "topic": topic
                    }
                )

                st.success("Blog generated successfully!")

                # Display result
                st.subheader("Generated Blog")

                st.markdown(str(result))


                # Markdown download
                markdown_file = Path("news_blog_post.md")

                if markdown_file.exists():

                    with open(
                        markdown_file,
                        "rb"
                    ) as file:

                        st.download_button(
                            label="Download Markdown",
                            data=file,
                            file_name="news_blog_post.md",
                            mime="text/markdown"
                        )


                # PDF download
                pdf_file = Path("news_blog_post.pdf")

                if pdf_file.exists():

                    with open(
                        pdf_file,
                        "rb"
                    ) as file:

                        st.download_button(
                            label="Download PDF",
                            data=file,
                            file_name="news_blog_post.pdf",
                            mime="application/pdf"
                        )

            except Exception as e:

                st.error("Something went wrong.")

                st.exception(e)
                