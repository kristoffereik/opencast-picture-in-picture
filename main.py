import os.path
DIR = 'INN'
count = int(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])/2)
print("Number of files to output: " + str(count))
ext = ".mp4"

presenter_presentation = []
commands = []

for i in range(count):
    presenter = "INN\\"+ str(i+1) + "A"+ext
    presentation = "INN\\"+str(i+1) + "B"+ext
    print("presenter: " +presenter)
    print("presentation: " + presentation)
    command = ".\\mpeg\\bin\\ffmpeg -i " + presenter + " -i " + presentation + " -filter_complex vstack=inputs=2 -r 25 FERDIG\\" + str(i+1) + ".mp4"
    commands.append(command)


for command in commands:
    os.system("start cmd.exe @cmd /c "+command)
