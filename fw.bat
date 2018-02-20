rm -fr ~/Downloads/*
rm -f data/celebA/*
rm -f checkpoint/celebA_64_64_64/*
watchmedo shell-command --patterns="*" --command "python fc.py" ../../Downloads
