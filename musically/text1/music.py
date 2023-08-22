import mido
from mido import MidiFile, MidiTrack, Message

# Generate some example lyrics
generated_lyrics = input("Enter your lyrics: ")

# Generate a corresponding MIDI sequence based on lyrics
def generate_midi_from_lyrics(lyrics):
    # Process lyrics, generate MIDI events
    # Replace this with your actual mapping and generation logic
    
    # For demonstration purposes, let's just generate random notes
    midi_sequence = []
    for word in lyrics.split():
        note = mido.Message('note_on', note=90, velocity=50, time=500)
        note = mido.Message('note_on', note=80, velocity=100, time=700)
        midi_sequence.append(note)
    
    return midi_sequence

# Create a MIDI file and add the generated MIDI sequence
def create_midi_file(midi_sequence, filename='generated_music.mid'):
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    for msg in midi_sequence:
        track.append(msg)

    midi_file.save(filename)

# Generate MIDI sequence from lyrics and create MIDI file
generated_midi_sequence = generate_midi_from_lyrics(generated_lyrics)
create_midi_file(generated_midi_sequence)

print(generate_midi_from_lyrics)
