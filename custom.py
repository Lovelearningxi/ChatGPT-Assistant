from set_context import set_context

# 用户名
user_name = '珂仔生活实录'
gpt_name = 'ChatGPT'
# 头像(svg格式) 来自 https://www.dicebear.com/playground?style=identicon
user_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" fill="none" shape-rendering="auto" width="512" height="512"><desc>"Lorelei Neutral" by "Lisa Wischofsky", licensed under "CC0 1.0". / Remix of the original. - Created with dicebear.com</desc><metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:RDF><cc:Work><dc:title>Lorelei Neutral</dc:title><dc:creator><cc:Agent rdf:about="https://www.instagram.com/lischi_art/"><dc:title>Lisa Wischofsky</dc:title></cc:Agent></dc:creator><dc:source>https://www.figma.com/community/file/1198749693280469639</dc:source><cc:license rdf:resource="https://creativecommons.org/licenses/zero/1.0/" /></cc:Work></rdf:RDF></metadata><mask id="viewboxMask"><rect width="600" height="600" rx="0" ry="0" x="0" y="0" fill="#fff" /></mask><g mask="url(#viewboxMask)"><rect fill="#ffffff" width="600" height="600" x="0" y="0" /><g transform="translate(-246 -234)"><path d="M503 394c7 0 14 2 19 6 4 2 7 4 8 8 1 2 0 5-2 6-5 1-10-2-14-3l-9-1c-13-1-26 1-39 4a169 169 0 0 0-60 31c-4 2-9 5-14 4-3 0-3-4-2-7 1-6 7-11 12-16 10-9 23-15 35-20 20-9 44-14 66-12ZM659 396c7-2 14-1 20 3 4 3 8 6 9 11 1 3 1 6-2 7s-7 1-10-1c-5-3-9-6-15-6-5 0-10 1-14 3-8 4-16 11-20 19l-6 9h-3v-6c2-8 7-16 13-22 7-8 17-15 28-17Z" fill="#000000"/></g><g transform="translate(-246 -234)"><path d="M490 492c7 3 13 8 19 13 6 6 12 13 13 22 0 2 1 5-2 6l-4-8c2 9-3 20-12 24-6 3-13 4-19 3-9-1-17-6-23-13-4-6-6-14-4-21 1-8 5-15 11-19a90 90 0 0 0-55 14c-5 3-10 7-13 12-2 3-5 5-9 5-6 0-10-7-8-12l8-11c12-10 26-18 41-22 19-6 40-2 57 7ZM681 484c6 2 14 4 17 9 4 6 1 13-6 14 2 8 2 17-3 24-7 9-23 11-31 3-5-6-9-14-8-22 1-4 3-7 6-11-12 3-21 11-28 20-4 5-6 10-9 16l-5 1 1-6a90 90 0 0 1 39-43c8-5 17-7 27-5Z" fill="#000000"/></g><g transform="translate(-246 -234)"></g><g transform="translate(-246 -234)"><path fill-rule="evenodd" clip-rule="evenodd" d="M622 659c1-4-5-4-7-4-15 0-30 3-45 7a441 441 0 0 0-84 36c-6 3-11 7-15 13l-2 4 5-1c5-5 12-8 18-12 0 7 0 14 4 20 3 6 9 10 15 11 9 1 19-3 26-9 11-8 18-20 24-32 3-6 3-11 3-17 16-6 33-9 49-12h1c3 0 6-1 8-4Zm-84 48c6-8 11-18 14-29l-27 10c0 7-4 14-7 21l-1-6v-1l2-12-23 10v1c2 6 4 14 9 18 4 5 10 5 16 3 7-3 13-9 17-15Z" fill="#000000"/></g><g transform="translate(-246 -234)"><path d="M609 602c1 9-4 16-9 23-4 3-9 6-15 6s-13-3-19-5c-4-2-8-3-11-6l5-4c9-1 17 3 25 4 4 0 7-3 9-6 5-5 9-10 15-12Z" fill="#000000"/></g><g transform="translate(-246 -234)"></g></g></svg>"""
gpt_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5 5" fill="none" shape-rendering="crispEdges" width="512" height="512"><desc>"Identicon" by "Florian Körner", licensed under "CC0 1.0". / Remix of the original. - Created with dicebear.com</desc><metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:RDF><cc:Work><dc:title>Identicon</dc:title><dc:creator><cc:Agent rdf:about="https://dicebear.com"><dc:title>Florian Körner</dc:title></cc:Agent></dc:creator><dc:source>https://dicebear.com</dc:source><cc:license rdf:resource="https://creativecommons.org/publicdomain/zero/1.0/" /></cc:Work></rdf:RDF></metadata><mask id="viewboxMask"><rect width="5" height="5" rx="0" ry="0" x="0" y="0" fill="#fff" /></mask><g mask="url(#viewboxMask)"><path d="M1 0H0v1h1V0ZM5 0H4v1h1V0Z" fill="#ffb300"/><path fill="#ffb300" d="M1 1h3v1H1z"/><path fill="#ffb300" d="M1 2h3v1H1z"/><path fill="#ffb300" d="M2 3h1v1H2z"/><path fill="#ffb300" d="M1 4h3v1H1z"/></g></svg>"""
# 内容背景
user_background_color = ''
gpt_background_color = 'rgba(225, 230, 235, 0.5)'
# 模型初始设置
initial_content_all = {
    "history": [],
    "paras": {
        "temperature": 1.0,
        "top_p": 1.0,
        "presence_penalty": 0.0,
        "frequency_penalty": 0.0,
    },
    "contexts": {
        'context_select': '不设置',
        'context_input': '',
        'context_level': 4
    }
}
# 上下文
set_context_all = {"不设置": ""}
set_context_all.update(set_context)

# 自定义css、js
css_code = """
    <style>
    section[data-testid="stSidebar"] > div > div:nth-child(2) {
        padding-top: 0.75rem !important;
    }
    
    section.main > div {
        padding-top: 10px;
    }
    
    section[data-testid="stSidebar"] h1 {
        text-shadow: 2px 2px #ccc;
        font-size: 28px !important;
        font-family: "微软雅黑", "auto";
        margin-bottom: 6px;
        font-weight: 500 !important;
    }
    
    section[data-testid="stSidebar"] .stRadio {
        overflow: overlay;
        height: 28vh;
    }
    
    hr {
        margin-top: 20px;
        margin-bottom: 30px;
    }
    
    .avatar {
        display: flex;
        align-items: center;
        gap: 10px;
        pointer-events: none;
        margin: -8px 10px -16px;
    }
    
    .avatar svg {
        width: 30px;
        height: 30px;
    }
    
    .avatar h2 {
        font-size: 20px;
        margin: 0;
    }
    
    .content-div {
        padding: 5px 20px;
        margin: 5px;
        text-align: left;
        border-radius: 10px;
        border: none;
        line-height: 1.6;
        font-size: 17px;
    }
    
    .content-div.assistant p {
        padding: 4px;
        margin: 2px;
    }
    
    .content-div.user p {
        padding: 4px;
        margin: -5px 2px -3px;
    }
    
    div[data-testid="stForm"] {
        border: none;
        padding: 0;
    }
    
    button[kind="primaryFormSubmit"] {
        border: none;
        padding: 0;
    }
    
    div[data-testid="stForm"] + div[data-testid="stHorizontalBlock"] div[data-baseweb="select"] > div:nth-child(1) {
        background-color: transparent;
        justify-content: center;
        font-weight: 300;
        border-radius: 0.25rem;
        margin: 0;
        line-height: 1.4;
        border: 1px solid rgba(49, 51, 63, 0.2);
    }
    </style>
"""

js_code = """
<script>
function checkElements() {
    const textinput = window.parent.document.querySelector("textarea[aria-label='**输入：**']");   //label需要相对应
    const textarea = window.parent.document.querySelector("div[data-baseweb = 'textarea']");
    const button = window.parent.document.querySelector("button[kind='secondaryFormSubmit']");
    const tabs = window.parent.document.querySelectorAll('button[data-baseweb="tab"] p');
    const tabs_div = window.parent.document.querySelector('div[role="tablist"]');
    const tab_panels = window.parent.document.querySelectorAll('div[data-baseweb="tab-panel"]');

    if (textinput && textarea && button && tabs && tabs_div && tab_panels) {
        // 双击点位输入框，同时抑制双击时选中文本事件
        window.parent.document.addEventListener('dblclick', function (event) {
            let activeTab = tabs_div.querySelector('button[aria-selected="true"]');
            if (activeTab.querySelector('p').textContent === '💬 聊天') {
                textinput.focus();
            } else {
                tabs[0].click();
                const waitMs = 50;

                function waitForFocus() {
                    if (window.parent.document.activeElement === textinput) {
                    } else {
                        setTimeout(function () {
                            textinput.focus();
                            waitForFocus();
                        }, waitMs);
                    }
                }

                waitForFocus();
            }
        });
        window.parent.document.addEventListener('mousedown', (event) => {
            if (event.detail === 2) {
                event.preventDefault();
            }
        });
        textinput.addEventListener('focusin', function (event) {
            event.stopPropagation();
            textarea.style.borderColor = 'rgb(255,75,75)';
        });
        textinput.addEventListener('focusout', function (event) {
            event.stopPropagation();
            textarea.style.borderColor = 'white';
        });

        // Ctrl + Enter快捷方式
        window.parent.document.addEventListener("keydown", event => {
            if (event.ctrlKey && event.key === "Enter") {
                if (textinput.textContent !== '') {
                    button.click();
                }
                textinput.blur();
            }
        });

        // 设置 Tab 键
        textinput.addEventListener('keydown', function (event) {
            if (event.keyCode === 9) {
                // 阻止默认行为
                event.preventDefault();
                if (!window.parent.getSelection().toString()) {
                    // 获取当前光标位置
                    const start = this.selectionStart;
                    const end = this.selectionEnd;
                    // 在光标位置插入制表符
                    this.value = this.value.substring(0, start) + '\t' + this.value.substring(end);
                    // 将光标移动到插入的制表符之后
                    this.selectionStart = this.selectionEnd = start + 1;
                }
            }
        });

        // 处理tabs 在第一次切换时的渲染问题
        tabs.forEach(function (tab, index) {
            const tab_panel_child = tab_panels[index].querySelectorAll("*");

            function set_visibility(state) {
                tab_panels[index].style.visibility = state;
                tab_panel_child.forEach(function (child) {
                    child.style.visibility = state;
                });
            }

            tab.addEventListener("click", function (event) {
                set_visibility('hidden')

                let element = tab_panels[index].querySelector('div[data-testid="stVerticalBlock"]');
                let main_block = window.parent.document.querySelector('section.main div[data-testid="stVerticalBlock"]');
                const waitMs = 50;

                function waitForLayout() {
                    if (element.offsetWidth === main_block.offsetWidth) {
                        set_visibility("visible");
                    } else {
                        setTimeout(waitForLayout, waitMs);
                    }
                }

                waitForLayout();
            });
        });
    } else {
        setTimeout(checkElements, 100);
    }
}

checkElements()
</script>
"""
