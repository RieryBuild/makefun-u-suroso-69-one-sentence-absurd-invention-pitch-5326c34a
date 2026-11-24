import os

PITCH = "A fitted sheet with four tiny seatbelts that buckle its corners to the mattress, so it can't pop off and wake you at 3 a.m."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PITCH)
