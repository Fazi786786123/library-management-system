from models.member import Member


class MemberService:
    """
    Handles all member-related operations.

    Attributes:
        members (dict): Dictionary storing all members by member_id.
        next_id (int): Counter for generating unique member IDs.
    """

    def __init__(self):
        self.members = {}
        self.next_id = 1

    def generate_member_id(self):
        """Generates a unique member ID."""
        member_id = f"M{str(self.next_id).zfill(3)}"
        self.next_id += 1
        return member_id

    def register_member(self, name, email):
        """
        Registers a new member.

        Args:
            name (str): Full name of the member.
            email (str): Email address of the member.

        Returns:
            Member: The newly created member object.
        """
        member_id = self.generate_member_id()
        new_member = Member(member_id, name, email)
        self.members[member_id] = new_member
        return new_member

    def get_member(self, member_id):
        """
        Finds a member by their ID.

        Args:
            member_id (str): ID of the member.

        Returns:
            Member or None: Member object if found, else None.
        """
        return self.members.get(member_id, None)

    def get_all_members(self):
        """Returns a list of all members."""
        return list(self.members.values())

    def deactivate_member(self, member_id):
        """
        Deactivates a member account.

        Args:
            member_id (str): ID of the member to deactivate.

        Returns:
            bool: True if deactivated, False if not found.
        """
        member = self.get_member(member_id)
        if member:
            member.deactivate()
            return True
        return False