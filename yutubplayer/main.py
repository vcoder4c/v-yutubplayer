from base import YutubPlayer, NotExistVideo
from cmd import Cmd


class CmdYutubPlayer(Cmd):
    intro = 'Search and play youtube by command line'

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.yutub_player = YutubPlayer()

    def do_exit(self, inp):
        print("Bye")
        return True

    def do_search(self, query):
        print("Searching '{}'".format(query))
        self.yutub_player.search(query=query)
        self.yutub_player.list()

    def do_list(self, *args):
        self.yutub_player.list()

    def do_play(self, idx):
        try:
            self.yutub_player.play(int(idx))
        except NotExistVideo:
            print(f'Not found video {idx}')
        except Exception as e:
            print(f'Invalid {e}')

    def do_pause(self, *args):
        self.yutub_player.pause()

    def do_resume(self, *args):
        self.yutub_player.resume()

    def do_clear(self, *args):
        self.yutub_player.clear()


CmdYutubPlayer().cmdloop()
