def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Transcribe audio with Whisper")
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        help="Path to input audio file",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    import whisper

    model = whisper.load_model("tiny")
    result = model.transcribe(args.input)
    print(result["text"])


if __name__ == "__main__":
    main()
