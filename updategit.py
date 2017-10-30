import shutil

for path in self._chapter_paths:
            for root, dirs, files in os.walk(path):
                for extension in ["ipynb", "lyx"]:
                    _fname = "{fname}.{ext}".format(fname=filename,
                                                    ext=extension)
                    if _fname in files:
                        return os.path.join(root, _fname)
