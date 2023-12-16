from src.runner import runner
from timeit import default_timer

testfile = "test.md"


with open(testfile, "r") as f:
    len_ = len(f.read())

start = default_timer()
if __name__ == "__main__":
    language = "cs"
    title = "dokument"
    file = runner(language, title, filename=testfile)
    data = file.run()
    file.make_file()
    file.save_file(data)

stop = default_timer()
print((stop-start)*100, "ms")
print(len_)