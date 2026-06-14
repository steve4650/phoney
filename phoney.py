def main():
    args = parse_args()

    if args.input:
        process_input(args.input)

    if args.output:
        create_audio_response(args.output)

    if args.llm:
        test_llm()


def parse_args():
    """parse CLI args..."""
    import argparse

    parser = argparse.ArgumentParser(description="Transcribe audio with Whisper or create TTS output with KittenTTS")
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        help="Path to input audio file",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        help="Path to write generated TTS audio file",
    )
    parser.add_argument(
        "--llm",
        dest="llm",
        action="store_true",
        help="Test LLM responses with qwen3.6:27b model",
    )
    args = parser.parse_args()

    if not args.input and not args.output and not args.llm:
        parser.error("one of -i/--input, -o/--output, or --llm is required")

    return args


def process_input(input_path):
    """the -i command. process the input audio file with Whisper and print the transcription to stdout."""
    import whisper

    model = whisper.load_model("tiny")
    result = model.transcribe(input_path)
    print(result["text"])


def create_audio_response(output_path):
    """the -o command. create an audio response with KittenTTS and write it to the specified path."""
    import soundfile as sf
    from kittentts import KittenTTS

    model = KittenTTS("KittenML/kitten-tts-nano-0.8")
    audio = model.generate("Now is the time for all good men to come to the aid of the party.", voice="Leo")
    sf.write(output_path, audio, 24000)
    print(f"Wrote audio to {output_path}")


def test_llm():
    """the --llm command. test LLM responses with the qwen3.6:27b model."""
    from ollama import ChatResponse, chat

    response: ChatResponse = chat(
        model="qwen3.6:27b",
        messages=[
            {
                "role": "user",
                "content": "Why is the sky blue?",
            },
        ],
    )
    print(response["message"]["content"])
    # or access fields directly from the response object
    print(response.message.content)


if __name__ == "__main__":
    main()
