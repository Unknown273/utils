try:
  file_contents = ""
  with open("requirements.txt", "r") as myFile:
    pkgs = myFile.read()
    pkgs = pkgs.splitlines()

  for pkg in pkgs:
      file_contents += pkg.split('==')[0] + "\n"

  with open("requirements.txt", "w") as myFile:
    myFile.write(file_contents)
    print("Successfully generated the new requirements.txt file")

except FileNotFoundError:
  print(
  '''The requirements.txt file doesn't exist yet
You can generate it with the command
pip freeze > requirements.txt'''
)
