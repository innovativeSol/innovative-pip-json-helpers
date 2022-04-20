"""Console script for json_helpers."""

import fire


def help():
    print("json_helpers")
    print("=" * len("json_helpers"))
    print("Common JSON usage patterns.")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
