import whisper


def main():
    model = whisper.load_model("tiny")
    result = model.transcribe("test_audio/coach_k.opus")
    print(result["text"])


if __name__ == "__main__":
    main()
