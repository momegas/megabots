# def _ignore_warnings():
#     import logging
#     import warnings

#     logging.captureWarnings(True)
#     warnings.filterwarnings(
#         "ignore",
#         category=DeprecationWarning,
#         message="Deprecated call to `pkg_resources.declare_namespace('google')`.",
#     )


# _ignore_warnings()

# import os
# import signal
# import subprocess

# import requests
# from requests.adapters import HTTPAdapter, Retry

# megabot_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def _session_with_retry() -> requests.Session:
#     s = requests.Session()
#     retries = Retry(
#         total=50, backoff_factor=1, status_forcelist=[404, 500, 502, 503, 504]
#     )
#     s.mount("http://", HTTPAdapter(max_retries=retries))
#     return s


# class LCServeLocally:
#     def __init__(self, port: int = 8000):
#         self.port = port
#         self.command = " ".join(
#             [
#                 "lc-serve",
#                 "deploy",
#                 "local",
#                 "megabots.api",
#                 "--port",
#                 str(self.port),
#             ]
#         )

#     def __enter__(self):
#         self.p = subprocess.Popen(
#             self.command, cwd=megabot_dir, shell=True, preexec_fn=os.setsid
#         )

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.p.terminate()
#         os.killpg(os.getpgid(self.p.pid), signal.SIGTERM)


# def test_lcserve_successful():
#     port = 8000
#     lcserve_host = f"http://localhost:{port}"

#     with LCServeLocally(port=port):
#         resp = _session_with_retry().post(
#             url=f"{lcserve_host}/ask",
#             json={"question": "What is your name?"},
#         )
#         assert resp.status_code == 200
#         assert "result" in resp.json()
#         assert isinstance(resp.json()["result"], str)


# def test_lcserve_invalid_request():
#     port = 8000
#     lcserve_host = f"http://localhost:{port}"

#     with LCServeLocally(port=port):
#         resp = _session_with_retry().post(
#             url=f"{lcserve_host}/ask",
#             json={"foo": "bar"},
#         )
#         assert resp.status_code == 422
#         assert "detail" in resp.json()
#         assert resp.json()["detail"] == [
#             {
#                 "loc": ["body", "question"],
#                 "msg": "field required",
#                 "type": "value_error.missing",
#             }
#         ]
