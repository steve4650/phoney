import argparse

import whisper


def parse_args():
    parser = argparse.ArgumentParser(description="Transcribe audio with Whisper")
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        required=True,
        help="Path to input audio file",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    process_audio(args.input)

def process_audio(input_path):
    model = whisper.load_model("tiny")
    result = model.transcribe(input_path)
    print(result["text"])


if __name__ == "__main__":
    main()
