# Turtle Coordinate

A small collection of Python turtle programs, built while learning event handling and loops.

## Files

- **`sketch.py`**: a turtle you control with the keyboard to draw on the screen.
- **`race.py`**: a turtle race where you bet on which colour will win.

## Requirements

- Python 3.x
- The `turtle` module, which comes with standard Python

No extra packages are needed.

## Setup

```bash
git clone https://github.com/htetnay-origin/Turtle_Coordinate.git
cd Turtle_Coordinate
python3 sketch.py   # or race.py
```

## sketch.py: draw with the keyboard

| Key | Action |
| --- | --- |
| `w` | Move forward 10 steps |
| `s` | Move backward 10 steps |
| `a` | Turn left 10 degrees |
| `d` | Turn right 10 degrees |
| `c` | Clear the drawing and return to the centre |

Click the window to close it.

## race.py: bet on a turtle

1. Enter a colour when prompted: `red`, `orange`, `yellow`, `green`, `blue` or `purple`.
2. Six turtles start in a line and move forward by random steps.
3. The first turtle past the finish line decides the result. You win if your colour matches.

## What I learned

- Keyboard events with `screen.listen()` and `screen.onkey()`
- Passing functions as values, without calling them
- Using `for` loops and `while` loops to animate objects
- Storing many objects in a list
- Checking a turtle's position with `xcor()` and its colour with `pencolor()`

## Known issues

- If you cancel the bet prompt, `race.py` raises an error because `is_race_on` is never set.
- The race loop doesn't stop after the first finisher, so the result message can print more than once.