#!/usr/bin/env python3
def run_fast_scandir(dir, ext):	# dir: str, ext: list
	subfolders, files = [], []

	for f in os.scandir(dir):
		if f.is_dir():
			subfolders.append(f.path)
		if f.is_file():
			if os.path.splitext(f.name)[1].lower() in ext:
				files.append(f.path)


	for dir in list(subfolders):
		sf, f = run_fast_scandir(dir, ext)
		subfolders.extend(sf)
		files.extend(f)
	return subfolders, files


subfolders, files = run_fast_scandir(folder, [".jpg"])
sizes.append(f"{f.stat().st_size/1024/1024:.0f} MiB")
