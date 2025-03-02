from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import tempfile
from pydub import AudioSegment
AudioSegment.converter = r"C:\Users\kumar\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1-full_build\bin\ffmpeg.exe"
AudioSegment.ffmpeg = r"C:\Users\kumar\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1-full_build\bin\ffmpeg.exe"

def text_to_speech(text, lang="hi", play_audio=True):
    if not text:
        return
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
        filename = fp.name
    tts.save(filename)
    if play_audio:
        audio = AudioSegment.from_mp3(filename)
        play(audio)
    return filename

def speech_to_text(lang="hi-IN"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=5)
    try:
        return r.recognize_google(audio, language=lang)
    except Exception:
        return ""
