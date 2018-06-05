FFMPEG_BIN = "ffmpeg"

import subprocess as sp
import numpy

import watermark.core.image as robust

def embed_video(input_video, watermark_string, output_video):
    command_read = [FFMPEG_BIN,
                    '-i', input_video,
                    '-f', 'image2pipe',
                    '-pix_fmt', 'yuv420p', 
                    '-vcodec', 'rawvideo', '-']
    pipe_read = sp.Popen(command_read, stdout=sp.PIPE, bufsize=10 ** 8)

    command_write = [FFMPEG_BIN,
                     '-y',  # (optional) overwrite output file if it exists
                     '-f', 'rawvideo',
                     '-vcodec', 'rawvideo',
                     '-s', '1920x1080',
                     '-pix_fmt', 'yuv420p',
                     '-i', '-',  # The input comes from a pipe
                     '-q:v', '2',
                     output_video]

    pipe_write = sp.Popen(command_write, stdin=sp.PIPE)

    raw_image = pipe_read.stdout.read(1920 * 1080 * 3)

    while raw_image != None and len(raw_image) != 0:
        # transform the byte read into a numpy array
        image = numpy.fromstring(raw_image, dtype='uint8')
        image = image.reshape((1080, 1920, 3))
        # throw away the data in the pipe's buffer.
        pipe_read.stdout.flush()

        img_tmp = image[:1080, :1920, 0]
        robust.embed_watermark(img_tmp, watermark_string)

        pipe_write.stdin.write(image.tostring())

        raw_image = pipe_read.stdout.read(1920 * 1080 * 3)


def extract_video(input_video):
    command_read = [FFMPEG_BIN,
                    '-i', input_video,
                    '-f', 'image2pipe',
                    '-pix_fmt', 'yuv420p',
                    '-vcodec', 'rawvideo', '-']
    pipe_read = sp.Popen(command_read, stdout=sp.PIPE, bufsize=10 ** 8)

    raw_image = pipe_read.stdout.read(1920 * 1080 * 3)

    while raw_image != None and len(raw_image) != 0:
        # transform the byte read into a numpy array
        image = numpy.fromstring(raw_image, dtype='uint8')
        image = image.reshape((1080, 1920, 3))
        # throw away the data in the pipe's buffer.
        pipe_read.stdout.flush()

        img_tmp = image[:1080, :1920, 0]
        robust.extract_watermark(img_tmp)

        raw_image = pipe_read.stdout.read(1920 * 1080 * 3)


if __name__ == "__main__":
    # embed_video("testvideo.mxf", "anjing", "embed.ts")
    extract_video("embed.ts")
