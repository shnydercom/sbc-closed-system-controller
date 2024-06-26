from ffmpeg import FFmpeg
import os
import subprocess

# import pymkv


# ffmpeg -i input.h264 -i input.pts -c:v copy -c:a aac -strict experimental output.mp4

RECORDINGS = "recordings"
DATE_FOLDER = "2024-06-26"
MKV_FOLDER = "mkv"


def main():
    input_folder = RECORDINGS + "/" + DATE_FOLDER + "/"
    directory = os.fsencode(input_folder)

    output_folder = os.fsencode(RECORDINGS + "/" + MKV_FOLDER)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".h264"):
            h264_path = os.path.join(os.fsdecode(directory), filename)
            pts_path = h264_path.replace(".h264", "_pts.txt")
            output_path_and_filename = h264_path.replace(".h264", "")
            output_path_and_filename = output_path_and_filename.replace(
                DATE_FOLDER, MKV_FOLDER
            )
            convert_h264_to_mkv(h264_path, pts_path, output_path_and_filename)
            """fullpath = os.path.join(os.fsdecode(directory), filename)
            exec_single_file(
                fullpath,
            )"""
            continue
        else:
            continue


def convert_h264_to_mkv(h264_file, pts_file, output_file):
    # https://www.raspberrypi.com/documentation/computers/camera_software.html#save-pts
    # mkvmerge -o test.mkv --timecodes 0:timestamps.txt test.h264

    # avoiding a format error, defaulting to v2
    txt_file = open(pts_file, "r+")
    print(txt_file.writable())
    lines = txt_file.readlines()
    if len(lines) > 0 and not lines[0].startswith("# timestamp format"):
        lines.insert(0, "# timestamp format v2\n")
        txt_file.seek(0)
        txt_file.write("".join(lines))
        txt_file.truncate()
    subprocess.run(
        [
            "mkvmerge",
            "-o",
            output_file + ".mkv",
            "--timecodes",
            "0:" + pts_file,
            h264_file,
        ]
    )
    print(f"Conversion successful! Output saved as {output_file}")


# didn't get this to work on rpi5
def convert_h264_to_mp4(h264_file, pts_file, output_file):
    try:
        # Run FFmpeg command
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                h264_file,
                "-i",
                pts_file,
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                "-strict",
                "experimental",
                output_file,
            ]
        )
        print(f"Conversion successful! Output saved as {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")


# didn't get this to work either
def exec_single_file(h264_path: str):
    pts_path = h264_path.replace(".h264", "_pts.pts")
    output_path_and_filename = h264_path.replace(".h264", "")

    ffmpeg = (
        FFmpeg()
        # "ffmpeg",
        #    "-i", h264_file,
        #    "-i", pts_file,
        #    "-c:v", "copy",
        #    "-c:a", "aac",
        #    "-strict", "experimental",
        # .option("y")
        .input(h264_path)
        .input(pts_path)
        .option("c:v", "copy")
        .option("c:a", "aac")
        .option("strict", "experimental")
        .output(
            output_path_and_filename + ".mp4",
            # preset="veryslow",
            # crf=24,
        )
    )

    ffmpeg.execute()


if __name__ == "__main__":
    main()
