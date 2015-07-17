from subprocess import Popen, PIPE

def play(mp3Path):
    p = Popen(["mpg123", mp3Path], stdout=PIPE, stderr=PIPE)
    return p

def stop(process):
    process.kill()

p = play("music.mp3")
stop(p)
