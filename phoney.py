def parse_args():
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
    args = parser.parse_args()

    if not args.input and not args.output:
        parser.error("one of -i/--input or -o/--output is required")

    return args


def main():
    args = parse_args()

    if args.input:
        process_input(args.input)

    if args.output:
        create_audio_response(args.output)


def process_input(input_path):
    import whisper

    model = whisper.load_model("tiny")
    result = model.transcribe(input_path)
    print(result["text"])


def create_audio_response(output_path):
    import soundfile as sf
    from kittentts import KittenTTS

    model = KittenTTS("KittenML/kitten-tts-nano-0.8")
    audio = model.generate("Now is the time for all good men to come to the aid of the party.", voice="Leo")
    sf.write(output_path, audio, 24000)
    print(f"Wrote audio to {output_path}")


if __name__ == "__main__":
    main()
