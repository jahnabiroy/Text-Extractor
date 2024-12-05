def write_to_file(content, multimedia):
    with open(multimedia + "_output.txt", "w", encoding="utf-8") as f:
        f.write("Transcript :\n")
        f.write(content)
