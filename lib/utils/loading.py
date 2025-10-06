#!/usr/bin/env python

#TODO: implement loading cursor

import sys
import threading

class LoadingCursor:
    def __init__(self):
        self.loading = False
        self.thread = None
    
    def start(self):
        self.loading = True
        self.thread = threading.Thread(target=self._animate)
        self.thread.daemon = True
        self.thread.start()
    """
    def _animate(self):
        while self.loading:
            for cursor in ['|          |', '|.         |', '|..        |', '|...       |', '| ...      |', '|  ...     |', '|   ...    |', '|    ...   |', '|     ...  |', '|      ... |', '|       ...|', '|        ..|', '|         .|', '|          |']:
                if not self.loading:
                    break
                sys.stdout.write(f'\r{cursor}')
                sys.stdout.flush()
                time.sleep(0.1)
    
    def stop(self):
        self.loading = False
        if self.thread:
            self.thread.join()
        sys.stdout.write('\r')
        sys.stdout.flush()
        #sys.stdout.write('\rDone!            \n')
        """