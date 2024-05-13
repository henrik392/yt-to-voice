from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>HTMX + FastAPI Demo</title>
            <script src="https://unpkg.com/htmx.org"></script>
        </head>
        <body>
            <h1>Hello from FastAPI</h1>
            <button hx-get="/time" hx-target="#time" hx-swap="innerHTML">
                What time is it?
            </button>
            <div id="time">Press the button to see the time.</div>
        </body>
    </html>
    """


@app.get("/time")
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."


# if __name__ == '__main__':
#     video_id, file_path = download_audio(
#         "https://www.youtube.com/watch?v=S_RorY_FRvo&ab_channel=Fireship")

#     # file_name = r'Erlang in 100 Seconds.mp3'

#     voice = VoiceGenerator(video_id, file_path)
#     voice.generate_audio(
#         """
# This has been Foodi in 100 seconds. Let me know what you want to see next in the comments. Thanks for watching, and I will see you in the next one.
#         """
#     )
