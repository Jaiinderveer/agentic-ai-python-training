import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Customer Support", page_icon="🎧")

st.title("🎧 Customer Support")

st.write(
    """
Welcome to the Customer Support Assistant.

I can help you learn how to use the Task Delegation System.

### I can help with:
- Creating tasks
- Updating tasks
- Deleting tasks
- Viewing saved tasks
- Explaining application features

Click the microphone below to start talking.
"""
)

components.html("""
<!DOCTYPE html>
<html>
<body style="margin:0;background:#111;">
<elevenlabs-convai
agent-id="agent_0801ky1nhx39e9cvs7bmr40rc8wa"
variant="expanded">
</elevenlabs-convai>

<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async></script>
</body>
</html>
""", height=700)