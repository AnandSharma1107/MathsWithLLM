import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler
from agent import create_agent

## Setting up the Streamlit app
st.set_page_config(page_title="Agentic AI for Mathematics, Reasoning & Knowledge",page_icon="🔢")
st.title("Agentic AI for Mathematics, Reasoning & Knowledge")
st.caption("Powered by GPT-OSS-120B")

groq_api_key=st.sidebar.text_input(label="Groq API Key",type="password")


if not groq_api_key:
    st.info("Please add your Groq API key first")
    st.stop()

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, How can I help you today?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## Lets start the interaction
question=st.text_area("Enter your question:","A number is 15. You add 5 to it, then subtract 3. After that, you double the result. What number do you get at the end?")

if st.button("Find Answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)
            if "agent" not in st.session_state:
                st.session_state.agent = create_agent(groq_api_key)
            assistant_agent = st.session_state.agent

            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response = assistant_agent.run(question)
            st.session_state.messages.append({'role':'assistant',"content":response})
            st.write('### Response:')
            st.success(response)

    else:
        st.warning("Please enter the question")









