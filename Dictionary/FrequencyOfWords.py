para = "The sun dipped below the horizon, casting a warm amber glow across the quiet village. Birds chirped their final songs of the day as the scent of jasmine drifted through the air. Children laughed in the distance, their silhouettes dancing in the fading light. Inside a small cottage, an old radio hummed softly, playing tunes from a bygone era. The world seemed to pause for a moment, wrapped in the gentle embrace of twilight, where memories mingled with the promise of tomorrow."

cleaned_chars = []

for char in para:
    if char.isalnum() or char.isspace():
        cleaned_chars.append(char.lower())
    else:
        cleaned_chars.append("")

cleaned = ''.join(cleaned_chars)

print(cleaned)

words = cleaned.split()

print(words)

frequency = {}

for x in words:
    frequency[x] = frequency.get(x,0) +1

print(frequency)