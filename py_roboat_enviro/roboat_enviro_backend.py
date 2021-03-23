import json

from uplink import Consumer, Header, Path, Query, get, post


class RoboatEnviroData(Consumer):
    """[summary]

    Args:
        Consumer ([type]): [description]
    """

    @get("users?username={username}")
    def get_users(self, username: Path):
        """Get users.

        Args:
            username (Path): [description]
        """
        return

    @post("users/search?filters={filters}")
    def search_users(self, filters):
        """Search users

        Args:
            filters ([type]): [description]
        """
        return
