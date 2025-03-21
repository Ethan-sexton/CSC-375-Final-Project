import dataset.wav_generation as wv
wv.generateFile("A", 4)

def makeAll():
    #Generate a wav file for each note in each octave with a varying amount of noise
    notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    note = 0
    for note in notes: 
        octave = 0
        while octave <= 8:
            noise = 0
            while noise <= .5:
                wv.generateFile(note, octave, noise)
                noise += .02
            octave += 1