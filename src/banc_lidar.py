from argparse import ArgumentParser
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from sys import stdin, stdout
from typing import TypeVar

import filters


@dataclass
class Data[T]:
    data: T


@dataclass
class NeedsPrompting:
    pass


@dataclass
class Quit:
    pass


@dataclass
class Back:
    pass


@dataclass
class BadLabelError:
    error: str


@dataclass
class Error[T]:
    error: T


ConfiguredFilter = Callable[[list[float]], list[float]]


def read_input(
    input_filename,
) -> Data[list[str]] | NeedsPrompting | Error[FileNotFoundError]:
    if input_filename is None:
        # if stdin is empty, prompt the user for selection of the data
        data: list[str] = stdin.readlines()
        if len(data) == 0:
            return NeedsPrompting()
        return Data(data)
    try:
        with open(input_filename, "r") as f:
            return Data(f.readlines())
    except FileNotFoundError as e:
        return Error(e)


def parse_filter(filter_label: str) -> Data[ConfiguredFilter] | Error[str]:
    # TODO: could fail
    label, *args = filter_label.split("&")
    match label:
        case "1":
            min, max = map(float, args)
            return Data(lambda data, min=min, max=max: filters.min_max(data, min, max))
        case "2":
            return Data(lambda data: filters.sliding_average(data, window_size=3))
        case "3":
            return Data(lambda data: filters.sliding_median_of_3(data))
        case other:
            return Error(f"This filter label is not recognized: {other}")


def load_filter(filter_label) -> Data[ConfiguredFilter] | Error[str] | NeedsPrompting:
    if filter_label is None:
        return NeedsPrompting()
    match parse_filter(filter_label):
        case Error(e):
            return Error(e)
        case Data(d):
            return Data(d)


def prompt[D, E](
    question: str,
    validator: Callable[[str], Data[D] | Error[E]],
    validator_failed_msg: None | Callable[[Error[E]], str] = None,
    default: None | D = None,
) -> Data[D] | Back | Quit:
    while True:
        print(question)
        print("- q for Quit, b for Back")
        if default:
            print(f"- Enter for default ({default})")
        input_text = input("> ").strip()
        if input_text == "q":
            return Quit()
        if input_text == "b":
            return Back()
        match validator(input_text):
            case Error(e):
                if validator_failed_msg:
                    print(validator_failed_msg(Error(e)))
                continue
            case Data(d):
                return Data(d)


def prompt_for_input_file() -> Data[list[float]] | Quit:
    while True:
        input_text = input("where is the input? (q to quit)")
        if input_text == "q":
            return Quit()
        try:
            with open(input_text) as f:
                file_contents = f.readlines()
                try:
                    data = list(map(float, file_contents))
                    return Data(data)
                except ValueError:
                    print("Unexpected contents.")
                    continue
        except FileNotFoundError:
            print("this file does not exist or is unreachable.")
            continue


def prompt_for_filter() -> Data[ConfiguredFilter] | Quit:
    while True:
        input_text = input("which filter? (q to quit)")
        match input_text:
            case "q":
                return Quit()
            case "1":
                match prompt_filter_1():
                    case Back():
                        continue
                    case other:
                        return other
            case other:
                print(f"Invalid filter name: {other}")
                continue


def prompt_filter_1() -> Data[ConfiguredFilter] | Quit | Back:
    while True:
        input_text = input("specify minimum: (q to quit, b for back)")
        match input_text:
            case "q":
                return Quit()
            case "b":
                return Back()
            case other:
                try:
                    minimum = float(other)
                except ValueError:
                    continue


def prompt_filter_1_arg1():
    pass


def prompt_for_output_file():
    while True:
        input_text = input("where should the data be written? (q to quit)")
        if input_text == "q":
            return Quit()
        if Path(input_text).exists():
            return Data(input_text)
        else:
            print("The entered path does not exist or is unreachable.")
            continue

def validator_input_file(file_name) -> Data[list[float]] | Error[str]:
    try:
        with open(file_name) as f:
            file_contents = f.readlines()
            data = list(map(float, file_contents))
            return Data(data)
    except FileNotFoundError:
        return Error("This file does not exist.")
    except ValueError:
        return Error("Unexpected file contents.")

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    parser.add_argument("-f", "--filter")
    parser.add_argument("--hide-stats", action="store_true")

    args = parser.parse_args()

    should_prompt_for_output_if_not_exists = False

    match read_input(args.input):
        case Error(e):
            print(f"Input file not found: {e.filename}")
            return
        case NeedsPrompting():
            should_prompt_for_output_if_not_exists = True
            match prompt(
                question="where is the input?",
                validator=validator_input_file,
                validator_failed_msg=lambda e: e.error,
            ):
                case Quit() | Back():
                    print("Okay...")
                    return
                case Data(d):
                    data = d
        case Data(d):
            input_lines = d
            try:
                data = list(map(float, input_lines))
            except ValueError:
                print("Unexpected input contents.")
                return

    match parse_filter(args.filter):
        case Error(e):
            print(e)
            return
        case NeedsPrompting():
            match prompt_for_filter():
                case Quit():
                    print("Okay, then :(")
                    return
                case Data(d):
                    filter = d
        case Data(d):
            filter = d

    output = filter(data)

    if args.output is not None:
        with open(args.output) as f:
            f.writelines(map(str, output))
        return

    if not should_prompt_for_output_if_not_exists:
        stdout.writelines(map(str, output))
        stdout.flush()
        return

    match prompt_for_output_file():
        case Quit():
            print("So close to the end! T_T")
            return
        case Data(file_name):
            with open(file_name) as f:
                f.writelines(map(str, output))
            return


if __name__ == "__main__":
    main()
