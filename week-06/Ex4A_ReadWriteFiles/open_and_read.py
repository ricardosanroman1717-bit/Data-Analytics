from pathlib import Path

file_path = Path(__file__).with_name("about_me.txt")

f = open(file_path, "r", encoding="utf-8")
print("Full file:")
print(f.read())
f.close()

f = open(file_path, "r", encoding="utf-8")
print("First 50 characters:")
print(f.read(50))
print("Next 50 characters:")
print(f.read(50))
f.close()

f = open(file_path, "r", encoding="utf-8")
print("First 10 characters of the first line:")
print(f.readline(10))
print("Rest of the first line:")
print(f.readline())
print("Next four lines:")
for i in range(1, 5):
    print(f.readline(), end="")
print("\n")
f.close()

f = open(file_path, "r", encoding="utf-8")
print("readlines() with no argument:")
print(f.readlines())
f.close()

f = open(file_path, "r", encoding="utf-8")
print("readlines(1) followed by readlines(1):")
print(f.readlines(1))
print(f.readlines(1))
print("readlines(10) followed by readlines(10):")
print(f.readlines(10))
print(f.readlines(10))
print("readlines(100):")
print(f.readlines(100))
print("readlines(-1) after the previous reads:")
print(f.readlines(-1))
f.close()

f = open(file_path, "r", encoding="utf-8")
print("readlines(-1) from the beginning:")
print(f.readlines(-1))
f.close()

f = open(file_path, "r", encoding="utf-8")
first_50 = f.read(50)
next_four_lines = []
for i in range(1, 5):
    next_four_lines.append(f.readline())
next_100_lines = f.readlines(100)

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100_lines}")
f.close()
