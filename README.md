# Videonotat PiP

This tool batch produces picture in picture videos from paired Opencast recordings. Each pair consists of a presenter video and a presentation video. The script stacks each pair vertically and outputs ready to use combined files.

## Requirements
- Windows environment
- FFmpeg
- Input videos in MP4 format

## Folder Structure
- `INN` contains input files
- `FERDIG` receives finished files
- `mpeg` contains bundled FFmpeg binaries
- `main.py` or `main.exe` runs the process

## How It Works
Place your video pairs in the `INN` folder. Files must follow this naming pattern:

- Presenter video: `1A.mp4`
- Presentation video: `1B.mp4`
- Next pair: `2A.mp4` and `2B.mp4`
- Continue incrementing numbers for each pair

The script counts how many pairs exist, generates FFmpeg commands and executes them automatically. Each output file is written to `FERDIG` as:

- 1.mp4
- 2.mp4
- 3.mp4

## Steps
1. Put all presenter and presentation videos into `INN`.
2. Rename them so each pair has the format `nA.mp4` and `nB.mp4`.
3. Run `main.exe` or run `python main.py`.
4. Finished PiP videos appear in `FERDIG`.

## Notes
- The videos are stacked vertically at 25 fps.
- Make sure each pair uses consistent numbering.