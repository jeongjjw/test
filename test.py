"""
Run solutions from one problem.
code from https://github.com/hendrycks/apps/blob/main/eval/test_one_solution.py
"""
import numpy as np
import os
import pprint
import multiprocessing
import time
import testing_util as test_util

from typing import Dict

def check_correctness(problem, generation, timeout, debug):
    """Check correctness of code generation with a global timeout.
    The global timeout is to catch some extreme/rare cases not handled by the timeouts
    inside `run_test`"""
    def _temp_run(problem, generation, debug, result):
        try:
            result.append(test_util.run_test(problem=problem, test=generation, debug=debug))
            # Useful for debugging the multiprocessing.
            # result.append(run_test(problem=problem, test=generation, debug=debug))
            if debug:
                print(f"Test completed with result: {result}")
        except Exception as e:
            if debug:
                print(f"Error in _temp_run: {e}")

    manager = multiprocessing.Manager()
    result = manager.list()
    p = multiprocessing.Process(target=_temp_run, args=(problem, generation, debug, result))
    p.start()
    p.join(timeout=timeout + 1)
    if p.is_alive():
        if debug:
            print(f"Process is still alive. Killing the process.")
        p.kill()
    if not result:
        # Remark: ideally we would consider that all tests failed but we can't access number of tests here easily
        # so we use 21=the average number of tests for a smaple in the test split instead 
        avg_number_tests = 21
        result = [[-1] * avg_number_tests]
        if debug:
            print(f"Global timeout occurred, returning default result.")
    if debug:
        print(f"Final result: {result}")
    return result[0]