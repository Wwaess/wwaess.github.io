"""
This Python file attempts to mimic a faceted data system
in Python. The original idea was from "Faceted Dynamic 
Information Flow via Control and Data Monads", though that 
was in Haskell. 
"""

# 1. Faceted values

class Facet:
    """
    A facet is a value that can be viewed differently 
    by different observers.
    """
    def __init__(self, label, high, low):
        self.label = label      # e.g. "H"
        self.high = high        # value for privileged observers
        self.low = low          # value for unprivileged observers

    def project(self, view):
        """Return the appropriate facet for a given observer view (set of labels)."""
        # FIX: projection must be recursive in case high/low are also facets
        branch = self.high if self.label in view else self.low
        if isinstance(branch, Facet):
            return branch.project(view)
        return branch


def facet(label, high, low):
    """Helper function to create a facet."""
    return Facet(label, high, low)

def public(value):
    """Create a public facet (same value for all observers)."""
    # NOTE: returning raw values is fine, but requires checks elsewhere
    return value


# 2. Program counter

class PC:
    """
    The program Counter (PC) tracks implicit flows, 
    i.e. the current set of labels that are in effect
    """
    def __init__(self):
        self.labels = set()

    def push(self, label):
        """Add a label to the PC."""
        self.labels.add(label)

    def pop(self, label):
        """Remove a label from the PC."""
        self.labels.discard(label)

    def current_view(self):
        """Return the current view (set of labels) for projection."""
        return set(self.labels)  # FIX: return a copy to avoid mutation issues
    
    def __repr__(self):
        return f"PC({self.labels})"
    

# 3. Faceted reference cells

class FacetedRef:
    """
    A faceted reference cell that can hold a faceted value.
    """
    def __init__(self, value):
        self.value = value  # should be a Facet

    def read(self, pc):
        """
        Read the value, 
        projecting according to the current PC.
        """
        # FIX: handle both raw values and facets
        if isinstance(self.value, Facet):
            return self.value.project(pc.current_view())
        return self.value

    def write(self, pc, new_value):
        """
        Write a new value, 
        taking into account the current PC.
        """
        # FIX: removed accidental nested function definition
        v = new_value

        # FIX: wrap value under all labels in the PC (implicit flow tracking)
        for label in pc.current_view():
            v = Facet(label, v, self.value)

        self.value = v


# 4. FIO monad (effectful computations)

class FIO:
    """
    A minimal FIO monad: wraps a function pc -> result.
    """
    def __init__(self, action):
        self.action = action

    def bind(self, f):
        """
        Monadic bind: chain computations while threading the PC.
        """
        def new_action(pc):
            result = self.action(pc)
            return f(result).action(pc)
        return FIO(new_action)

    def run(self, pc=None):
        pc = pc or PC()
        return self.action(pc)


# 5. Faceted I/O Handles

class FHandle:
    """
    A faceted output handle.
    Only writes if the PC is compatible with the handle's view.
    """
    def __init__(self, view):
        self.view = set(view)
        self.buffer = []

    def write(self, pc, value):
        """
        Only allow writes if all labels in PC are visible to this handle.
        """
        # FIX: labels is a set, not a function
        if pc.labels.issubset(self.view):
            # FIX: project facets before writing
            if isinstance(value, Facet):
                v = value.project(self.view)
            else:
                v = value
            self.buffer.append(str(v))

    def read_all(self):
        return "".join(self.buffer)

    def __repr__(self):
        return f"FHandle(view={self.view}, buffer={self.buffer})"


# 6. Example Usage

if __name__ == "__main__":
    # Program counter
    pc = PC()

    # A secret value: high facet = True, low facet = False
    secret = facet("H", True, False)

    # A public reference cell
    y = FacetedRef(public(True))

    # Simulate branching on a secret
    pc.push("H")
    if secret.project({"H"}):  # high observer's branch
        y.write(pc, public(False))
    pc.pop("H")

    # Observers
    low_view = set()
    high_view = {"H"}

    val = y.value  # FIX: read() already projects, so use raw value here
    print(
        "Low observer sees:",
        
        val.project(low_view) 
        if isinstance(val, Facet) 
        else val
        )
    print(
        "High observer sees:",
        
        val.project(high_view) 
        if isinstance(val, Facet) 
        else val
        )