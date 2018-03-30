class Invitation:
    def __init__(self, name, num_invited):
        self.name = name
        self.num_invited = num_invited
    
    def __str__(self):
        return "Invitation('" + self.name + "', " + str(self.num_invited) + ")"
    
    def __repr__(self):
        return "Invitation('" + self.name + "', " + str(self.num_invited) + ")"
        
    def __eq__(self, other):
        return self.name == other.name and self.num_invited == other.num_invited
    
    def __lt__(self, other):
        if self.name < other.name: return True
        elif self.name > other.name: return False
        elif self.num_invited < other.num_invited: return True
        else: return False 
        #if self.name < other.name: return True
        #if self.num_invited < other.num_invited: return True
        #return False
    
class Response:
    def __init__(self, name, ans, num_attending):
        self.name = name
        self.ans = ans
        self.num_attending = num_attending
    
    def __str__(self):
        return "Response('" + self.name + "', " + str(self.ans) + ", " + str(self.num_attending) + ")"
    
    def __repr__(self):
        return "Response('" + self.name + "', " + str(self.ans) + ", " + str(self.num_attending) + ")"
        
    def __eq__(self, other):
        return self.num_attending == other.num_attending and self.name == other.name
    
    def __lt__(self, other):
        if self.name < other.name: return True
        elif self.name > other.name: return False
        elif self.ans < other.ans: return True
        elif self.ans > other.ans: return False
        elif self.num_attending < other.num_attending: return True
        else: return False

class InviteNotFoundError(LookupError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "no invite for '" + self.name + "' found."
    
    def __repr__(self):
        return "InviteNotFoundError('" + self.name + "')"
        
    def __eq__(self, other):
        return self.name == other.name

class TooManyError(ValueError):
    def __init__(self, num_requested, num_allowed):
        self.num_requested = num_requested
        self.num_allowed = num_allowed
    
    def __str__(self):
        return "too many: " + str(self.num_requested) + " requested, " + str(self.num_allowed) + " allowed."
    
    def __repr__(self):
        return "TooManyError(" + str(self.num_requested) + ", " + str(self.num_allowed) + ")"
        
    def __eq__(self, other):
        return self.num_requested == other.num_requested and self.num_allowed == other.num_allowed

class Event:
    def	__init__(self, title, invites=None, responses=None):
        self.title = title
        self.invites = sorted(invites) if invites is not None else []
        self.responses = sorted(responses) if responses is not None else []
        
    def __str__(self):
        return "Event('" + self.title + "', " + str(self.invites) + ", " + str(self.responses) + ")" 
    
    def __repr__(self):
        return "Event('" + self.title + "', " + str(self.invites) + ", " + str(self.responses) + ")" 
        
    def __eq__(self, other):
        return self.title == other.title and self.invites == other.invites and self.responses == other.responses
    
    def find_invite(self, name):
        for i in self.invites:
            if i.name == name:
                return i
        raise InviteNotFoundError(name)
    
    def pop_invite(self, name):
        i = self.find_invite(name)
        self.invites.remove(i)
        try:
            r = self.find_response(name)
            self.responses.remove(r)
        except:
            return i
        return i
    
    def add_invite(self, inv):
        for invitation in self.invites:
            if invitation.name == inv.name:
                self.invites.remove(invitation)
        self.invites.append(inv)
        self.invites.sort()
        return self.invites

    def find_response(self, name):
        for r in self.responses:
            if r.name == name:
                return r
        raise LookupError("no Response found with name='" + name + "'.")
    
    def pop_response(self, name):
        r = self.find_response(name)
        self.responses.remove(r)
        self.responses = sorted(self.responses)
        return r
    
    def read_response(self, response):
        invitation = self.find_invite(response.name)
        try:
            self.pop_response(response.name)
        except:
            pass
        if invitation.num_invited < response.num_attending:
            raise TooManyError(response.num_attending, invitation.num_invited)
        if not response.ans:
            response.num_attending = 0
        self.responses.append(response)
        self.responses.sort()
    
    def count_attendees(self):
        return sum([r.num_attending if r.num_attending else 0 for r in self.responses])
    
    def count_pending(self):
        pending = 0
        for i in self.invites:
            try:
                self.find_response(i.name)
            except:
                pending += i.num_invited
        return pending

    def max_attendance(self):
        return self.count_attendees() + self.count_pending()
    
    def count_rejections(self):
        rejections = 0
        for r in self.responses:
            if not r.ans: rejections += self.find_invite(r.name).num_invited
            else: rejections += self.find_invite(r.name).num_invited - r.num_attending
        return rejections
    
    def rescind_invitation(self, name):
        try:
            self.pop_invite(name)
            self.pop_response(name)
        except:
            return None