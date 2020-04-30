import HTPA32x32d
HTPA32x32d.tools.VERBOSE = True
import os
raw_dir = "raw" # this is your directory that contains raw .TXT files from HTPA32x32d, all named YYYYMMDD_HHmm_ID{id}.TXT
preparer = HTPA32x32d.tools.TPA_RGB_Preparer()
preparer.config(os.path.join(raw_dir, "config.json")) # now fill config.json
HTPA32x32d.tools.SYNCHRONIZATION_MAX_ERROR = 0.6#E.G.
preparer.prepare() # now fill labels and make_config.json.
