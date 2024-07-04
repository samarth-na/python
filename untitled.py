from subprocess import PIPE, Popen

name = "as"
args = ["-c", "import os; print(os.environ['FOO'])"]
print(args)

p = Popen(args, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
print(out)
print(err)
