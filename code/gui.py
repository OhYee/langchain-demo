
import gradio as gr
from lc import lc
from utils.const import *

with gr.Blocks() as iface:
    gr.Markdown(
        """<h1><center>大模型会话测试</center></h1>
        <center><font size=3>
        </center></font>
        """
    )
    history_state = gr.State()

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Row():
                llm_dropdown = gr.Dropdown(
                    [
                        LLM.OPEN_AI,
                        # LLM.CHAT_GLM,
                    ],
                    label="大模型选择",
                    value=LLM.OPEN_AI,
                    interactive=True
                )

                openai_token_ipt = gr.Textbox(label="OpenAI Token", visible=True, interactive=True)

        with gr.Column(scale=4):
            with gr.Row():
                chatbot_area = gr.Chatbot(label=llm_dropdown.value).style(height=400)
            with gr.Row():
                message_ipt = gr.Textbox(label='请输入问题')
            with gr.Row():
                clear_btn = gr.Button("清空")
                send_btn = gr.Button("发送")

            with gr.Row():
                gr.Markdown(
                    """提醒：<br>
                    [Chinese-LangChain](https://github.com/yanqiangmiffy/Chinese-LangChain) <br>
                    有任何使用问题[Github Issue区](https://github.com/yanqiangmiffy/Chinese-LangChain)进行反馈. <br>
                    """
                )
        with gr.Column(scale=2):
            search = gr.Textbox(label='搜索结果')


    # functions
        
    def send(openai_key, msg, history):
        print(openai_key, msg, history)
        
        result = lc.call(openai_key, msg)
        
        print(result)

        if history == None:
            history = []
            
        history.append((msg, result))
        
        return msg, history, history, ""

    # binding functions
    
    llm_dropdown.change(
        lambda llm: (gr.Chatbot.update(label=llm, value=""), gr.Textbox.update(visible=llm==LLM.OPEN_AI), None),
        inputs=[llm_dropdown],
        outputs=[chatbot_area, openai_token_ipt, history_state]
    )

    send_btn.click(
        send,
        inputs=[ openai_token_ipt, message_ipt, history_state ],
        outputs=[ message_ipt, chatbot_area, history_state, search ]
    )

    # 清空历史对话按钮 提交
    clear_btn.click(
        fn=lambda: ('', None),
        inputs=[],
        outputs=[chatbot_area, history_state],
        queue=False
    )

    # 输入框 回车
    message_ipt.submit(
        send,
        inputs=[ openai_token_ipt, message_ipt, history_state ],
        outputs=[message_ipt, chatbot_area, history_state, search]
    )