from pathlib import Path

file_path = Path(__file__).with_name("about_me.txt")
night_out = "Perfect night out: I would go to a live music show in Denver and get dinner afterward."

f = open(file_path, "a+", encoding="utf-8")
f.seek(0)
existing_text = f.read()

if night_out not in existing_text:
    if existing_text and not existing_text.endswith("\n"):
        f.write("\n")
    f.write(night_out + "\n")

f.close()
