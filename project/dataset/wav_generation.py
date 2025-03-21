import wave
import numpy as np
import random as rd
import matplotlib as mpl


#Dictionary of note names to their respective frequencies at octave 0
notes_dict = {
    "C" : "16.3516",
    "C#" : "17.32391",
    "D" : "18.35405",
    "D#" : "19.44544",
    "E" : "20.60172",
    "F" : "21.82676",
    "F#" : "23.12465",
    "G" : "24.49971",
    "G#": "25.95654",
    "A" : "27.5",
    "A#" : "29.13524",
    "B" : "30.86771"
}

def generateWav(note, octave, noise_percent = 0.0, amplitude = 0.5, duration = 10):
    #Set Audio Parameters
    frame_rate = 44100 # Samples per second (44100 is standard)
    channels = 1 # 1 is mono audio
    sample_width = 4 # Number of bytes per sample
    
    frequency = float(notes_dict[note]) * pow(2, octave) #As you move up an octave, you double the frequency
    print(f"Frequency: {frequency} hz")
    
    #Generate sine wave with matching frequency, amplitude, and duration
    total_frames = int(frame_rate * duration)
    time = np.linspace(0, duration, total_frames, False)
    print(time)
    sine_wave = np.sin(2.0 * time * frequency * np.pi)
    normalized_sine_wave = sine_wave * amplitude
    
    noise_wave = noise_percent * np.random.normal(0, 1, len(time)) # Generate a generic noisy signal  
    noisy_sine_wave = normalized_sine_wave + noise_wave # Add it to the sine wave
    
    #Put sine wave in wav file
    numerical_sine_wave = np.int16(noisy_sine_wave * 32767) # 32767 = (2^15)-1 = min/max for a 16 bit int
    #Save wav file in NOTE_DIR\NOTEOCTAVE NOISE RAND.wav
    filename = f"..\..\Training Data\sounds\{note}\{note}{octave} {noise_percent} {rd.randint(0,1000)}.wav"
    with wave.open(filename, 'w') as output_file:
        #Sets file parameters
        output_file.setnchannels(channels)
        output_file.setframerate(frame_rate)
        output_file.setsampwidth(sample_width)
        
        #Saves to file
        output_file.writeframes(numerical_sine_wave.tobytes())
        print(f"Successfully wrote {note}{octave} to {filename}")

def makeAll():
    #Generate a wav file for each note in each octave with a varying amount of noise
    notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    note = 0
    for note in notes: 
        octave = 0
        while octave <= 8:
            noise = 0
            while noise <= .5:
                generateWav(note, octave, noise)
                noise += .02
            octave += 1
    