# Python Meeting Düsseldorf - Spring Sprint 2024
- Python Meeting Düsseldorf: https://www.pyddf.de/
- Sprint Meetup page: https://www.meetup.com/python-meeting-dusseldorf/events/299529260/

## Experiments with Taipy

### Resources
- Github project: https://github.com/malemburg/pyddf-spring-sprint-2024
- Taipy home page: https://www.taipy.io/
- Documentation: https://docs.taipy.io/en/latest/
- Get started: https://docs.taipy.io/en/latest/getting_started/
- Intro video: https://www.youtube.com/watch?v=PDkP1jxXfiA

### Prepare env
- make install-venv install-requirements
- create exampleN.py files based on Getting Started guide and tutorial

## Observations

### example1.py
- global vars are just used for initialization, not updated later on
	- updates go into state parameter of on-change APIs
- adding new variables requires a restart
	- the auto reloader doesn't seem the handle them correctly and creates weird errors
- auto reload also doesn't update when markdown is changed
	- it seems the auto-reloader isn't ready for prime time yet
- markdown for headers does not seem to apply to widgets
	- widget sizes don't adapt automatically
- Taipy appears to use some WASM as runtime
	- ca. 10MB in total
- Uses WebSockets for interactivity
	- slider changes are reported via WS
- Restarting the app causes a new browser tab to open
	- if you don't pay attention, you suddenly have 10s of tabs all listening and working with the same backend app, making it very sluggish
- Changes to state variables propogate to the client side automatically
	- You can also call other functions from an on_change trigger function. If those functions change state, these changes will also propagate.
- Taipy uses Plotly for charting
	- full Plotly charting API available for customization
- All global variables get converted into state variables and are subject to the automatic state exchange with the client

### example2-5.py
- The Taipy UI does not indicate when the server connection goes down
	- perhaps there's some way to create a widget for this
- There doesn't appear to be a way to select rows of a table and interact with them
	- It is possible to set a callback when selecting rows and marking selected rows would be possible via a CSS callback, but that's cumbersome
	- Should be a standard parameter of tables
