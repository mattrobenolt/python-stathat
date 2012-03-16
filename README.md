# A better Python library for [StatHat](http://www.stathat.com)
Implements the [StatHat](http://www.stathat.com) [EZ and Classic API](http://www.stathat.com/docs/api), and supports (and encourages) asynchronous usage with [gevent](http://www.gevent.org/).

## Installation
```
$ pip install python-stathat
```

## EZ API usage
```python
from stathat import StatHatEZ
stats = StatHatEZ('matt@ydekproductions.com', 'awesome stuff')
stats.tick()  # Increment a counter by 1
stats.count(5)  # Increment a counter by 5
stats.value(0.275)  # Track specific values, such as loadavg or uptime, etc.
print stats.count(5, async=False)  # Force async off
```
Async features are detected automatically based on if [gevent](http://www.gevent.org/) is available or not. Async can be disabled by passing `async=False` to any method.

## Classic API usage
```python
from stathat import StatHat
stats = StatHat('{{ my user key }}', '{{ my stat key }}')
stats.tick()  # Increment a counter by 1
stats.count(5)  # Increment a counter by 5
stats.value(0.275)  # Track specific values, such as loadavg or uptime, etc.
print stats.count(5, async=False)  # Force async off
```

## Error handling
Error handling is only relevant in non-async mode. No exceptions will be raised in async mode.

```python
from stathat import StatHatEZ, StatHatError
stats = StatHatEZ('matt@ydekproductions.com', 'awesome stuff')
try:
    stats.tick()
except StatHatError, e:
    print "Broke!", e
```

## Shortcuts
These methods are provided as a shortcut for one-off calls. Errors are raised and handled the same way as the normal calls.

```python
import stathat
stathat.ez_count('matt@ydekproductions.com', 'awesome stuff', 5)
stathat.ez_value('matt@ydekproductions.com', 'awesome stuff', 0.275)
stathat.classic_count('{{ my user key }}', '{{ my stat key }}', 5)
stathat.classic_value('{{ my user key }}', '{{ my stat key }}', 0.275)
stathat.ez_count('matt@ydekproductions.com', 'awesome stuff', 5, async=False)  # Disable async
```

## (optional) Async support
First, [gevent](http://www.gevent.org/) is required to use any async features. Async features are automatically disabled gracefully if [gevent](http://www.gevent.org/) is not available.

Async mode allows a ton of requests to be made without slowing down the main application thread.

This behavior can be overridden and force requests to happen normally by passing `async=False` to any method.

Async requests will always return True no matter what the actual response is. The entire script would have to wait until the response came back before moving on otherwise, defeating the entire purpose of making the request asynchronously.

It's recommended to first make a test with `async=False` to make sure parameters are correct and your keys are working before going full-blown async mode.

### Checking for async
```python
from stathat import StatHat
if StatHat.has_async():
    print "Yes!"
else:
    print "Nope. :("
````

### Installing [gevent](http://www.gevent.org/)
```
$ pip install gevent
```
Installing [gevent](http://www.gevent.org/) allows much faster logging in a "send-and-forget" fashion.
__Note:__ libevent headers are required for installation.

## Gotchas
 * [StatHat](http://www.sitehat.com) does not return an error when your `site_key` is incorrect. They will only return an error when the `user_key` is wrong.

## Todo
 * Support for a thread pool to allow async when gevent isn't available.
