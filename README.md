# python_request_performance_test

This is a simple way to test different kinds of requests to make sure which one has a better performance.

In the shell, run:

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Once the env was up and running, Feel free to run the command below to test each file for a perfomance test

```
python <file_name>
```

**Sugestion** : Fallow the path below to see clearly the difference in speed
- First run `send_http_reqs_sync.py` to see how long will it take so a sync request to be made without any session object
- Second run `send_http_reqs_with_session.py` to see just by adding a session object to the request how much will change the performance of it
- Third run `multi_threading.py` to check with multi threading without ThreadPoolExecutor
- Fourth run `multi_threading_thread_pool.py` to check multi threading with ThreadPoolExecutor
- Finally run `asyncio_aiohttp.py` To see the magic of event loop system of python

**NOTE** This is to show the power of event loop which is a default feature in JavaScript, However the last solution is is actually performing faster that Node JS. Python is the Winner in this case.


** Credit To ** https://python.plainenglish.io/send-http-requests-as-fast-as-possible-in-python-304134d46604 