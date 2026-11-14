# Exercise recording

The GIF renders actual captured output from `python -m examples.descent` and
`python -m unittest discover -s tests`. The first command calls the original
`Solution.get_minimizer` for each displayed iteration count, starting from +5 and
-5. It demonstrates a scalar quadratic exercise, not GPT training.

The original gradient-descent implementation is unchanged. Source hashes and
full command output are recorded in `demo-recording.json`. To rebuild the GIF,
install Pillow in a development environment and run `python scripts/record_demo.py`.
Pillow is needed only for recording; the exercise, walkthrough, and tests need no
third-party dependencies. The animation uses reading pauses, not real-time timing.
