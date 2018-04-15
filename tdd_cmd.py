
import os
import sys
import time
import threading
import queue

"""--------------------------------------------------------------------------"""
""" MAIN TEST THREAD """
"""--------------------------------------------------------------------------"""
class thread_tdd(threading.Thread):
    """
    class for invoke ceedling test in infinite loop
    """
    def __init__(self, threadID, name, delay, command):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.del_s = delay
        self.boost = False
        self.t_exit= False
        self.cmd = command

    def print_del(self):
        """
        make delay beetween test and show flow of time (on ascii progress bar)
        """
        cnt = self.del_s
        print('<{}>|<- delay time'.format('-'*(self.del_s - 2)))
        while (cnt > 0) and (self.boost == False) and (self.speed_up() == False):
            time.sleep(1) # one second delay
            cnt = cnt - 1
            sys.stdout.write("-" )
            sys.stdout.flush()
            self.boost = False

    def test_inf(self):
        """
        function do ceedling test until exitFlag is not set
        """
        while self.t_exit == False:
            #os.system('ceedling clean')
            os.system('ceedling {}'.format(self.name))
            self.print_del()
            

    def run(self):
        print("Starting " + self.name)
        self.test_inf()
        print( "Exiting " + self.name)
    
    def stop(self):
        self.t_exit= True

    def speed_up(self):
        try:
            obj = self.cmd.get_nowait()
            return True
        except:
            return False
